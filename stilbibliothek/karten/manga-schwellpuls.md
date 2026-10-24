---
id: manga-schwellpuls
name: Manga-Schwellpuls
familie: zeichentrick
kurz: Wenige Manga-Zeichnungen einer einzigen Figur in reinem Schwarz und Weiß, immer wieder neu geschwellt, verrauscht und gezoomt, Gründe auch invertiert, im dichten Beat-Schnitt.
kern: [echtes 1-Bit ohne Grau und ohne Papierton, eine Figur aus sechs bis acht Bildern endlos variiert durch Schwelle und Ausschnitt, Schnitt dicht und zum Ende noch dichter]
energie: 5
format_quelle: "4:3"
laenge_s: [10, 20]
messung:
  shot_median_s: 0.23
  schnitte_pro_s: 5.8
  schnitte_verlauf: [5.3, 5.5, 6.7]
  bpm: 115
  schnitt_auf_beat: mittel
  lufs: -9.5
  helligkeit: 0.41
  kontrast: 0.39
  farbigkeit: 0.0
schnittmuster_16tel: [8, 4, 8, 1, 3, 4, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 2, 2, 4, 1, 1, 1, 1, 4, 2, 2, 2, 2, 1, 3, 4, 2, 2, 2, 2, 1, 1, 1, 1, 3, 1, 1, 4]
palette:
  tusche: "#010101"
  weiss: "#FDFDFD"
  korn_hell: "#A6A6A6"
  korn_dunkel: "#585858"
effekte: [harter-schnitt, blitzbild, stottern, wiederholung, zoom-schlag, push-in, pull-out, schwellwert, invertieren, schwarzweiss, filmkorn, anime-zeichnung, beat-getrieben, ton-stopp, schwellwert-puls, dither, streifenversatz]
kamera: Keine echte Kamera; jedes Bild bekommt einen schnellen Digitalzoom von wenigen Prozent hinein oder heraus, dazu ein, zwei Zoom-Schläge auf den Höhepunkten.
ton: Sehr laut gemischt (−9,5 LUFS), Beat um 115 BPM, Spitzen an 0 dBFS; Stimme in den Bildern nicht erkennbar, harter Schluss auf Schwarz.
braucht: [illustrationen]
motor_aufwand: klein
einsatz: [hook, intro, musikvideo, portrait, uebergang]
abnahme:
  shot_median_s: [0.18, 0.28]
  schnitte_pro_s: [4.6, 7.0]
  helligkeit: [0.33, 0.49]
  farbigkeit: [0.00, 0.02]
  lufs: [-10.5, -8.5]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Manga-Schwellpuls

Ein Manga-Panel, das im Takt durch die Schwelle gejagt wird. Es gibt nur eine Figur und eine Handvoll Zeichnungen; die Energie kommt daraus, dass dieselben Bilder auf jedem Beat heller, dunkler, verrauscht, im Halbschatten, vor invertiertem Grund oder enger geschnitten wiederkommen. Gesichter nie invertieren, dunkle Gesichtsflächen nur als Halbschatten.

## Kern
- **Echtes 1-Bit:** Reines Schwarz und reines Weiß, kein Papierton, kein Grau. Graustufen gibt es nur als Rauschen (Dither) und einmal als kurzes Original-Blitzbild.
- **Wenige Bilder, endlos variiert:** Sechs bis acht Zeichnungen einer Figur tragen das ganze Stück. Jede kommt drei- bis sechsmal wieder, mit anderer Schwelle, anderem Ausschnitt, mal im Halbschatten vor invertiertem Grund, mal als Rauschen. Neue Motive braucht der Stil nicht.
- **Dichter Schnitt, der noch dichter wird:** 5,3 → 5,5 → 6,7 Schnitte je Sekunde. Am Ende Leerbilder in Weiß und Schwarz im Wechsel, dann Schwarz.

## Erkennung
- **Bild:** `#010101` und `#FDFDFD`, sonst nichts. Manga-Zeichnungen mit wildem Haar, harten Schatten und Tuschespritzern; dahinter Splatter-Flächen, die in großen weißen oder schwarzen Klecksen auslaufen, und grafische Bruchstücke (Linienbündel, Kreise, Kritzel). Dieselbe Zeichnung erscheint mit niedriger Schwelle fast weiß, mit hoher fast schwarz. Einige Bilder sind als grobes Zufallsrauschen gerastert. Senkrechte gestrichelte Störstreifen neben dem Kopf. Einmal pro Hälfte blitzt das Original in Graustufen mit Korn auf. Gemessen: Helligkeit 0,41, Kontrast 0,39, Farbigkeit 0, 54 % der Fläche schwarz.
- **Schnitt:** 76 Schnitte in 13 Sekunden, Median-Shot 0,23 s (zwei Sechzehntel bei 115 BPM), längster 1,0 s. 54 % der Schnitte auf dem Raster gegen 31 % bei Zufall, Rundungsabweichung 0,28: der Takt ist spürbar, aber locker. Übergänge: harter Schnitt, Leerbild weiß oder schwarz von zwei Frames, Stottern (dasselbe Bild zwei- bis viermal mit neuem Ausschnitt), ein Zoom-Schlag.
- **Ton:** −9,5 LUFS, Lautheitsspanne 5,9 LU, True Peak 0,1 dBFS. Laut, druckvoll, harter Abbruch.
- **Text:** keiner.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Gesicht frontal ganz nah | 28 % | Gesicht füllt 100 % der Bildhöhe, Augen auf 40 % von oben, mittig; hell geschwellt oder im Halbschatten (Gesichter nie invertieren) | 1 bis 3 Sechzehntel |
| Halbfigur im Profil vor Splatter | 25 % | Figur links, Kopf 30 bis 40 % der Bildhöhe, rechts Bruchstücke und Tuschewolke, unten weißer Klecks | 2 bis 4 Sechzehntel, oft vier Varianten hintereinander |
| Kopf klein im Schwarz | 15 % | Kopf und Schultern 50 bis 60 % der Bildhöhe, mittig, Rest schwarz, Störstreifen links und rechts | 2 bis 8 Sechzehntel |
| Detail (Auge, Haar, Hals) | 12 % | Ausschnitt so eng, dass die Form abstrakt wird, diagonal | 1 bis 2 Sechzehntel |
| Leerbild weiß oder schwarz | 12 % | ganzes Bild eine Farbe | 1 Sechzehntel |
| Graustufen-Original mit Korn | 4 % | zwei Figuren nebeneinander, grau, verrauscht | 1 Sechzehntel |
| Ganzkörper frontal auf Weiß | 4 % | Figur 90 % der Bildhöhe, rechts, viel Weiß links | 1 bis 4 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1 s):** Kopf klein im Schwarz, erst verrauscht, dann klar; eine volle Sekunde Stand.
- **Aufbau (1 bis 4 s):** Gesicht frontal hell, Halbfigur im Profil, Details, Maske im Rauschen; erste Leerbilder.
- **Stotter-Kette (4 bis 5 s):** dieselbe Halbfigur vier Mal mit wanderndem Ausschnitt.
- **Mitte (5 bis 9 s):** Profil groß, Kopf klein mit Störstreifen, Gesichter in schneller Folge, Graustufen-Blitz.
- **Verdichtung (9 bis 12 s):** Halbfigur dreimal, ein extremer Zoom-Schlag, Leerbilder schwarz, weiß, schwarz in Einzel-Frames.
- **Schluss (12 bis 13 s):** Gesicht hell, dasselbe Gesicht dunkel, Weiß, dann eine halbe Sekunde Schwarz.

## Schnittmuster
Bauplan für 16,7 s bei 115 BPM (128 Sechzehntel zu 0,13 s, acht Takte). Inhalt austauschbar, Rhythmus bleibt.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-7 | Kopf klein im Schwarz, Rauschen löst sich zu klarem 1-Bit | hart | Intro, Riser |
| 2 | 8-11 | Gesicht frontal, niedrige Schwelle | hart | Beat setzt ein |
| 3 | 12-19 | Halbfigur vor Splatter, Zoom heraus | hart | Beat |
| 4 | 20-23 | Detail Haar, dann Detail Auge | hart | Tick, Snare |
| 5 | 24-25 | Gesicht mit Rauschen | hart | Hit |
| 6 | 26, 27 | Leerbild weiß, dann Graustufen-Original | Blitzbild | Hit |
| 7 | 28-29 | Ganzkörper frontal zweimal | Stottern | Tick |
| 8 | 30-45 | Halbfigur vier Mal je vier Sechzehntel, Ausschnitt und Schwelle wandern | Stottern | Beat |
| 9 | 46-53 | Profil groß im Schwarz, dann Profil vor Bruchstücken | hart | Beat |
| 10 | 54-61 | Kopf klein, Störstreifen, dann im Halbschatten | hart | Bass |
| 11 | 62-71 | Auge, Gesicht hell, Gesicht im Rauschen, Gesicht dunkel, je zwei bis drei | hart | Beat |
| 12 | 72-79 | Halbfigur vor Splatter, zweimal | Stottern | Beat |
| 13 | 80-95 | Verdichtung: alle Bilder je ein bis zwei Sechzehntel, Graustufen-Original einmal | hart | Beat voll |
| 14 | 96-103 | Ganzkörper, dann Halbfigur dreimal mit steigender Schwelle | Stottern | Riser |
| 15 | 104 | Halbfigur, Zoom-Schlag auf 140 % | Zoom-Schlag | Hit |
| 16 | 105-109 | Schwarz, Detail, Weiß, Detail, Weiß | Blitzbild | Stotter-Hits |
| 17 | 110-115 | Gesicht hell, dann dasselbe dunkel | hart | letzter Hit |
| 18 | 116-127 | Schwarz | hart | Musik stoppt auf 116 |

## Rezept für einen Code-Motor
- **Grund:** Kein Papier. Leerbilder sind reines `#FFFFFF` oder `#000000`.
- **Bildbehandlung:** Jede Zeichnung einmal entsättigen, dann Schwellwert mit variabler Schwelle zwischen 35 und 70 % (SVG `feComponentTransfer` mit `type="discrete"` und `tableValues="0 1"`, die Schwelle über ein vorgeschaltetes `type="linear"` mit wechselndem intercept verschieben; in Canvas per Pixel-Schleife auf einer gecachten Graustufen-Kopie). **Schwellwert-Puls:** auf jedem Achtel springt die Schwelle um 10 bis 15 Punkte, im Stottern wandert sie stetig. **Dither:** vor dem Schwellwert weißes Rauschen mit ±25 % Amplitude in Körnern von 1 bis 2 px addieren (neues Seed je Frame), so entsteht das grobe Zufallsraster. **Invertieren** nur Gründe (Splatter, Fokuslinien, Tinte), bei rund 20 % der Bilder; **Gesichter nie invertieren, dunkle Gesichtsflächen nur als Halbschatten** (ein Negativ auf Haut liest sich als dunkel geschminkte Karikatur). Graustufen-Blitz: Original entsättigt, Korn 15 %, nur zwei bis drei Frames.
- **Bausteine:** Splatter-Maske (Rauschfeld mit baseFrequency 0,02 bis 0,04, auf 50 % geschwellt, dann `feMorphology` erode 2 für Spritzerkanten), legt sich als weißer oder schwarzer Klecks über das untere Drittel; Störstreifen (20 bis 40 senkrechte gestrichelte Linien, 1 bis 2 px breit, Strichlänge 1 bis 2 % der Bildhöhe, in zwei Bändern von je 10 % Bildbreite links und rechts des Kopfes, zwei bis vier Frames, dann weg); Zoom (je Shot 3 bis 8 % Push oder Pull, linear, über die ganze Shot-Dauer); Zoom-Schlag (ein Frame auf 140 %, zurück in drei Frames).
- **Typografie:** Die Vorlage hat keinen Text. Wird einer gebraucht: ein Wort je Beat in sehr fetter Grotesk mit Kanji-Anmutung (frei lizenziert zum Beispiel Dela Gothic One), weiß auf Schwarz oder schwarz auf Weiß, 15 bis 20 % der Bildhöhe, ebenfalls geschwellt.
- **Bewegung:** Sechzehntel-Raster der gemessenen Musik. Zustände dauern ein bis vier Sechzehntel, Halte bis acht nur am Anfang. Leerbilder genau zwei Frames bei 30 fps. Jede Zeichnung höchstens zweimal direkt hintereinander mit gleicher Schwelle.
- **Formate:** In 9:16 werden die Gesichter auf 70 % der Bildhöhe gesetzt und oben und unten mit Splatter aufgefüllt; Halbfiguren rücken in die Mitte, die Bruchstücke wandern über und unter den Kopf. In 16:9 Gesichter auf volle Höhe, Splatter füllt die Seiten.
- **Neue Kennungen:** `neu:schwellwert-puls`: Die Schwelle des Zweitons springt im Takt, dasselbe Bild wird heller oder dunkler. `neu:dither`: Zufallsrauschen vor dem Schwellwert ergibt ein grobes Punktraster. `neu:streifen-glitch`: Senkrechte gestrichelte Störstreifen stehen für zwei bis vier Frames neben dem Motiv.

## Material
- **Bilder (Gesicht):** `black and white manga illustration of a [subject], extreme close-up of the face, heavy black ink, rough brush strokes, ink splatter, wild hair strands, hard shadows, high contrast, no grey, no screentone`
- **Bilder (Halbfigur):** `black and white manga panel of a [subject] in profile, half body on the left, abstract ink shapes and splashes exploding to the right, heavy blacks, high contrast, no grey`
- **Musik:** `Aggressive drift phonk, 115 BPM, distorted cowbell melody, heavy 808 bass, hard clap on two and four, eight bars, filtered intro for the first two seconds, full drop at two seconds, short stutter fill at fourteen seconds, hard stop at fifteen seconds, instrumental, no vocals`
- **Geräusche:** keine nötig; höchstens ein trockener Hit auf dem Zoom-Schlag, 10 dB unter dem Beat.

## Regler
- Schwellenbereich: eng (45 bis 60 %) für ruhigere Variante, weit (30 bis 75 %) für mehr Flackern.
- Anteil Dither-Bilder: 0 bis 20 %.
- Anzahl Zeichnungen: vier bis zehn; mehr als zehn nimmt dem Stil das Wiederkehren.
- Tempo: 100 bis 130 BPM.
- Eine einzige Akzentfarbe ist möglich, kippt den Stil aber Richtung Kopierer; dann Familie wechseln.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` im Kopf dieser Karte treffen; Farbigkeit muss praktisch null sein.
- Standbild-Prüfung: Histogramm hat nur zwei Spitzen (außer im Graustufen-Blitz); Augen an drei zufälligen Stellen lesbar.
- Streifen bei 12 fps: dieselbe Zeichnung kehrt mindestens dreimal wieder, jeweils sichtbar anders geschwellt; die Dichte steigt im letzten Drittel.

## Fallen
- Graustufen-Material ohne Schwelle durchrutschen lassen → wirkt wie Fehler; Graustufen nur als bewusster Blitz von zwei bis drei Frames.
- Schwelle für alle Bilder gleich → das Pulsieren fehlt; Schwelle je Beat verschieben.
- Gesichter versinken bei hoher Schwelle im Schwarz → für Gesichter höchstens 60 %, Augen müssen bleiben.
- Leerbilder in Weiß und Schwarz im schnellen Wechsel sind eine Epilepsie-Gefahr → höchstens drei harte Wechsel je Sekunde außerhalb des Schlusses, Schlussfolge kürzer als eine Sekunde.
- Zu viele verschiedene Zeichnungen → wirkt wie ein Bilderdurchlauf; die Wiederkehr ist der Stil.
- Die Lautheit der Vorlage (−9,5 LUFS) übersteuert auf manchen Plattformen → Master auf −11 bis −10 LUFS mit höchstens −1 dBTP.
- Eigene Figur ganz ins Schwarz gezogen (nur Augen und Lichter weiß) wirkt wie eine gefüllte Maske → Gesichter nie invertieren, dunkle Gesichtsflächen nur als Halbschatten (eine Hälfte); Schwelle auf Gesichtern höchstens 55 % (Erfahrung 16.10.2026)
- Halbschatten aus einem waagerechten Verlauf zieht eine Lineal-Kante über glatte Flächen → Kante mit der weichgezeichneten Helligkeit verschieben
- Dither in 1-px-Körnern wird am Handy grau → Körner um 2 px
- Weißer Grund und helle Kleidung heben die Helligkeit weit über die Abnahme → schwarze und invertierte Gründe, Figuren auf Schwarz
- Video-Material geschwellt Bild für Bild prüfen: geschwellte Flure und Lichtwechsel ergeben Zufallsformen (auch gesichtsähnliche) und Flackern
- Shots in Stotter-Teile zerlegen startet Clips neu → Startzeit je Teil mitführen; Stotter-Teile mit ähnlicher Helligkeit erkennt die Schnittmessung nicht, gebaute Dichte liegt über der gemessenen
- Bildtexte auf Posen mit offenem Mund lesen sich wie gesprochen, auch ohne Stimme → nur auf geschlossene Münder
- Die eingebaute Sechzehntel-Lücke vor einem Phrasenschlag im Bett ist der sauberste Ort für den harten Stopp vor einer Pointe
- Invertierte Figur (Haut schwarz, Bart, Lippen, Augen weiß), auch nur als Detail von Auge oder Hand → Karikaturbild; Umkehrung nur je Schicht auf Gründen und Clips, nie auf der Figur, im Werkzeug als Sperre
- Linearer Ausblendverlauf unter einem Brustbild wird von der Schwelle zur linealgeraden Schnittkante → Alpha-Maske mit zerrissener Tuschekante oder Kante unter ein Band legen
- Hell-Dunkel-Wechsel auf Gamma-Mittelwerten zählen unterschätzt: auf linearer Luminanz mit Sprung über 0,20 messen; Leerbilder in schnellen Läufen sparen, Zoom-Schlag lieber weiterlaufen lassen
- Ein reiner Umriss eines Alltagsgegenstands liest sich nicht als Gegenstand → dunkle Fläche mit hellen Kennzeichen (Papier im Schacht) und weißem Gegenlicht-Rand
