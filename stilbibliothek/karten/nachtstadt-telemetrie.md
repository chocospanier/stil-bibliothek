---
id: nachtstadt-telemetrie
name: Nachtstadt-Telemetrie
familie: glitch
kurz: Leere Orte einer Stadt bei Nacht in Magenta und Violett, ruhig gefilmt, überlagert von einer feinen Messoberfläche mit Etiketten, Zeigelinien, Zählern und Zeitleiste, als würde eine Maschine die Nacht protokollieren.
kern: [ruhige Nachtbilder in Magenta-Violett mit nassen Spiegelungen, feine Mess-Oberfläche (Etiketten mit Zeigelinie, Zählerkasten, Zeitleiste, Ecken), ganz wenig Bewegung und lange Halte gegen Ende]
energie: 2
format_quelle: "16:9"
laenge_s: [12, 25]
messung:
  shot_median_s: 0.67
  schnitte_pro_s: 1.3
  schnitte_verlauf: [1.5, 1.6, 0.9]
  bpm: 94
  schnitt_auf_beat: mittel
  lufs: -14.1
  helligkeit: 0.11
  kontrast: 0.15
  farbigkeit: 0.16
schnittmuster_16tel: [3, 4, 5, 3, 3, 7, 6, 7, 2, 2, 1, 2, 27, 3, 4, 20]
palette:
  nacht: "#0E0012"
  violett_tief: "#16031C"
  pflaume: "#4B1F48"
  magenta: "#B13F73"
  rosa_licht: "#B4809B"
  hud_cyan: "#5BC8E8"
  hud_weiss: "#E8E6EC"
  hud_rot: "#E8344E"
effekte: [harter-schnitt, wischer, push-in, kamera-steht, neon, glow, vignette, filmkorn, bewegungsunschaerfe, hud, mono-zeile, zahl-walze, titelkarte, partikel, tracking-etiketten]
kamera: Meist stehend oder sehr langsamer Push; Bewegung kommt aus Regen, Dampf und Wischern zwischen den Bildern.
ton: Ruhige, atmende Elektronik (−14,1 LUFS, 4,7 LU Spanne, Spitzen nur −5 dBFS) um 94 BPM; Stimme nicht feststellbar, vermutlich Regen und Stadtgeräusche.
braucht: [footage-ort, nur-typo]
motor_aufwand: mittel
einsatz: [intro, trailer, ganzes-kurzvideo, uebergang]
abnahme:
  shot_median_s: [0.54, 0.80]
  schnitte_pro_s: [1.0, 1.6]
  helligkeit: [0.08, 0.14]
  farbigkeit: [0.13, 0.19]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Nachtstadt-Telemetrie

Eine Stadt um drei Uhr nachts, gesehen durch die Augen eines Messsystems: leere Gänge, Gerätereihen, Unterführungen, Pfützen, und über allem eine feine Oberfläche, die jedes Ding beschriftet, zählt und protokolliert. Die Wirkung kommt aus der Ruhe und der kühlen Präzision der Grafik auf warmem Neon.

## Kern
- **Magenta-Violett-Nacht:** Fast schwarz (Helligkeit 0,11), Neon in Magenta und Rosa, nasse Böden mit Spiegelungen, Dampf im Gegenlicht, kleine blaue Gegenlichter. Keine Menschen im Vordergrund, höchstens Silhouetten von hinten.
- **Telemetrie-Oberfläche:** Kleine Etiketten mit Kästchen-Kennung und Zeigelinie zu Dingen im Bild, ein Zählerkasten oben rechts mit großer Zahl und Mini-Balken, eine Zeitleiste über die ganze Breite unten, Sucher-Ecken, Bildzähler oben rechts. Alles fein, 1 px, nie laut.
- **Ruhe und lange Halte:** Zu Beginn Einstellungen von 0,5 bis 1,2 s, dann zwei lange Halte von 4,3 und 3,2 s, in denen nur Grafik und Regen arbeiten.

## Erkennung
- **Bild:** Nacht `#0E0012`, Violett `#16031C`, Pflaume `#4B1F48`, Magenta `#B13F73`, Rosa-Licht `#B4809B`; vereinzelt kühles Blau in Innenräumen. Grafik in Weiß `#E8E6EC`, Cyan `#5BC8E8`, Signalrot `#E8344E`. Korn, Vignette, Glow auf Neonflächen, Bewegungsunschärfe als Übergang. Gemessen: Helligkeit 0,11, Kontrast 0,15, Farbigkeit 0,16, 65 % fast schwarz.
- **Schnitt:** 22 Schnitte in 16,4 Sekunden, Median 0,67 s, längste Einstellung 4,3 s. Dichte 1,5 → 1,6 → 0,9 Schnitte je Sekunde. 45 % der Schnitte auf dem Raster gegen 25 % bei Zufall. Übergänge: harter Schnitt, Wischer (verwischtes Neon von zwei bis zehn Frames), einmal ein Glitch-Bild.
- **Ton:** −14,1 LUFS, Lautheitsspanne 4,7 LU, True Peak −5,0 dBFS. Viel Luft.
- **Text:** Titel einmal groß in schmaler fetter Grotesk weiß mitten im Bild; danach dauerhaft oben links klein als Kopfzeile mit Unterzeile; Etiketten mit Kennung „L1, L2“ in Kästchen, Bezeichnung und Messwert, zweite Zeile in einer anderen Schrift kleiner; Zählerkasten mit Überschrift in cyanem Balken, große Zahl, drei Werte-Zeilen in Cyan, Rot und Weiß; Zeitleiste mit Sekundenmarken unten.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Fluchtpunkt-Gang mit Neon | 20 % | Gang oder Unterführung zentralperspektivisch, Fluchtpunkt mittig, Neonkästen links und rechts, nasser Boden | 3 bis 7 Sechzehntel |
| Ort mit Gerät | 15 % | Automaten oder Maschinen in Reihe, mittig bis rechts, 30 bis 60 % der Bildhöhe, Etikett mit Zeigelinie | 5 bis 7 Sechzehntel |
| Silhouetten von hinten | 10 % | zwei Gestalten in Kapuzen unten links und rechts, Dampf und Gegenlicht zwischen ihnen | 3 bis 7 Sechzehntel |
| Neon-Unschärfe | 15 % | ganzes Bild verwischt in Magenta | 1 bis 2 Sechzehntel |
| Leere Straße mit Messlinien | 20 % | Straße dunkel, Neon klein rechts, Fachwerk aus roten Linien oben, Messlinie quer | 27 Sechzehntel (Halt) |
| Objekt am Boden | 10 % | kleine Kugel oder Gegenstand unten mittig, 10 % der Bildhöhe, Pfütze, Zaun dahinter | 4 Sechzehntel |
| Pfütze mit Regenringen | 10 % | Pfütze mittig, Neon spiegelt sich, Ringe mit Messkreis | 20 Sechzehntel (Halt) |

## Dramaturgie
- **Hook (0 bis 1,2 s):** Neon-Unschärfe, dann ein Fluchtpunkt-Gang mit ersten Etiketten.
- **Titel (1,2 bis 2 s):** Titelwort groß über einer leuchtenden Gerätereihe.
- **Orte (2 bis 6,2 s):** Raum mit Geräten (unscharf, dann scharf mit sitzender Gestalt), Silhouetten im Dampf, Gerätereihe.
- **Unruhe (6,2 bis 7,6 s):** drei Neon-Wischer im Wechsel mit dem Gang.
- **Halt 1 (7,6 bis 11,9 s):** leere Straße, Messlinien, ein Neonzeichen flackert und erlischt.
- **Zwei Orte (12 bis 13,2 s):** Rolltreppe, Objekt am Boden.
- **Halt 2 (13,2 bis 16,4 s):** Pfütze mit Regenringen und Messkreis.

## Schnittmuster
Bauplan für 18 s bei 94 BPM (112 Sechzehntel zu 0,16 s). Ruhiger Stil: Einstellungen drei bis sieben Sechzehntel, zwei lange Halte.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-2 | Neon-Unschärfe | hart | Pad, Regen |
| 2 | 3-6 | Fluchtpunkt-Gang, Etiketten zeichnen sich | Wischer | Puls setzt ein |
| 3 | 7-11 | Gerätereihe, Titelwort groß, dann in die Kopfzeile | hart | Akzent |
| 4 | 12-14 | Ort unscharf | hart | Beat |
| 5 | 15-21 | Ort scharf mit sitzender Gestalt, Etikett an der Gestalt | hart | Beat |
| 6 | 22-27 | Silhouetten im Dampf, Temperatur-Etikett | hart | Zischen |
| 7 | 28-34 | Geräte im Dunkeln, Zähler springt | hart | Beat |
| 8 | 35-40 | Neon-Wischer, Gang, Wischer | Wischer | Swell |
| 9 | 41-67 | Halt: leere Straße, Messlinien, Neon erlischt | hart | nur Pad und Regen |
| 10 | 68-71 | Rolltreppe mit zwei Etiketten | hart | Puls |
| 11 | 72-75 | Objekt am Boden, Funk-Etikett blinkt | hart | Puls |
| 12 | 76-103 | Halt: Pfütze, Regenringe, Messkreis | hart | Ausklang |
| 13 | 104-111 | Schwarz, Kopfzeile bleibt kurz | Blende | Stille |

## Rezept für einen Code-Motor
- **Grund:** keiner; Aufnahmen füllen das Bild.
- **Bildbehandlung:** Grading: Schwarz auf `#0E0012`, Mitten Richtung `#4B1F48`, Lichter Richtung `#B4809B`; blaue Lichter bleiben. Glow auf Neon (Schwelle 75 %, Weichzeichner 2 % der Bildhöhe, `screen` 60 %), Korn 6 %, Vignette 35 %, leichte Halation rosa.
- **Bausteine (alle 1 px, bei 1080 px Höhe):** Etikett (Kästchen mit Kennung 1,5 % der Bildhöhe, daneben Bezeichnung 1,6 % in Weiß, darunter zweite Zeile 1,2 % in Grau, halbtransparenter dunkler Grund 40 %, Zeigelinie in Cyan zum Objekt mit Punkt am Ende; zeichnet sich in sechs Frames); Zählerkasten (oben rechts, 9 % × 13 % der Bildgröße, cyaner Kopfbalken mit Bezeichnung, große Zahl 4 % der Bildhöhe, die per Walze steigt, drei Wertezeilen mit Punkten in Cyan, Rot, Weiß, darunter zehn Mini-Balken, die zur Musik wippen); Kopfzeile (oben links, Titel 2,5 % fett, Unterzeile 1,2 %, Linie darunter); Bildzähler (oben rechts über dem Kasten, „Telemetrie“ klein, Bildnummer 1,4 %); Zeitleiste (unten über die volle Breite, 3 % vom Rand, Marken je Sekunde, Laufzeit links); Sucher-Ecken (vier Winkel in der Mitte des Bildes, Schenkel 2 %); Messkreis (konzentrische Kreise 1 px um die Regenringe, wachsen mit); Messlinien (Fachwerk aus roten Linien, 40 % Deckung, über der Straße).
- **Typografie:** Titel in schmaler fetter Grotesk (frei lizenziert zum Beispiel Barlow Condensed 700), Etiketten in Grotesk (zum Beispiel Barlow 500), Zahlen und Zeitleiste in Mono (zum Beispiel JetBrains Mono 500), zweite Etikettzeile in einer zweiten Schrift oder Sprache klein.
- **Bewegung:** Bild steht oder Push 2 bis 4 % über die Einstellung. Grafik lebt: Zähler zählen, Balken wippen, Etiketten zeichnen sich zu Beginn jeder Einstellung, Bildzähler läuft. Wischer zwei bis zehn Frames.
- **Formate:** Quelle 16:9. In 9:16 Zählerkasten oben rechts kleiner, Kopfzeile oben links, Zeitleiste über die unteren 15 % hinaus nach oben verlegen; Fluchtpunkt-Gänge und Pfützen passen gut hochkant. In 16:9 wie die Quelle.
- **Neue Kennungen:** `neu:telemetrie-etikett`: Ein kleines Kästchen mit Kennung und Bezeichnung zeigt per Zeigelinie auf ein Ding im Bild.

## Material
- **Bilder (Ort):** `empty [subject] in a city at 3am, magenta and pink neon light, wet reflective floor, light haze, no people, cinematic, grainy, deep shadows, centered one-point perspective`
- **Bilder (Pfütze):** `close-up of a rain puddle on asphalt at night reflecting magenta and blue neon signs, raindrops forming rings, shallow depth of field, moody`
- **Musik:** `Minimal nocturnal electronic, 94 BPM, soft muffled kick, sub bass, granular pads, rain and distant traffic textures, gentle pulse from one second, short swell at six point two seconds, drums drop out from seven point six to eleven point nine seconds leaving only pads and rain, soft pulse returns briefly, fades out from thirteen seconds, instrumental, no vocals`
- **Geräusche:** Regen durchgehend (−20 dB), Neonbrummen, Zischen beim Dampf, digitale Ticks bei jedem neuen Etikett (−18 dB).

## Regler
- Lichtfarbe: Magenta-Violett ist der Kern; Cyan-Grün oder Bernstein gehen als ganze Stimmung.
- Dichte der Oberfläche: von zwei Etiketten bis vollem Kasten-Set; mehr als drei Etiketten je Bild wird unruhig.
- Haltelänge: 2 bis 5 s.
- Für Daten-Themen: Zählerkasten zeigt echte Werte (Preise, Temperaturen, Zähler) mit Quelle.
- Mit Sprechstimme: Stimme in den Halten, Etiketten erscheinen auf den Schlüsselwörtern.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen, besonders die sehr niedrige Helligkeit.
- Standbild-Prüfung: jede Zeigelinie endet an einem echten Ding im Bild; Grafik ist bei 1080 px gestochen scharf; keine Fläche heller als die Neonzeichen.
- Streifen bei 12 fps: Halte stehen mindestens 3 s; Zähler und Balken bewegen sich in den Halten.

## Fallen
- Grafik zu dick oder zu groß → wirkt wie Spiel-Oberfläche; 1 px Linien, Texte 1,2 bis 1,6 % der Bildhöhe.
- Etiketten mit erfundenen Messwerten in Nachrichtenstücken → nur echte oder klar fiktive Daten.
- Zu helles Material → Neon verliert Wirkung; vor dem Grading Belichtung senken.
- Schrift auf 9:16 zu klein → mindestens 1,8 % der Bildhöhe im Hochformat.
- Lesbarkeit in Fremdsprache als Deko → zweite Zeile nur, wenn sie zum Kanal passt.
