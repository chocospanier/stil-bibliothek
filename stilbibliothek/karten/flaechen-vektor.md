---
id: flaechen-vektor
name: "Flächenvektor"
familie: strichzeichnung
kurz: "Flache Vektorformen schließen sich Pfad für Pfad, Füllung springt ein, lange Schlagschatten und feines Korn geben Tiefe."
kern: ["die Füllung springt ein, sobald sich ein Pfad schließt", lange Schlagschatten im 45-Grad-Winkel mit Verlauf, feines Korn nur auf den Schattenseiten]
energie: 3
format_quelle: "9:16"
laenge_s: [12, 60]
bauweg: animskill
animskill:
  motor: anidoodle
  stil: "flatVector"
  quelle: "skills/anidoodle/references/styles/flatVector.md"
  schrift: [hand, grotesk]
lizenz: "Apache-2.0; NOTICE des Motors in LIZENZ.md und Abspann, Klangpaket des Motors nicht enthalten und nicht nötig"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 8
  schnitte_pro_s: 0.12
  ereignisse_pro_s: 1.0
  lufs: -14
  helligkeit: 0.75
  farbigkeit: 0.21
palette:
  grund: "#F2EEE6"
  text: "#1F2A44"
  akzent: "#F06A4A"
  licht: "#FFC857"
  blau: "#3A7CA5"
effekte: [strich-fuer-strich, kamera-steht, papier, geraeusche, symbol-pop]
kamera: "Die Kamera steht, solange gezeichnet wird; zwischen den Durchgängen schiebt sie langsam über das Blatt (2 bis 5 % Push-in) oder zieht am Schluss zurück."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber Stift, Pinsel, Kreide, Schere oder Nadel auf dem Material, leise und im Takt der Striche, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, intro, uebergang]
zweck: [erklaeren, wissen, marke-image]
branchen_passt: [technik, bildung, finanzen]
branchen_nie: []
abnahme:
  shot_median_s: [3, 40]
  schnitte_pro_s: [0.0, 0.4]
  helligkeit: [0.57, 0.9]
  farbigkeit: [0.06, 0.46]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
spielraum:
  palette: akzent
  schrift: klasse
  blitzbild_bilder: [2, 4]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.4, 1.0]
  korn: [0.0, 0.04]
  vignette: [0.0, 0.3]
  beat_versatz_16tel: [0, 1]
  textgroesse_prozent: [-10, 10]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: text
  hell: grund
  licht: licht
quelle: Eigene Beschreibung eines offenen Zeichen-Motors (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken des Motors übernommen.
---
# Flächenvektor

Flache Vektorformen schließen sich Pfad für Pfad, Füllung springt ein, lange Schlagschatten und feines Korn geben Tiefe. Die Energie kommt aus dem Entstehen selbst: der Zuschauer sieht eine Hand arbeiten, ohne dass je eine Hand zu sehen ist.

## Kern
- Die Füllung springt ein, sobald sich ein Pfad schließt.
- Lange Schlagschatten im 45-Grad-Winkel mit Verlauf.
- Feines Korn nur auf den Schattenseiten.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Zeichenstift-Pfade einer Vektor-App, flache Füllungen, die landen, sobald sich ein Pfad schließt, lange Schatten mit Verlauf, ein Kornpinsel auf den Schattenseiten. Farben: grund `#F2EEE6`, text `#1F2A44`, akzent `#F06A4A`, licht `#FFC857`, blau `#3A7CA5`.
- **Bewegung:** Nichts blendet ein, alles wird gezeichnet: der Strich wächst im Tempo einer Hand, nach jedem Durchgang ein kurzer Atem, danach atmet das fertige Bild weiter (Wind, Licht, Wasser).
- **Ton:** Leises Bett aus Code-Musik, darüber Stift, Pinsel, Kreide, Schere oder Nadel auf dem Material, leise und im Takt der Striche; die Stimme liegt vorn.
- **Text:** Wenige Wörter, als Untertitel der Brücke oder im Material gezeichnet (Handschrift, Kreide, Stempel); nie Text über das halbe Bild.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Das Bild entsteht | 45 % | Motiv 40 bis 70 % der Bildhöhe nach Drittelregel, Grund ist das Medium (Papier, Tafel, Leinen, Holz) | 3 bis 8 s je Durchgang |
| Atmendes Bild | 25 % | fertiges Motiv, eine kleine Bewegung (Wind, Licht, Wasser, ein Blinzeln) | 1 bis 3 s |
| Fahrt über das Blatt | 20 % | langsame Fahrt über das fertige Bild zum nächsten Detail | 2 bis 4 s |
| Wort im Medium | 10 % | ein bis vier Wörter, unteres Sechstel frei | 1,5 bis 3 s |

## Regler
Tempo der Hand (ein Durchgang 2 bis 8 s), Dichte der Striche, Anteil Entstehen gegen fertiges Bild, Kamera (steht, schiebt, zieht zurück), Akzent und Licht aus dem Zug. Fest bleiben Medium, Reihenfolge der Striche und Grund. Der Zug tauscht nur Akzent und Licht, Grund und Linie bleiben die des Stils.

## Fallen
- Umlaute und ß zeichnet die Federschrift (Normschrift) des Motors erst mit dem Flicken aus `einrichten.py` (federschrift.ts); ein frischer Klon ohne Flicken lässt sie weg. Nach dem Einrichten `--pruefen` laufen lassen und ein Wort mit Umlaut als Probe zeichnen; bis dahin Wörter mit Umlaut als Untertitel der Brücke.
- Der letzte Geräusch-Cue ist nie `impact`: der Schluss klingt hell (`chime`), sonst meldet die Tonprüfung einen dumpfen Schlag.
- Eine Form, die aufploppt oder einfadet, verrät den Code: für Filme den Zeichenweg des Stils nehmen (Modul mit Draw im Namen, wo es eins gibt), nicht das fertige Standbild.
- Toter Raum fällt im Prüfschritt des Motors durch: in jeder Sekunde ändert sich sichtbar etwas, ein fertiges Bild atmet (Wind, Licht, Kamera).
- Der Motor rechnet streng gleich bei jedem Lauf und kennt keine nachträglichen Filter: Unschärfe, Korn und Farbe gehören in den Stil, nicht als Filter auf das fertige Video.
- Ein fremder Farbtausch macht aus dem Stil nur seinen Nachbarstil in falschen Farben: der Zug tauscht Akzent und Licht, Medium und Grund bleiben.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: Stift, Pinsel, Kreide, Schere oder Nadel auf dem Material, leise und im Takt der Striche. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `anidoodle`, Stil `flatVector`, Quelle im Motor `skills/anidoodle/references/styles/flatVector.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor anidoodle --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/anidoodle.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a phone slowly turning into a wallet“.

```json
{"film": "anidoodle/film.ts", "geraeusche": [{"kind": "ink", "wort": "<Stichwort>", "gainDb": -6}]}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 3 bis 40 s, Schnitte je Sekunde 0,0 bis 0,4, Helligkeit 0,57 bis 0,9, Farbigkeit 0,06 bis 0,46, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
