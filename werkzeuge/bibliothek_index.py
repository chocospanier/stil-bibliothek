#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bibliothek_index.py  -  prueft und indiziert die Stil-Karten der Stil-Bibliothek. 0 Credits.

Liest  <bib>/karten/*.md  (Kopfblock YAML + Text) und schreibt:
  <bib>/index.json     alle Karten maschinenlesbar (Kopfblock + Pfad), dazu "klassen" (Creator-Klassen der Kennungen aus
                       EFFEKT_VOKABULAR.md), "creator" (Zaehlung ja/eingeschraenkt/nein) und "zahlen": Karten, Familien, Bausteine,
                       Beispiele und Helfer des Pakets; die eine Quelle für jede Zahl in den Texten
Zahlen: Das Skript zählt Karten und Familien (karten/), Bausteine (starter/src/bausteine/index.ts, nummerierte Exporte),
Beispiele (Kompositionen aus starter/src/beispiele/ in den Root-Dateien) und Helfer (starter/werkzeuge, ohne py.mjs) und
sucht in allen Texten des Pakets Stellen wie „289 Stil-Karten“, „28 Bausteine“, „<n> Beispiele“. Weicht eine ab, steht sie
unter "zahlen_widerspruch"; --zahlen-setzen schreibt die gezählten Werte hinein (Karten selbst, INDEX.md und Bauberichte
bleiben unberührt).
  <bib>/INDEX.md       Uebersicht je Familie
  <bib>/EFFEKTE.md     Auszaehlung der Effekt-Kennungen ueber alle Karten (bekannt / neu)
Prueft je Karte: Pflichtfelder (seit 31.10.2026 auch creator, spielraum, palettenrolle; Werte von creator; bei bauweg animskill
seit 06.11.2026 sollwerte, animskill.motor/stil/quelle und lizenz statt messung, eigene Abschnitte), Effekt-Kennungen
gegen EFFEKT_VOKABULAR.md, Gedankenstriche, zweck/branchen_passt/branchen_nie gegen ZWECKE.md (seit 05.11.2026),
und mit --leck <begriffe.txt> (ein Begriff je Zeile) ob gesperrte Namen in einer Karte stehen.
Lautheit: Standard ist -14 LUFS; nennt eine Karte einen Bereich, gilt die Karte, solange er sich mit -14 +- 1
ueberschneidet. Karten, deren abnahme.lufs ganz ausserhalb liegt, markiert INDEX.md (Messwerte bleiben, wie sie sind).

Filtern (schreibt nichts, gibt eine Tabelle aus):
  python -I bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook
  Je Bedingung schluessel=wert; mehrere Werte mit Komma heissen "eins davon" (einsatz=hook,intro); bei Listen-Feldern
  (braucht, einsatz, effekte) reicht ein Treffer in der Liste. Zahlen auch mit >=, <=, != (energie>=4).
  "Nur diese" bei Listen: braucht<=nur-typo,illustrationen heisst, die Liste ist eine Teilmenge (jedes Element ist
  eins der genannten); "alle diese": effekte>=titelkarte,korn heisst, alle genannten stehen in der Liste.
  nur_code=ja (abgeleitet): braucht ist Teilmenge von {nur-typo, illustrationen}, die Karte geht ohne Fotos,
  Footage, Produkt und 3D; Spalte "nur Code" in der Tabelle.
  Mehrere Bedingungen muessen alle passen.

Schlag-Pruefung: Nennt das Feld ton einen Abstand ("Schlag alle 1,5 s", "Treffer etwa alle drei Sekunden") und ein
Tempo ("60 BPM"), prueft das Skript, ob der Abstand ein ganzes Vielfaches eines Schlags ist (oder ein halber oder
viertel Schlag), Toleranz 12 %. Widersprueche stehen in der Ausgabe und in INDEX.md; umgeschrieben wird nichts.

Aufruf:
  python -I bibliothek_index.py [--bib <stilbibliothek>] [--leck <begriffe.txt>] [--nur-pruefen] [--filter ...] [--zahlen-setzen]
  Ohne --bib gilt der Ordner stilbibliothek/ neben werkzeuge/.
"""
import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

PFLICHT = ["id", "name", "familie", "kurz", "kern", "energie", "messung", "palette", "effekte", "kamera", "ton",
           "braucht", "motor_aufwand", "einsatz", "abnahme",
           # Wuerfel-Felder (Etappe 0 Bauplan Wuerfelstile, 31.10.2026; gefuellt von karten_wuerfelfelder.py)
           "creator", "spielraum", "palettenrolle"]
CREATOR_WERTE = {"ja", "eingeschraenkt", "nein"}
ABSCHNITTE = ["## Kern", "## Erkennung", "## Bildtypen", "## Dramaturgie", "## Schnittmuster",
              "## Rezept", "## Material", "## Regler", "## Abnahme", "## Fallen"]
# Karten mit bauweg animskill (Zeichen-Motoren, seit 06.11.2026, Vorlage KARTE_VORLAGE_MOTOR.md): statt messung die Sollwerte
# fuer den eigenen Render, dazu Motor, Stil-Kennung im Motor und Lizenzhinweis; Schnittmuster und Rezept macht der Motor
PFLICHT_MOTOR = [f for f in PFLICHT if f != "messung"] + ["sollwerte", "animskill", "lizenz"]
ABSCHNITTE_MOTOR = ["## Kern", "## Erkennung", "## Bildtypen", "## Regler", "## Fallen", "## Ton", "## Bauweg", "## Abnahme"]
ZEICHEN_MOTOREN = {"huashu", "anidoodle", "zeichnen", "handzeichnung", "manim", "pinsel", "jsanim", "kino3d"}  # kino3d: 3D-Kino seit 1.6
# Woerter, die in Vorlagen-Namen vorkommen, aber auch normale Fachwoerter sind: nicht als Leck werten
ALLTAG = {"edit", "vibe", "vibes", "style", "aesthetic", "montage", "look", "check", "cinematic", "film", "dark",
          "moody", "noir", "car", "comic", "star", "nocturne", "monochrome", "cartoon", "glitch", "scrapbook",
          "y2k", "lookbook", "collage", "painting", "flow", "fashion", "music", "video", "beat", "pop", "art",
          "camera", "shots", "preset", "edits", "aura", "frame", "dance", "motion", "scan", "neon",
          "ochre"}  # ochre: Autorenname, zugleich Farbwort in englischen Prompts


LUFS_ZIEL, LUFS_TOLERANZ = -14.0, 1.0


def lufs_lage(kopf):
    """(Band, vereinbar) fuer abnahme.lufs: vereinbar, wenn sich das Band mit -14 +- 1 ueberschneidet; None ohne Band"""
    band = (kopf.get("abnahme") or {}).get("lufs") if isinstance(kopf, dict) else None
    if not isinstance(band, (list, tuple)) or len(band) != 2:
        return None
    lo, hi = sorted(float(x) for x in band)
    return (lo, hi), (lo <= LUFS_ZIEL + LUFS_TOLERANZ and hi >= LUFS_ZIEL - LUFS_TOLERANZ)


def bedingung(text):
    m = re.match(r"^([a-z_0-9]+)\s*(>=|<=|!=|=)\s*(.+)$", text.strip())
    if not m:
        sys.exit(f"Filter '{text}' nicht lesbar; Form schluessel=wert, etwa braucht=nur-typo oder energie>=4")
    return m.group(1), m.group(2), [w.strip() for w in m.group(3).split(",") if w.strip()]


CODE_MATERIAL = {"nur-typo", "illustrationen"}


def nur_code(kopf):
    braucht = {str(x) for x in (kopf.get("braucht") or [])}
    return bool(braucht) and braucht <= CODE_MATERIAL


ZAHLWORT = {"eine": 1, "einer": 1, "einen": 1, "zwei": 2, "drei": 3, "vier": 4, "fuenf": 5, "fünf": 5, "sechs": 6,
            "sieben": 7, "acht": 8, "zehn": 10, "anderthalb": 1.5, "eineinhalb": 1.5}
ABSTAND = re.compile(r"alle\s+(?:etwa\s+|rund\s+|knapp\s+)?(\d+(?:[.,]\d+)?|[a-zäöü]+)\s*(?:s\b|sek|sekunde)", re.I)
TEMPO = re.compile(r"(\d+(?:[.,]\d+)?)\s*BPM", re.I)


def schlag_widerspruch(kopf):
    """Liste von (Abstand s, BPM, Verhaeltnis in Schlaegen, Textstelle) fuer ton-Angaben, die nicht aufs Raster passen."""
    ton = str(kopf.get("ton") or "")
    tempi = [float(m.group(1).replace(",", ".")) for m in TEMPO.finditer(ton)]
    if not tempi:
        return []
    bpm = tempi[0]
    aus = []
    for m in ABSTAND.finditer(ton):
        roh = m.group(1).lower()
        sek = float(roh.replace(",", ".")) if roh[0].isdigit() else ZAHLWORT.get(roh)
        if not sek:
            continue
        schlaege = sek / (60.0 / bpm)
        kandidaten = [0.25, 0.5] + list(range(1, 65))
        naechst = min(kandidaten, key=lambda k: abs(schlaege - k) / k)
        if abs(schlaege - naechst) / naechst > 0.12:
            stelle = ton[max(0, m.start() - 25): m.end() + 5].strip()
            aus.append((sek, bpm, round(schlaege, 2), stelle))
    return aus


def zahl(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def passt(kopf, schluessel, op, werte):
    feld = kopf.get(schluessel)
    if schluessel == "nur_code":
        feld = "ja" if nur_code(kopf) else "nein"
    liste = [x for x in (feld if isinstance(feld, list) else [feld]) if x is not None]
    if op in (">=", "<=") and isinstance(feld, list) and any(zahl(w) is None for w in werte):
        # Listen-Mengen: <= Teilmenge ("nur diese"), >= Obermenge ("alle diese")
        menge = {str(x).lower() for x in liste}
        werte_m = {w.lower() for w in werte}
        return bool(menge) and menge <= werte_m if op == "<=" else werte_m <= menge
    if op in (">=", "<="):
        grenze = zahl(werte[0])
        if grenze is None:
            sys.exit(f"Filter {schluessel}{op}{werte[0]}: Zahl erwartet")
        return any(zahl(x) is not None and (zahl(x) >= grenze if op == ">=" else zahl(x) <= grenze) for x in liste)
    treffer = any(str(x).lower() == w.lower() or (zahl(x) is not None and zahl(x) == zahl(w)) for x in liste for w in werte)
    return not treffer if op == "!=" else treffer


def filtern(karten, bedingungen):
    bed = [bedingung(b) for b in bedingungen]
    treffer = [k for k in karten if all(passt(k, *b) for b in bed)]
    print(f"{len(treffer)} von {len(karten)} Karten passen zu: {' und '.join(bedingungen)}")
    if not treffer:
        return
    print()
    print("| Karte | Familie | Energie | Aufwand | braucht | nur Code | einsatz | LUFS | kurz |")
    print("|---|---|---:|---|---|---|---|---|---|")
    for k in sorted(treffer, key=lambda k: (str(k.get("familie")), -(k.get("energie") or 0), k["id"])):
        lage = lufs_lage(k)
        lufs = "" if lage is None else (f"{lage[0][0]:g} bis {lage[0][1]:g}" + ("" if lage[1] else " ⚠"))
        kurz = str(k.get("kurz") or "")
        kurz = kurz if len(kurz) <= 90 else kurz[:87] + "..."
        print(f"| {k['id']} | {k.get('familie')} | {k.get('energie')} | {k.get('motor_aufwand')} | "
              f"{', '.join(map(str, k.get('braucht') or []))} | {'ja' if nur_code(k) else 'nein'} | {', '.join(map(str, k.get('einsatz') or []))} | {lufs} | {kurz} |")
    print()
    print("Karte lesen: stilbibliothek/karten/<Karte>.md. ⚠ = abnahme.lufs liegt ganz ausserhalb -14 +- 1 (siehe INDEX.md).")


def kopf_und_text(p):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", t, re.S)
    if not m:
        return None, t
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError as e:
        return {"_yaml_fehler": str(e)}, m.group(2)


def vokabular(bib):
    t = (bib / "EFFEKT_VOKABULAR.md").read_text(encoding="utf-8")
    ids = set()
    for m in re.finditer(r"^\|\s*`([^`]+)`(?:\s*/\s*`([^`]+)`)?\s*\|", t, re.M):
        ids.add(m.group(1))
        if m.group(2):
            ids.add(m.group(2))
    return ids


def klassen(bib):
    """Klassen fuer den Creator-Modus aus EFFEKT_VOKABULAR.md (Abschnitt "Klassen fuer den Creator-Modus"): {klasse: [kennungen]}"""
    t = (bib / "EFFEKT_VOKABULAR.md").read_text(encoding="utf-8")
    m = re.search(r"^## Klassen für den Creator-Modus\s*$(.*?)(?=^## |\Z)", t, re.M | re.S)
    kl = {}
    if m:
        for z in m.group(1).splitlines():
            r = re.match(r"^\|\s*([a-z]+)\s*\|\s*(.*?)\s*\|", z)
            if r and r.group(1) != "klasse":
                kl[r.group(1)] = re.findall(r"`([^`]+)`", r.group(2))
    return kl


def leck_begriffe(datei):
    """Gesperrte Begriffe aus einer Textdatei, ein Begriff je Zeile (Namen fremder Vorlagen, Personen, Marken)."""
    if not datei:
        return []
    zeilen = Path(datei).read_text(encoding="utf-8").splitlines()
    begriffe = {z.strip() for z in zeilen if z.strip() and not z.startswith("#")}
    return sorted(begriffe, key=len, reverse=True)


def zweck_vokabular(bib):
    """Feste Woerter aus ZWECKE.md: ({zwecke}, {branchen}); None, wenn die Datei fehlt (dann keine Pruefung)"""
    p = bib / "ZWECKE.md"
    if not p.exists():
        return None
    t = p.read_text(encoding="utf-8")
    teile = {}
    for name in ("Zwecke", "Branchen"):
        m = re.search(rf"^## {name}\b.*?$(.*?)(?=^## |\Z)", t, re.M | re.S)
        teile[name] = set(re.findall(r"^\|\s*`([^`]+)`\s*\|", m.group(1), re.M)) if m else set()
    return teile["Zwecke"], teile["Branchen"]


ZVOK = None


def pruefe(p, kopf, text, vok, leck):
    probleme = []
    if kopf is None:
        return ["kein Kopfblock"], set()
    if "_yaml_fehler" in kopf:
        return [f"YAML-Fehler: {kopf['_yaml_fehler'][:120]}"], set()
    motor_karte = kopf.get("bauweg") == "animskill"
    for f in (PFLICHT_MOTOR if motor_karte else PFLICHT):
        if f not in kopf or kopf[f] in (None, "", []):
            probleme.append(f"Feld fehlt: {f}")
    if motor_karte:
        a = kopf.get("animskill") if isinstance(kopf.get("animskill"), dict) else {}
        if a.get("motor") not in ZEICHEN_MOTOREN:
            probleme.append(f"animskill.motor unbekannt: {a.get('motor')} (erlaubt: {', '.join(sorted(ZEICHEN_MOTOREN))})")
        for f in ("stil", "quelle"):
            if not a.get(f):
                probleme.append(f"animskill.{f} fehlt")
    elif kopf.get("bauweg") not in (None, "motor", "handbau"):
        probleme.append(f"bauweg unbekannt: {kopf.get('bauweg')}")
    if kopf.get("id") and kopf["id"] != p.stem:
        probleme.append(f"id '{kopf['id']}' passt nicht zum Dateinamen")
    for a in (ABSCHNITTE_MOTOR if motor_karte else ABSCHNITTE):
        if a not in text:
            probleme.append(f"Abschnitt fehlt: {a}")
    neu = set()
    for e in kopf.get("effekte") or []:
        e = str(e)
        if e.startswith("neu:"):
            neu.add(e[4:])
        elif e not in vok:
            probleme.append(f"unbekannter Effekt: {e}")
    if kopf.get("creator") not in (None, *CREATOR_WERTE):
        probleme.append(f"creator muss ja, eingeschraenkt oder nein sein: {kopf.get('creator')}")
    if kopf.get("creator") == "eingeschraenkt" and not kopf.get("creator_ohne"):
        probleme.append("creator eingeschraenkt ohne creator_ohne")
    if kopf.get("creator") == "nein" and not kopf.get("creator_grund"):
        probleme.append("creator nein ohne creator_grund")
    if ZVOK:
        for feld, erlaubt in (("zweck", ZVOK[0]), ("branchen_passt", ZVOK[1]), ("branchen_nie", ZVOK[1])):
            if feld not in kopf:
                probleme.append(f"Feld fehlt: {feld}")
                continue
            if not isinstance(kopf[feld], list):
                probleme.append(f"{feld} muss eine Liste sein")
                continue
            for w in kopf[feld]:
                if str(w) not in erlaubt:
                    probleme.append(f"{feld}: unbekannter Wert {w} (ZWECKE.md)")
        doppelt = set(map(str, kopf.get("branchen_passt") or [])) & set(map(str, kopf.get("branchen_nie") or []))
        if doppelt:
            probleme.append(f"Branche in passt und nie: {', '.join(sorted(doppelt))}")
    roh = p.read_text(encoding="utf-8")
    if "—" in roh or "–" in roh:
        probleme.append(f"Gedankenstriche: {roh.count(chr(0x2014)) + roh.count(chr(0x2013))}")
    tief = roh.lower()
    for b in leck:
        if re.search(r"(?<![\w-])" + re.escape(b.lower()) + r"(?![\w-])", tief):
            probleme.append(f"LECK: '{b}'")
    return probleme, neu


ZAHLWOERTER = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf"]
ZAHL_MUSTER = [
    ("karten", r"(?<![\d,.])(\d+)( (?:beschriebene[n]? )?(?:Stil-Karten|Stilkarten|Video-Stile[n]?))"),
    ("familien", r"(?<![\d,.])(\d+)( Familien)"),
    ("bausteine", r"(?<![\d,.])(\d+)( Bausteine[n]?)"),
    ("helfer", r"(?<![\d,.])(\d+)( Helfer[n]?)\b"),
    ("beispiele", r"\b(zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|\d+)( (?:durchgebaute[n]? |fertige[n]? )?Beispiel(?:e|en)\b)"),
]


def zahlen_zaehlen(paket: Path, karten: list, familien: int) -> dict:
    """Die Zahlen des Pakets aus den Dateien selbst"""
    st = paket / "starter"
    bausteine = 0
    idx = st / "src" / "bausteine" / "index.ts"
    if idx.exists():
        nummern = [int(m) for m in re.findall(r"^export .*//\s*(\d+)\s*$", idx.read_text(encoding="utf-8"), re.M)]
        bausteine = max(nummern) if nummern else 0
    beispiele = set()
    for root in [st / "src" / "Root.tsx", *sorted((st / "src" / "beispiele").glob("*/Root.tsx"))]:
        if not root.exists():
            continue
        t = root.read_text(encoding="utf-8")
        aus_beispielen = set()
        for namen, quelle in re.findall(r"import \{([^}]*)\} from '(\./beispiele/[^']*|\./[A-Z][^']*)'", t):
            if root.name == "Root.tsx" and root.parent.name == "src" and not quelle.startswith("./beispiele/"):
                continue
            aus_beispielen |= {n.strip() for n in namen.split(",")}
        for k in re.findall(r"component=\{(\w+)\}", t):
            if k in aus_beispielen and k not in ("Bausteinprobe", "Schriftmuster", "CreatorGegenprobe"):
                beispiele.add(k)
    helfer = sorted(p.name for p in (st / "werkzeuge").glob("*") if p.suffix in (".py", ".mjs") and p.name != "py.mjs") if (st / "werkzeuge").exists() else []
    return {"karten": len(karten), "familien": familien, "bausteine": bausteine, "beispiele": len(beispiele),
            "beispiel_namen": sorted(beispiele), "helfer": len(helfer), "helfer_namen": helfer}


def zahlen_texte(paket: Path):
    """alle Texte, in denen Zahlen des Pakets stehen dürfen (ohne Karten, erzeugte Dateien, Prüf- und Bauberichte)"""
    for p in sorted(paket.rglob("*")):
        teile = set(p.relative_to(paket).parts)
        if not p.is_file() or teile & {"node_modules", "out", "karten", ".remotion", "__pycache__"} or any(x.startswith("pruef") for x in teile):
            continue
        if p.name in ("INDEX.md", "EFFEKTE.md", "index.json", "package-lock.json") or p.name.startswith("BAUBERICHT"):
            continue
        if p.suffix in (".md", ".tsx", ".ts", ".py", ".mjs") or p.name == "package.json":
            yield p


def zahlen_pruefen(paket: Path, zahlen: dict, setzen: bool = False) -> list:
    funde = []
    for p in zahlen_texte(paket):
        t = p.read_text(encoding="utf-8")
        neu = t
        for schluessel, muster in ZAHL_MUSTER:
            soll = zahlen[schluessel]
            for m in reversed(list(re.finditer(muster, neu))):
                vorher = neu[max(0, m.start() - 60):m.start()]
                # Geschichte ist kein Widerspruch: „aus der Auszählung von 101 Stil-Karten“, „die drei Beispiele der Familie …“
                if "Auszählung" in vorher or "Stand 1" in vorher[-12:] or neu[m.end():m.end() + 12].startswith(" der Familie"):
                    continue
                roh = m.group(1)
                ist = int(roh) if roh.isdigit() else ZAHLWOERTER.index(roh)
                if ist == soll:
                    continue
                zeile = neu.count("\n", 0, m.start()) + 1
                funde.append(f"{p.relative_to(paket).as_posix()}:{zeile}: „{m.group(0)}“, gezählt {soll}")
                if setzen:
                    ersatz = str(soll) if roh.isdigit() else ZAHLWOERTER[soll] if soll < len(ZAHLWOERTER) else str(soll)
                    neu = neu[:m.start(1)] + ersatz + neu[m.end(1):]
        if setzen and neu != t:
            p.write_text(neu, encoding="utf-8")
    return funde


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", default=str(Path(__file__).resolve().parent.parent / "stilbibliothek"))
    ap.add_argument("--leck")
    ap.add_argument("--nur-pruefen", action="store_true")
    ap.add_argument("--filter", nargs="+", metavar="SCHLUESSEL=WERT", help="Karten filtern, z. B. braucht=nur-typo einsatz=hook")
    ap.add_argument("--zahlen-setzen", action="store_true", help="gezählte Zahlen in die Texte des Pakets schreiben")
    a = ap.parse_args()
    bib = Path(a.bib)
    vok = vokabular(bib)
    global ZVOK
    ZVOK = zweck_vokabular(bib)
    leck = leck_begriffe(a.leck)
    karten, alle_probleme = [], {}
    eff_zaehl, neu_zaehl = Counter(), Counter()
    for p in sorted((bib / "karten").glob("*.md")):
        kopf, text = kopf_und_text(p)
        probleme, neu = pruefe(p, kopf, text, vok, leck)
        if probleme:
            alle_probleme[p.name] = probleme
        if kopf and "_yaml_fehler" not in kopf:
            k = dict(kopf)
            k["datei"] = f"karten/{p.name}"
            k["nur_code"] = nur_code(kopf)
            if kopf.get("bauweg") == "animskill" and isinstance(kopf.get("animskill"), dict):
                k["zeichen_motor"] = kopf["animskill"].get("motor")  # Filter: --filter zeichen_motor=huashu
            karten.append(k)
            for e in kopf.get("effekte") or []:
                e = str(e)
                (neu_zaehl if e.startswith("neu:") else eff_zaehl)[e.replace("neu:", "")] += 1
    if a.filter:
        filtern(karten, a.filter)
        return
    abweichler = [(k, lufs_lage(k)[0]) for k in karten if lufs_lage(k) and not lufs_lage(k)[1]]
    familien = len({str(k.get("familie")) for k in karten})
    zahlen = zahlen_zaehlen(bib.parent, karten, familien)
    zahl_funde = zahlen_pruefen(bib.parent, zahlen, a.zahlen_setzen)
    schlag = [(k, w) for k in karten for w in schlag_widerspruch(k)]
    print(json.dumps({"karten": len(karten), "mit_problemen": len(alle_probleme), "lufs_ausserhalb_14_pm_1": len(abweichler),
                      "nur_code": sum(1 for k in karten if k.get("nur_code")), "ton_schlag_widerspruch": len(schlag),
                      "zahlen": {k: v for k, v in zahlen.items() if not k.endswith("_namen")},
                      ("zahlen_gesetzt" if a.zahlen_setzen else "zahlen_widerspruch"): len(zahl_funde)},
                     ensure_ascii=False))
    for n, pr in alle_probleme.items():
        print(f"- {n}: " + "; ".join(pr))
    for f in zahl_funde:
        print(f"- ZAHL {'gesetzt' if a.zahlen_setzen else 'weicht ab'}: {f}")
    for k, (lo, hi) in abweichler:
        print(f"- LUFS {k['id']}: abnahme.lufs {lo:g} bis {hi:g}, keine Ueberschneidung mit -14 +- 1 (in INDEX.md markiert)")
    for k, (sek, bpm, schl, stelle) in schlag:
        print(f"- SCHLAG {k['id']}: ton nennt alle {sek:g} s bei {bpm:g} BPM = {schl:g} Schlaege, kein ganzer Schlag ({stelle})")
    if a.nur_pruefen:
        return
    kl = klassen(bib)
    creator_zaehl = dict(Counter(str(k.get("creator")) for k in karten))
    (bib / "index.json").write_text(json.dumps({"anzahl": len(karten), "zahlen": zahlen, "klassen": kl, "creator": creator_zaehl, "karten": karten},
                                               ensure_ascii=False, indent=1,
                                               default=str), encoding="utf-8")
    fam = defaultdict(list)
    for k in karten:
        fam[str(k.get("familie"))].append(k)
    z = ["# Stil-Bibliothek: Index", "", f"{len(karten)} Stil-Karten in {len(fam)} Familien. Maschinenlesbar: `index.json`.", "",
         "So liest man die Felder: `braucht` heißt „eins davon reicht“; ob das eigene Material trägt, entscheidet der Kern der Karte "
         "(Beispiel: ein Kern ohne Fotos lässt sich mit Illustrationen oder nur Typo bauen). `abnahme` gilt im Format der Quelle "
         "(`format_quelle`). Formatfest sind Schnitte je Sekunde, Shot-Median und LUFS; Helligkeit und Farbigkeit dürfen im Hochformat "
         "um 0,03 höher liegen, außer die Karte hat einen eigenen Block `abnahme_9x16`. Gemessen wird mit `starter/werkzeuge/abnahme.py`.",
         "",
         "Lautheit: −14 LUFS ist der Standard. Nennt die Karte einen Bereich, gilt die Karte, solange er innerhalb −14 ± 1 bleibt "
         "(Ziel dann im gemeinsamen Teil, etwa −13,5). ⚠ LUFS hinter einer Karte heißt: Ihr Bereich liegt ganz außerhalb von −14 ± 1; "
         "die Messwerte der Vorlage bleiben stehen, gebaut wird trotzdem mit −14 ± 1, und dieser eine Wert fällt in der Abnahme durch.",
         "",
         "Filtern: `python -I werkzeuge/bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook` gibt die passenden "
         "Karten als Tabelle aus. Nur mit Code baubar (braucht nur `nur-typo` oder `illustrationen`): `--filter nur_code=ja` oder "
         "`--filter braucht<=nur-typo,illustrationen`.",
         "",
         "✎ hinter einer Karte heißt: Ein Zeichen-Motor malt den Stil aus Code (`bauweg: animskill`, Motor-Kennung dahinter, Vorlage "
         "`KARTE_VORLAGE_MOTOR.md`); die Karte hat Sollwerte statt einer Messung. Nur diese Karten: `--filter bauweg=animskill`, "
         "je Motor `--filter zeichen_motor=huashu`.",
         ""]
    for f in sorted(fam, key=lambda x: (-len(fam[x]), x)):
        z += [f"## {f} ({len(fam[f])})", "", "| Karte | kurz | Energie | Aufwand | Einsatz |", "|---|---|---:|---|---|"]
        for k in sorted(fam[f], key=lambda k: (-(k.get("energie") or 0), k["id"])):
            ein = ", ".join(map(str, k.get("einsatz") or []))
            lage = lufs_lage(k)
            marke = f" ⚠ LUFS {lage[0][0]:g} bis {lage[0][1]:g}" if lage and not lage[1] else ""
            if k.get("zeichen_motor"):
                marke += f" ✎ `{k['zeichen_motor']}`"
            z.append(f"| [{k.get('name')}]({k['datei']}){marke} | {k.get('kurz')} | {k.get('energie')} | {k.get('motor_aufwand')} | {ein} |")
        z.append("")
    abw = sorted((k for k in karten if lufs_lage(k) and not lufs_lage(k)[1]), key=lambda k: k["id"])
    z += ["## Schlag-Angaben im Ton gegen das Tempo", ""]
    if schlag:
        z += [f"{len(schlag)} Stellen: Das Feld `ton` nennt einen Schlagabstand, der bei dem genannten Tempo kein ganzer Schlag ist "
              "(Toleranz 12 %). Nicht umgeschrieben; beim Bau gilt das gemessene Raster (`takt.py`), der Abstand im Text ist dann eine "
              "Beschreibung, keine Vorgabe.", "", "| Karte | Abstand | Tempo | in Schlägen | Textstelle |", "|---|---:|---:|---:|---|"]
        z += [f"| [{k.get('name')}]({k['datei']}) | {sek:g} s | {bpm:g} BPM | {schl:g} | {stelle} |" for k, (sek, bpm, schl, stelle) in schlag]
    else:
        z.append("Keine: Jeder Schlagabstand im Feld `ton` passt aufs genannte Tempo.")
    z += ["", "## Lautheit außerhalb −14 ± 1", ""]
    if abw:
        z += [f"{len(abw)} Karten nennen in `abnahme.lufs` einen Bereich ohne Überschneidung mit −14 ± 1 (Messwert der Vorlage, nicht "
              "umgeschrieben). Gebaut wird mit −14 ± 1; der LUFS-Wert der Abnahme ist bei diesen Karten kein Ziel.", "",
              "| Karte | abnahme.lufs |", "|---|---|"]
        z += [f"| [{k.get('name')}]({k['datei']}) | {lufs_lage(k)[0][0]:g} bis {lufs_lage(k)[0][1]:g} |" for k in abw]
    else:
        z.append("Keine: Jeder Bereich in `abnahme.lufs` überschneidet sich mit −14 ± 1.")
    z.append("")
    (bib / "INDEX.md").write_text("\n".join(z), encoding="utf-8")
    e = ["# Effekte über alle Karten", "", f"Auszählung über {len(karten)} Karten. Bekannte Kennungen aus `EFFEKT_VOKABULAR.md`, "
         "darunter die neu vorgeschlagenen.", "", "| Effekt | Karten | Anteil |", "|---|---:|---:|"]
    for k, n in eff_zaehl.most_common():
        e.append(f"| `{k}` | {n} | {round(100 * n / max(len(karten), 1))} % |")
    e += ["", "## Neu vorgeschlagen", "", "| Effekt | Karten |", "|---|---:|"]
    for k, n in neu_zaehl.most_common():
        e.append(f"| `{k}` | {n} |")
    (bib / "EFFEKTE.md").write_text("\n".join(e) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
