---
id: vorher-nachher
name: Vorher-Nachher
familie: produktspot
kurz: Ein Produktspot als Gegenüberstellung im geteilten Bild; oben das Alte auf gedeckter Fläche (oder als Bild aus den Props), unten das Neue auf dem Grund, zwei bis drei kurze Zeilenpaare, die alte Zeile wird in Akzentfarbe gestrichen, dann schiebt die Teilung das Alte hinaus und das echte Produkt steht allein als Held mit Preis und Schlusskarte.
kern: [geteiltes Bild mit Linie in Akzentfarbe und zwei Etiketten für alt und neu, Zeilenpaare in großen schmalen Versalien bei denen die alte Zeile auf dem Schlag gestrichen wird, das freigestellte Produkt als Konstante auf der neuen Seite und am Ende allein als Held mit Preis und Schlusskarte]
energie: 3
format_quelle: "9:16"
laenge_s: [15, 25]
messung:
  shot_median_s: 19.5
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm: 120
  schnitt_auf_beat: hoch
  lufs: null
  helligkeit: 0.171
  kontrast: 0.217
  farbigkeit: 0.149
schnittmuster_16tel: [16, 24, 24, 24, 24, 20, 32]
palette:
  grund: "#111111"
  text: "#FFFFFF"
  akzent: "#E3120B"
  licht: "#4A4A4A"
effekte: [harter-schnitt, split-screen, masken-wechsel, wort-auf-beat, freisteller, push-in, titelkarte, beat-getrieben]
kamera: Steht; die Teilung öffnet sich wie zwei Türen über dem Titelbild, am Ende schiebt sie das Alte nach oben hinaus; Held und Schlusskarte fahren langsam heran.
ton: Ruhig treibender Beat um 110 bis 120 BPM; der Strich durch die alte Zeile sitzt auf dem Schlag. Mit Stimme folgen die Paare den Wortzeiten.
braucht: [produkt, nur-typo]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo]
zweck: [produktwerbung, angebot, erklaeren]
branchen_passt: [werkstatt-auto, handwerk, technik, lebensmittel-feinkost, gastro, sport, immobilien]
branchen_nie: [kinder-familie, musik-kultur]
abnahme:
  shot_median_s: [12.0, 25.0]
  schnitte_pro_s: [0.0, 0.2]
  helligkeit: [0.12, 0.24]
  farbigkeit: [0.09, 0.22]
  lufs: [-15, -13]
# Würfel-Felder: Markenfarben über Rollen (der Motor leitet Fläche, gedeckt und Licht selbst ab), Schrift in der Klasse
creator: nein
creator_grund: "Das geteilte Bild (split-screen, Klasse rahmen) ist der Kern; ohne Teilung ist es nicht der Stil"
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
quelle: Eigener Entwurf (Strang P2, 05.11.2026) nach dem Handwerk von Vorher-Nachher-Anzeigen; keine Vorlage, keine Motive, Texte oder Marken übernommen.
---

# Vorher-Nachher

Die älteste Verkaufsform der Welt, sauber gesetzt: Was du heute machst, was du mit dem Produkt machst. Die Energie kommt nicht aus Schnitten, sondern aus dem Strich, der die alte Zeile auf dem Schlag durchstreicht, und aus dem Moment, in dem die Teilung das Alte aus dem Bild schiebt und nur noch das Produkt steht.

## Kern
- **Geteiltes Bild:** 9:16 oben alt (gedeckte Fläche: Grund mit 11 % Text; oder ein Bild aus `inhalt.alt`, mit Verlauf aus dem Grund für die Schrift), unten neu auf dem Grund; Linie in Akzentfarbe bei 47 % der Höhe, Etiketten über und unter der Linie (alt auf Grund, neu auf Akzentfläche). 16:9 links und rechts.
- **Zeilenpaare:** alte Zeile steigt aus der Maske, auf dem nächsten Schlag streicht ein Balken in Akzentfarbe jede Zeile durch, sechs Bilder später steigt die neue Zeile mit einem senkrechten Akzentbalken davor. Bis 3 Zeilen, Schrift bis 11,5 % der Höhe.
- **Produkt als Held:** das freigestellte Foto steht während der Paare klein rechts auf der neuen Seite (Konstante), dann schiebt die Teilung das Alte nach oben hinaus, das Produkt steigt groß in die Mitte, Name und Merkmale darüber, Preisschild gleitet herein, Schlusskarte.

## Erkennung
- **Bild:** drei Rollen (Grund, Text, Akzent) und ihre Ableitungen; die alte Seite immer gedeckter als die neue. Keine Zeichnungen von Gegenständen: ohne Bild ist die alte Seite reine Schrift.
- **Schnitt:** Titelbild, die Türen schließen sich darüber (9 Bilder), Paare je 2 bis 3,5 s mit Wechsel der Zeilen in der Maske, Held, Schlusskarte mit einem Vorhang in Akzentfarbe von unten.
- **Ton:** fertige Mischung aus den Props (`ton`), stumm möglich; Strich auf dem Schlag des Rasters.
- **Text:** alle Aussagen in der schmalen Titelschrift (Versalien), Etiketten und Merkmale in der Grotesk ab 2,8 % der Höhe.

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Titelbild | 10 % | Frage oder Satz mittig oben (bis 3 Zeilen), Produkt 46 % hoch, Standfläche bei 83 % | 2 s |
| Paar | 45 % | oben alte Zeile über der Linie, unten neue Zeile links, Produkt 27 % hoch rechts unten | 2 bis 3,5 s je Paar |
| Held | 20 % | Name oben mittig, Merkmale darunter, Produkt 42 % hoch mittig | 2,5 bis 3 s |
| Preis | 10 % | Produkt nach links unten (74 %), Preisschild 50 % breit gleitet rechts herein | 2,5 s |
| Schlusskarte | 15 % | Logo oben, Produkt 29 % hoch, Dringlichkeit als Zeile, Handlungsaufforderung als Fläche, Webadresse | 3,5 s |

## Dramaturgie
- **Hook (0 bis 2 s):** Frage und Produkt stehen ab Bild 0.
- **Aufbau (2 bis 11 s):** die Türen schließen sich, drei Paare; jedes Paar: alt, Strich auf dem Schlag, neu.
- **Schlag (11 bis 14 s):** die Teilung schiebt das Alte hinaus, das Produkt steigt groß ins Bild.
- **Halt (14 bis 17 s):** Name, Merkmale, Preis.
- **Schluss (17 bis 21 s):** Schlusskarte.

## Schnittmuster
Bauplan bei 120 BPM; die Länge rechnet der Motor aus den Texten (Lesezeit 3,3 Wörter je Sekunde plus Halt, mit Stimme aus den Wortzeiten), Grenzen auf Schlägen. Wachsen dürfen Titel, Paare mit langen Zeilen und Schluss.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-15 | Titelbild | Start | Einsatz |
| 2 | 16-39 | Paar 1 (Türen schließen sich) | Türen | Strich auf Schlag |
| 3 | 40-63 | Paar 2 | Zeilen in der Maske | Strich auf Schlag |
| 4 | 64-87 | Paar 3 | Zeilen in der Maske | Strich auf Schlag |
| 5 | 88-111 | Held | Teilung schiebt hinaus | Akzent |
| 6 | 112-131 | Preis | durchgehend | |
| 7 | 132-163 | Schlusskarte | Vorhang Akzent | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Rollenfarbe grund; alte Seite gedeckte Fläche oder Bild mit Verlauf aus dem Grund (82 bis 88 % Deckung unten), nie gefiltert.
- **Bausteine:** `gemeinsam_p2.tsx` wie beim Angebots-Ticker; eigene Teile in `VorherNachher.tsx`: Etikett, PaarSzene, HeldSzene, Vorhang.
- **Typografie:** wie Angebots-Ticker; die neue Zeile ist schmaler gesetzt (Platz für das Produkt).
- **Bewegung:** Standardkurve (0,2, 0, 0, 1) für Teilung und Türen (9 bis 12 Bilder), Masken 9 Bilder, Strich 9 Bilder je Zeile, Preisschild als Feder ohne Überschwingen.
- **Schlusskarte:** eigene Anordnung (`art: seite`): Logo links oben mit Akzentlinie, Produkt groß rechts, Preis, Zeile, Knopf und Webadresse links darunter.
- **Formate:** 9:16 (Pflicht), 16:9 (Teilung senkrecht in der Mitte), 1:1. Kompositionen `VorherNachher`, `VorherNachher-16x9`, `VorherNachher-1x1`.

## Props
`inhalt` als ein Objekt: `titel`, `etiketten` (genau zwei, etwa „Vorher“, „Nachher“), `paare` (mindestens zwei, je `{alt, neu}`), `alt: {src}` (optional, Bild der alten Seite), `streichen` (Standard ja; nein, wenn die alte Seite eine Frage ist statt einer Gewohnheit), `produkt: {src}`, `name`, `merkmale`, `preis: {text, zeile?}`, `dringlichkeit` (Zeile auf der Schlusskarte), `logo: {src} | {text, serif?}`, `web`, `cta`. Daneben `farben`, `logoPlatte`, `ton`, `woerter`, `takt`, `fps` wie beim Angebots-Ticker. Pflicht: titel, etiketten, paare, produkt, name, logo, web, cta. Beispiel: `starter/beispiele/vorher-nachher/props.json`.

## Material
- **Bilder:** echtes Produktfoto, freigestellt. Für die alte Seite optional ein echtes Foto der alten Lösung (vom Kunden), sonst Schrift.
- **Musik:** `Confident modern commercial track, 116 BPM, warm kick on every beat, crisp snare on 2 and 4, plucked synth arpeggio, round bass; 0-2 s arpeggio only, 2-11 s full groove with a short accent hit at the start of every second bar, 11 s rising swell into a single bright hit, 11-17 s groove with more air, 17-21 s groove thins to arpeggio and ends on a soft final hit, instrumental, no vocals`
- **Geräusche:** ein trockener Strich-Klang auf jedem Durchstreichen; 12 dB unter der Musik.

## Regler
- Zwei oder drei Paare (vier werden zur Liste).
- Bild für die alte Seite ja oder nein.
- Preis ja oder nein, Dringlichkeitszeile ja oder nein.

## Abnahme
Gemessen an der eigenen Basis (`wuerfeln.py motor`, Beispiel-Props, stumm, 9:16, 19,5 s): Helligkeit 0,171, Kontrast 0,217, Farbigkeit 0,149; die Schnitterkennung findet 0 harte Schnitte (Türen, Masken, Teilung und Vorhang sind weiche Übergänge), darum Shot-Median gleich Länge. Die Fenster in `abnahme` sind diese Werte mit Rand. Helle Häuser (Feinkost) laufen mit eigenen `farben` außerhalb dieses Fensters.
- Standbild: alte Zeile gestrichen und lesbar (Kontrast auf der gedeckten Fläche mindestens 4,6), neue Zeile und Produkt überlappen nie.
- Streifen: Strich auf dem Schlag, kein Bild ohne Text länger als 0,4 s.

## Fallen
- (Bau 05.11.2026) Zwischen Titelbild und erstem Paar stand ein schwarzes Bild; die Teilung schließt sich jetzt als zwei Türen über dem weiterlaufenden Titelbild.
- (Bau) Erste Fassung 30 s: Lesezeit mit 2,3 Wörtern je Sekunde und langem Halt ist für große Werbezeilen zu langsam; 3,3 und 0,6 s Halt.
- (Bau) Gedeckte Fläche in linearem Licht gemischt wurde Mittelgrau und machte die alte Zeile flau; sRGB-Mischung.
- (Bau) 16:9: die neue Zeile lief unter das Produkt; Satzbreite um die Produktbreite kürzen.
- Vergleiche nur mit Tatsachen; die alte Seite beschreibt eine Gewohnheit, nie einen Mitbewerber mit Namen.
- Bei Lebensmitteln keine Wirk- oder Gesundheitsversprechen auf der neuen Seite.
- (Prüfrunde 1) Im Titelbild fuhr das Produkt beim Heranfahren in die Titelzeile; Produkthöhe aus dem Abstand Titel bis Standfläche rechnen, inklusive Maßstab am Ende der Fahrt, mindestens 60 px Luft.
- (Prüfrunde 1) Dreizeilige neue Zeile („KALT, UNTER 27 °C“) reichte in die unteren 15 %; die Schrift schrumpft jetzt, bis die Unterkante bei 84 % liegt.
- (Prüfrunde 1) Die alte Seite darf keine unbelegte Behauptung über andere sein (Feinkost: „üblich warm extrahiert“). Für Lebensmittel die alte Seite als Frage setzen und `streichen: false`.
- (Prüfrunde 1) Die Türen schnitten das Titelprodukt sichtbar in einen Streifen und das Produkt der neuen Seite fuhr unter den Türen ins Bild; Türen 6 Bilder, das Produkt kommt erst danach und nur innerhalb der neuen Seite (Maske über den unteren 15 %).
- (Prüfrunde 1) Der Vorhang zur Schlusskarte deckte nie ganz, dahinter sprang der Inhalt; jetzt läuft eine volle Fläche durch, der Wechsel liegt verdeckt.
- (Prüfrunde 1) Drei Paare im selben Aufbau lesen sich wie Folien; je Paar ein Akzent (Produkt rückt beim Erscheinen der neuen Zeile um 4,5 % an), Halt 0,4 s.
