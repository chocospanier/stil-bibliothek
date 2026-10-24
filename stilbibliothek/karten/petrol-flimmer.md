---
id: petrol-flimmer
name: Petrol-Flimmer
familie: filmlook
kurz: Quadratisches Porträt-Footage in kaltem Petrol mit milchigen Lichtern und grobem Korn, fünf Bildwechsel je Sekunde, dazwischen Unschärfe-Blitze, Streifenmasken, invertierte Gesichter in Lachsrosa und schräg gelegte Fotostreifen.
kern: [Duoton Petrol bis Milchweiß mit grobem Korn und schwerer Vignette, Bildwechsel im Achtel- bis Sechzehntelbereich über die ganze Länge, Störbilder als Satzzeichen (Unschärfe, Streifenmaske, Negativ in Lachsrosa)]
energie: 5
format_quelle: "1:1"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.13
  schnitte_pro_s: 5.3
  schnitte_verlauf: [4.64, 6.03, 5.26]
  bpm: 60
  schnitt_auf_beat: mittel
  lufs: -11.4
  helligkeit: 0.32
  kontrast: 0.25
  farbigkeit: 0.07
schnittmuster_16tel: [7, 3, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 1]
palette:
  grund: "#0A1419"
  petrol: "#3D5357"
  nebel: "#829192"
  licht: "#D3DBD7"
  negativ: "#C98F80"
effekte: [harter-schnitt, blitzbild, stottern, wiederholung, bild-im-bild, duoton, invertieren, filmkorn, vignette, mono-zeile, beat-getrieben, querband, unschaerfe-blitz]
kamera: Einzelne Einstellungen stehen oder treiben leicht; die Bewegung entsteht fast nur durch den Schnitt und durch Sprünge zwischen Totale, Halbnah und Detail derselben Figur.
ton: Lauter, druckvoller Beat (−11,4 LUFS, kaum Dynamik) mit 60 BPM als Grundpuls, darüber Achtel und Sechzehntel, auf denen die Bilder springen.
braucht: [fotos-figur, footage-ort]
motor_aufwand: mittel
einsatz: [hook, trailer, portrait, uebergang]
abnahme:
  shot_median_s: [0.10, 0.17]
  schnitte_pro_s: [4.2, 6.4]
  helligkeit: [0.26, 0.38]
  farbigkeit: [0.05, 0.10]
  lufs: [-12.5, -10.5]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Petrol-Flimmer

Wie ein alter, kalt eingefärbter Filmstreifen über eine Person, der zu schnell durch den Projektor läuft. Die Energie kommt aus dem Dauerflimmern: 103 Schnitte in 19 Sekunden, und alle paar Sekunden ein Störbild, das den Blick wieder einfängt.

## Kern
- **Petrol-Duoton mit Korn:** Schatten fast schwarz mit Blaugrün, Mitten Petrol, Lichter milchig statt weiß. Grobes Korn und eine schwere Vignette machen daraus Film. Neutrales Schwarzweiß oder warme Haut kippen den Stil sofort.
- **Dauerflimmern:** Median-Shot 0,13 s, also vier Bilder bei 30 fps. Das Tempo bleibt über die ganze Länge hoch, nur der allererste Shot steht 1,7 s.
- **Störbilder als Satzzeichen:** Ein bis drei Bilder völlige Unschärfe, ein Bild als schmaler Streifen zwischen schwarzen Balken, eine kurze Strecke als Negativ, das Haut in Lachsrosa verwandelt, und Fotostreifen mit weißem Rand, die schräg über das Bild fallen. Sie gliedern das Flimmern wie Kommas.

## Erkennung
- **Bild:** quadratisch. Helligkeit 0,32, Farbigkeit 0,07: kaum Farbe, aber durchgehend kalt. Hauptgruppen `#0A1419` (42 %), `#3D5357`, `#829192`, `#D3DBD7`. Lichter milchig, Schatten satt, Korn deutlich (Deckung um 10 %), Vignette dunkelt die Ecken um 40 %. Gelegentlich ein dünner senkrechter Kratzer. Eine winzige Timecode-Zeile (Monospace, 1 % der Bildhöhe) steht in manchen Bildern mitten im Bild.
- **Schnitt:** 91 Shots in 19,4 s, 89 davon kürzer als eine Sekunde, längster 1,7 s (der Einstieg). Dichte 4,6, 6,0, 5,3 Schnitte je Sekunde über die Drittel. Viele Shots sind null bis ein Sechzehntel lang (bei 60 BPM also ein bis vier Bilder). Dieselbe Einstellung kehrt oft zwei- bis dreimal zurück (Stottern zwischen zwei Bildern).
- **Ton:** −11,4 LUFS, Lautheitsspanne 0,9 LU, True Peak über 0 dB: durchgehend laut und gepresst. Grundpuls 60 BPM, vermutlich mit 120-BPM-Hi-Hats.
- **Text:** kein Stiltext. Nur die Timecode-Zeile als Filmzitat.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Porträt nah | 25 % | Gesicht 50 bis 70 % der Bildhöhe, oft oben angeschnitten, Blick nach unten oder seitlich | 1 bis 2 Sechzehntel |
| Detail Kleidung oder Hand | 15 % | Kragen, Krawatte, Hand füllen das ganze Bild, Gesicht nur am oberen Rand | 1 Sechzehntel |
| Ganzkörper im Raum | 20 % | Figur 70 bis 90 % der Bildhöhe, mittig, Architektur oder Rasen dahinter | 1 bis 3 Sechzehntel |
| Rückenansicht in der Menge | 15 % | Schultern füllen die untere Hälfte, Kopf bei 30 % der Höhe, Menschen unscharf daneben | 1 Sechzehntel |
| Unschärfe-Blitz | 8 % | dasselbe Motiv völlig defokussiert, nur Licht und Form | 1 bis 3 Bilder |
| Streifenmaske | 5 % | Bild nur in einem waagerechten Streifen von 25 bis 30 % der Höhe sichtbar, oben und unten Schwarz | 2 bis 5 Bilder |
| Negativ in Lachsrosa | 5 % | Gesicht invertiert, groß, füllt das Bild | 3 bis 4 Bilder je Zustand, drei Zustände |
| Fotostreifen schräg | 5 % | ein bis drei Streifen mit weißem Rand (1,5 % der Bildbreite), je 15 bis 25 % der Bildhöhe, um 3 bis 8° gedreht, über Schwarz oder über ein Ganzkörperbild gelegt | 3 bis 10 Bilder |
| Schwarzbild | 2 % | Schwarz | 2 bis 3 Bilder |

## Dramaturgie
- **Hook (0 bis 1,7 s):** die einzige ruhige Einstellung: Figur kommt halbnah auf die Kamera zu. Dann ein Streifen-Bild, dann bricht das Flimmern los.
- **Aufbau (1,7 bis 9 s):** Porträt, Detail, Rücken, Ganzkörper im Wechsel, dazwischen Unschärfe-Blitze. Dichte steigt.
- **Schlag (um 9,3 s):** drei Bilder Negativ in Lachsrosa, ein Fotostreifen auf Schwarz, drei Streifen über dem Ganzkörperbild.
- **Verdichtung (10 bis 17 s):** höchste Dichte, Stottern zwischen zwei Einstellungen, eine Streifenmaske je Sekunde.
- **Schluss (17 bis 19,4 s):** ein langer Unschärfe-Blitz, dann Schwarz mit Timecode.

## Schnittmuster
Bauplan für 16 s bei 120 BPM gezählt (128 Sechzehntel zu je 0,125 s; bei 60 BPM Grundpuls sind das Zweiunddreißigstel). Musik vorher messen.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-13 | Figur halbnah, kommt auf die Kamera zu | Start | Beat ab dem ersten Bild |
| 2 | 14-19 | Streifenmaske: Rückenansicht im Streifen | hart | Hit |
| 3 | 20-21 | Porträt nah | hart | |
| 4 | 22 | Unschärfe-Blitz | Blitzbild | |
| 5 | 23 | Schwarz | hart | |
| 6 | 24-25, 26 | Ganzkörper, Stottern auf dasselbe Bild | Stottern | Hi-Hat |
| 7 | 27-34 | acht Einzel-Sechzehntel: Rücken, Rücken nah, Detail, Ganzkörper im Wechsel | hart | Hi-Hats |
| 8 | 35-50 | sechzehn Einzel-Sechzehntel, jedes vierte ein Unschärfe-Blitz | hart | Beat |
| 9 | 51-54 | Porträt halbnah, ruhiger | hart | Atem: Hi-Hats setzen aus |
| 10 | 55-57 | Negativ in Lachsrosa, drei Zustände | hart | Hit |
| 11 | 58-59 | ein Fotostreifen auf Schwarz | hart | Pop |
| 12 | 60-62 | drei Fotostreifen über Ganzkörper | hart | Pop je Streifen |
| 13 | 63-100 | Verdichtung, Einzel-Sechzehntel und Stottern, eine Streifenmaske je acht Sechzehntel | hart | Beat |
| 14 | 101-108 | Porträt nah, Blick in die Kamera | hart | letzter Takt |
| 15 | 109-119 | Unschärfe-Blitz, lang | weich | Musik fällt ab |
| 16 | 120-127 | Schwarz mit Timecode-Zeile | hart | Stopp |

## Rezept für einen Code-Motor
- **Grund:** Schwarz `#0A1419`, wo Streifenmaske oder Schlussbild es brauchen.
- **Bildbehandlung:** entsättigen, dann Duoton über Kurven: Schatten `#0A1419`, Mitten `#3D5357`, Lichter `#D3DBD7` (SVG `feComponentTransfer` je Kanal, Rot 0,04 0,24 0,83; Grün 0,08 0,33 0,86; Blau 0,10 0,34 0,84). Lichter über 85 % weich abschneiden, damit sie milchig bleiben. Korn 10 % Deckung, Größe 2 px bei 1080 Breite, je Frame neu. Vignette 40 % an den Ecken. Alle 1 bis 2 s für 2 bis 4 Bilder ein senkrechter Kratzer mit 1 px Breite.
- **Bausteine:** Unschärfe-Blitz (dasselbe Bild mit Gauß 4 % der Bildhöhe), Streifenmaske (Rechteck 25 bis 30 % der Höhe, Lage zufällig zwischen 30 und 60 %, Rest `#0A1419`), Negativ (Bild invertieren, dann mit Kurve Rot +20 %, Blau −15 % auf Lachsrosa ziehen, Ziel `#C98F80` in den Mitten), Fotostreifen (Ausschnitt mit Seitenverhältnis 3:1 bis 4:3, weißer Rand 1,5 % der Bildbreite, Drehung −8° bis +8°, kleiner Schatten 0,5 %), Timecode-Zeile.
- **Typografie:** nur Timecode in Monospace, zum Beispiel IBM Plex Mono 400, 1 bis 1,5 % der Bildhöhe, `#D3DBD7` mit 60 % Deckung, mittig.
- **Bewegung:** Bildwechsel auf Sechzehnteln, viele Zustände nur ein bis vier Bilder. Leichter Drift je Shot (1 % Skalierung), sonst keine Kamera. Stottern: zwei Bilder im Wechsel A, B, A je ein Sechzehntel.
- **Formate:** 1:1 ist das Original. In 9:16 oben und unten je 22 % Schwarz mit Korn lassen und das Quadrat mittig setzen, das wirkt wie ein Filmfenster; oder Motiv auf 9:16 beschneiden, Gesichter in die obere Hälfte. In 16:9 das Quadrat mittig mit schwarzen Seiten oder zwei Quadrate nebeneinander im Stottern.

## Material
- **Bilder:** `cinematic film still of [subject], cold desaturated teal tones, milky highlights, heavy film grain, soft vignette, overcast light, moody vintage 1990s film look`
- **Bilder (Detail):** `extreme close-up film still of [subject]'s collar and hands, cold teal grade, heavy grain, shallow depth of field, moody`
- **Musik:** `Dark cinematic phonk-trap hybrid, 120 BPM felt as 60, heavy distorted 808, crisp sixteenth hi-hats, reversed piano stabs, vinyl crackle; 0-2 s piano alone, 2 s full beat drops, 7 s hi-hats cut out for one bar, 8 s impact and full beat returns, 14 s beat filters down, 16 s stops, instrumental, no vocals`
- **Geräusche:** Filmprojektor-Rattern 25 dB unter der Musik, ein Kamera-Auslöser je Fotostreifen, ein dumpfer Hit auf dem Negativ.

## Regler
- Duoton-Farbe: Petrol ist der Kern; Graublau oder Oliv tragen auch, Negativ dann in der Komplementärfarbe.
- Tempo: Median 0,1 bis 0,25 s. Darüber verliert es das Flimmern.
- Störbild-Dichte: ein Störbild je ein bis zwei Sekunden.
- Figur: eine Person, viele Einstellungen. Wechselnde Personen machen es zur Montage ohne Mitte.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen.
- Standbild an drei Stellen: keine warme Farbe außer im Negativ, Lichter milchig, Korn sichtbar.
- Streifen bei 12 fps: Störbilder verteilt, nicht gehäuft; erster Shot ruhig und lang.

## Fallen
- Hell-Dunkel-Wechsel mit Schwarzbildern öfter als dreimal je Sekunde → Flimmer- und Epilepsie-Gefahr. Schwarzbilder sparsam, Unschärfe statt Schwarz.
- Zu sauberes Footage → wirkt digital. Korn und Vignette nie unter 8 % und 30 %.
- Negativ ohne Farbziehung → Gesicht wird Cyan statt Lachs. Nach dem Invertieren auf Rosa ziehen.
- Jeder Shot ein neues Motiv → das Auge findet keinen Halt. Einstellungen wiederkehren lassen und stottern.
- Fotostreifen gerade gelegt → wirkt wie ein Layout. Immer schräg, mit weißem Rand.
