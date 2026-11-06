---
id: kante-im-studio
name: "Kante im Studio"
familie: 3d-objekt
kurz: "Ein Objekt frei auf dunklem Grund, zwei Kantenlichter warm und kühl zeichnen seine Form, ein weiches Licht von oben links gibt ihm Körper."
kern: [Objekt frei auf dunklem Grund ohne Zimmer, "zwei Kantenlichter, warm von hinten links und kühl von hinten rechts", weiches Schlüssellicht von oben links]
energie: 2
format_quelle: "9:16"
laenge_s: [8, 20]
bauweg: animskill
animskill:
  motor: kino3d
  stil: "studio_kante"
  quelle: "src/kino/motor/licht.ts"
  schrift: [schmal, grotesk]
lizenz: "Eigener Code des Pakets (Paketlizenz); three.js, React Three Fiber MIT, postprocessing Zlib, Remotion nach LIZENZ.md Abschnitt 9; Schriften OFL"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 12
  schnitte_pro_s: 0.05
  ereignisse_pro_s: 0.7
  lufs: -14
  helligkeit: 0.36
  farbigkeit: 0.11
palette:
  grund: "#0A0A0B"
  text: "#F4F4F4"
  akzent: "#FFD0A0"
  licht: "#FFF1E2"
  blau: "#A8C4FF"
  wand: "#202124"
effekte: [3d-render, 3d-schrift, geringe-schaerfentiefe, orbit, push-in, glow, vignette, filmkorn, makro-material, untertitel, sprechstimme, geraeusche]
kamera: "Ein langsamer Bogen um das Objekt, Nahschuss über Material und Kante, zum Schluss ein Push-in auf die Pointe; fließend, nie über 6 Bilder Stillstand."
ton: "Helles, leises Bett aus Code (allein um −24 LUFS), Atmo Studio, wenige klare Geräusche (Schimmer, Klick, Whoosh), die Stimme trägt; gesamt −14 LUFS, Schluss mit hellem Akkord."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo, intro]
zweck: [produktwerbung, angebot, marke-image]
branchen_passt: [technik, mode-beauty, lebensmittel-feinkost, werkstatt-auto, handwerk]
branchen_nie: []
abnahme:
  shot_median_s: [5, 60]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.2, 0.55]
  farbigkeit: [0.04, 0.22]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 4]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.3, 0.7]
  korn: [0.0, 0.04]
  vignette: [0.3, 0.5]
  beat_versatz_16tel: [0, 1]
  textgroesse_prozent: [-10, 10]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: grund
  hell: text
  licht: licht
quelle: Eigene Beschreibung des 3D-Kino-Motors des Pakets (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken Dritter übernommen.
---
# Kante im Studio

Ein Objekt steht frei auf dunklem Grund, kein Zimmer, kein Fenster. Zwei Kantenlichter, eins warm, eins kühl, ziehen seine Umrisse nach, ein weiches Licht von oben links gibt ihm Körper. Ruhig und wertig wie ein Produktfoto, das sich bewegt; die Spannung liegt im Material und in der Fahrt um die Form.

## Kern
- Objekt frei auf dunklem Grund (`set.typ: studio`), gern auf einem Podest.
- Zwei Kantenlichter: warm 120 cd von hinten links, kühl 90 cd von hinten rechts.
- Weiches Schlüssellicht 70 cd von oben links, Halbschatten 0,8.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 3D aus Code, dunkler Grund ohne Nebel, Volumen nur aus dem Schlüssellicht (0,25). Farben: grund `#0A0A0B`, text `#F4F4F4`, akzent `#FFD0A0`, licht `#FFF1E2`, blau `#A8C4FF`, wand `#202124`.
- **Bewegung:** Bogen um das Objekt, Lichtkanten wandern über die Form; was sich am Objekt bewegt (Deckel, Flamme, Zeiger), bewegt sich auf den Wörtern der Stimme.
- **Ton:** Helles, leises Bett, Atmo Studio, wenige klare Geräusche, Stimme vorn.
- **Text:** Ein bis drei 3D-Wörter (Stil `messing` oder `glut`), Name oder Preis als Wort im Raum nur, wenn die Bestellung es will; dazu Untertitel.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Bogen um das Objekt | 40 % | Objekt 40 bis 60 %, Mitte, Kanten sichtbar, Grund dunkel | 4 bis 7 s |
| Nahschuss über Material | 30 % | Oberfläche 70 bis 100 %, Kratzer, Rillen, Glanz | 3 bis 5 s |
| Push-in auf die Pointe | 20 % | Objekt 50 bis 70 %, Wort im Raum darüber | 2 bis 4 s |
| Wort im Raum | 10 % | ein 3D-Wort vor dem Objekt, mindestens 1,2 s sichtbar | 1,2 bis 3 s |

## Regler
Objekt und Podest, Grundfarbe (`set.farbe`, dunkel halten), Stärke und Farbe der Kanten über `licht.kanten`, Belichtung (`"licht": {"rezept": "studio_kante", "post": {"belichtung": 0.85}}`), Kamerarezepte, Wörter. Fest bleiben der dunkle Grund und die zwei farbigen Kanten. Bei `produktwerbung` und `angebot` nimmt die Grundfarbe den Hausgrund und die 3D-Wörter den Hausakzent; das Licht bleibt das des Rezepts.

## Fallen
- Im Paket gibt es keine Beispielszene mit diesem Rezept: von `beispiel/espresso` ableiten, `"set": {"typ": "studio", "farbe": "#1b1d22"}`, Zimmer-Beiwerk (Pflanze, Bücher, Fenster) weglassen, `dampf` nur, wenn das Objekt dampft.
- Helle Metallflächen fressen aus: in der Probe war eine Alu-Kanne vorn fast weiß, die Kanten glühten im Bloom. Belichtung 0,8 bis 0,9 über `licht.post.belichtung`, Rauheit um 0,35 bis 0,4, und am Standbild prüfen.
- Glattes Metall braucht Metall: `metall: 1`, Rauheit um 0,3, sonst sieht es aus wie Gips.
- Ohne Fenster gibt es keine Lichtschächte; das Volumen kommt nur aus dem Schlüssellicht und bleibt schwach. Wer Schächte will, nimmt die Karte `lamellen-goldstunde`.
- Echte Produkte des Kunden sind hier nachgebaute 3D-Formen, keine Fotos: Form und Farbe gegen ein Foto des Produkts prüfen, Logos nur, wenn der Mensch es will.

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems. In der Szene: `"ton": {"bett": {"stimmung": "hell"}, "atmo": "studio", "schluss": "akkord_hell", "ereignisse": [{"t": "w2", "typ": "schimmer", "staerke": 0.5, "dauer": 1.4}]}`.

## Bauweg
3D-Kino-Motor `kino3d`, Licht-Rezept `studio_kante`, Quelle `src/kino/motor/licht.ts`. Kein Remotion-Bau im Starter: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor kino3d --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec` (Felder im Kopf von `starter/werkzeuge/animskills/motoren/kino3d.py`):

```json
{"szene": "kino3d/szene.json", "licht": "studio_kante"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 5 bis 60 s, Schnitte je Sekunde 0,0 bis 0,3, Helligkeit 0,2 bis 0,55, Farbigkeit 0,04 bis 0,22, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Helligkeit und Farbigkeit stammen aus einem Probe-Standbild. Vor dem Vollrender: Layout-Check ohne blocker, drei Standbilder zeigen alle drei Kern-Merkmale, keine Fläche des Objekts ist weiß ausgefressen.
