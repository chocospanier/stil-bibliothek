---
id: angebots-ticker
name: Angebots-Ticker
familie: produktspot
kurz: Ein Handels-Spot in Markenfarben, der im Takt nach vorn drückt; große Wörter steigen aus Masken, ein schräges Band in Akzentfarbe wischt von Szene zu Szene, das echte Produktfoto fährt ein und landet, ein Preisschild knallt auf den Schlag, die Dringlichkeit läuft als Band durch, Schlusskarte mit Logo, Handlungsaufforderung und Webadresse.
kern: [große schmale Versalwörter im Takt aus Masken auf wechselnden Flächen aus Grund und Akzent, echtes freigestelltes Produktfoto mit Licht und Bodenschatten das einfährt und landet, Preisschild oder Dringlichkeitsband als Treffer und eine Schlusskarte mit Logo und Handlungsaufforderung]
energie: 4
format_quelle: "9:16"
laenge_s: [15, 25]
messung:
  shot_median_s: 17.0
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm: 120
  schnitt_auf_beat: hoch
  lufs: null
  helligkeit: 0.195
  kontrast: 0.248
  farbigkeit: 0.42
schnittmuster_16tel: [16, 12, 12, 8, 32, 16, 28]
palette:
  grund: "#111111"
  text: "#FFFFFF"
  akzent: "#E3120B"
  licht: "#4A4A4A"
effekte: [harter-schnitt, wischer, wort-auf-beat, masken-wechsel, freisteller, push-in, titelkarte, beat-getrieben]
kamera: Steht; jede Szene fährt langsam heran (2 bis 4 %), beim Aufschlag von Produkt und Preisschild ein kurzes Rütteln von 8 Bildern.
ton: Treibender Handels-Beat um 120 BPM mit klaren Schlägen; Schnitte, Landung und Preisschild sitzen auf Schlägen. Mit Stimme folgen die Szenen den Wortzeiten.
braucht: [produkt, nur-typo]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo, hook]
zweck: [produktwerbung, angebot]
branchen_passt: [werkstatt-auto, handwerk, technik, sport, gastro]
branchen_nie: [finanzen, gesundheit, kinder-familie]
abnahme:
  shot_median_s: [12.0, 25.0]
  schnitte_pro_s: [0.0, 0.2]
  helligkeit: [0.14, 0.26]
  farbigkeit: [0.3, 0.52]
  lufs: [-15, -13]
# Würfel-Felder: Markenfarben über Rollen (der Motor leitet Fläche, gedeckt und Licht selbst ab), Schrift in der Klasse
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 2]
  stottern_wiederholungen: [1, 1]
  push_in_prozent: [2, 4]
  wackeln_faktor: [0.6, 1.2]
  korn: [0, 0]
  vignette: [0, 0]
  beat_versatz_16tel: [0, 0]
  textgroesse_prozent: [-8, 8]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: grund
  hell: text
  licht: licht
quelle: Eigener Entwurf (Strang P2, 05.11.2026) nach dem Handwerk von Handels- und Angebotsspots; keine Vorlage, keine Motive, Texte oder Marken übernommen.
---

# Angebots-Ticker

Ein Spot, den ein Laden ohne Agentur posten kann und der trotzdem nach Agentur aussieht: echte Produktfotos, Markenfarben, wenige große Wörter, alles auf dem Schlag. Die Energie kommt aus dem Wechsel der Flächen (Grund, Akzent, Grund), aus Wörtern, die von unten aus einer Maske steigen, und aus zwei Aufschlägen: das Produkt landet, das Preisschild knallt.

## Kern
- **Wörter im Takt:** schmale, fette Versalien (Barlow Condensed 800, im Würfel jede schmale Schrift) füllen 85 % der Breite, höchstens drei Zeilen, steigen Zeile für Zeile aus einer Maske (9 Bilder, 3 Bilder versetzt). Jede Schlagzeile hat eine eigene Fläche: gerade Zeilen auf der Akzentfläche, ungerade auf dem Grund.
- **Das echte Produkt:** ein freigestelltes Foto aus den Props, nie gefiltert, nie verzerrt. Licht dahinter (Grund mit 24 % Text gemischt), weicher Bodenschatten darunter. Es fährt mit Schwung ein (Spur aus drei blassen Kopien, keine Unschärfe) und landet auf dem Schlag; in den Schlagzeilen steht es klein als Konstante.
- **Treffer und Schluss:** Preisschild in Akzentfläche mit Loch und Spitze knallt auf den Schlag (Maßstab 1,45 auf 1, eine Kontur als Druckwelle, kein Blitz), dann die Dringlichkeit auf einem schrägen Band mit Laufband darunter, dann Logo, Produkt, Handlungsaufforderung (Fläche mit einem Glanz) und Webadresse.

## Erkennung
- **Bild:** drei Rollen: Grund (Werkstatt `#111111`), Text (`#FFFFFF`), Akzent (`#E3120B`). Ableitungen nur aus diesen: Akzentfläche (Helligkeitsstufe des Akzents, bis die bessere Schriftfarbe 4,6 hält), gedeckte Fläche (Grund mit 11 % Text), Licht (Grund mit 24 % Text), Schatten. Keine Texturen, kein Korn, keine Vignette, keine Zeichnungen von Gegenständen.
- **Schnitt:** 7 bis 9 Szenen in 15 bis 22 s, jede Grenze auf einem Schlag, Wischer mit einem schrägen Band (8 Bilder) zwischen den Szenen; Produkt und Preis sind eine durchgehende Einstellung.
- **Ton:** fertige Mischung aus den Props (`ton`); stumm möglich. Akzente (Landung, Preisschild, Merkmale) auf Schlägen des Rasters aus `takt`.
- **Text:** Titel, Schlagzeilen, Name und Dringlichkeit in der schmalen Titelschrift (Versalien); Merkmale, Handlungsaufforderung und Webadresse in der Grotesk (Inter 600/800, im Würfel jede Grotesk). Alles links bündig außer Dringlichkeit und Schlusskarte.

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Titelbild | 10 % | Titel oben links (bis 3 Zeilen, 12 % Schrifthöhe), Akzentbalken darunter, Produkt 40 % hoch, Standfläche bei 83 % | 2 s |
| Schlagzeile | 30 % | Wörter mittig bei 36 % der Höhe, Akzent- oder Grundfläche, Produkt 17 % hoch abwechselnd rechts und links, Laufband bei 80 % | 1 bis 2 s je Zeile |
| Produkt landet | 15 % | Name oben links, Merkmale als Etiketten darunter (eins je Schlag), Produkt 42 % hoch mittig | 2,5 bis 3,5 s |
| Preis | 15 % | Produkt rückt nach links unten (74 %), Preisschild 52 % breit rechts oben schräg | 2,5 s |
| Dringlichkeit | 10 % | schräges Band (23 % hoch, minus 4 Grad) bei 40 %, Laufband bei 68 % | 2 s |
| Schlusskarte | 20 % | Logo oben (auf Platte bei dunklem Grund), Produkt 29 % hoch, Handlungsaufforderung als Fläche bei 67 %, Webadresse darunter | 3,5 bis 4 s |

## Dramaturgie
- **Hook (0 bis 2 s):** Titelbild steht ab Bild 0 komplett (Titel, Produkt), der Akzentbalken wächst, das Produkt rückt an.
- **Aufbau (2 bis 8 s):** Schlagzeilen im Takt, Flächen wechseln, Wischband zwischen jeder.
- **Schlag (8 bis 13 s):** Produkt fliegt ein und landet auf dem Schlag, Merkmale je Schlag; Preisschild knallt auf den nächsten Schlag.
- **Halt (13 bis 15 s):** Dringlichkeit auf dem Band, Laufband.
- **Schluss (15 bis 19 s):** Logo, Produkt, Handlungsaufforderung, Webadresse; Glanz über die Fläche, langsames Heranfahren.

## Schnittmuster
Bauplan bei 120 BPM (Sechzehntel 0,125 s); die Länge rechnet der Motor aus den Texten (Lesezeit 3 Wörter je Sekunde plus Halt, mit Stimme aus den Wortzeiten), Grenzen immer auf Schlägen. Wachsen dürfen Titel, Schluss und jede Schlagzeile mit langem Text.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-15 | Titelbild | Start | Einsatz |
| 2 | 16-27 | Schlagzeile 1 (Akzentfläche) | Wischband | Schlag |
| 3 | 28-43 | Schlagzeile 2 (Grund) | Wischband | Schlag |
| 4 | 44-51 | Schlagzeile 3 (Akzentfläche) | Wischband | Schlag |
| 5 | 52-79 | Produkt landet, Merkmale | Wischband | Landung auf Schlag |
| 6 | 80-99 | Preisschild | durchgehend | Aufschlag auf Schlag |
| 7 | 100-115 | Dringlichkeit | Wischband | |
| 8 | 116-147 | Schlusskarte | Wischband | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Rollenfarbe grund; Flächen ganzflächig, keine Verläufe außer Licht hinter dem Produkt und Schatten darunter.
- **Bildbehandlung:** keine Filter auf Produkt oder Logo. Logo auf Platte (`logoPlatte`), wenn der Grund dunkel ist; Plattenfarbe frei (etwa der Grund des Logos).
- **Bausteine:** `src/beispiele/motoren/gemeinsam_p2.tsx`: MaskenZeilen, Produkt, LogoMarke, Preisschild, Merkmale, Laufband, Schlusskarte, WischEin, Szenenplan `plane()`, Fehlerhinweis.
- **Typografie:** Titelschrift schmal und fett, Größe so, dass die längste Zeile 85 % der Breite füllt (höchstens 12 bis 13,5 % der Höhe); Zahl und Einheit bleiben zusammen. Lauftext Grotesk ab 2,8 % der Höhe (54 px).
- **Bewegung:** Eingänge ease-out-expo (0,16, 1, 0,3, 1), Abgänge ease-in; Wörter 9 Bilder, Wischband 8 Bilder, Landung ein Schlag, Preisschild 5 Bilder; Push-in 2 bis 4 % je Szene.
- **Formate:** 9:16 (Pflicht), 16:9 (Titel und Name links, Produkt rechts, Preisschild links unten), 1:1 (wie 9:16, Prozentwerte). Kompositionen `AngebotsTicker`, `AngebotsTicker-16x9`, `AngebotsTicker-1x1`.

## Props
`inhalt` als ein Objekt (eigene Props ersetzen das Beispiel ganz): `titel` („|“ bricht um), `schlag` (Liste), `produkt: {src}`, `name`, `merkmale`, `preis: {text, zeile?}`, `dringlichkeit`, `logo: {src} | {text, serif?}` (Wortmarke, mit `serif: true` in EB Garamond wie ein Etikett), `web`, `cta`, `hintergrund: {src}` (unter dem Titelbild, abgedunkelt durch eine Fläche, nie gefiltert). Daneben: `farben: {grund, text, akzent}` (Markenfarben, gehen über den Würfel), `logoPlatte`, `ton: {src}`, `woerter` (WortDatei), `takt: {bpm, null_s}`, `fps`. Pflicht: titel, schlag, produkt, name, logo, web, cta; fehlt eins, steht der rote Hinweis im Bild. Das Laufband unter den Schlagzeilen zeigt je Szene ein Merkmal; die Dringlichkeit steht nur in ihrer eigenen Szene, der Preis zusätzlich auf der Schlusskarte. Die Länge ist mindestens 15 s (der Schluss wächst). Beispiel: `starter/beispiele/angebots-ticker/props.json`.

## Material
- **Bilder:** echtes Produktfoto des Kunden, freigestellt (`freistellen.py` oder rembg). Ohne Foto: `product packshot of [subject], three-quarter view, soft studio light from upper left, isolated on plain light grey, no text, no logo`, dann freistellen.
- **Musik:** `Punchy retail commercial track, 120 BPM, tight kick on every beat, claps on 2 and 4, short bright synth stabs, driving bass; 0-2 s kick and stabs, 2-8 s full groove, 8 s and 10.5 s single accent hits, 13-15 s groove continues, 15-19 s groove drops to kick and stabs and ends on a clean final hit, instrumental, no vocals`
- **Geräusche:** ein kurzer Wisch auf jedem Wischband, ein tiefer Aufschlag bei Landung und Preisschild; 10 bis 14 dB unter der Musik.

## Regler
- Zahl der Schlagzeilen: eins bis vier (mehr wird zur Liste).
- Preis ja oder nein; ohne Preis folgt die Dringlichkeit direkt auf das Produkt.
- Dringlichkeit ja oder nein (Datum, „Nur diese Woche“, „Solange der Vorrat reicht“, nur was stimmt).
- Takt: 100 bis 130 BPM; darunter verliert der Spot den Handelsdruck.

## Abnahme
Gemessen an der eigenen Basis (`wuerfeln.py motor`, Beispiel-Props, stumm, 9:16, 17 s): Helligkeit 0,195, Kontrast 0,248, Farbigkeit 0,42 (die Akzentflächen), die Schnitterkennung findet 0 harte Schnitte: Wischband und Masken sind weiche Übergänge, darum Shot-Median gleich Länge. Die Fenster in `abnahme` sind diese Werte mit Rand; die Szenen (7 bis 9) zählt man im Streifen. Das Fenster gilt für dunkle Häuser; ein helles Haus (Feinkost) liegt bei Helligkeit um 0,8 und wird mit eigenen `farben` gebaut, nicht über den Würfel.
- Standbild: Produkt nie angeschnitten, Schrift 40 px vom Rand auch im Aufschlag, nichts Bedeutendes in den unteren 15 %.
- Kontrast Schrift zu Fläche mindestens 4,5 (der Motor meldet es, Wächter `p2-kontrast-*`).
- Streifen 12 fps: Landung und Preisschild auf einem Schlag, höchstens ein Wechsel Grund/Akzent je Sekunde.

## Fallen
- (Bau 05.11.2026) Würfel-Farbtausch über dem Motor dreht die Ableitungen (gedeckte Fläche, Licht) um den Akzentwinkel statt sie neu abzuleiten; darum liegt der Inhalt neben der Bühne (`P2Buehne`) und nimmt die Rollen aus `stil.rollen.ziel` selbst.
- (Bau) Mischung zweier Rollen in linearem Licht macht aus 7 % Weiß auf Schwarz ein Mittelgrau; im sRGB-Raum mischen wie eine Deckkraft-Ebene.
- (Bau) „27 °C“ brach am Leerzeichen um; Zahl und Einheit werden vor dem Satz mit festem Leerzeichen verbunden.
- (Bau) Preisschild mit Maßstab 1,9 im Aufschlag ragte über den Rand; 1,45 und Mitte bei 60 % der Breite.
- (Bau) Kontaktbögen zeigen im Wischband zwei Laufbänder gegeneinander, das sieht klein wie überlappender Text aus; in voller Größe prüfen.
- Akzent ohne Kontrast zur Schrift (Olivgrün mit Creme oder Dunkelgrün): der Motor stuft die Akzentfläche ab, bis 4,6 hält; der Akzent als Linie bleibt die Markenfarbe.
- Keine erfundenen Zahlen und keine erfundene Dringlichkeit: Preis, Datum, Aktion nur aus dem Auftrag.
- (Prüfrunde 1) Dieselbe Dringlichkeitszeile lief als Laufband unter jeder Schlagzeile und dann noch zweimal in ihrer Szene: rund zehnmal derselbe Satz wirkt wie Vorlage. Laufband zeigt je Szene ein Merkmal, die Dringlichkeit genau einmal, darunter das Produkt groß.
- (Prüfrunde 1) Produkt per Deckkraft über der Akzentfläche eingeblendet sah 5 Bilder lang rot eingefärbt aus, wie ein Filter. Produkt nur mit Bewegung oder Maske hereinholen, nie mit Deckkraft über Farbe.
- (Prüfrunde 1) Beim Preis rückte das Produkt bis 28 px an den Rand; Lage aus der Produktbreite rechnen, mindestens 60 px Rand.
- (Prüfrunde 1) Für ein Premium-Lebensmittel (Öl) wirkt der Handels-Ticker billig; lebensmittel-feinkost steht darum nicht mehr in `branchen_passt` (neutral). Für Feinkost besser `vorher-nachher` oder eine ruhige Familie.
- (Prüfrunde 1) Erfundene Dringlichkeit („Solange der Vorrat reicht“) ist ein Blocker; ohne bestätigte Aktion `dringlichkeit` weglassen.
- Das Logo des Kunden kam als PNG mit eigenem hellgrauem Grund; auf Schwarz bleibt es eine Platte. Für eine saubere Schlusskarte das Logo freigestellt oder als SVG mit heller Fassung anfordern.
