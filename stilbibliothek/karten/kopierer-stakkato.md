---
id: kopierer-stakkato
name: Kopierer-Stakkato
familie: kopierer
kurz: Fotokopie in Zweiton mit genau einem Signalrot, Bilder springen im Sechzehntel auf einem langsamen, schweren Beat.
kern: [Zweiton Papier und Tusche ohne Grau, genau eine leuchtende Akzentfarbe, Schnitte im Sechzehntel bei stehender Kamera]
energie: 5
format_quelle: "4:3"
laenge_s: [10, 25]
messung:
  shot_median_s: 0.17
  schnitte_pro_s: 4.3
  schnitte_verlauf: [3.7, 7.3, 1.9]
  bpm: 80
  schnitt_auf_beat: mittel
  lufs: -14.2
  helligkeit: 0.42
  kontrast: 0.30
  farbigkeit: 0.13
schnittmuster_16tel: [1, 3, 2, 1, 1, 2, 0, 2, 1, 1, 1, 4, 3, 4, 2, 2, 3, 3, 0, 0, 4, 3, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 8, 2, 1, 3, 3, 8, 3, 5]
palette:
  grund: "#E8E2D8"
  zeichnung: "#14110F"
  akzent: "#CD1726"
  schatten: "#6F5D5A"
effekte: [harter-schnitt, blitzbild, stottern, wiederholung, standbild-halt, kamera-steht, schwellwert, invertieren, ein-akzent, papier, filmkorn, strahlenkranz, kritzel, stempel, wortkolonne, mono-zeile, titelkarte, beat-getrieben, atem-vor-schlag, ton-stopp]
kamera: Steht; Bewegung entsteht nur durch Kopier-Jitter von wenigen Pixeln und durch den Schnitt.
ton: Instrumentaler, schwerer Beat um 80 BPM mit Halbtempo-Gefühl, durchgehend laut, keine Stimme, harter Stopp vor der Schlusskarte.
braucht: [fotos-figur, illustrationen, nur-typo]
motor_aufwand: mittel
einsatz: [trailer, hook, intro]
abnahme:
  shot_median_s: [0.15, 0.25]
  schnitte_pro_s: [3.0, 5.0]
  helligkeit: [0.35, 0.50]
  farbigkeit: [0.08, 0.18]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Kopierer-Stakkato

Sieht aus wie ein Stapel Fotokopien, der im Takt durch den Kopierer gejagt wird. Die Energie kommt fast nur aus dem Schnitt: 90 Schnitte in 21 Sekunden, die Kamera steht.

## Kern
- **Zweiton ohne Grau:** Jedes Bild, ob Foto oder Zeichnung, besteht nur aus Papier und Tusche. Ein einziges Graustufen-Foto bricht die Illusion.
- **Genau eine leuchtende Farbe:** Das Rot ist die Stimme des Stücks. Es markiert, was wichtig ist; eine zweite Farbe macht daraus ein Plakat statt eine Kopie.
- **Sechzehntel-Schnitt bei stehender Kamera:** Der Rhythmus entsteht durch Bildwechsel, nie durch Fahrt. Wer die Kamera bewegt, verliert den Kopierer-Charakter.

## Erkennung
- **Bild:** Papierweiß mit Kopiererstaub (feine dunkle Sprenkel, dünne senkrechte Kratzer) und Tuscheschwarz. Fotos sehen aus wie durch den Kopierer gelaufen: harter Schwellwert, Schatten laufen zu. Illustrationen sind Holzschnitt oder Stich mit dichter Schraffur. 30 bis 50 % der Bilder sind invertiert: Tusche als Grund, Zeichnung in Papierweiß. Das Signalrot färbt nur Stempel, Kritzel, Wortkolonnen und höchstens ein Objekt je Bild. Gemessen: Helligkeit 0,42, Kontrast 0,30, Farbigkeit nur 0,13, 42 % der Fläche fast schwarz.
- **Schnitt:** Median-Shot 0,17 s, 64 von 67 Shots kürzer als eine Sekunde, längster 1,5 s. Das Tempo steigt bis zur Mitte (3,7 → 7,3 Schnitte je Sekunde) und fällt zum Schluss auf 1,9. Raster: Sechzehntel bei 80 BPM (0,19 s), Halte auf Achteln und Vierteln, dazu elf Flackerbilder von zwei Frames. Übergänge: harter Schnitt, Blitzbild in Rot oder Weiß, Strahlenkranz direkt vor dem Schlag. Keine Blenden.
- **Ton:** instrumentaler Beat, −14 LUFS, Lautheitsspanne nur 2,2 LU, also durchgehend laut. Keine Stimme. Der Pegel steigt in den ersten neun Sekunden um rund 3 dB.
- **Text:** Text ist Bildmaterial, nicht Botschaft. Vier Rollen: Gummistempel in Rot, schief, mit rauem Rand; dasselbe Wort fünfmal untereinander als Kolonne, flackernd; Marker-Kritzel (Kreis, Kreuz, Pfeil) über dem Motiv; eine kleine Schreibmaschinen-Zeile unten links wie eine Bildunterschrift.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Foto-Kopie Person | 25 % | halbnah bis groß, Kopf und Schultern 50 bis 90 % der Bildhöhe, oft angeschnitten; auf Papier oder invertiert | 1 bis 4 Sechzehntel |
| Foto-Kopie Ort mit kleiner Figur | 15 % | weit, starke Diagonale (Rampe, Brücke, Treppe), Figur 10 bis 20 % der Bildhöhe, viel Schwarz | 2 bis 4 Sechzehntel |
| Holzschnitt-Illustration (Tier, Symbol) | 30 % | füllt 80 bis 100 % der Bildhöhe, frontal, mittig; ein Akzent-Kritzel darüber (Kreuz, Kreis) | 2 bis 4 Sechzehntel |
| Hauptobjekt in Akzentfarbe | 15 % | mittig, 70 bis 90 % der Bildhöhe, als Triptychon dreimal nebeneinander; roter Kreis drumherum | 1 bis 3 Sechzehntel je Zustand |
| Typo über Foto (Kolonne, Stempel) | 10 % | Kolonne im rechten Drittel, fünf Zeilen à 7 % der Bildhöhe; Stempel schief in einer Ecke | 2 bis 8 Sechzehntel |
| Schlusskarte | 5 % | ein Wort mittig, 20 % der Bildhöhe, rote Linie darunter, Mono-Zeile links, Stempel rechts unten | 8 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1 s):** das Hauptobjekt groß, rot umkringelt, Mono-Zeile unten links; dann sofort Triptychon.
- **Aufbau (1 bis 9 s):** Foto und Holzschnitt wechseln im Sechzehntel, jedes zweite bis dritte Bild invertiert, Kolonnen und Stempel setzen Akzente. Schnittdichte steigt.
- **Atem und Schlag (um 9 s, erster Schlag von Takt 4):** ein Sechzehntel Strahlenkranz auf Schwarz, dann Blitzbild in Rot, das stärkste Motiv füllt das Bild.
- **Verdichtung (9 bis 14 s):** längste Strecke mit Einzel-Sechzehnteln und Flackerbildern, höchste Schnittdichte.
- **Halt (15 bis 18 s):** zwei lange Einstellungen von 1,5 s, die Kolonne wächst im Takt.
- **Schluss (ab 20 s):** Musik stoppt hart, Schlusskarte steht eine volle Sekunde.

## Schnittmuster
Bauplan für 18 s bei 80 BPM (96 Sechzehntel, sechs Takte). Inhalt austauschbar, Rhythmus bleibt. Musik-Raster immer am fertigen Musikbett messen und die Sechzehntel darauf umrechnen.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0 bis 1 | Typo: Stempel mit Titelwort auf Papier | harter Schnitt | Stempel |
| 2 | 2 bis 3 | Foto-Kopie Person groß | hart | Beat setzt ein |
| 3 | 4, 5, 6 | Triptychon der Person, je Sechzehntel springt eine Kopie in eine neue Pose | Stottern | Tick je Sprung |
| 4 | 7 bis 9 | Hauptobjekt oder Karte, drei Akzent-Punkte ploppen | hart | Pop je Punkt |
| 5 | 10 bis 13 | dasselbe Bild, Kritzel-Kreis zeichnet sich, Mono-Zeile unten links | hart | Wisch |
| 6 | 14 bis 15 | invertiert: Wortkolonne | hart | Beat |
| 7 | 16 bis 19, 20 bis 23, 24 bis 27 | drei Holzschnitte, je einer mit Kopier-Sprung in der Mitte | hart | Tick |
| 8 | 28 bis 31 | Kette oder Reihe, je Sechzehntel kippt ein Element | hart | Klick je Element |
| 9 | 32 bis 35 | Foto-Kopie Person, Kolonne rechts | hart | Beat |
| 10 | 36, 37, 38 bis 39 | Person in drei Posen, die letzte steht zwei Sechzehntel | Stottern | Tick |
| 11 | 40 bis 43 | Person, Kritzel-Pfeil zeichnet sich zum Rand | hart | Wisch |
| 12 | 44 bis 46 | Rückblick: drei frühere Bilder je ein Sechzehntel | hart | Pop |
| 13 | 47 | Atem: Strahlenkranz weiß auf Schwarz | hart | nur Riser |
| 14 | 48 | Schlag: rotes Vollbild | Blitzbild | Hit und Aufprall |
| 15 | 49 bis 63 | Verdichtung: Hauptobjekt riesig, dann Einzel-Sechzehntel aus allen Bildtypen, zwei Flackerbilder | hart | Beat |
| 16 | 64 bis 71 | Halt: eine Einstellung, Kolonne wächst je Viertel um eine Zeile | keiner | Beat dünner |
| 17 | 72 bis 79 | Halt: Person oder Objekt, Stempel schlägt auf dem Viertel ein | hart | Stempel |
| 18 | 80 bis 82, 83 bis 85, 86 bis 87 | drei kurze Schlussbilder | hart | Beat |
| 19 | 88 bis 95 | Schlusskarte | hart | Musik stoppt auf 88 |

## Rezept für einen Code-Motor
- **Grund:** Papier aus Code: helles Creme, Rauschen mit festem Seed, rund 1,5 % dunkle Sprenkel, drei bis fünf senkrechte Kratzer, die je Sechzehntel springen. Darüber feines Filmkorn (Deckung 4 bis 6 %).
- **Bildbehandlung:** Fotos und Figuren entsättigen, dann Schwellwert (SVG: `feColorMatrix` mit `saturate 0`, danach `feComponentTransfer` mit `type="discrete" tableValues="0 1"`, Schwelle bei 55 bis 60 % Helligkeit, damit Gesichter nicht ausbleichen). Mit `mix-blend-mode: multiply` aufs Papier legen, auf Tusche-Grund invertiert mit `screen`. Gefilterte Bilder einmal vorrechnen und cachen, nicht je Frame filtern.
- **Bausteine:** Stempel (Rahmen mit 3 % der Bildbreite Strichstärke, Drehung −6° bis +4°, Rand über `feTurbulence` mit baseFrequency 0,9 und `feDisplacementMap` mit scale 6 aufgeraut, Deckung mit Rauschmaske 85 bis 100 %), Kritzel als SVG-Pfad mit `stroke-dashoffset`, der sich in sechs Bildern zeichnet, Wortkolonne, Mono-Bildunterschrift, Strahlenkranz (24 Keile aus der Bildmitte), Blitzbild, Triptychon mit ±8 px und ±1° Versatz je Kopie.
- **Typografie:** Stempel und Kolonne in fetter geometrischer Grotesk, Versalien, Rot (frei lizenziert zum Beispiel Outfit 800 oder Archivo Black). Schlusswort dieselbe Schrift in Tusche, 20 % der Bildhöhe. Bildunterschrift in Monospace (zum Beispiel JetBrains Mono 400), klein geschrieben mit Punkt, mindestens 3,5 % der Bildhöhe, 4 % Abstand vom Rand.
- **Bewegung:** Alle Wechsel auf dem Sechzehntel-Raster der gemessenen Musik. Im Aufbau wechselt das Bild alle ein bis zwei Sechzehntel, nie mehr als vier ohne Wechsel. Stempel schlagen in drei Bildern ein (Skala 1,5 → 0,95 → 1,0). Kopier-Jitter: je Sechzehntel ±2 px Versatz, ±0,3° Drehung. Kamera steht.
- **Formate:** In 9:16 rückt alles in die Mitte; Personen und Objekte 45 bis 60 % der Bildhöhe, Triptychon bleibt nebeneinander mit schmaleren Kopien oder wird zum Stapel aus drei Zeilen; Kolonne über die volle Breite im oberen Drittel; Mono-Zeile über den unteren 15 % (dort liegen die App-Bedienelemente). In 16:9 füllt Papier die Ränder, das Triptychon passt ohne Änderung.

## Material
- **Bilder (Holzschnitt):** `woodcut illustration of a [subject], black ink on off-white paper, dense crosshatching, extreme contrast, no grey tones, no color, centered, fills the frame, printmaking texture`
- **Bilder (Fotos):** keine Prompts nötig; jedes kontrastreiche Foto mit klarer Silhouette funktioniert. Weiche, flache Fotos vorher auf Kontrast ziehen.
- **Musik:** `Raw industrial trailer beat, 80 BPM, half-time feel, distorted kick, cracking snare on two and four, ticking sixteenth-note hi-hats, tape hiss, one gritty brass stab on the first beat of every bar, tension riser into a hard hit at nine seconds, hard stop at seventeen seconds, instrumental, no vocals, no orchestra, no strings`
- **Geräusche:** Stempel, Klick, Tick, Aufprall, Wisch; 12 bis 18 dB unter dem Beat. Stille nur im Atem vor dem Schlag.

## Regler
- Akzentfarbe: Rot ist der Klassiker, jede einzelne gesättigte Farbe trägt (Signalgelb, Kobaltblau).
- Anteil invertierter Bilder: 20 bis 50 %.
- Tempo: 70 bis 95 BPM; darüber wird Sechzehntel-Schnitt zu Flackern.
- Verhältnis Holzschnitt zu Foto: von reiner Foto-Kopie bis reiner Holzschnitt-Strecke.
- Mit einer gesprochenen Zeile in der Halt-Passage wird daraus ein Kanal-Trailer.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` im Kopf dieser Karte treffen.
- Standbild-Prüfung an drei zufälligen Stellen: kein Grauwert im Foto, höchstens eine leuchtende Farbe, Gesichter an Augen und Mund lesbar.
- Streifen bei 12 fps ansehen: kein Zustand kürzer als drei Bilder außer gewollten Flackerbildern, Schlag sitzt auf dem gemessenen Downbeat.

## Fallen
- Schwellwert bei 50 % frisst helle Haut; nur Augen und Bart bleiben → Schwelle 55 bis 60 %, Konturen tragen das Gesicht.
- Ein Zustand kürzer als drei Bilder wirkt wie Flackern statt Rhythmus → mindestens drei Bilder (0,1 s) je Zustand, Flackerbilder nur gezielt in der Verdichtung.
- Schneller Hell-Dunkel-Wechsel über mehr als eine Sekunde ist eine Epilepsie-Gefahr → nicht öfter als dreimal je Sekunde invertieren.
- Raster aus dem Prompt statt aus der Messung → nach vier Takten laufen die Schnitte aus dem Takt. Immer am fertigen Musikbett BPM und ersten Downbeat messen.
- Stempelrand ohne Rauschmaske sieht nach Vektorgrafik aus → Rand aufrauen und Deckung brechen.
- Helle Kleidung verschwindet auf Papiergrund → solche Figuren auf Tusche-Grund setzen oder mit Rasterpunkt-Schatten absetzen.
- Gesprochene Zeile länger als der Takt → nicht das Bild ans Wort biegen, sondern den Takt um ganze Sechzehntel verlängern.
