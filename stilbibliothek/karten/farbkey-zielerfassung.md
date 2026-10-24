---
id: farbkey-zielerfassung
name: Farbkey mit Zielerfassung
familie: auto-beat
kurz: Schwarzweiß-Bilder eines Fahrzeugs, nur sein Lack leuchtet in einer Farbe, dünne Messlinien und ein Zielrahmen erfassen es wie ein Scanner, schräge Kamera und dreifach gestapelte Makros auf einem harten Beat.
kern: [Schwarzweiß mit genau einer Farbe auf dem Lack, dünnes Mess-HUD mit Linien und Zielrahmen, schräge Kamera und gestapelte Dreifach-Makros]
energie: 4
format_quelle: "9:16"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.63
  schnitte_pro_s: 2.4
  schnitte_verlauf: [2.2, 2.0, 3.0]
  bpm: 140
  schnitt_auf_beat: mittel
  lufs: -14.2
  helligkeit: 0.27
  kontrast: 0.24
  farbigkeit: 0.06
schnittmuster_16tel: [2, 8, 1, 4, 5, 7, 5, 7, 6, 11, 10, 10, 10, 1, 6, 1, 10, 6, 6, 1, 8, 7, 1, 3, 1, 5, 7, 6, 12]
palette:
  grund: "#080708"
  asphalt: "#443C41"
  himmel: "#C9C9C9"
  lack: "#A46790"
  lack_licht: "#D9A6CB"
  titel: "#FDABD1"
  hud: "#E6E6E6"
effekte: [harter-schnitt, blitzbild, wiederholung, orbit, schwenk, ein-akzent, schwarzweiss, filmkorn, glow, hud, mono-zeile, titelkarte, partikel, beat-getrieben, drop, schraeglage]
kamera: Schnell und schräg; Orbits um Details, tiefe Weitwinkel-Fahrten knapp über dem Boden, das Bild kippt 15 bis 30 Grad.
ton: Harter, stark verdichteter Beat um 140 BPM (Halbtempo 70), leises Intro bis 3,5 s, dann Drop und durchgehend gleich laut, Ausblende am Ende.
braucht: [produkt, footage-ort, nur-typo]
motor_aufwand: mittel
einsatz: [hook, trailer, produkt, ganzes-kurzvideo]
abnahme:
  shot_median_s: [0.50, 0.76]
  schnitte_pro_s: [1.9, 2.9]
  helligkeit: [0.22, 0.33]
  farbigkeit: [0.04, 0.08]
  lufs: [-15.2, -13.2]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Farbkey mit Zielerfassung

Wie ein technisches Dossier über ein einziges Fahrzeug: Die Welt ist schwarzweiß, nur der Lack hat Farbe, und ein feines Mess-HUD tastet ihn ab. Die Energie kommt aus der schrägen, schnellen Kamera und aus den Dreifach-Stapeln, die ein Detail wie einen Datensatz wiederholen.

## Kern
- **Schwarzweiß mit einer Lackfarbe:** Himmel, Asphalt, Reifen, Chrom sind grau; nur der Lack bleibt farbig (hier ein kühles Rosa). Gemessene Farbigkeit nur 0,06, obwohl die Farbe das Thema ist. Eine zweite Farbe zerstört den Key.
- **Feines Mess-HUD:** Haarlinien von einem Etikett zu einem kleinen Quadrat, Koordinaten, die mitzählen, ein Zielrahmen mit Eckwinkeln. Alles dünn und klein, nie ein dickes Interface.
- **Schräge Kamera und Dreifach-Stapel:** Das Bild kippt, die Kamera fliegt knapp über den Boden; Makros erscheinen dreimal übereinander. Gerade, ruhige Bilder machen daraus einen Autohaus-Clip.

## Erkennung
- **Bild:** Zwei Welten. Studio: schwarzer Grund (#080708), Makros von Leuchte, Grill, Radkasten, Rad; der Lack mit weichem weißem Glanzreflex. Außen: weite Betonfläche unter bewölktem Himmel, starker Kontrast, Himmel hellgrau (#C9C9C9), Asphalt dunkel (#443C41). Lack im Schatten #A46790, im Licht #D9A6CB. Gemessen: Helligkeit 0,27, Kontrast 0,24, 43 % der Fläche fast schwarz. Sichtbares Filmkorn, Scheinwerfer blühen weich auf.
- **Schnitt:** Median-Shot 0,63 s, längster 1,2 s, alle Shots unter 1,3 s. Schnittdichte 2,2, 2,0, 3,0 je Sekunde, also Steigerung zum Schluss. 14 der 43 Schnitte sind Ein-Bild-Blitze: ein Scheinwerfer überbelichtet zu Weiß. Raster: Sechzehntel bei 140 BPM (0,11 s), typische Längen 5 bis 7 und 10 Sechzehntel. Übergänge hart, keine Blenden außer am Schluss.
- **Ton:** Erste 3,5 s leise (−15 dB), dann Drop und ab da gleichbleibend −10 dB bis 16,5 s, danach Ausblende. Lautheitsspanne nur 0,8 LU, also stark verdichtet. Keine Stimme. Genre aus den Daten nicht sicher; vermutlich ein dunkler Trap- oder Phonk-Beat.
- **Text:** Vier Rollen, alle in Monospace, klein, weiß oder lackfarben: Callout-Etikett mit Haarlinie zu einem Quadrat; Koordinaten, die je zwei Bilder umspringen; Zielrahmen mit Name oben und Entfernung unten, die Entfernung ändert sich zwischen den Auftritten; Scan-Zähler oben links mit Diagonallinien durchs Bild. Am Ende eine Titelkarte: schmale fette Grotesk in hellem Rosa, darunter eine Monospace-Zeile, graue Bokeh-Kreise.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Studio-Makro mit Callout | 30 % | Detail füllt 100 bis 130 % der Bildhöhe, angeschnitten, Lack unten, Schwarz oben; Callout-Quadrat 5 % der Breite im Bildzentrum | 5 bis 8 Sechzehntel |
| Dreifach-Stapel | 15 % | dasselbe Makro in drei waagrechten Streifen je ein Drittel der Höhe, ohne Steg | 6 bis 10 Sechzehntel |
| Front frontal mit Zielrahmen | 20 % | Froschperspektive, Fahrzeug füllt 95 % der Breite, Front bei 45 bis 65 % der Höhe, Himmel oben; Rahmen 45 % der Breite über dem unteren Frontteil | 6 bis 10 Sechzehntel |
| Schräge Fahrt | 25 % | Bild 15 bis 30 Grad gekippt, Weitwinkel knapp über dem Boden, Fahrzeug 40 bis 80 % der Höhe, Boden verwischt | 6 bis 11 Sechzehntel |
| Überbelichtungs-Blitz | 5 % | Scheinwerfer groß, zu Weiß ausgebrannt | 1 Sechzehntel |
| Titelkarte | 5 % | Titel bei 74 % der Höhe, 5 % der Bildhöhe, darunter Monospace-Zeile; Bokeh-Kreise | 12 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1,3 s):** Schwarz, Rad-Makro im Dunkel, ein Blitz: der Scheinwerfer brennt aus.
- **Dossier (1,3 bis 3,5 s):** Studio-Makros mit Callouts, ein Dreifach-Stapel. Musik noch leise.
- **Drop (3,5 s):** Raus ins Freie, schräge Fahrt über die Betonfläche, Himmel dramatisch.
- **Erfassung (6 bis 13 s):** Zielrahmen auf der Front, schräge Vorbeifahrten, Scan-Linien, zwei Dreifach-Stapel der Leuchte (erst ausgebrannt, dann klar), Zielrahmen wieder mit neuer Entfernung.
- **Rückkehr (14,4 bis 16,8 s):** Blitz, Front mit Licht, dann dieselben Studio-Makros wie am Anfang, schnellste Passage.
- **Schluss (16,9 bis 18 s):** Titelkarte mit Bokeh, Musik blendet aus.

## Schnittmuster
Bauplan für 16 s bei 140 BPM (149 Sechzehntel). Ein Sechzehntel ist 0,107 s, also gut drei Bilder bei 30 fps.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-3 | Schwarz | hart | leises Intro, Tick |
| 2 | 4-11 | Rad-Makro im Dunkel, langsamer Orbit | hart | Pad |
| 3 | 12, 13-16 | Blitz Scheinwerfer, dann Leuchte klar | Blitzbild | Zisch |
| 4 | 17-21 | Grill-Makro, Callout zeichnet sich, Koordinaten zählen | hart | Daten-Tick |
| 5 | 22-28 | Heckleuchte mit Callout | hart | Tick |
| 6 | 29-31 | Dreifach-Stapel Karosseriekante | hart | Riser |
| 7 | 32-39 | Drop: schräge Fahrt knapp über dem Boden | hart | Drop, voller Beat |
| 8 | 40-45 | Front frontal, Zielrahmen rastet ein | hart | Piep |
| 9 | 46-55 | schräge Vorbeifahrt, 25 Grad gekippt | hart | Whoosh |
| 10 | 56-65 | Radkasten in Bodennähe, Boden verwischt | hart | Beat |
| 11 | 66, 67-76 | Blitz, dann Front mit Scan-Linien und zwei Etiketten | Blitzbild | Hit |
| 12 | 77-82, 83-88 | Dreifach-Stapel Leuchte ausgebrannt, dann klar | hart | Beat |
| 13 | 89-96 | Zielrahmen zweite Runde, Entfernung kleiner | hart | Piep |
| 14 | 97-103 | Unterfahrt, fast schwarz, Lack blitzt am Rand | hart | Bass |
| 15 | 104, 105-112 | Blitz, Front mit Licht an | Blitzbild | Hit |
| 16 | 113-118 | Grill mit Callout wie Slot 4 | hart | Tick |
| 17 | 119-126 | Heck mit Callout wie Slot 5 | hart | Tick |
| 18 | 127-132 | Dreifach-Stapel Kante wie Slot 6 | hart | Beat |
| 19 | 133-148 | Titelkarte mit Bokeh | hart | Musik blendet ab 141 aus |

## Rezept für einen Code-Motor
- **Grund:** Studio-Bilder auf #080708; Titelkarte mit radialem Verlauf von #1A1A1A in der Mitte zu #050505 am Rand.
- **Bildbehandlung:** Farbkey je Pixel: Farbton im Lackbereich (für Rosa 300 bis 345 Grad) und Sättigung über 0,2 behalten, mit 15 Grad weicher Kante; alles andere auf Luminanz setzen. Danach S-Kurve, Schwarzpunkt bei 6 %, Himmel bis 85 % hell. Filmkorn als Rauschen mit festem Seed je Bild, Deckung 6 %. Scheinwerfer-Blühen: Lichter über 90 % herauslösen, 16 px weichzeichnen, `screen` bei 50 %. Key einmal je Clip vorrechnen.
- **Bausteine:** Callout (Etikett in Monospace, Haarlinie 1 px bei 1080 px Breite, Quadrat 5 % der Bildbreite; Linie zeichnet sich in 3 Bildern, Koordinaten springen alle 2 Bilder um ein bis fünf Einheiten); Zielrahmen (Rechteck 45 % der Breite und 14 % der Höhe, Linie 1,5 px in #D9A6CB, weiße Eckwinkel 3 % lang, rastet in 4 Bildern von 110 % auf 100 % Größe ein; Name darüber links, Entfernung darunter links); Scan-Linien (zwei Haarlinien quer durchs Bild von Etiketten aus, Zähler oben links); Dreifach-Stapel (drei Streifen je ein Drittel der Höhe, gleicher Clip, gleicher Ausschnitt); Überbelichtungs-Blitz (Belichtung ×3 plus Blühen, genau ein Sechzehntel); Bokeh (12 graue Kreise, 2 bis 5 % der Bildbreite, 10 bis 25 % Deckung, 2 px weich, steigen langsam).
- **Typografie:** HUD in Monospace, Versalien, 1,6 % der Bildhöhe (die Vorlage nutzt 1,1 %, auf dem Handy zu klein), Weiß mit 85 % Deckung, Zielrahmen-Text im Lackton (zum Beispiel JetBrains Mono 400 oder IBM Plex Mono). Titel in schmaler fetter Grotesk, Versalien, #FDABD1, 5 % der Bildhöhe (zum Beispiel Antonio 700 oder Oswald 600), Unterzeile Monospace 1,3 %, 10 % gesperrt.
- **Bewegung:** Schnitte auf dem Sechzehntel-Raster, meist 5 bis 10 Sechzehntel lang. Schräglage per Drehung 15 bis 30 Grad und Skalierung 1,3, damit keine Ecken frei werden; bei Fahrten Drehung über den Shot um 3 bis 5 Grad weiterlaufen lassen. Orbits in Studio-Makros langsam (10 Grad je Sekunde). HUD steht fest im Bild, nur Zahlen und Linien bewegen sich.
- **Formate:** In 9:16 wie beschrieben. In 16:9 wird der Dreifach-Stapel zu drei Spalten nebeneinander; Fronten füllen 60 % der Breite, Zielrahmen mittig über der Front; Schräglage bleibt; Titel mittig bei 60 % der Höhe; HUD-Etiketten in die äußeren Drittel.

## Material
- **Bilder (Studio):** `macro studio shot of the headlight and grille of a [subject] in glossy pastel paint, pure black background, single soft top light, sharp white reflection on the paint, high contrast, fine film grain, vertical frame`
- **Bilder (Außen):** `low wide-angle shot of a [subject] driving across an empty concrete apron under a dramatic overcast sky, camera tilted 25 degrees near the ground, motion blur on the ground, high contrast black and white except the paint`
- **Musik:** `Dark minimal trap beat, 140 BPM with half-time feel, deep 808 bass, sharp hi-hat rolls, cold synth pad, 0-3.4 s filtered intro with ticking clock, 3.4 s drop into full beat, constant level, 16 s fade out over 1.5 s, instrumental, no vocals`
- **Geräusche:** Piep beim Einrasten des Zielrahmens, Daten-Tick bei jedem Callout, Whoosh bei schrägen Vorbeifahrten, Zischen beim Blitz; 10 bis 14 dB unter dem Beat.

## Regler
- Lackfarbe: jede Farbe, die in der Umgebung nicht vorkommt (Rosa, Mint, Signalorange, Kobalt).
- HUD-Dichte: von einem Callout je Bild bis zu Zielrahmen plus Scan-Linien; nie mehr als drei HUD-Elemente gleichzeitig.
- Schräglage: 10 bis 30 Grad; ohne Schräglage wird es sachlich und ruhiger.
- Studio-Anteil: 30 bis 60 %; die Rückkehr ins Studio am Ende hält das Stück zusammen.
- Statt Fahrzeug funktioniert jedes Objekt mit klarer Farbe (Sneaker, Gerät, Flasche).

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; Farbigkeit unter 0,08 beweist, dass der Key sauber ist.
- Standbild an drei Stellen: außer dem Lack kein farbiges Pixel (auch keine Hauttöne, Schilder, Himmelsblau), HUD lesbar, aber nie dicker als 2 px.
- Streifen bei 12 fps: Blitze genau ein Sechzehntel, Zielrahmen-Zahlen ändern sich zwischen den Auftritten, Drop fällt mit dem ersten Außenbild zusammen.

## Fallen
- Farbkey frisst Teile des Lacks in Schatten und Reflexen → Sättigungsschwelle senken, weiche Kante breiter, Maske leicht weichzeichnen.
- Hauttöne oder rote Leuchten liegen nahe am Lackton → Farbbereich enger fassen oder diese Flächen getrennt entsättigen.
- HUD wird zum Spiel-Interface → nur Haarlinien, kleine Schrift, keine Flächen, keine Leuchtfarben außer dem Lackton.
- Schräglage mit freien Ecken → immer mitskalieren.
- Gestapelte Makros mit unterschiedlichem Ausschnitt wirken zufällig → identischer Ausschnitt in allen drei Streifen.
- Monospace-Texte aus echten Daten (Koordinaten, Hexwerte) dürfen nicht nach Marke klingen → eigene neutrale Etiketten schreiben.
