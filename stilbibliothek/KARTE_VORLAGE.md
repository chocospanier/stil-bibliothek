---
id: <kurzname-mit-bindestrich, eigener Name, nie der Name der Vorlage>
name: <Anzeigename>
familie: <Familien-Kennung, siehe FAMILIEN.md>
kurz: <ein Satz: was man sieht und wie es wirkt>
kern: [<Merkmal 1>, <Merkmal 2>, <Merkmal 3>]   # ohne diese drei ist es nicht der Stil
energie: <1 ruhig bis 5 rasant>
format_quelle: "<9:16 | 16:9 | 4:3 | 1:1>"
laenge_s: [<von>, <bis>]
messung:
  shot_median_s: <aus messung.json>
  schnitte_pro_s: <schnitte_pro_min / 60, eine Nachkommastelle>
  schnitte_verlauf: [<Anfang>, <Mitte>, <Ende>]   # Schnitte je Sekunde je Drittel
  bpm: <Schätzung; Halb- oder Doppeltempo möglich, mit dem Bild abgleichen>
  schnitt_auf_beat: <niedrig | mittel | hoch>   # Anteil gegen Zufallswert und Rundungsabweichung des Schnittmusters
  lufs: <integriert>
  helligkeit: <0..1>
  kontrast: <0..1>
  farbigkeit: <0..1>
schnittmuster_16tel: [<Shot-Längen in Sechzehnteln, erste 24 bis 40 Werte aus messung.json>]
palette:
  <rolle>: "<#HEX>"        # Rollen: grund, zeichnung, akzent, licht, haut, text ...
effekte: [<Kennungen aus EFFEKT_VOKABULAR.md, neue als neu:kennung>]
kamera: <ein Satz>
ton: <ein Satz>
braucht: [<fotos-figur | illustrationen | footage-ort | produkt | nur-typo | 3d>]   # eins davon reicht; am Kern prüfen, ob das eigene Material ihn trägt
motor_aufwand: <klein | mittel | gross>
einsatz: [<trailer | hook | intro | uebergang | ganzes-kurzvideo | musikvideo | produkt | portrait>]
abnahme:                  # Zielwerte für den eigenen Render im Format der Quelle, gemessen mit starter/werkzeuge/abnahme.py
  shot_median_s: [<min>, <max>]     # formatfest
  schnitte_pro_s: [<min>, <max>]    # formatfest
  helligkeit: [<min>, <max>]        # formatabhängig
  farbigkeit: [<min>, <max>]        # formatabhängig
  lufs: [<min>, <max>]              # formatfest
abnahme_9x16:             # optional: eigene Werte fürs Hochformat, wenn format_quelle nicht 9:16 ist; fehlt der Block, gilt abnahme mit +0,03 auf die obere Grenze von Helligkeit und Farbigkeit
  helligkeit: [<min>, <max>]
  farbigkeit: [<min>, <max>]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# <Name>

<Ein bis zwei Sätze: Wirkung und woher die Energie kommt.>

## Kern
Die drei Merkmale aus `kern`, je ein Satz, warum sie den Stil tragen. Wer nur diese drei trifft, ist zu 80 % da.

## Erkennung
- **Bild:** <Grund, Bildbehandlung, Farben mit Rollen, Textur, Licht>
- **Schnitt:** <Zahlen aus der Messung in Worten, Übergangsarten, Raster>
- **Ton:** <Musikcharakter, Tempo, Stimme ja/nein, Geräusche, Lautheit>
- **Text:** <Rollen des Textes, Schriftcharakter, Position, Bewegung>

## Bildtypen
Jede Art von Einstellung, die vorkommt, als Tabelle. Motive allgemein benennen („Tier als Holzschnitt“, nicht das konkrete Tier der Vorlage).

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|

## Dramaturgie
<Energiekurve mit Sekunden oder Takten: Hook (0 bis 2 s), Aufbau, Atem, Schlag, Halt, Schluss.>

## Schnittmuster
Kopfblock = gemessene Schnitte, Tabelle = Bauplan: `schnittmuster_16tel` zählt nur die harten Schnitte der Vorlage, weiche Übergänge nicht; die Tabelle darf deshalb mehr Slots haben. Strecken: In der Tabelle markieren, welche Slots wachsen dürfen (Hook, Atem, Schluss); kurze Slots bleiben, sonst kippt der Rhythmus.
Ein Bauplan für ein eigenes Stück von 15 bis 20 s, abgeleitet aus dem gemessenen Rhythmus: je Zeile Sechzehntel (oder Sekunden bei Stilen ohne Beat), Bildtyp aus der Tabelle oben, Übergang, Ton-Ereignis. Inhalt austauschbar, Rhythmus bleibt.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|

## Rezept für einen Code-Motor
- **Grund:** <wie der Hintergrund entsteht>
- **Bildbehandlung:** <Filter, Masken, Textur; wie man sie in Remotion/Canvas/SVG baut, mit Zahlen>
- **Bausteine:** <welche Elemente gebraucht werden, je mit Maßen und Timing>
- **Typografie:** <Schriftcharakter mit einem frei lizenzierten Beispiel, Größen relativ zur Bildhöhe, Betonung>
- **Bewegung:** <Raster, Haltezeiten, Übergänge, Kamera, Easing>
- **Formate:** <wie der Stil in 9:16 und 16:9 übersetzt wird: wohin das Motiv rückt, was beschnitten werden darf>

## Material
- **Bilder:** <ein bis zwei generische englische Bild-Prompts für das Rohmaterial (Illustration, Kulisse, Figur), die den Look schon mitbringen>
- **Musik:** <ein englischer Musik-Prompt: Genre, BPM, Instrumente, Aufbau mit Sekunden, „instrumental, no vocals“>
- **Geräusche:** <welche, wie laut unter der Musik>

## Regler
<Was sich innerhalb des Stils verändern lässt, ohne dass er kippt.>

## Abnahme
<Wie man den eigenen Render prüft: Zielwerte aus `abnahme` plus zwei, drei Augen-Prüfungen am Standbild.>
Formatfest sind Schnitte je Sekunde, Shot-Median und LUFS. Helligkeit und Farbigkeit hängen vom Format ab: Im Hochformat decken Motive anteilig weniger Fläche; ohne Block `abnahme_9x16` gilt dort die obere Grenze +0,03.

## Fallen
- <Falle → Lösung>
