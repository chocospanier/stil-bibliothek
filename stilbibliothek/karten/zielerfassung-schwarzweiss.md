---
id: zielerfassung-schwarzweiss
name: Zielerfassung Schwarzweiß
familie: glitch
kurz: "Ein Hochkant-Porträt in hartem Schwarzweiß, das wie eine Zielerfassung abläuft: Punktwolke formt das Gesicht, Terminalzeilen tippen, Augen im Kachelraster, Ziffernwände, Silhouetten-Gitter; nur ein Kleidungsstück ist farbig."
kern: [Schwarzweiß in vielen Härtegraden (Punktraster, Graustufe, Negativ, 1-Bit-Silhouette) im schnellen Wechsel, Erfassungs-Sprache (tippende Terminalzeile, Ziffernwand, Kachelraster, Silhouetten im Auge), genau ein farbiges Kleidungsstück als Auflösung]
energie: 5
format_quelle: "9:16"
laenge_s: [10, 18]
messung:
  shot_median_s: 0.20
  schnitte_pro_s: 4.6
  schnitte_verlauf: [3.7, 5.3, 4.8]
  bpm: 69
  schnitt_auf_beat: mittel
  lufs: -14.1
  helligkeit: 0.42
  kontrast: 0.31
  farbigkeit: 0.01
schnittmuster_16tel: [1, 0, 1, 2, 1, 2, 0, 1, 0, 1, 0, 3, 3, 2, 1, 0, 5, 0, 0, 0, 0, 2, 2, 2, 1, 1, 0, 2, 2, 2, 1, 0, 2, 2, 1, 2, 1, 0, 0, 0]
palette:
  schwarz: "#070707"
  dunkelgrau: "#505552"
  hellgrau: "#A9ABA9"
  weiss: "#F7F7F7"
  ziffern: "#C8C8C8"
  akzent_gruen: "#2E8155"
effekte: [harter-schnitt, blitzbild, stottern, wiederholung, raster-collage, glitch-uebergang, push-in, schwarzweiss, schwellwert, invertieren, ein-akzent, augen-makro, silhouette, klone, freisteller, partikel, mono-zeile, wortkolonne, hud, beat-getrieben, punktwolke, ziffernwand, nachbild]
kamera: Studio-Aufnahmen mit kurzen Pushs und Ruckzooms; viel Bewegung entsteht aus Schnitt, Negativ-Wechsel und Echos (Bewegungsnachzieher), nicht aus Kamerafahrten.
ton: Dichter Beat, gemessen 69 BPM (Achtel-Raster etwa 0,22 s, vermutlich Doppeltempo um 138), −14,1 LUFS mit nur 1,9 LU Spanne; Stimme nicht feststellbar.
braucht: [fotos-figur, nur-typo]
motor_aufwand: mittel
einsatz: [hook, portrait, produkt, intro]
abnahme:
  shot_median_s: [0.16, 0.24]
  schnitte_pro_s: [3.7, 5.5]
  helligkeit: [0.34, 0.50]
  farbigkeit: [0.00, 0.03]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Zielerfassung Schwarzweiß

Ein Porträt, das sich anfühlt, als würde ein System eine Person suchen, finden und erfassen. Alles ist Schwarzweiß in allen Härten, Terminalzeilen tippen mit, und erst ganz am Ende ist ein einziges Kleidungsstück farbig. Die Energie kommt aus dem Wechsel der Härtegrade im Achtel und aus den Erfassungs-Bildern.

## Kern
- **Viele Härtegrade Schwarzweiß:** Punktwolke aus weißen Punkten, weiches Graustufenfoto, Negativ, harte 1-Bit-Silhouette (schwarz auf weiß und weiß auf schwarz), Streifenmaske. Die Wechsel zwischen den Härten sind der Schnitt.
- **Erfassungs-Sprache:** Eine kleine Terminalzeile oben links tippt Status-Meldungen mit Blockcursor, Augen erscheinen als Kachelraster, ganze Wände aus großen Ziffern und Kennungen füllen das Bild, Silhouetten stehen in der Pupille, ein Raster aus vielen kleinen Figuren zeigt Posen.
- **Ein Akzent als Auflösung:** Ein Kleidungsstück ist farbig (hier ein Grün), zuerst kurz am Anfang als Vorgriff, dann als Schlussbild. Sonst Farbigkeit null.

## Erkennung
- **Bild:** Schwarz `#070707`, Dunkelgrau `#505552`, Hellgrau `#A9ABA9`, Weiß `#F7F7F7`, Ziffern in hellem Grau `#C8C8C8`, Akzent `#2E8155`. Studio mit weißer Hohlkehle und schwarzer Decke als Bogen oben. Bewegungsechos: drei bis fünf halbtransparente Nachbilder der Figur. Streifenmaske: waagerechte Balken legen sich über das Bild, Kontur der Figur mit mehrfacher, welliger Umrisslinie. Gemessen: Helligkeit 0,42, Kontrast 0,31, Farbigkeit 0,01, 40 % fast schwarz.
- **Schnitt:** 63 Schnitte in 13,6 Sekunden, Median 0,20 s, längste Einstellung 1,1 s. Dichte 3,7 → 5,3 → 4,8 Schnitte je Sekunde, bis zum Ende dicht. 30 % der Schnitte auf dem Raster gegen 18 % bei Zufall, Rundungsabweichung 0,28: Takt spürbar, aber locker. Übergänge: harter Schnitt, Weiß- oder Schwarzbild von zwei bis drei Frames, Negativ-Sprung (dieselbe Pose schwarz auf weiß, dann weiß auf schwarz), Kachel-Glitch.
- **Ton:** −14,1 LUFS, Lautheitsspanne 1,9 LU, True Peak −1,9 dBFS.
- **Text:** Terminalzeilen klein kursiv in Mono oben links, beginnen mit einem Größer-Zeichen und tippen Buchstabe für Buchstabe; Ziffernwand aus fünf bis sechs Zeilen schmaler, sehr großer Grotesk, angeschnitten über die Bildbreite, mit Zahlen und Kennungen.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Punktwolke Kopf | 8 % | Kopf und Schultern im Profil, 80 % der Bildhöhe, Punkte verdichten sich zu Raster | 1 bis 3 Achtel |
| 1-Bit-Silhouette ganz | 15 % | Figur ganz, 90 % der Bildhöhe, mittig, schwarz auf Weiß oder invertiert, Bodenlinie | 1 bis 2 Achtel |
| Negativ-Gesicht | 10 % | Gesicht 70 % der Bildhöhe, frontal, invertiert grau | 2 bis 3 Achtel |
| Augen nah und Kachelraster | 15 % | Auge groß, oder 3 × 5 Kacheln aus Augenausschnitten | 1 bis 5 Achtel |
| Silhouetten in der Pupille | 5 % | Auge groß, darin ein bis drei weiße Figur-Silhouetten untereinander | 2 Achtel |
| Ziffernwand | 8 % | fünf bis sechs Zeilen über die ganze Breite, weiße Silhouetten dazwischen | 1 Achtel je Wand |
| Figur mit Echos | 8 % | Figur ganz im Studio, 85 % der Bildhöhe, drei bis fünf Nachbilder | 2 Achtel |
| Posen-Raster | 10 % | 3 × 4 kleine Figuren, je 15 % der Bildhöhe, normal oder invertiert | 1 bis 3 Achtel |
| Schrei oder Ausdruck nah | 8 % | Gesicht 90 % der Bildhöhe, Mund offen, normal und negativ | 2 Achtel |
| Streifenmaske | 5 % | Figur ganz vor waagerechten Balken oder Gesicht mit Streifen und Wellenkontur | 2 bis 3 Achtel |
| Akzent-Bild | 8 % | Kopf und Schultern im Profil oder Augen über hochgezogenem Kragen, Kleidungsstück farbig | 1 bis 2 Achtel |

## Dramaturgie
- **Hook (0 bis 0,8 s):** Schwarzbild mit zwei Streifen, Punktwolke formt einen Kopf, Terminalzeile tippt eine kurze Statusmeldung.
- **Gefunden (0,8 bis 2,6 s):** Negativ-Figur mit Statuszeilen, 1-Bit-Silhouette, Weißbild, kurzer Farbvorgriff am Kragen mit tippender Zeile, Negativ-Gesicht.
- **Augen (2,6 bis 5,4 s):** dunkles Porträt, Kachelraster aus Augen, Hautkacheln, Negativ-Auge, Auge mit Silhouette in der Pupille, Ziffernwände, Schwarz.
- **Posen (5,4 bis 8,2 s):** Silhouetten im Auge, Figur mit Echos, Profil, Posen-Raster normal und invertiert im Wechsel.
- **Ausbruch (8,2 bis 10,5 s):** Streifenmaske im Gesicht, Ziffernwand, Schrei normal und negativ, Silhouette invertiert.
- **Verdichtung (10,5 bis 13,2 s):** alle Bildtypen im Achtel, Figur vor Balken.
- **Auflösung (13,2 bis 13,6 s):** Profil mit farbigem Kleidungsstück.

## Schnittmuster
Bauplan für 15 s auf einem Achtel-Raster von 0,22 s (68 Achtel; bei 138 BPM sind das Sechzehntel). Inhalt austauschbar, Rhythmus bleibt.

| Slot | Achtel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0 | Schwarz mit zwei waagerechten Streifen, Cursor blinkt | hart | Piepen |
| 2 | 1-3 | Punktwolke formt Kopf, Terminalzeile tippt | hart | Daten-Rauschen |
| 3 | 4-5 | Negativ-Figur mit zwei Statuszeilen | hart | Beat setzt ein |
| 4 | 6-7 | 1-Bit-Silhouette, Weißbild, dieselbe Silhouette | Blitzbild | Hit |
| 5 | 8-9 | Augen über farbigem Kragen, Zeile tippt | hart | Akzent |
| 6 | 10-12 | Negativ-Gesicht | hart | Beat |
| 7 | 13-17 | dunkles Porträt, Kachelraster aus Augen, Hautkacheln | Glitch | Ticks |
| 8 | 18-22 | Auge mit Silhouette in der Pupille | hart | Swell |
| 9 | 23-25 | drei Ziffernwände je ein Achtel, Schwarz | hart | Hits |
| 10 | 26-28 | drei Silhouetten untereinander im Auge | hart | Beat |
| 11 | 29-32 | Figur mit Echos, zweimal näher | hart | Beat |
| 12 | 33-38 | Profil, dann Posen-Raster invertiert, normal, invertiert, normal | Stottern | Beat voll |
| 13 | 39-41 | Gesicht mit Streifen und Wellenkontur | hart | Bass |
| 14 | 42 | Ziffernwand | hart | Hit |
| 15 | 43-46 | Schrei normal, dann negativ | hart | Schrei-Sample oder Hit |
| 16 | 47-48 | 1-Bit-Silhouette invertiert, dann normal | Stottern | Beat |
| 17 | 49-61 | Verdichtung: alle Bildtypen je ein Achtel, Figur vor Balken | hart | Beat voll |
| 18 | 62-67 | Akzent-Bild: Profil mit farbigem Kleidungsstück, steht | hart | letzter Hit |

## Rezept für einen Code-Motor
- **Grund:** Schwarz `#070707` oder Weiß `#F7F7F7`; Studio-Aufnahmen auf weißer Hohlkehle.
- **Bildbehandlung:** Alles entsättigen außer einer Akzentmaske (Kleidungsstück freistellen, dort Originalfarbe lassen oder auf `#2E8155` tönen). Härtegrade als Filter-Satz: Graustufe weich; Negativ (`feColorMatrix` invertiert); 1-Bit (Schwelle 50 %, eine Variante invertiert); Punktwolke (Helligkeit in ein Punktraster mit 1 bis 1,5 % Zellgröße umrechnen, Punktgröße nach Helligkeit, in den ersten drei Bildern zufällig verstreut, dann ins Raster einrastend). Echo: vier Kopien desselben Clips mit 2, 4, 6, 8 Frames Verzögerung, je 25 % Deckung.
- **Bausteine:** Terminalzeile (oben links, 4 % vom Rand, Mono kursiv 1,6 % der Bildhöhe, beginnt mit „>“, zwei Frames je Buchstabe, Blockcursor blinkt im Achtel); Kachelraster (3 × 5 Kacheln aus nahen Ausschnitten, jede mit leicht anderer Helligkeit, eine bis zwei Kacheln um ±5 % versetzt); Ziffernwand (fünf bis sechs Zeilen, Zeilenhöhe 17 % der Bildhöhe, schmale Grotesk in `#C8C8C8` auf Schwarz, angeschnitten links und rechts, Inhalt: Ziffern mit Punkt und kurze Kennungen, je Achtel neu); Silhouetten im Auge (Figur-Freisteller weiß, 10 bis 12 % der Bildhöhe, ein bis drei untereinander); Posen-Raster (3 × 4 Freisteller-Posen, je 15 % der Bildhöhe); Streifenmaske (Balken 3 % hoch, Abstand 6 %, über die Figur; Wellenkontur: fünf Umrisslinien der Figur in 1 % Abstand, leicht verzerrt).
- **Typografie:** Ziffernwand in schmaler, schwerer Grotesk (frei lizenziert zum Beispiel Oswald 600 oder Antonio 700). Terminalzeile in Mono kursiv (zum Beispiel IBM Plex Mono Italic 400), klein geschrieben.
- **Bewegung:** Achtel-Raster der gemessenen Musik; Einstellungen ein bis drei Achtel, Halte bis fünf nur bei Augen und im Schlussbild. Negativ-Sprünge im Stottern. Leichte Pushs (3 %) in Gesichtern.
- **Formate:** Quelle 9:16. In 16:9 Figuren mittig mit Schwarz oder Weiß seitlich, Kachelraster 5 × 3 quer, Ziffernwand in drei Zeilen über die Breite; Terminalzeile bleibt oben links.
- **Neue Kennungen:** `neu:punktwolke`: Das Motiv besteht aus Punkten, die sich zu einem Raster ordnen. `neu:ziffernwand`: Bildfüllende Zeilen großer Ziffern und Kennungen. `neu:echo-spur`: Halbtransparente Nachbilder folgen der bewegten Figur.

## Material
- **Bilder (Figur):** `full body studio photo of [subject] standing still in a white cyclorama with a black ceiling curve, wearing one garment in [accent color], high contrast black and white lighting, sharp, editorial`
- **Bilder (Nah):** `extreme close-up of [subject]'s eye, black and white, hard light, visible skin texture, macro`
- **Musik:** `Dark minimal trap, 138 BPM double-time feel, sparse 808, sharp rimshots, digital glitch percussion, data-beep sounds, starts with a short computer beep, beat from zero point eight seconds, short drop-out at five point three seconds, dense section from ten point five seconds, final hit at thirteen point two seconds, instrumental, no vocals`
- **Geräusche:** Tipp-Klicken der Terminalzeile, Piepen bei „gefunden“, Datenrauschen bei Punktwolke und Ziffernwand; 10 bis 14 dB unter dem Beat.

## Regler
- Akzentfarbe: jede Farbe, die das eine Kleidungsstück oder Produkt wirklich hat.
- Anteil 1-Bit und Negativ: 30 bis 60 %.
- Terminalzeilen: drei bis sechs im Stück, je höchstens fünf Wörter.
- Für Produkte: statt der Person wird ein Produkt erfasst; Akzent ist dann das Produkt.
- Tempo: Achtel zwischen 0,18 und 0,25 s.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; Farbigkeit muss bis zum Schlussbild praktisch null sein.
- Standbild-Prüfung: außer dem Akzent kein Farbpixel; Terminalzeile lesbar; Ziffernwand angeschnitten, aber als Zahlen erkennbar.
- Streifen bei 12 fps: Negativ-Sprünge sitzen auf Achteln; Schlussbild steht mindestens 0,4 s.

## Fallen
- Negativ und 1-Bit im Einzelbild-Wechsel über Sekunden sind eine Epilepsie-Gefahr → höchstens drei harte Hell-Dunkel-Wechsel je Sekunde, Verdichtung kürzer als 2,5 s.
- Akzent zu oft zeigen → die Auflösung verpufft; höchstens einmal vorher kurz.
- Punktwolke mit zu feinen Punkten → wirkt wie Rauschen; Zelle mindestens 1 % der Bildhöhe.
- Ziffernwand mit echten Koordinaten oder Personendaten → nur erfundene, neutrale Zahlen.
- Marken-Schriftzüge auf Kleidung → neutral halten oder eigene.
- Figur ohne farbiges Kleidungsstück (weißes Hemd) → den Akzent auf ein anderes echtes Farbmerkmal legen (Augenfarbe), Farbmaske nur auf Pixel mit dominanter Akzentfarbe, sonst färbt der weiche Rand die Haut.
- Mit Erzählstimme halbiert sich die Schnittdichte (erstes Werk 2,7 statt 3,7 bis 5,5 Schnitte je Sekunde bei Median 0,23 s): Erklärbilder brauchen zwei bis vier Achtel. Ausgleich über Ruckzooms und Wechsel Graustufe ↔ Negativ im selben Bild; Ruckzooms unter 10 % zählt die Schnitterkennung nicht.
- Terminalzeile per Differenzmodus ist auf Kachelraster und Ziffernwand unleserlich → schwarzer Kasten dahinter; oberste 200 px freilassen (Plattform-Leiste).
- Weißblitz länger als zwei Bilder wirkt wie ein Fehler; Negativ-Raster direkt vor Schwarzbild und Schlussbild ergibt vier harte Sprünge in einer Sekunde → Mittelhelligkeit je Bild messen (Sprung größer 0,2, höchstens drei je Sekunde).
- Musikmodell hält das Tempo, aber nicht die Zeitmarken im Prompt → Drop und Schlusstreffer im Schnitt setzen (Take verschieben, Intro in ganzen Takten schleifen, Treffer nach 0,12 s nur noch Bass).
- Zahlenreihen, die über den Rand laufen, zeigen im Ruckzoom halbe Werte und ein einzelnes Minus wie einen Gedankenstrich → feste Zahl ganzer Werte plus „…“, 60 px Rand, Zoom so begrenzen, dass Bild und Werte drin bleiben; zwei Reihen nie deckungsgleich übereinander, sondern halb deckend und eine halbe Zeile versetzt.
- Blinzeln aus einer anderen Pose übernimmt deren Brauen (doppelte Brauen) → Lider gezeichnet nur in der Augenöffnung, halb, zu, zu, halb.
