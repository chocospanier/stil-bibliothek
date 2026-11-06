---
id: lampenkegel-nacht
name: "Lampenkegel bei Nacht"
familie: 3d-objekt
kurz: "Nachts auf dem Schreibtisch: eine Schirmlampe wirft einen warmen Kegel auf ein einzelnes Ding, ringsum ist es dunkel und kühl."
kern: [eine Schirmlampe als einzige warme Quelle im dunklen Zimmer, sichtbarer Lampenkegel mit Staub, "kühles Mondlicht im Rücken, tiefe Schatten"]
energie: 2
format_quelle: "9:16"
laenge_s: [10, 25]
bauweg: animskill
animskill:
  motor: kino3d
  stil: "nacht_lampe"
  quelle: "src/kino/motor/licht.ts"
  schrift: [schmal, grotesk]
lizenz: "Eigener Code des Pakets (Paketlizenz); three.js, React Three Fiber MIT, postprocessing Zlib, Remotion nach LIZENZ.md Abschnitt 9; Schriften OFL"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 14
  schnitte_pro_s: 0.05
  ereignisse_pro_s: 0.8
  lufs: -14
  helligkeit: 0.38
  farbigkeit: 0.19
palette:
  grund: "#0A0705"
  text: "#F7EFE4"
  akzent: "#FFB468"
  licht: "#FFD29A"
  blau: "#22305E"
effekte: [3d-render, 3d-schrift, partikel, geringe-schaerfentiefe, push-in, orbit, glow, vignette, filmkorn, farblook-warm-kalt, untertitel, sprechstimme, geraeusche]
kamera: "Push-in in den Kegel, Nahschuss auf das Detail, das sich bewegt, am Schluss ein Bogen; fließend, nie über 6 Bilder Stillstand."
ton: "Leises Nacht-Bett aus Code (allein um −24 LUFS), Atmo Nachtzimmer, feine Geräusche (Tick, Nadel, Licht an, Metall), die Stimme trägt; gesamt −14 LUFS, heller Schluss."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, intro, produkt]
zweck: [wissen, geschichte, stimmung, erklaeren]
branchen_passt: [bildung, handwerk, tourismus, musik-kultur, technik]
branchen_nie: []
abnahme:
  shot_median_s: [5, 60]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.22, 0.55]
  farbigkeit: [0.1, 0.3]
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
# Lampenkegel bei Nacht

Ein Schreibtisch in der Nacht, eine Schirmlampe wirft einen warmen Kegel auf ein einzelnes Ding, im Kegel tanzt Staub, dahinter ist das Zimmer dunkel und kühl. Konzentriert und still; die Spannung kommt aus dem Detail im Licht, das sich bewegt (Nadel schlägt aus, Zeiger rückt, Deckel öffnet sich).

## Kern
- Eine Schirmlampe als einzige warme Quelle (3,2 cd, Spot 36°, Halbschatten 0,6).
- Der Lampenkegel ist sichtbar: Volumen aus der Lampe (Stärke 0,5, Dichte 0,35, g 0,5) mit Staub.
- Kühles Mondlicht im Rücken, tiefe Schatten, Belichtung 1,0.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 3D aus Code, warmer Kegel in kühler Nacht. Farben: grund `#0A0705`, text `#F7EFE4`, akzent `#FFB468`, licht `#FFD29A`, blau `#22305E`.
- **Bewegung:** Kamera fährt in den Kegel; im Licht bewegt sich ein Detail des Helden (Requisit `kompass`: Nadel schwingt gedämpft nach Nord ab `nadelAb`).
- **Ton:** Leises Nacht-Bett, Atmo Nachtzimmer, Geräusche auf den Bewegungen, Stimme vorn.
- **Text:** Zwei bis drei 3D-Wörter (Stil `messing` oder `glut`) in der oberen Bildhälfte, dazu Untertitel.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Push-in in den Kegel | 35 % | Held 30 bis 50 %, Lampe oder ihr Kegel im Bild, Rand dunkel | 3 bis 6 s |
| Nahschuss auf das bewegte Detail | 35 % | Detail 60 bis 90 %, enge Schärfe | 3 bis 6 s |
| Bogen zum Schluss | 20 % | Held 35 bis 55 %, Mondlicht als Kante | 3 bis 5 s |
| Wort im Raum | 10 % | ein 3D-Wort vor dem Helden, mindestens 1,2 s sichtbar | 1,2 bis 3 s |

## Regler
Heldenfigur und Beiwerk (Landkarte, Notiz, Stift, Bücher), Lage der Lampe, Kegelwinkel, Stärke des Monds, Kamerarezepte, Wörter. Fest bleiben die eine warme Quelle, der sichtbare Kegel und die dunklen Ränder. Der Zug darf Tisch und Akzent der Untertitel setzen; das Licht bleibt das des Rezepts.

## Fallen
- Das Rezept braucht eine `schirmlampe` unter den Requisiten; sie liefert Pose und Kegel. Ohne sie fehlt das Hauptlicht.
- Lampe im Nahbereich: Candela klein halten (rund 3 cd auf 0,5 m), sonst wird die Karte oder das Zifferblatt weiß.
- Blendung ohne Sichtprüfung leuchtet durch Schirm und Deckel: der Motor prüft je Bild den Strahl Kamera zu Quelle; `blendung.quelle` auf `lampe` lassen, nicht auf feste Koordinaten.
- Ein Deckel braucht ein Scharnier, sonst wirkt er wie eine lose Scheibe.
- Wörter werfen keine Schatten (ein Wortschatten auf dem Zifferblatt sah aus wie ein dritter Zeiger); so lassen.
- Wörter hinter dem Helden werden verdeckt: der Motor stellt Wörter immer vor den Helden, die Schärfe nimmt sie weich mit.

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems. In der Szene: `"ton": {"bett": {"stimmung": "nacht"}, "atmo": "nacht_zimmer", "schluss": "glocke_leise", "ereignisse": [{"t": "w6", "typ": "nadel", "staerke": 0.6, "dauer": 2.0}]}`.

## Bauweg
3D-Kino-Motor `kino3d`, Licht-Rezept `nacht_lampe`, Quelle `src/kino/motor/licht.ts`. Muster zum Lesen: `starter/werkzeuge/animskills/motoren/kino3d_dateien/beispiel/kompass/szene.json`. Kein Remotion-Bau im Starter: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor kino3d --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec` (Felder im Kopf von `starter/werkzeuge/animskills/motoren/kino3d.py`):

```json
{"szene": "kino3d/szene.json", "licht": "nacht_lampe"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 5 bis 60 s, Schnitte je Sekunde 0,0 bis 0,3, Helligkeit 0,22 bis 0,55, Farbigkeit 0,1 bis 0,3, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Helligkeit und Farbigkeit stammen aus einem Probe-Standbild. Vor dem Vollrender: Layout-Check ohne blocker, drei Standbilder zeigen alle drei Kern-Merkmale, nichts im Kegel ist ausgefressen.
