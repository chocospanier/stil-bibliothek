---
id: tiefenkarte-fenster
name: Tiefenkarte mit Farbfenstern
familie: glitch
kurz: Das ganze Video läuft als graue Tiefenkarte im Nebel (nah dunkel, fern weiß), nur Augen, Lippen und kleine Pixelflecken zeigen sich in rechteckigen Fenstern in echter Farbe; Schnitt exakt auf jedem Viertel eines langsamen Beats.
kern: [Footage als weiche Tiefenkarte in Grau bis Weiß statt als Bild, rechteckige Farbfenster nur auf Augen, Lippen und Gesicht, ein Schnitt auf jedem Viertel ohne Ausnahme]
energie: 3
format_quelle: "16:9"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.93
  schnitte_pro_s: 1.0
  schnitte_verlauf: [0.98, 1.14, 0.98]
  bpm: 66
  schnitt_auf_beat: hoch
  lufs: -7.3
  helligkeit: 0.59
  kontrast: 0.22
  farbigkeit: 0.05
schnittmuster_16tel: [8, 4, 4, 4, 4, 4, 0, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 8]
palette:
  nebel: "#E5E2E1"
  mitte: "#AA999C"
  nah: "#604E4F"
  schwarz: "#040101"
  fenster_haut: "#E8B4A6"
  fenster_lippe: "#D9707A"
  fenster_auge: "#6C8FB0"
effekte: [harter-schnitt, silhouette, augen-makro, tanz, beat-getrieben, push-in, ton-stopp, tiefenkarte, farbfenster]
kamera: Übernimmt die langsamen Fahrten des Ausgangsmaterials (meist leichter Push-in); in der Tiefenkarte wirken sie wie Schweben im Nebel.
ton: Langsamer, sehr lauter Beat um 66 BPM (−7,3 LUFS, fast ohne Dynamik), jeder Schlag ein Schnitt, am Ende harter Stopp auf Schwarz.
braucht: [fotos-figur, footage-ort]
motor_aufwand: mittel
einsatz: [musikvideo, hook, uebergang, portrait]
abnahme:
  shot_median_s: [0.8, 1.05]
  schnitte_pro_s: [0.85, 1.2]
  helligkeit: [0.50, 0.68]
  farbigkeit: [0.03, 0.08]
  lufs: [-9, -7]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Tiefenkarte mit Farbfenstern

Sieht aus, als würde eine Maschine ein Musikvideo nur als Entfernung sehen: Figuren werden zu grauen Schemen im Nebel, und nur dort, wo ein Mensch etwas ausdrückt (Augen, Mund), schneidet ein Fenster die Wirklichkeit in Farbe hinein. Die Energie kommt aus dem gnadenlos gleichmäßigen Viertel-Schnitt.

## Kern
- **Tiefenkarte statt Bild:** Jeder Shot ist eine weiche Graustufen-Tiefenkarte: was nah ist, ist dunkles Graubraun, was fern ist, löst sich in Weiß auf. Keine Textur, keine Kleidung, nur Formen. Ohne diese Umwandlung bleibt ein gewöhnliches Musikvideo.
- **Farbfenster auf Ausdruck:** Rechteckige Ausschnitte des Originals in voller Farbe sitzen exakt auf Augen, Lippen oder einem ganzen Gesicht; dazu verstreute Pixelflecken von 1 bis 2 % der Bildhöhe. Das Fenster ist der Blickfang jedes Shots.
- **Viertel ohne Ausnahme:** Fast jeder Shot dauert genau ein Viertel (0,91 s bei 66 BPM), drei Shots zwei Viertel, ein einziges Flackerbild. Die Abweichung vom Raster ist mit 0,11 sehr klein.

## Erkennung
- **Bild:** hell (Helligkeit 0,59), fast farblos (0,05), weicher Nebel. Graustufen mit leichtem Rotbraun: Nebel `#E5E2E1`, Mitte `#AA999C`, Nähe `#604E4F`. Farbe nur in den Fenstern (Haut, Lippenrot, Augenblau) und den Pixelflecken. Der allererste Shot zeigt kurz das Originalbild in Farbe, dann kippt alles ins Grau.
- **Schnitt:** 18 Shots in 18,4 s, Median 0,93 s, Dichte gleichmäßig 1,0 bis 1,1 Schnitte je Sekunde. Raster: Viertel bei 66 BPM. Nur harte Schnitte; das Ende ist Schwarz mit einem kleinen roten Punkt.
- **Ton:** −7,3 LUFS, Lautheitsspanne 0,7 LU, True Peak über 0 dB: extrem laut, gepresst. Langsamer Beat.
- **Text:** keiner.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Gesicht frontal nah, Augenfenster | 25 % | Kopf füllt 90 bis 110 % der Bildhöhe, mittig; Fenster 35 bis 45 % der Bildbreite, 15 bis 20 % der Höhe, auf Augenhöhe bei 30 bis 45 % der Bildhöhe | 4 Sechzehntel |
| Gesicht nah, Lippenfenster | 15 % | wie oben; Fenster 15 bis 25 % der Breite, 8 bis 12 % der Höhe, auf dem Mund bei 55 bis 75 % der Höhe | 4 Sechzehntel |
| Augen-Makro als Tiefenkarte | 5 % | zwei helle Augenhöhlen füllen die Breite, oder Augenfenster über die halbe Breite | 4 bis 8 Sechzehntel |
| Figur sitzend auf großer Blüte | 10 % | Figur 40 % der Bildhöhe, mittig, Blütenform als Schemen, kleines Gesichtsfenster | 4 Sechzehntel |
| Hauptfigur vor Tanzgruppe | 25 % | Hauptfigur mittig 60 bis 80 % der Bildhöhe, Gruppe dahinter heller und kleiner; Gesichtsfenster klein (5 % der Höhe) plus Pixelflecken | 4 Sechzehntel |
| Profil oder Rücken nah | 15 % | Kopf und Schulter rechts, 80 % der Höhe, Nebel links | 4 Sechzehntel |
| Schluss Schwarz | 5 % | Schwarz mit rotem Punkt 1 % der Bildhöhe mittig | 1 s |

## Dramaturgie
- **Hook (0 bis 1,8 s):** ein Augenblick Originalfarbe, Gesicht frontal; dann wird es zur Tiefenkarte und das erste Augenfenster öffnet sich.
- **Aufbau (1,8 bis 6,5 s):** jedes Viertel ein neuer Ort im Nebel: Augenhöhlen, Blüte, Profil, Tanzgruppe. Fenster wechseln zwischen Augen, Gesicht und Pixelflecken.
- **Flackern (6,4 s):** ein einziges Bild, dann zwei Viertel ein Gesicht mit großem Augenfenster.
- **Mitte (7,4 bis 16 s):** derselbe Kreislauf, die Fenster werden größer und farbiger.
- **Schluss (16,5 bis 18,4 s):** Lippenfenster als letzter Shot, harter Stopp auf Schwarz.

## Schnittmuster
Bauplan für 16 s bei 66 BPM (68 Sechzehntel zu je 0,227 s, 17 Viertel), dann eine Sekunde Schwarz.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-1 | Gesicht frontal in Originalfarbe | Start | erster Schlag |
| 2 | 2-7 | dasselbe Gesicht als Tiefenkarte, Augen- und Lippenfenster | hart | |
| 3 | 8-11 | Augen-Makro als Tiefenkarte | hart | Schlag |
| 4 | 12-15 | Figur auf Blüte, kleines Gesichtsfenster | hart | Schlag |
| 5 | 16-19 | Profil nah, zwei Pixelflecken | hart | Schlag |
| 6 | 20-23 | Hauptfigur vor Gruppe, Gesichtsfenster | hart | Schlag |
| 7 | 24-27 | Gruppe vor großer Pflanzenform, Pixelflecken | hart | Schlag |
| 8 | 28 | Flackerbild: Gesicht ohne Fenster (zwei Bilder) | hart | |
| 9 | 29-35 | Gesicht nah, großes Augenfenster | hart | Schlag, gehalten |
| 10 | 36-39 | Hauptfigur tanzt vor Gruppe | hart | Schlag |
| 11 | 40-47 | Gesicht nah, Lippenfenster, Mund bewegt sich | hart | zwei Schläge |
| 12 | 48-51 | Figur auf Blüte | hart | Schlag |
| 13 | 52-55 | drei Figuren mit erhobenen Armen, Fenster auf dem Bauch der Mittleren | hart | Schlag |
| 14 | 56-59 | Gesicht mit Augenfenster quer über die Breite | hart | Schlag |
| 15 | 60-63 | Hauptfigur vor Gruppe | hart | Schlag |
| 16 | 64-67 | Gesicht nah, Lippenfenster | hart | letzter Schlag |
| 17 | danach 1 s | Schwarz mit rotem Punkt | hart | Stopp |

## Rezept für einen Code-Motor
- **Grund:** die Tiefenkarte selbst.
- **Bildbehandlung:** Für jedes Bild einmal eine Tiefenkarte vorrechnen (ein frei verfügbares Tiefenschätzmodell wie Depth Anything oder MiDaS, lokal, 0 Kosten), als Video speichern. Dann umfärben: nah (Tiefenwert hoch) auf `#604E4F`, mittel auf `#AA999C`, fern auf `#E5E2E1`, Kurve weich (Gamma 0,8), damit der Hintergrund im Nebel versinkt. `feGaussianBlur` mit 0,3 % der Bildhöhe glättet Stufen. Leichte Vignette nach Weiß (Ränder +5 % heller) verstärkt den Nebel.
- **Farbfenster:** Rechteck aus dem Originalbild an derselben Stelle ausschneiden und darüber legen, ohne Rand, ohne Schatten. Augenfenster 35 bis 45 % der Bildbreite mal 15 bis 20 % der Höhe; Lippenfenster 15 bis 25 % mal 8 bis 12 %. Position je Frame mit einem Gesichtsdetektor nachführen (zum Beispiel MediaPipe Face Mesh), sonst rutscht das Fenster vom Auge. Pixelflecken: vier bis acht Quadrate von 1 bis 2 % der Bildhöhe aus dem Original, verstreut, springen jedes Viertel an neue Stellen.
- **Bausteine:** Tiefenkarten-Video, Original-Video, Gesichts-Tracking, Fenster, Pixelflecken, Schwarzbild mit rotem Punkt.
- **Typografie:** keine.
- **Bewegung:** Schnitt exakt auf jedem Viertel, am fertigen Musikbett gemessen. Fenster erscheinen mit dem Schnitt und bleiben ganz still auf ihrem Ziel. Kamera aus dem Material.
- **Formate:** 16:9 ist das Original. In 9:16 Gesichter mittig und größer; das Augenfenster wird schmaler (70 % der Bildbreite, 8 % der Höhe), Gruppenbilder auf die Hauptfigur beschneiden; Nebel oben und unten darf viel Platz bekommen.

## Material
- **Bilder:** jedes Performance- oder Porträtmaterial mit klarer Tiefenstaffelung (Figur vorne, Gruppe oder Kulisse hinten); die Tiefenkarte entsteht im Motor. Für eigene Keyframes: `music video still of [subject] performing in front of a group of dancers on a foggy stage, strong depth separation, centered composition, clean silhouette`
- **Bilder (Porträt):** `beauty close-up of [subject] looking into the camera, sharp eyes, glossy lips, centered, plain background`
- **Musik:** `Slow heavy trap ballad, 66 BPM, massive distorted 808 on every beat, sparse snare on two and four, airy synth choir pad, glassy bell melody; 0-1 s bell alone, 1 s full beat, steady quarter-note hits to 16 s, hard stop at 16 s, one second of silence, instrumental, no vocals`
- **Geräusche:** ein kurzes digitales Zirpen, wenn ein Fenster aufgeht, 18 dB unter der Musik. Sonst nichts.

## Regler
- Fensterfarbe: Original in voller Sättigung ist der Kern; alternativ alle Fenster in einer Akzentfarbe eingefärbt.
- Nebelfarbe: warmes Grau ist die Vorlage, kaltes Blaugrau trägt auch.
- Tempo: 60 bis 80 BPM, immer ein Shot je Viertel.
- Fensteranteil: 3 bis 15 % der Bildfläche; darüber verliert die Tiefenkarte ihre Wirkung.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; Farbigkeit unter 0,08 beweist, dass Farbe nur in Fenstern steckt.
- Standbild an drei Stellen: Fenster sitzt exakt auf Augen oder Mund, keine Kleidungstextur in der Tiefenkarte.
- Streifen bei 12 fps: jeder Wechsel auf einem Viertel, Fenster zittern nicht.

## Fallen
- Tiefenkarte zu hart gestuft → wirkt wie ein Rechenfehler. Weichzeichnen und Kurve sanft.
- Fenster ohne Tracking → rutschen vom Gesicht. Gesichtsdetektor je Frame.
- Nah und fern vertauscht (nah weiß) → die Figur verschwindet im Nebel. Nah ist dunkel.
- Zu viele Pixelflecken → wirkt wie Fehler statt Gestaltung. Höchstens acht je Shot.
- Lautheit nachgemacht ohne Begrenzer → verzerrt. Für unsere Kanäle eher −10 LUFS anpeilen und die Abnahme dann anpassen.
