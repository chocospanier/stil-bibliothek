---
id: weitwinkel-umkreisung
name: Weitwinkel-Umkreisung
familie: 3d-objekt
kurz: Eine einzige Kamerafahrt im Weitwinkel dicht an einem langen, verchromten, mit Aufklebern beklebten Objekt entlang, umkreist sie zwischen strahlenförmig abstehenden Kabeln und zieht am Ende weit nach unten heraus.
kern: [eine durchgehende Einstellung ohne Schnitt, Weitwinkel ganz nah am Objekt mit Orbit und Steigen, Chrom und bunte Aufkleber vor Schwarz mit roten und blauen Kantenlichtern]
energie: 3
format_quelle: "3:4"
laenge_s: [4, 8]
messung:
  shot_median_s: 5.6
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm:
  schnitt_auf_beat:
  lufs:
  helligkeit: 0.20
  kontrast: 0.30
  farbigkeit: 0.17
schnittmuster_16tel: []
palette:
  grund: "#080403"
  schatten_warm: "#663D3A"
  chrom_licht: "#EFE9E4"
  chrom_warm: "#C1957C"
  kante_rot: "#D4553A"
  kante_blau: "#5C74C5"
  funke: "#EA8A4F"
effekte: [orbit, fpv, pull-out, kamera-steht, 3d-render, glow, bewegungsunschaerfe, geringe-schaerfentiefe, chroma-versatz, klebeband-sticker, fischauge]
kamera: Ein durchgehender Orbit von etwa 270° um die Säule, dabei langsames Steigen entlang der Längsachse, Weitwinkel mit leichter Tonnenverzeichnung, in der letzten Sekunde ein schneller Zug nach unten heraus, bis die ganze Struktur klein und senkrecht im Bild steht.
ton: "Vorlage ohne Tonspur; Musik frei wählbar, siehe Abschnitt Material."
braucht: [3d, produkt]
motor_aufwand: mittel
einsatz: [uebergang, intro, produkt, hook]
abnahme:
  shot_median_s: [4.5, 7.0]
  schnitte_pro_s: [0.0, 0.1]
  helligkeit: [0.16, 0.24]
  farbigkeit: [0.14, 0.21]
  lufs: []
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Weitwinkel-Umkreisung

Eine Kamera, die sich um ein glänzendes Objekt windet wie eine Fliege um eine Lampe: ganz nah, im Weitwinkel, zwischen abstehenden Kabeln hindurch, bis sie am Ende herauszieht und zeigt, wie groß das Ding ist. Die Wirkung kommt allein aus der Kamerabewegung und dem Glanz; es gibt keinen Schnitt. Im Rezept steht als Beispiel eine Säule; jedes lange, glänzende Objekt trägt den Stil.

## Kern
- **Eine Einstellung:** 5,6 s am Stück, kein Schnitt. Alles, was passiert, ist Kamera.
- **Weitwinkel ganz nah:** Das Objekt füllt 60 bis 100 % der Bildhöhe, läuft diagonal durchs Bild und verjüngt sich stark zur Spitze (starke Perspektive). Kabel im Vordergrund wischen unscharf vorbei.
- **Chrom, Sticker, farbige Kanten:** Spiegelnder Chrom mit dicht geklebten, bunten Aufklebern und Kabelbindern, vor fast schwarzem Grund; Kantenlicht rot von einer, blau von der anderen Seite, warme Lichtpunkte als Funken.

## Erkennung
- **Bild:** Grund `#080403`, warme Schatten `#663D3A`, Chromlicht `#EFE9E4` und `#C1957C`, Kantenlicht Rot `#D4553A` und Blau `#5C74C5`, Funken `#EA8A4F`. Aufkleber in vielen bunten Farben, aber klein. Leichte chromatische Aberration an Kabelkanten, Bewegungsunschärfe auf Vordergrundkabeln, geringe Schärfentiefe. Gemessen: Helligkeit 0,20, Kontrast 0,30, Farbigkeit 0,17, 63 % fast schwarz.
- **Schnitt:** keiner. Bewegung gemessen als Zug heraus, Seitwärts und Orbit, Tempo mittel.
- **Ton:** Die Vorschau hat keine Tonspur.
- **Text:** keiner außer dem, was auf den Aufklebern steht (nur Textur).

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Objekt nah, diagonal | 55 % | Säule von unten links nach oben rechts oder umgekehrt, 80 bis 100 % der Bildhöhe, Aufkleber lesbar groß, Kabel strahlen ab | 0 bis 3 s |
| Objekt von unten, Spitze oben | 30 % | Säule senkrecht mittig, verjüngt sich zur Spitze, Licht an der Spitze, Kabel sternförmig, Spirale aus Draht links | 3 bis 4,6 s |
| Rückzug, ganze Struktur | 15 % | Säule dünn und senkrecht mittig, 100 % der Bildhöhe, Kabelnetz um sie herum, viel Schwarz | 4,6 bis 5,6 s |

## Dramaturgie
- **Hook (0 bis 0,5 s):** sofort mitten in der Bewegung, ganz nah am Chrom, ein Funke blitzt.
- **Umkreisen (0,5 bis 3 s):** die Kamera dreht um die Säule, Aufkleber ziehen vorbei, das Licht wechselt von rot zu blau.
- **Steigen (3 bis 4,6 s):** Blick wandert nach oben, die Säule richtet sich auf, die Spitze leuchtet, Kabel spreizen sich.
- **Rückzug (4,6 bis 5,6 s):** schneller Zug nach unten heraus, die Struktur wird dünn und groß, Ende auf fast schwarzem Bild.

## Schnittmuster
Kein Schnitt; der Bauplan ist eine Kamerakurve für 6 s. Wird Musik untergelegt, die Lichtwechsel und den Rückzug auf Taktanfänge legen.

| Slot | Sekunden | Kamera | Übergang | Ton (Vorschlag) |
|---|---|---|---|---|
| 1 | 0,0-0,5 | Start im Orbit, Abstand 0,6 Säulendurchmesser, Säule diagonal | keiner | Whoosh-Anfang |
| 2 | 0,5-1,5 | Orbit 90°, Kantenlicht rot | keiner | Beat setzt ein |
| 3 | 1,5-2,5 | Orbit weitere 90°, Kantenlicht wechselt zu blau, Kabel wischen im Vordergrund | keiner | Beat |
| 4 | 2,5-3,0 | Orbit 45°, Kamera kippt nach oben | keiner | Riser |
| 5 | 3,0-4,6 | Steigen entlang der Säule, Spitze leuchtet | keiner | Riser |
| 6 | 4,6-5,6 | schneller Zug nach unten heraus, Abstand ×8 | keiner | Hit auf 4,6 |
| 7 | 5,6-6,0 | Halt auf ganzer Struktur, Licht dimmt | keiner | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Schwarz `#080403` mit sehr schwachem warmem Verlauf von unten.
- **Bildbehandlung:** Three.js oder Blender. Säule als langer Zylinder, der sich nach oben verjüngt, Material Metall 1,0, Rauheit 0,15, Umgebungskarte dunkel mit zwei farbigen Flächenlichtern (Rot `#D4553A` links, Blau `#5C74C5` rechts) und einem warmen Spot oben. Aufkleber als Decals (20 bis 40 Stück, eigene Grafiken, mit leicht glänzender Folie). Kabelbinder als schmale schwarze Ringe. Kabel: 30 bis 60 Röhren, Radius 0,5 % der Säulenlänge, strahlen aus der Säule und biegen sich, Material Chrom und schwarzes Gummi gemischt. Kamera: Brennweite 14 bis 18 mm (Kleinbild), leichte Tonnenverzeichnung als Nachbearbeitung (Stärke 0,15). Nachbearbeitung: Bloom auf Lichtpunkten (Schwelle 0,85, Stärke 0,8), chromatische Aberration 0,3 %, Bewegungsunschärfe (Verschlusswinkel 180°), Schärfentiefe mit Fokus auf der Säulenoberfläche, Korn 3 %.
- **Bausteine:** Kamerakurve (Orbit um die Säulenachse, Winkel über die Zeit mit Ease-in-out von 0 auf 270°, Höhe steigt linear um 40 % der Säulenlänge, Abstand konstant 0,6 Durchmesser bis 4,6 s, danach in 30 Frames auf 8 Durchmesser mit Ease-in, gleichzeitig Blick nach oben); Funken (fünf bis zehn warme Lichtpunkte auf Kanten, blinken kurz).
- **Typografie:** keine. Wird ein Titel gebraucht, erst im letzten Halt, klein unten mittig, schlichte Grotesk (frei lizenziert zum Beispiel Inter 600), 3 % der Bildhöhe.
- **Bewegung:** siehe Kamerakurve; keine Schnitte, kein Ruckeln, Geschwindigkeit fließt.
- **Formate:** Quelle 3:4. In 9:16 passt die senkrechte Säule ideal, Orbit bleibt gleich, Zug heraus endet mit Säule über 100 % der Bildhöhe. In 16:9 Säule diagonal legen und Orbit weiter weg beginnen (0,9 Durchmesser), damit links und rechts Kabel das Bild füllen.
- **Neue Kennungen:** `neu:weitwinkel-nah`: Die Kamera ist im Weitwinkel ganz nah am Objekt, die Perspektive stark übertrieben.

## Material
- **Bilder (Objekt):** `extreme close-up wide angle 3D render of a tall chrome pole covered in colorful vinyl stickers and black cable ties, many chrome and rubber cables radiating outward, red rim light on one side and blue rim light on the other, warm sparks, pitch black background, shallow depth of field, cinematic`
- **Bilder (Variante Produkt):** `extreme close-up wide angle 3D render of [subject] with a polished chrome surface and custom stickers, cables radiating outward, red and blue rim light, black background`
- **Musik:** `Short punchy electronic sting, 120 BPM, whoosh intro, tight kick from zero point five seconds, rising synth from three seconds, big hit at four point six seconds, reverb tail to six seconds, instrumental, no vocals`
- **Geräusche:** Luftzug beim Orbit, metallisches Klirren, wenn Kabel nah vorbeiwischen, tiefer Whoosh beim Zug heraus; 8 bis 12 dB unter der Musik.

## Regler
- Objekt: Säule, Flasche, Fahrzeug, Skulptur, alles Lange mit Glanz.
- Orbit-Winkel: 180 bis 360°.
- Länge: 4 bis 8 s; länger wird es zur Produktdemo.
- Kantenlichter: zwei Farben; eine Farbe wirkt edler, ruhiger.
- Als Übergang: Zug heraus endet auf Schwarz, dort setzt das nächste Bild an.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; kein erkannter Schnitt.
- Standbild-Prüfung: Säule an jeder Stelle mindestens 60 % der Bildhöhe bis zum Rückzug; Kanten zeigen Rot und Blau; Aufkleber sind eigene Grafiken.
- Streifen bei 12 fps: Orbit ohne Ruckler, Geschwindigkeit steigt und fällt weich; der Zug heraus sitzt auf dem Hit.

## Fallen
- Fremde Logos oder Markennamen auf den Aufklebern → nur eigene oder generische Grafiken.
- Zu starke Verzeichnung → Objekt wird zur Wurst; Tonnenverzeichnung höchstens 0,2.
- Ohne Vordergrundkabel fehlt das Tiefengefühl → mindestens drei Kabel, die nah an der Kamera vorbeiwischen.
- Gleichmäßige Kamerageschwindigkeit wirkt wie eine Drehbühne → Ease-in-out und ein schneller Rückzug am Ende.
- Generiertes Video mit Formdrift (Aufkleber verändern sich) → besser in 3D rendern, dort bleibt jedes Detail stabil.
- Im Makro (Kamera 4 bis 8 cm vor der Oberfläche) ist Blende 2,2 so flach, dass kein Aufkleber scharf wird → Blende um 4,5 und Schärfe per Sehstrahl auf die Oberfläche legen, nicht auf die Achse (erlebt beim Bau, 16.10.2026).
- Zu viele steil abstehende Kabel machen aus dem Objekt einen Igel → rund 28 Kabel, eher waagerecht abstrahlend; jedes Kabel gegen die Kamerabahn messen (nie unter 1,4 cm, nur vier bis sechs Wischer zwischen 1,4 und 3,2 cm).
- Wartet die GPU (Warteschlange der Bildmaschine, hängender Videolauf), rechnet Blender Cycles auf der CPU gut genug: 723 × 1286, 20 Proben adaptiv plus OIDN, 7 bis 14 s je Bild; eine fast stehende Schlusskamera als Standbild plus 2D-Heranfahren bauen.
- Kameralicht und ein starkes rotes Kantenlicht waschen bunte Aufkleber blassrosa aus und heben die Helligkeit weit über 0,24 → beides schwach halten, das Schwarz muss überwiegen.
- Große Flächenlichter nah am Chrom spiegeln sich breit und heben die Helligkeit, statt sie zu senken; der Chrom muss überwiegend Schwarz spiegeln, Farbe nur als schmale Kante. Aufkleber klein halten (bei einem 8-cm-Objekt 2 bis 3 cm), sonst wird das Bild pastellig hell.
- Beim Steigen zur Spitze nicht über die Ebene der abstehenden Kabel gehen: sonst ist oben nur Schwarz, und eine Drehung um eine rotationssymmetrische Spitze sieht aus wie Stillstand. Nach dem Kippen noch heranfahren.
- Der Zug heraus muss nicht im Schwarz enden: Wer eine Figur als Bildtafel hinter das Objekt in denselben 3D-Raum stellt (Finger als zweite Tafel davor, beide aus der Schlusskamera deckungsgleich), bekommt Enthüllung und Pointe in derselben Einstellung.
