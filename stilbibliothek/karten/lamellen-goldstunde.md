---
id: lamellen-goldstunde
name: "Lamellen-Goldstunde"
familie: 3d-objekt
kurz: "Ein Ding auf dem Tisch im warmen Abendlicht, das durch Lamellen fällt; Lichtschächte im Staub, die Kamera gleitet heran."
kern: [warmes Sonnenlicht in Streifen durch Lamellen auf dem Helden, sichtbare Lichtschächte mit Staub, "eine Heldenfigur mit Gebrauchsspuren in geringer Schärfentiefe"]
energie: 2
format_quelle: "9:16"
laenge_s: [10, 25]
bauweg: animskill
animskill:
  motor: kino3d
  stil: "goldstunde_jalousie"
  quelle: "src/kino/motor/licht.ts"
  schrift: [schmal, grotesk]
lizenz: "Eigener Code des Pakets (Paketlizenz); three.js, React Three Fiber MIT, postprocessing Zlib, Remotion nach LIZENZ.md Abschnitt 9; Schriften OFL"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 14
  schnitte_pro_s: 0.05
  ereignisse_pro_s: 0.8
  lufs: -14
  helligkeit: 0.33
  farbigkeit: 0.16
palette:
  grund: "#2A1A10"
  text: "#F7EFE4"
  akzent: "#FFAB5E"
  licht: "#FFD9A0"
  wand: "#C9B49A"
effekte: [3d-render, 3d-schrift, lichtstreifen, partikel, geringe-schaerfentiefe, push-in, orbit, glow, vignette, filmkorn, farblook-warm-kalt, untertitel, sprechstimme, geraeusche]
kamera: "Immer in Bewegung: Push-in aus der Halbtotalen, Nahschuss mit enger Schärfe, am Schluss ein langsamer Bogen; die Segmente gehen fließend ineinander, nie über 6 Bilder Stillstand."
ton: "Leises Bett aus Code (warme Flächen, keine Trommeln, allein um −24 LUFS), Atmo Küche, Geräusche auf den Aktionen, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell mit einer leisen Glocke."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, produkt, intro]
zweck: [erklaeren, wissen, produktwerbung, stimmung]
branchen_passt: [lebensmittel-feinkost, gastro, handwerk, bildung, technik]
branchen_nie: []
abnahme:
  shot_median_s: [5, 60]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.2, 0.48]
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
# Lamellen-Goldstunde

Ein einzelnes Ding auf einem Holztisch, die tiefe Sonne fällt durch eine Jalousie und legt warme Streifen darüber, im Staub stehen die Lichtschächte. Ruhig und warm; die Spannung kommt aus der Fahrt heran und aus dem Moment, in dem das Ding etwas tut (zischen, rieseln, ausschlagen).

## Kern
- Warmes Sonnenlicht in Streifen durch Lamellen trifft den Helden (das Fenster zielt von selbst auf ihn).
- Sichtbare Lichtschächte: echtes Volumenlicht mit Staub, nicht nur ein heller Fleck.
- Eine Heldenfigur mit Gebrauchsspuren (Kratzer, Ränder, Flecken), der Hintergrund weich in der Schärfentiefe.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 3D aus Code mit Kinolicht: Sonne Stärke 13, Azimut −68°, Höhe 20°, Volumen Dichte 0,26, Belichtung 0,92, Schatten leicht kühl, Lichter warm. Farben: grund `#2A1A10`, text `#F7EFE4`, akzent `#FFAB5E`, licht `#FFD9A0`, wand `#C9B49A`.
- **Bewegung:** Die Kamera fährt immer; Dinge mit Handlung bewegen sich selbst (Flamme ab Bild, Sand läuft, Nadel schwingt aus, Dampf wächst als weiche Schwaden).
- **Ton:** Warmes Bett aus Akkordflächen, Atmo Küche, Geräusche auf den Aktionen (zisch, blubbern, dampf, klick), Stimme vorn.
- **Text:** Zwei bis vier Schlagwörter als 3D-Buchstaben im Raum (Anton, Stil `glut`), dazu Untertitel; der Löser setzt jedes Wort so, dass es nie angeschnitten ist und nie den Helden verdeckt.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Push-in aus der Halbtotalen | 35 % | Held 25 bis 45 %, Mitte, Fenster mit Lamellen seitlich, Lichtschächte sichtbar | 3 bis 6 s |
| Nahschuss mit enger Schärfe | 35 % | ein Teil des Helden 60 bis 90 %, Streifen auf der Oberfläche, Rest weich | 3 bis 6 s |
| Bogen zum Schluss | 20 % | Held 35 bis 55 %, Kamera kreist langsam, Schärfe weiter | 3 bis 5 s |
| Wort im Raum | 10 % | ein 3D-Wort vor dem Helden, obere Bildhälfte, mindestens 1,2 s sichtbar | 1,2 bis 3 s |

## Regler
Heldenfigur und Beiwerk, Fensterseite (links oder hinten), Lamellenwinkel, Tischfarbe (`set.tisch`), Kamerarezepte und ihre Längen, Zahl der 3D-Wörter (zwei bis vier), einzelne Lichtwerte über `licht` in der Szene (etwa `"sonne": {"az": -60}`). Fest bleiben Licht durch Lamellen, Volumen und die warme Grundstimmung. Der Zug darf die Tischfarbe und die Farbe der Untertitel-Akzente setzen; das Licht bleibt das des Rezepts.

## Fallen
- Wände dürfen nicht über die Zimmerecke hinausragen, sonst schatten sie das Fenster ab und die Sonne kommt nicht herein.
- Sonne quer zur Blickachse macht kaum sichtbare Schächte, Gegenlicht macht Schächte, aber der Held zeigt die Schattenseite: im Rezept steht der Kompromiss (Seitenlicht von vorn, g 0,35, Dunst mit Rauschen 0,85), nicht verstellen.
- Glattes Metall zeigt keine Lamellenstreifen: `metall: 1`, Rauheit um 0,3 bis 0,4, sonst wirkt eine Kanne wie Gips oder spiegelt nur.
- Detail-Einstellungen lassen keinen Platz für 3D-Wörter: Wörter in Halbtotalen legen, der Layout-Check (`zeitplan`) meldet es.
- Dampf als Flächen wirkt wie Regen auf Glas; der Motor nimmt weiche Schwaden als Punkt-Sprites, `dampf` mit `ab`, `voll` und `hoehe` setzen.
- Untertitel auf hellem Grund sind unlesbar: die Kino-Untertitel des Motors weichen dem Helden aus (dafür `"untertitel": {"an": false}` in der Bestellung), sonst setzt die Brücke sie unten.
- Die Beispielszenen sind für 9:16 gebaut; im Querformat Wortplätze und Abstände neu prüfen (Layout-Check und ein Standbild).

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems. In der Szene: `"ton": {"bett": {"stimmung": "warm"}, "atmo": "kueche", "schluss": "glocke_leise", "sfx_lufs": -23.5, "ereignisse": [{"t": "w1", "typ": "zisch", "staerke": 0.55, "dauer": 1.1}]}`; Ereignisse auf Wortanfänge (`"w5"`).

## Bauweg
3D-Kino-Motor `kino3d`, Licht-Rezept `goldstunde_jalousie`, Quelle `src/kino/motor/licht.ts`. Muster zum Lesen: `starter/werkzeuge/animskills/motoren/kino3d_dateien/beispiel/espresso/szene.json`. Kein Remotion-Bau im Starter: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor kino3d --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json --nur stimme
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json --nur look --zeiten 0.5,5,10
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec` (Felder im Kopf von `starter/werkzeuge/animskills/motoren/kino3d.py`); die Szene schreibst du nach dieser Karte, Zeitangaben an die Wortliste der Stimme:

```json
{"szene": "kino3d/szene.json", "licht": "goldstunde_jalousie"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 5 bis 60 s (die Kamera schneidet nicht, sie fährt), Schnitte je Sekunde 0,0 bis 0,3, Helligkeit 0,2 bis 0,48, Farbigkeit 0,08 bis 0,28, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Helligkeit und Farbigkeit stammen aus einem Probe-Standbild. Vor dem Vollrender: Layout-Check ohne Meldung der Stufe blocker, drei Standbilder zeigen alle drei Kern-Merkmale, die Bildprüfung des Motors (`kino3d_bildpruefung.json`) meldet kein schwarzes und kein ausgewaschenes Bild.
