---
id: glas-blaue-stunde
name: "Glas zur blauen Stunde"
familie: 3d-objekt
kurz: "Ein Ding am Fenster, draußen die blaue Stunde mit Stadtlichtern als Bokeh, ein warmes Kantenlicht zeichnet Glas und Rand."
kern: [kühles Fensterlicht von hinten mit warmem Kantenlicht, Stadtlichter als weiches Bokeh hinter dem Helden, "Glas oder klare Form mit echter Brechung"]
energie: 2
format_quelle: "9:16"
laenge_s: [10, 25]
bauweg: animskill
animskill:
  motor: kino3d
  stil: "blaue_stunde"
  quelle: "src/kino/motor/licht.ts"
  schrift: [schmal, grotesk]
lizenz: "Eigener Code des Pakets (Paketlizenz); three.js, React Three Fiber MIT, postprocessing Zlib, Remotion nach LIZENZ.md Abschnitt 9; Schriften OFL"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 14
  schnitte_pro_s: 0.05
  ereignisse_pro_s: 0.7
  lufs: -14
  helligkeit: 0.4
  farbigkeit: 0.16
palette:
  grund: "#0B0D18"
  text: "#F1F2F8"
  akzent: "#FFB070"
  licht: "#7F9DFF"
  blau: "#3E5AA0"
effekte: [3d-render, 3d-schrift, geringe-schaerfentiefe, partikel, orbit, push-in, glow, vignette, filmkorn, farblook-warm-kalt, untertitel, sprechstimme, geraeusche]
kamera: "Ein langsamer Bogen um den Helden, dann ein Nahschuss auf Glas und Kante, zum Schluss ein Push-in; fließend, nie über 6 Bilder Stillstand."
ton: "Kühles, leises Bett aus Code (allein um −24 LUFS), Atmo Stadt am Abend, feine Geräusche (Sand, Schimmer, Tick), die Stimme trägt; gesamt −14 LUFS, heller Schluss."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, intro, produkt]
zweck: [wissen, zitat, stimmung, erklaeren]
branchen_passt: [bildung, immobilien, finanzen, technik, tourismus]
branchen_nie: []
abnahme:
  shot_median_s: [5, 60]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.25, 0.55]
  farbigkeit: [0.08, 0.28]
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
# Glas zur blauen Stunde

Ein Ding steht vor einem großen Fenster, draußen ist es blau und die Lichter der Stadt zerfließen zu weichen Kreisen. Ein warmes Kantenlicht von vorn rechts zeichnet Rand und Glas. Still und nachdenklich; die Energie kommt aus der Kreisfahrt und aus dem, was im Glas passiert.

## Kern
- Kühles Fensterlicht von hinten (Stärke 1,5) und ein warmes Kantenlicht (60 cd, nah) zeichnen den Helden.
- Stadtlichter als Bokeh hinter dem Helden, der Hintergrund bleibt weich.
- Glas oder eine klare Form mit echter Brechung (Dicke, Absorption, Farbsäume).

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 3D aus Code, Belichtung 0,78, Volumen nur schwach (0,12, g 0,2), Staub kühl. Farben: grund `#0B0D18`, text `#F1F2F8`, akzent `#FFB070`, licht `#7F9DFF`, blau `#3E5AA0`.
- **Bewegung:** Bogen um den Helden, die Bokeh-Kreise wandern mit; der Held tut etwas Leises (Sand läuft, Wasser steht, Licht bricht).
- **Ton:** Kühles Bett, Atmo Stadt am Abend, feine Geräusche, Stimme vorn.
- **Text:** Zwei bis drei 3D-Wörter (Stil `eis` oder `kreide`) in der oberen Bildhälfte, dazu Untertitel.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Bogen vor dem Fenster | 40 % | Held 35 bis 55 %, Mitte, Fenster mit Bokeh dahinter | 4 bis 7 s |
| Nahschuss auf Glas und Kante | 30 % | Glas 60 bis 90 %, Brechung und Kantenlicht sichtbar | 3 bis 5 s |
| Push-in zum Schluss | 20 % | Held 40 bis 70 %, Wort im Raum oder Pointe | 2 bis 4 s |
| Wort im Raum | 10 % | ein 3D-Wort vor dem Helden, mindestens 1,2 s sichtbar | 1,2 bis 3 s |

## Regler
Heldenfigur (Sanduhr, Wasserglas oder eigene Form), Fensterseite, Stärke des Kantenlichts, Zahl der Stadtlichter über `licht.himmel`, Kamerarezepte, Wörter. Fest bleiben die Spreizung kühl außen, warm an der Kante, und das Bokeh. Der Zug darf Tischfarbe und Akzent der Untertitel setzen; das Licht bleibt das des Rezepts.

## Fallen
- Blick ins Fensterlicht mit starkem Volumen und Vorwärtsstreuung gibt Milchglas: Volumen 0,12, g 0,2, Kantenlicht 60 cd nah (so im Rezept), nicht hochdrehen.
- Glas wirft keinen Schatten und steht nicht im Volumen; wer einen Schatten will, braucht eine undurchsichtige Fassung (Sanduhr mit Gestell).
- Sand braucht eine ebene Füllung an der Wand unter dem Kegel, sonst schwebt der Kegel; der Strahl braucht Körner, sonst ist er ein Stab (Requisit `sanduhr` macht beides).
- Detail-Einstellungen lassen keinen Platz für 3D-Wörter: Wörter in Halbtotalen legen.
- Die Beispielszene ist für 9:16 gebaut; im Querformat überlappen Wörter leichter den Rahmen des Helden (Probe 16:9: „IMMER GLEICH“ lag an der Oberkante der Sanduhr). Layout-Check und ein Standbild je Format.

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems. In der Szene: `"ton": {"bett": {"stimmung": "kuehl"}, "atmo": "stadt_abend", "schluss": "glocke_leise", "ereignisse": [{"t": "w3", "typ": "sand", "staerke": 0.5, "dauer": 2.0}]}`.

## Bauweg
3D-Kino-Motor `kino3d`, Licht-Rezept `blaue_stunde`, Quelle `src/kino/motor/licht.ts`. Muster zum Lesen: `starter/werkzeuge/animskills/motoren/kino3d_dateien/beispiel/sanduhr/szene.json`. Kein Remotion-Bau im Starter: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor kino3d --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec` (Felder im Kopf von `starter/werkzeuge/animskills/motoren/kino3d.py`):

```json
{"szene": "kino3d/szene.json", "licht": "blaue_stunde"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 5 bis 60 s, Schnitte je Sekunde 0,0 bis 0,3, Helligkeit 0,25 bis 0,55, Farbigkeit 0,08 bis 0,28, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Helligkeit und Farbigkeit stammen aus einem Probe-Standbild. Vor dem Vollrender: Layout-Check ohne blocker, drei Standbilder zeigen alle drei Kern-Merkmale, Bildmitte nie milchig.
