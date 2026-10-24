---
id: zine-raster
name: Zine-Raster
familie: scrapbook
kurz: Doppelseiten eines bunten Fanzines springen im Viertelnoten-Takt, Fotofelder und satte Farbfelder im Raster, verbunden durch Reißschwenks, Mosaik und Filmstaub.
kern: [Raster aus Fotofeldern und vollen Farbfeldern mit Kleintext, mindestens vier satte Druckfarben gleichzeitig, Layoutwechsel je Beat mit Reißschwenk oder Mosaik]
energie: 4
format_quelle: "4:3"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.83
  schnitte_pro_s: 1.4
  schnitte_verlauf: [1.9, 1.5, 0.9]
  bpm: 69
  schnitt_auf_beat: mittel
  lufs: -15.6
  helligkeit: 0.42
  kontrast: 0.23
  farbigkeit: 0.18
schnittmuster_16tel: [4, 4, 4, 4, 7, 3, 1, 3, 16, 1, 3, 0, 4, 4, 4, 8, 3, 20]
palette:
  papier: "#E7E0D7"
  tusche: "#1F1422"
  magenta: "#BB1455"
  violett: "#602D96"
  rost: "#9C3721"
  limette: "#D2E56E"
  kobalt: "#2D3ACB"
  balkengelb: "#EBC833"
  haut: "#A07461"
effekte: [harter-schnitt, wischer, glitch-uebergang, blende, raster-collage, bild-im-bild, freisteller, papier, filmkorn, duoton, halbton, handschrift, mono-zeile, push-in, beat-getrieben, passermarken, farbbalken-titel]
kamera: Flache Doppelseiten mit langsamem Push-in oder Drift, dazwischen Reißschwenks mit starker waagerechter Bewegungsunschärfe.
ton: Bassschweres, gedämpftes Instrumental um 69 BPM (Doppeltempo 138 möglich), keine Stimme, Pegel atmet zwischen −9 und −23 dBFS, am Ende vier Sekunden Ausblende über Schwarz.
braucht: [fotos-figur, nur-typo]
motor_aufwand: mittel
einsatz: [intro, hook, musikvideo, ganzes-kurzvideo]
abnahme:
  shot_median_s: [0.65, 1.0]
  schnitte_pro_s: [1.1, 1.8]
  helligkeit: [0.42, 0.58]
  farbigkeit: [0.15, 0.22]
  lufs: [-16.6, -14.6]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Zine-Raster

Wie ein selbstgedrucktes Fanheft, durch das jemand im Takt blättert: Fotofelder, Farbfelder, Schreibschrift, Staub. Die Energie kommt aus dem Layoutwechsel je Beat und den harten Reißschwenks, nicht aus Bewegung im Bild.

## Kern
- **Raster aus Foto- und Farbfeldern:** Jede Seite ist ein Gitter aus drei bis neun Feldern, ein Drittel davon reine Druckfarbe mit Kleintext oder Schreibschrift. Nur Fotos ergeben eine Galerie, kein Heft.
- **Vier und mehr satte Druckfarben:** Magenta, Violett, Rost, Limette, Kobalt, Gelb stehen nebeneinander. Das unterscheidet das Zine von leisen Pastell-Collagen; mit einer Farbe wird es zur Kopie.
- **Wechsel je Beat mit Reißschwenk oder Mosaik:** Seiten wechseln etwa alle 0,8 s, und fast jeder dritte Wechsel ist ein verwischter Reißschwenk oder ein Mosaik-Bild. Harte Schnitte allein wirken wie eine Diashow.

## Erkennung
- **Bild:** Papiergrund #E7E0D7 mit Filmstaub (helle Sprenkel auf Dunkel, dunkle auf Hell), feines Korn. Fotos warm, leicht ausgeblichen, Schwarz zu #1F1422 angehoben; einzelne Felder als Duoton in Magenta oder Violett, schmale Seitenstreifen als Schwarzweiß-Halbton. Akzentfarben siehe Palette. Gemessen: Helligkeit 0,42, Kontrast 0,23, Farbigkeit 0,18. Die Vorlage endet nach 16,3 s, danach 4,4 s Schwarz; ohne diesen Schwanz liegt die Helligkeit bei etwa 0,5.
- **Schnitt:** 18 erkannte Shots, 14 davon kürzer als eine Sekunde; im 4-fps-Streifen wechseln die Seiten häufiger, weil Reißschwenks und Mosaik weiche Schnitte sind. Median 0,83 s (mit Schwanz), Raster etwa vier Sechzehntel bei 69 BPM, also ein Viertel. Tempo fällt von 1,9 auf 0,9 Schnitte je s. Übergänge: harter Schnitt, waagerechter Reißschwenk mit Unschärfe über 4 bis 6 Bilder, Mosaik in 2 bis 3 Bildern, ein Papierriss quer durchs Bild, Blende im langsamen Teil.
- **Ton:** 79 % der Energie unter 250 Hz, Höhen gedämpft, keine Stimme, −15,6 LUFS. Pegel schwankt mit dem Arrangement, am Ende Ausblende über vier Sekunden.
- **Text:** Fünf Rollen. Große Schreibschrift über Fotos (Namen, Widmungen) in Weiß oder Rosé mit leichtem Schatten; drei kurze Wörter in Farbbalken untereinander; Blöcke aus Kleintext (8 bis 12 Zeilen, 1,2 % der Höhe) in Farbfeldern; kleine Signaturen in den Ecken; Punktmuster wie Blindenschrift als Ornament.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Raster-Seite | 35 % | 3×2 bis 4×3 Felder, Fugen 0,5 % Papier, Gesichter füllen ihr Feld zu 80 bis 100 %, ein bis drei Felder sind Farbfläche mit Kleintext oder Schreibschrift-Initiale | 4 Sechzehntel |
| Doppelseite mit Freistellern | 15 % | zwei bis drei Personen freigestellt, 70 bis 90 % der Höhe, über waagerechten Farbbalken (Magenta über Weiß), Fadenlinien diagonal, Schreibschrift-Etikett auf Limette | 4 bis 8 Sechzehntel |
| Dia im Rahmen | 15 % | abgerundetes Rechteck mit 2 % weißem Rand, 60 bis 70 % der Höhe, mittig auf Magenta oder Glitzer-Grund, links und rechts schmale Halbtonstreifen | 3 bis 4 Sechzehntel |
| Schreibschrift über Gruppenfoto | 15 % | Gruppenfoto randlos, warm und verwaschen, Schreibschrift 25 bis 35 % der Höhe quer darüber, Passerlinien | 4 bis 8 Sechzehntel |
| Übergangsbild | 15 % | Reißschwenk-Unschärfe, Mosaikblöcke (1/20 der Höhe) oder Kobalt-Querbalken mit Kleintext | 1 Sechzehntel |
| Schwarzer Auftakt | 5 % | Schwarz mit Staub und zwei bis drei dünnen weißen Passerkreuzen, die springen | 4 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1 s):** Schwarz, Staub, Passerkreuze springen; dann knallt die erste Raster-Seite voll ins Bild.
- **Aufbau (1 bis 6 s):** Raster-Seiten im Viertel, ein Papierriss läuft quer, Farbbalken-Wortsäule, das erste Dia.
- **Verdichtung (6 bis 9 s):** Doppelseite mit Freistellern, zwei Raster-Varianten kurz hintereinander.
- **Schlag (um 9,3 s und 10,5 s):** Mosaik und Reißschwenk, dann Kobalt-Querbalken als Vollbild.
- **Atem (13 bis 15 s):** Schreibschrift über Gruppenfoto, längste Einstellungen, Blende statt Schnitt.
- **Schluss (15 bis 16,3 s):** die Anfangsseite kehrt zurück, verwischt, Schwarz, Musik blendet aus.

## Schnittmuster
Bauplan für 16 s bei 69 BPM (Sechzehntel 0,217 s, 74 Sechzehntel). Seiten im Viertel, Übergangsbilder je ein Sechzehntel. Raster am fertigen Musikbett messen.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-3 | Schwarzer Auftakt, Passerkreuze springen je Sechzehntel | keiner | Knistern, Riser |
| 2 | 4-7 | Raster-Seite A (6 Felder) | harter Schnitt | Beat setzt ein |
| 3 | 8-11 | Raster-Seite B, zwei Felder anders | hart | Beat |
| 4 | 12-15 | Raster-Seite C mit Schreibschrift-Feld | Reißschwenk | Whoosh |
| 5 | 16-22 | Doppelseite, Papierriss läuft von links nach rechts | Riss | Papierreißen |
| 6 | 23-25 | Farbbalken-Wortsäule über Fotostreifen | hart | Snare |
| 7 | 26 | Mosaik | Mosaik | Bitcrush |
| 8 | 27-29 | Dia im Rahmen auf Magenta | hart | Beat |
| 9 | 30-45 | Doppelseite mit drei Freistellern, Push-in 4 % | Reißschwenk | Beat |
| 10 | 46 | Mosaik | Mosaik | Hit |
| 11 | 47-49 | Kobalt-Querbalken mit Kleintext | hart | Nachhall |
| 12 | 50-53 | Doppelseite Magenta, Fadenlinien zeichnen sich | Reißschwenk | Beat |
| 13 | 54-57 | Dia auf Glitzer-Grund | hart | Glitzer |
| 14 | 58-65 | Schreibschrift über Gruppenfoto | Blende 6 Bilder | Beat dünner |
| 15 | 66-69 | Raster-Seite A kehrt zurück | Reißschwenk | Beat |
| 16 | 70-74 | Raster-Seite A verwischt, Schwarz | Reißschwenk, Blende | Ausblende |

## Rezept für einen Code-Motor
- **Grund:** Papier #E7E0D7, Korn 6 bis 8 %, Staub-Ebene aus 150 bis 300 Sprenkeln (1 bis 4 px bei 1080 Höhe) und zwei bis drei Haaren, neu gewürfelt je Sechzehntel. Über Dunkel hell, über Hell dunkel (mix-blend-mode difference mit 40 % Deckung funktioniert für beides).
- **Bildbehandlung:** Fotos warm (+8 Temperatur), Schwarzpunkt auf #1F1422 heben, Sättigung −10 %. Duoton-Felder: entsättigen, dann `feColorMatrix` auf Verlauf von #1F1422 nach #BB1455 oder #602D96. Halbtonstreifen: Schwarzweiß, Raster 45°, Punktabstand 0,8 % der Höhe.
- **Bausteine:** Raster als CSS-Grid mit 0,5 % Fuge; Farbfeld mit Kleintext (8 bis 12 Zeilen, 1,2 % Höhe, Zeilenabstand 1,3); Schreibschrift-Initiale in einem Feld (60 % der Feldhöhe); Farbbalken-Wortsäule (drei Balken je 10 % der Höhe, Magenta, Schwarz, Petrol, Wort weiß mittig); Dia-Rahmen (Radius 6 % der Rahmenhöhe, Rand 2 % weiß, weicher Schatten 1 %); Passerkreuz aus zwei 1-px-Linien über die volle Bildbreite; Papierriss als SVG-Pfad mit gezackter Kante und weißer Faserkante 0,6 %.
- **Typografie:** Schreibschrift frei lizenziert zum Beispiel Pinyon Script oder Great Vibes, 25 bis 35 % der Höhe, Weiß mit 30 % Schatten. Balkenwörter in Archivo 700, Versalien, 6 % Höhe. Kleintext Inter 400, 1,2 % Höhe. Signaturen in Space Mono 400, 1,4 %.
- **Bewegung:** Seitenwechsel auf jedem Viertel (4 Sechzehntel). Reißschwenk: waagerechter Versatz 30 % der Breite und Bewegungsunschärfe 6 % der Breite über 4 Bilder, ease-in-out. Mosaik: 2 bis 3 Bilder mit Pixelblöcken 1/20 der Höhe. Innerhalb einer Seite Push-in 3 bis 5 % je Sekunde. Papierriss läuft in 6 Bildern über die Breite.
- **Formate:** Quelle 4:3. In 9:16 wird das Raster zwei Spalten breit und vier bis fünf Zeilen hoch, Schreibschrift läuft auf zwei Zeilen, Freisteller 55 bis 65 % der Höhe; unten 15 % frei halten. In 16:9 vier Spalten, Doppelseiten bekommen ein zusätzliches Farbfeld rechts.

## Material
- **Bilder (Porträt):** `candid close-up portrait of [subject], warm faded film photo, slight motion, flash in a dim room, grainy, raised blacks, 2000s point-and-shoot look, honest expression, tight crop`
- **Bilder (Freisteller):** `full-body photo of [subject] posing playfully, plain light background, even daylight, high detail, for cut-out collage`
- **Musik:** `Dusty lo-fi R&B instrumental, 69 BPM half-time feel with double-time hi-hats, deep sub bass, soft vinyl crackle, warm electric piano chords, muted snare, first second only crackle and a short riser, beat lands at 1 second, small stop and swell at 9 seconds, thinner groove from 13 to 15 seconds, full again at 15, slow fade to silence from 16 to 20 seconds, instrumental, no vocals`
- **Geräusche:** Knistern, Papierreißen, Whoosh bei Reißschwenks, Bitcrush-Knackser beim Mosaik; 12 bis 16 dB unter der Musik.

## Regler
- Farbanzahl: vier bis sechs Druckfarben; Pastell statt Sättigung kippt in Richtung Tagebuch-Collage.
- Feldanzahl: von drei (ruhig, lesbar) bis zwölf (Wimmelbild).
- Anteil Reißschwenk: jeder zweite bis jeder vierte Wechsel.
- Schreibschrift kann Namen, Datum oder ein Wort des Themas tragen; nie längere Sätze.

## Abnahme
- Render mit `video_schauen.py` messen, Zielwerte aus `abnahme`; wer einen schwarzen Schwanz anhängt, misst niedrigere Helligkeit.
- Standbild an drei Stellen: mindestens drei Druckfarben sichtbar, Gesichter in ihrem Feld groß, Staub auf hellen und dunklen Flächen erkennbar.
- 12-fps-Streifen: Seitenwechsel sitzen auf Vierteln, Reißschwenks dauern höchstens 6 Bilder.

## Fallen
- Raster mit gleichen Feldgrößen → wirkt wie eine Fototabelle. Feldgrößen mischen (ein großes, mehrere kleine).
- Kleintext lesbar und sinnvoll → zieht die Augen ab. Er ist Textur; Blindtext oder Wortlisten in 1,2 % Höhe genügen.
- Staub als statisches Bild → wirkt wie ein Filter. Je Sechzehntel neu würfeln.
- Mosaik länger als drei Bilder → sieht nach Fehler aus. Kurz halten und auf einen Schlag legen.
- Zu viele Reißschwenks hintereinander → schwammig. Nach jedem Schwenk mindestens eine scharfe Seite stehen lassen.
