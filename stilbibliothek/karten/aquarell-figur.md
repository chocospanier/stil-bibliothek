---
id: aquarell-figur
name: "Aquarell-Figur"
familie: malstil
kurz: "Eine eigene gezeichnete Figur spielt eine kleine Szene in Pinselstrichen und Aquarell, die Linie kocht leicht, jede Szene hat einen Übergang."
kern: [eine eigene Figur mit klarer Emotion trägt jede Szene, "Pinselstriche, flache Flächen und leicht kochende Kontur, alles von Hand", "kein Text im Bild, ein Übergang zu jeder Szene"]
energie: 3
format_quelle: "9:16"
laenge_s: [10, 60]
bauweg: animskill
animskill:
  motor: pinsel
  stil: "aquarell"
  quelle: "ANIMATION_GUIDE.md"
  schrift: [hand, grotesk]
lizenz: "MIT, dazu p5.js (LGPL-2.1) und p5.brush (MIT); die Beispielfigur des Motors nie verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 4.5
  schnitte_pro_s: 0.2
  ereignisse_pro_s: 1.2
  lufs: -14
  helligkeit: 0.76
  farbigkeit: 0.17
palette:
  grund: "#F5EFE2"
  text: "#2E2A28"
  akzent: "#D9734A"
  licht: "#F2C46B"
  blau: "#6E9BC2"
effekte: [malerei, push-in, geraeusche, stop-motion]
kamera: "Langsame Fahrt oder Push-in über die gemalte Szene (2 bis 5 %), Wechsel über den eigenen Übergang des Stils."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, intro, uebergang]
zweck: [geschichte, kinder, stimmung]
branchen_passt: [kinder-familie, bildung, musik-kultur]
branchen_nie: [finanzen]
abnahme:
  shot_median_s: [2, 20]
  schnitte_pro_s: [0.03, 0.5]
  helligkeit: [0.58, 0.91]
  farbigkeit: [0.05, 0.39]
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
  korn: [0.03, 0.06]
  vignette: [0.3, 0.5]
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
# Aquarell-Figur

Eine eigene gezeichnete Figur spielt eine kleine Szene in Pinselstrichen und Aquarell, die Linie kocht leicht, jede Szene hat einen Übergang. Getragen wird es vom Wiedererkennen einer Epoche, ohne dass ein bekanntes Bild nachgestellt wird.

## Kern
- Eine eigene Figur mit klarer Emotion trägt jede Szene.
- Pinselstriche, flache Flächen und leicht kochende Kontur, alles von Hand.
- Kein Text im Bild, ein Übergang zu jeder Szene.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** P5.js mit p5.brush: Pinselstriche, flache 2D-Flächen und leicht kochende Linie, Aquarellflächen, eine eigene Figur mit Modellblatt für Emotionen und Ansichten. Farben: grund `#F5EFE2`, text `#2E2A28`, akzent `#D9734A`, licht `#F2C46B`, blau `#6E9BC2`.
- **Bewegung:** Das Leitmotiv des Stils bewegt sich die ganze Zeit (Wirbel, Lichtfleck, Tusche, Goldglanz, Punkte); Szenen wechseln über den eigenen Übergang des Stils.
- **Ton:** Leises Bett aus Code-Musik, darüber leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang; die Stimme liegt vorn.
- **Text:** Ein bis vier Wörter in einer Leerfläche der Szene oder als Untertitel der Brücke; Schrift aus der Zeit des Stils, wenn sie lesbar bleibt.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Gemalte Szene lebt | 50 % | eigene Komposition für das Thema, Leitmotiv bewegt sich, Motiv 40 bis 70 % der Bildhöhe | 3 bis 6 s |
| Eintritt in den Stil | 15 % | der Übergang des Stils trägt den Wechsel | 0,6 bis 1,5 s |
| Nahaufnahme der Malspur | 15 % | Detail mit sichtbarem Material (Strich, Punkt, Blattgold, Tusche) | 1 bis 3 s |
| Weite mit Wort | 20 % | Landschaft oder Raum mit Leerfläche für ein bis vier Wörter, unteres Sechstel frei | 2 bis 4 s |

## Regler
Stärke der Leitmotiv-Bewegung, Länge je Szene, Anteil Nahaufnahme, Akzent und Licht aus dem Zug. Fest bleiben Pinselführung, Farblogik und Übergang des Stils. Der Zug tauscht nur Akzent und Licht, Grund und Linie bleiben die des Stils.

## Fallen
- In jeder Szene muss etwas passieren, und der Zuschauer braucht Zeit, es zu sehen: Handlung länger halten als gedacht, nie zwei Ereignisse zugleich.
- Die Figur des Originals ist das Maskottchen einer Firma und tabu (eine Szene, die sie aufruft, bricht den Render ab): Startfigur Klecks nehmen oder eine eigene Figur mit Modellblatt (Stimmungen, Ansichten) bauen.
- Aquarellflächen von p5.brush sind ohne eigene Grafikkarte langsam (Sekunden je Bild): auf schwachen Rechnern durch flache Flächen mit Pinselrand ersetzen.
- Die Regel des Motors lautet: kein Text im Bild. Wörter kommen als Untertitel über die Brücke.
- Motive bekannter Gemälde nie nachstellen: Malweise, Farblogik und Bewegung des Leitmotivs mitnehmen, den Bildinhalt für das eigene Thema neu komponieren.

## Ton
Dieser Motor liefert keinen Ton: das Bett kommt aus `musik.py` oder als Code-Musik eines anderen Motors, die Geräusche aus `taktbauer.py --nur-schlaege` oder eigenen Aufnahmen. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`.

## Bauweg
Zeichen-Motor `pinsel`, Stil `aquarell`, Quelle im Motor `ANIMATION_GUIDE.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor pinsel --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/pinsel.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a small fox trying to catch a butterfly“.

```json
{"sketch": "pinsel/szene.js"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 2 bis 20 s, Schnitte je Sekunde 0,03 bis 0,5, Helligkeit 0,58 bis 0,91, Farbigkeit 0,05 bis 0,39, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
