---
id: malerei-raster
name: Malerei-Raster
familie: malerei
kurz: Eine Farbreise von gemalten Szenen in rotem Rauchlicht über flache Vektorfiguren auf Creme zu kontrastreichem Schwarzweiß, verbunden durch ein Schweizer Typo-Raster aus dünnen Linien und Block-Glitches.
kern: [drei Bildwelten nacheinander (warme Malerei, flache Illustration auf Papier, Schwarzweiß-Foto), Typo-Raster mit dünnen roten Linien und Wörtern, die einzeln erscheinen, ruhiger Anfang mit langen gemalten Einstellungen]
energie: 2
format_quelle: "16:9"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.75
  schnitte_pro_s: 1.2
  schnitte_verlauf: [0.4, 2.0, 1.3]
  bpm: 63
  schnitt_auf_beat: mittel
  lufs: -14.2
  helligkeit: 0.32
  kontrast: 0.19
  farbigkeit: 0.11
schnittmuster_16tel: [8, 8, 9, 0, 0, 6, 0, 0, 3, 4, 4, 1, 2, 4, 2, 2, 0, 7, 7]
palette:
  rauch_dunkel: "#1E070B"
  glut: "#8A221E"
  lampe: "#DC723C"
  papier: "#F4F2F5"
  creme: "#EAE5D2"
  ocker: "#F6D865"
  tusche: "#1C1516"
  linie: "#8B1E28"
effekte: [harter-schnitt, glitch-uebergang, masken-wechsel, invertieren, push-in, malerei, schwarzweiss, papier, glow, vignette, text-hinter-figur, wort-auf-beat, mono-zeile, titelkarte, typo-raster, welten-folge]
kamera: In den gemalten Szenen langsamer Push hinein; Illustrationen und Fotos stehen fast, Bewegung im Mittelteil kommt aus den Übergängen.
ton: Gleichmäßig gemischtes Stück um 63 BPM, −14,2 LUFS bei nur 1,1 LU Spanne; nach den Bildern vermutlich Jazz oder Jazz-Hip-Hop, Stimme nicht feststellbar.
braucht: [illustrationen, fotos-figur, nur-typo]
motor_aufwand: mittel
einsatz: [intro, trailer, ganzes-kurzvideo, musikvideo]
abnahme:
  shot_median_s: [0.60, 0.90]
  schnitte_pro_s: [1.0, 1.5]
  helligkeit: [0.26, 0.39]
  farbigkeit: [0.08, 0.13]
  lufs: [-15.2, -13.2]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Malerei-Raster

Ein ruhiger Bilderbogen wie ein Plattencover, das sich umblättert: erst gemalte Szenen in rotem Rauchlicht, dann klare Vektorfiguren auf Papier mit einem feinen Typo-Raster, am Ende hartes Schwarzweiß. Die Wirkung kommt aus dem Wechsel der Bildwelten, nicht aus Tempo.

## Kern
- **Drei Bildwelten nacheinander:** warme Malerei mit Glut und Rauch, flache Illustration auf Weiß und Creme, kontrastreiches Schwarzweiß. Jede Welt hat ihren Abschnitt; gemischt wird nur am Übergang.
- **Typo-Raster:** Dünne dunkelrote Linien kreuzen sich auf weißem Grund, an den Kreuzungen tauchen kleine fette Grotesk-Wörter einzeln auf dem Beat auf. Dasselbe Raster legt sich später über ein Foto.
- **Ruhiger Anfang:** Drei gemalte Einstellungen von rund zwei Sekunden, dann erst wird geschnitten. Wer sofort schneidet, verliert die Malerei.

## Erkennung
- **Bild:** Malerei mit überlangen Figuren, Pinselstrich sichtbar, Licht von Lampions und Glut: dunkler Grund `#1E070B`, Glut `#8A221E`, Lampenlicht `#DC723C`. Ein riesiger dreizeiliger Satz in schmaler, angerauter Plakatschrift in Rot über einer gemalten Figur. Danach Papierweiß `#F4F2F5` mit Linien in `#8B1E28`, flache Vektorfiguren in Rot, Schwarz und Creme `#EAE5D2`, einmal eine Papierstruktur mit Ocker `#F6D865`. Am Ende Schwarzweiß mit tiefem Schwarz `#1C1516`, eine gezeichnete Szene in Grau, ein Foto mit Gegenlicht, ein Objekt von oben. Gemessen: Helligkeit 0,32, Kontrast 0,19, Farbigkeit 0,11, 40 % fast schwarz.
- **Schnitt:** 20 Schnitte in 16,5 Sekunden, Median 0,75 s. Dichte 0,4 → 2,0 → 1,3 Schnitte je Sekunde: drei lange Einstellungen, ein dichter Mittelteil, ruhiges Ende mit 1,6 s Objekt und 1,6 s Schwarz. 45 % der Schnitte auf dem Raster gegen 17 % bei Zufall. Übergänge: Block-Glitch (schwarze, graue und rote Rechtecke treppen durchs Bild, dazu Zeilen-Verschmieren), weiße Fläche schiebt sich über das Bild, ein Frame invertiert vor dem letzten Motiv.
- **Ton:** −14,2 LUFS, Lautheitsspanne 1,1 LU, True Peak −0,7 dBFS: sehr gleichmäßig.
- **Text:** vier Rollen: Plakat-Satz riesig über einer Figur; Raster-Wörter einzeln an Linienkreuzungen; zwei kleine Seitenlabels links und rechts auf halber Höhe; winzige Zeile mittig auf Schwarz am Ende.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Gemalte Szene im Rauchlicht | 25 % | Figur 60 bis 90 % der Bildhöhe, rechts oder mittig, Lichtquellen oben, Rauch | 8 bis 9 Sechzehntel |
| Plakat-Satz über Figur | 8 % | drei Zeilen füllen die Bildbreite, Figur dahinter angeschnitten | 8 Sechzehntel |
| Typo-Raster auf Weiß | 12 % | sechs bis zehn Linien, Wörter links oben bis Mitte, 6 bis 12 % der Bildhöhe | 6 Sechzehntel |
| Vektorfigur auf Creme | 15 % | Figur 70 bis 100 % der Bildhöhe, liegend oder Brustbild, große ruhige Flächen | 3 bis 4 Sechzehntel |
| Zeichnung in Schwarzweiß | 8 % | Figur vorne 60 % der Bildhöhe, Stadt und Brücke grau dahinter | 2 Sechzehntel |
| Schwarzweiß-Foto | 17 % | Musiker im Gegenlicht auf Schwarz oder Porträt halbnah, mit Raster-Wörtern | 2 bis 4 Sechzehntel |
| Objekt von oben | 10 % | rundes Objekt mittig links, 90 % der Bildhöhe, Hand am Rand | 7 Sechzehntel |
| Schwarz mit Mini-Zeile | 5 % | Zeile mittig, 1,2 % der Bildhöhe | 7 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 2 s):** gemalte Szene mit Lichtern und Rauch, langsamer Push.
- **Satz (2 bis 4 s):** Plakat-Satz riesig über einer gemalten Figur.
- **Stimmung (4 bis 6 s):** dunkle Szene mit Glutlicht.
- **Umbruch (6 bis 7,5 s):** ein rundes Objekt dreht, weiße Fläche schiebt sich darüber, Typo-Raster mit drei Wörtern einzeln.
- **Mittelteil (7,5 bis 10,5 s):** Block-Glitch, Vektorfiguren auf Creme, Seitenlabels, Papier mit Ocker.
- **Schwarzweiß (10,5 bis 13,2 s):** Zeichnung, Foto im Gegenlicht, Porträt mit Raster und Wörtern.
- **Schluss (13,2 bis 16,5 s):** ein Frame invertiert, Objekt von oben 1,6 s, Schwarz mit Mini-Zeile.

## Schnittmuster
Bauplan für 18 s bei 63 BPM (76 Sechzehntel zu 0,238 s, knapp fünf Takte). Hier lohnt es, in Sekunden mitzudenken: lange Einstellungen um 2 s, im Mittelteil 0,5 bis 1 s.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-7 | gemalte Szene im Rauchlicht, Push 6 % | hart | Intro |
| 2 | 8-15 | Plakat-Satz über gemalter Figur | hart | Beat setzt ein |
| 3 | 16-24 | dunkle gemalte Szene mit Glut | hart | Beat |
| 4 | 25 | rundes Objekt, weiße Fläche schiebt sich darüber | Masken-Wechsel | Wisch |
| 5 | 26-31 | Typo-Raster, drei Wörter je Viertel | hart | Beat, Tick je Wort |
| 6 | 32 | Block-Glitch in Rot und Grau | Glitch | Bitcrush |
| 7 | 33-36 | Vektorfigur liegend auf rotem Möbel | hart | Beat |
| 8 | 37-40 | Vektor-Brustbild auf Weiß und Grau | hart | Beat |
| 9 | 41-44 | Vektorfigur mit Seitenlabels | hart | Beat |
| 10 | 45-46 | Papier mit Ocker | hart | Akzent |
| 11 | 47-48 | Zeichnung in Schwarzweiß | hart | Beat |
| 12 | 49-52 | Foto im Gegenlicht auf Schwarz | hart | Beat |
| 13 | 53-56 | Porträt mit Raster-Wörtern, die einzeln erscheinen | hart | Tick je Wort |
| 14 | 57 | invertiertes Bild | Blitzbild | Hit |
| 15 | 58-66 | Objekt von oben | hart | Beat dünner |
| 16 | 67-75 | Schwarz mit Mini-Zeile | hart | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** drei Welten. Rauch: Verlauf `#1E070B` nach `#421B1E`, zwei Rauchschichten aus weichem Rauschen in `#8A221E` (20 % Deckung), driften 1 % je Sekunde. Papier: `#F4F2F5` mit 2 % Faserrauschen, Creme `#EAE5D2` mit grober Papierstruktur. Schwarz: `#1C1516`.
- **Bildbehandlung:** Malerei warm graden (Schatten nach `#1E070B`, Lichter nach `#DC723C`, Sättigung +10 %), Glow auf Lampen (Schwelle 85 %, Weichzeichner 3 % der Bildhöhe, `screen` 50 %), Vignette 30 %. Vektorfiguren unverändert, flach. Schwarzweiß-Fotos: entsättigen, Kurve hart (Schwarzpunkt 12 %, Weißpunkt 88 %), Korn 5 %.
- **Bausteine:** Typo-Raster (sechs bis zehn Linien von 1 px in `#8B1E28`, 60 % Deckung, waagerecht und senkrecht, zeichnen sich in vier Frames von einer Kante aus; Wörter erscheinen hart an Kreuzungen, je eins auf dem Viertel); Plakat-Satz (drei Zeilen, Gesamthöhe 80 % des Bildes, Rot `#8A221E` mit Kratzmaske, Figur freigestellt davor); Block-Glitch (vier bis sechs Rechtecke in Schwarz, Grau und Rot, treppenförmig versetzt, je zwei Frames, dazu ein Band von 20 % Bildhöhe, in dem eine Pixelzeile waagerecht gestreckt wird, drei Frames); Masken-Wechsel (weiße Fläche fährt in sechs Frames von oben über das Bild); Seitenlabels (zwei kleine Wörter links und rechts auf 50 % Höhe, 5 % vom Rand); Invertier-Blitz (ein Frame).
- **Typografie:** Raster-Wörter in fetter schmaler Grotesk (frei lizenziert zum Beispiel Archivo Narrow 700 oder Inter Tight 800), 6 bis 12 % der Bildhöhe, sehr eng gesperrt, Größen gemischt. Plakat-Satz in schmaler, schwerer Plakatschrift (zum Beispiel Anton), mit Kratzmaske. Seitenlabels und Mini-Zeile in schlichter Grotesk (zum Beispiel Inter 600), 2,5 % beziehungsweise 1,2 % der Bildhöhe.
- **Bewegung:** Gemalte Szenen mit Push 5 bis 8 % über 2 s, Ease-in-out. Vektorfiguren und Fotos stehen oder ziehen 2 %. Schnitte im Mittelteil auf Achtel und Viertel, Wörter auf Viertel.
- **Formate:** Quelle 16:9. In 9:16 gemalte Szenen auf die Figur beschneiden (Figur 70 % der Bildhöhe, Lichter oben behalten); Typo-Raster wird hochkant neu gesetzt, Wörter untereinander; Seitenlabels werden oben und unten statt links und rechts. In 16:9 wie die Quelle.
- **Neue Kennungen:** `neu:typo-raster`: Dünne Linien bilden ein Raster, an den Kreuzungen erscheinen Wörter einzeln. `neu:welten-folge`: Das Stück durchläuft nacheinander mehrere geschlossene Bildwelten.

## Material
- **Bilder (Malerei):** `expressive oil painting of [subject] in a smoky dimly lit room, warm red and orange lamplight, elongated stylized proportions, visible brush strokes, deep shadows, moody`
- **Bilder (Vektor):** `flat minimalist vector illustration of [subject], cream and white background, deep red and black shapes, elongated stylized proportions, large calm areas, subtle paper texture`
- **Musik:** `Smoky jazz hip-hop, 63 BPM, dusty boom bap drums, upright bass, muted trumpet phrases, vinyl crackle, soft Rhodes chords, very even dynamics, drums enter at two seconds, short filter dip at six seconds, drums thin out from fourteen seconds, ends with a lone trumpet note at sixteen seconds, instrumental, no vocals`
- **Geräusche:** Knistern einer Platte unter allem (−24 dB), Tick für jedes Raster-Wort, kurzes Bitcrush beim Block-Glitch; 12 bis 18 dB unter der Musik.

## Regler
- Reihenfolge der Welten: warm → Papier → Schwarzweiß ist der Kern; umgekehrt funktioniert als Rückblende.
- Länge der Anfangseinstellungen: 1,5 bis 2,5 s.
- Rasterfarbe: Dunkelrot oder Schwarz; nie bunt.
- Für Erklärstücke: Raster-Wörter tragen die Kernbegriffe, ein bis drei je Raster.
- Anteil Schwarzweiß: 20 bis 35 %.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen.
- Standbild-Prüfung: an je einer Stelle pro Welt ist die Welt eindeutig (warm gemalt, flach auf Papier, Schwarzweiß); Rasterlinien sind 1 px fein, nicht dicker.
- Streifen bei 12 fps: die ersten drei Einstellungen stehen je mindestens 1,5 s; Raster-Wörter erscheinen einzeln, nie alle gleichzeitig.

## Fallen
- Welten durchmischt statt nacheinander → wirkt wie eine zufällige Sammlung; je Abschnitt eine Welt.
- Rasterlinien zu dick oder zu dunkel → wirkt wie Tabelle statt Typografie; 1 px, 60 % Deckung.
- Echte Fotos bekannter Personen → Bildrechte und Persönlichkeitsrechte; nur eigene oder frei lizenzierte Fotos.
- Malerei mit KI-Glanz → im Prompt sichtbaren Pinselstrich und Leinwand verlangen, Glanzlichter dämpfen.
- Block-Glitch zu lang → stört die Ruhe; höchstens drei Frames.
