---
id: glasroentgen-akte
name: Glasröntgen-Akte
familie: erklaerstimme
kurz: Ein Wissens-Erklärer als Fallgeschichte im Dunkeln, gläserne Röntgenkörper als Motiv, darüber eine Akten- und Messebene aus Karteikarte, Stempelkästen, Zeigelinien und getippten Mono-Zeilen, unten eine Untertitel-Pille mit dem gesprochenen Wort im Cyan-Kasten.
kern: [gläserne röntgenhafte Körper auf fast schwarzem Grund mit Cyan als einziger Signalfarbe, eine Ermittlungsebene aus Karteikarte Stempelkästen Zeigelinien und getippten Mono-Zeilen die auf das gesprochene Wort reagiert, Untertitel-Pille über der freien Zone mit dem Aktivwort im Cyan-Kasten]
energie: 3
format_quelle: "9:16"
laenge_s: [45, 120]
messung:
  shot_median_s: 6.8
  schnitte_pro_s: 0.11
  schnitte_verlauf: [0.11, 0.16, 0.05]
  bpm: 60                   # Schätzung aus dem Bett, Halb- oder Doppeltempo möglich
  schnitt_auf_beat: niedrig
  lufs: -13.1
  helligkeit: 0.15
  kontrast: 0.20
  farbigkeit: 0.07
  ereignisse_pro_s: 0.54    # Grafik-Ereignisse im oberen und unteren Band je, Median-Abstand 0,9 bis 1,2 s
  woerter_pro_s: 2.85
schnittmuster_16tel: [27, 23, 43, 9, 53, 5, 6, 9, 12, 83, 48, 84, 43]
palette:
  grund: "#03050F"
  tiefe: "#2F3B4B"
  glas: "#637A8E"
  glaslicht: "#A9BECA"
  akzent: "#4FB8F0"
  papier: "#ECE8DF"
  tinte: "#1A1C22"
  text: "#F2F1EE"
  grau: "#7D848F"
effekte: [sprechstimme, untertitel, aktivwort, akten-karte, satzzeichen-punkt, 3d-render, ein-akzent, glow, partikel, hud, tracking-etiketten, schaubild, mono-zeile, schreibmaschine, stempel, zahl-walze, streifenversatz, glitch-uebergang, push-in, orbit, kamera-steht, harter-schnitt, wort-schnitt, textwende]
kamera: Ruhige, langsame Fahrten um gläserne Körper (Push-in, kleiner Orbit), ein Versuchsraum in Augenhöhe und als Draufsicht, Einstellungen von 1 bis 20 s; die Energie liefert die Grafikebene, nicht die Kamera.
ton: Eine klare Erzählstimme (etwa 2,9 Wörter je Sekunde) mit gesetzten Pausen vor Pointen, darunter ein dichtes Bett aus dunklem Synth und Geräuschen (Whoosh, Glitch, Klick, Tippen), laut gemastert mit kaum Dynamik.
braucht: [3d, nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, hook, trailer]
abnahme:
  shot_median_s: [4, 10]
  schnitte_pro_s: [0.05, 0.25]
  helligkeit: [0.09, 0.21]
  farbigkeit: [0.03, 0.11]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Glasröntgen-Akte

Ein Erklärstück, das ermittelt statt erklärt: Behauptung gegen Behauptung, eine Akte, ein Versuch, eine Messung, die Auflösung, eine Frage an den Zuschauer. Gläserne Körper im Dunkeln zeigen, was innen passiert; eine zweite Ebene aus Papier, Stempeln und Messgrafik reagiert auf jedes wichtige Wort. Die Energie kommt aus diesen Grafik-Ereignissen, etwa eines je Sekunde, bei ruhiger Kamera.

## Kern
- **Glas im Dunkeln, ein Akzent:** Röntgenhafte, durchsichtige Motive (Körperteil, Organ, gesichtslose Figur, Gerät) in Glasblau auf fast Schwarz, 62 % der Fläche fast schwarz. Nur Cyan zeigt, worauf es ankommt: Lichtbahn, Aktivwort, Stempel, Haken. Eine zweite Signalfarbe macht es bunt und beliebig.
- **Ermittlungsebene:** Karteikarte mit Reiter, Stempelkästen mit Rand, Zeigelinien mit Mono-Etiketten, Kopfzeilen, die sich mit Block-Cursor tippen, Zähler, Trefferbalken, Scanlinie mit Schichtzähler. Jedes Element erscheint oder leuchtet auf, wenn sein Wort gesprochen wird.
- **Untertitel-Pille mit Aktivwort-Kasten:** Zwei bis drei Wörter in fetter Kleinschrift auf schwarzer Platte mit feinem Rand, Zeilenmitte bei 75 % der Höhe; das gesprochene Wort steht in einem Cyan-Kasten mit dunkler Schrift, gesprochene Wörter weiß, kommende grau.

## Erkennung
- **Bild:** Fast-Schwarz mit Blaustich (`#03050F`), Glaskörper mit Fresnel-Kanten in `#A9BECA`, Innenleben dunkler, Lichtbahnen in Weiß-Cyan mit Glühen. Feiner Staub (helle Punkte, 0,1 bis 0,2 % groß). Ein grauer Versuchsraum mit kaltem Röhrenlicht als Kontrastwelt. Papier (`#ECE8DF`) ist die einzige helle Fläche und wirkt dadurch wie ein Beweisstück. Gemessen: Helligkeit 0,15, Kontrast 0,20, Farbigkeit 0,07.
- **Schnitt:** 12 harte Schnitte in 112 s, Median 6,8 s, Shots von 1,3 bis 21 s; im Mittelteil (Versuch) schneller (0,16 je s), am Schluss ruhig (0,05 je s). Grafik-Ereignisse oben und unten je rund 0,54 je Sekunde. Übergänge: harter Schnitt, Streifenversatz-Glitch beim Einschlag eines Stempels, Unschärfe-Einstieg beim Riesenwort.
- **Ton:** Klare Stimme, 2,85 Wörter je Sekunde, 20 Pausen über 0,4 s (vor jeder Pointe). Dichtes Bett nur 4 dB unter der Stimme, Geräusche auf jedem Grafik-Ereignis. Gemastert auf −13 LUFS.
- **Text:** Sechs Rollen. Untertitel-Pille (fette Grotesk Kleinschrift, 2,6 % hoch, y 75 %); Stempelkasten (fette Mono-Versalien gesperrt, 2,8 % hoch, Rand 0,3 %, gedreht −3 bis −6°, erst blass, dann hell auf das Wort); Etikett an Zeigelinie (Mono-Versalien 1,1 %, Punkt und Haarlinie); Kopfzeile oben links (Mono 1,3 %, gesperrt 0,2 em, Strich davor, Schlüsselwort in Cyan, tippt sich mit Block-Cursor); Karteikarte (Reiter mit Aktennummer, Name fett 5 %, Zeilen mit Haarlinien, schräger Stempel in Cyan-Umriss); Riesenwort in Kleinschrift mit Cyan-Punkt (13 % hoch, oben links oder mittig, als Pointe, höchstens dreimal je Stück). Wasserzeichen klein oben links (Mono 1 %).

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Glaskörper seitlich mit Lichtbahnen | 35 % | Motiv 55 bis 70 % hoch, rechts angeschnitten, Lichtbahnen leuchten Cyan, Etiketten an Zeigelinien | 5 bis 20 s |
| Glaskörper frontal | 20 % | Motiv mittig 50 % hoch, darüber Karteikarte oder zwei Vergleichskarten, Riesenwort oben | 5 bis 12 s |
| Versuchsraum in Augenhöhe | 10 % | gesichtslose Figur mittig 45 % hoch, kaltes Röhrenlicht, einige Gegenstände, Fluchtpunkt mittig | 1,3 bis 6 s |
| Draufsicht | 15 % | Versuchsraum als schräger Streifen von unten links nach oben rechts, Gegenstände mit Etiketten, Lichtspur, Zähler | 2 bis 13 s |
| Messbild mit Diagramm | 10 % | Kreisdiagramm 40 % der Breite oben, Glaskörper klein unten rechts, Fadenkreuz, Haken-Reihe | 5 bis 11 s |
| Schlussbild | 10 % | Versuchsraum, Gegenstände leuchten Cyan und erlöschen, zweizeilige Schlussfrage riesig mit Cyan-Fragezeichen | 3 bis 11 s |

## Dramaturgie
- **Hook (0 bis 5 s):** Zwei widersprechende Behauptungen als Stempelkästen (erst blass, leuchten auf ihr Wort auf), dann die Wende, dass beide stimmen; Streifenversatz-Glitch beim zweiten Stempel.
- **Fall (5 bis 25 %):** Akte schiebt ein, Zeilen tippen sich, Scanlinie läuft durch das Motiv.
- **Versuch (25 bis 45 %):** Draufsicht und Augenhöhe im Wechsel, Gegenstände mit Etiketten, ein Zähler, schnellste Schnitte.
- **Frage und Erklärung (45 bis 80 %):** Frage-Pille oben, Riesenwort als Pointe, Lichtbahnen zeichnen die Erklärung, Trefferbalken.
- **Wende auf den Zuschauer (80 bis 92 %):** Riesenwort mit Punkt, das den Zuschauer anspricht, Etiketten am Motiv.
- **Schluss (letzte 8 %):** Rückkehr in den Versuchsraum, Gegenstände leuchten auf und erlöschen, zweizeilige Frage, Stimme endet mit dem Bild.

## Schnittmuster
Bauplan für 30 s in Sekunden (Stimme gibt den Takt). Grafik-Ereignisse je Zeile in der Spalte Übergang. Wachsen dürfen Hook, Erklärung und Schluss; die Versuchs-Shots bleiben kurz (1,3 bis 3 s).

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0,0-4,6 | Glaskörper seitlich | Bild 0 mit zwei blassen Stempeln; Stempel 1 leuchtet auf sein Wort, Stempel 2 mit Streifenversatz | Stimme ab Bild 0, Glitch-Geräusch |
| 2 | 4,6-6,4 | Versuchsraum in Augenhöhe | harter Schnitt, Etikett an Zeigelinie | Stimme |
| 3 | 6,4-11,0 | Glaskörper frontal | hart; Karteikarte schiebt in 8 Bildern ein, zwei Zeilen tippen sich | Tippen leise |
| 4 | 11,0-12,8 | Draufsicht | hart; Kopfzeile tippt sich, Etiketten an Gegenständen | Whoosh |
| 5 | 12,8-14,1 | Versuchsraum in Augenhöhe | hart | Stimme |
| 6 | 14,1-16,4 | Draufsicht mit Lichtspur | hart; Zähler steht | Klick |
| 7 | 16,4-22,6 | Glaskörper seitlich, Push-in | hart; Frage-Pille oben, dann Riesenwort mit Punkt in 6 Bildern aus der Unschärfe | Pause 0,5 s vor dem Riesenwort |
| 8 | 22,6-26,0 | Glaskörper frontal | hart; zwei Etiketten an Zeigelinien | Stimme |
| 9 | 26,0-30,0 | Schlussbild Versuchsraum | hart; Gegenstände leuchten Cyan, erlöschen; Frage zweizeilig riesig | Stimme endet, Bett klingt aus |

## Rezept für einen Code-Motor
- **Grund:** Bild- oder Video-Material der Glaskörper (lokal erzeugt, siehe Material), darunter `#03050F`. Feiner Staub als `Partikel kind="dot"` (50 Punkte, 0,08 bis 0,18 %, `flicker` 0,4, Drift 0,3 % je s). Optional ein senkrechtes Haarlinien-Raster alle 8 % der Breite in `#FFFFFF` bei 3 % Deckung.
- **Bildbehandlung:** Material leicht kühlen (`Look mode="cold"`, `amount` 0,3), Schwarzwert halten. Glühen der Lichtbahnen ist im Material; Cyan-Elemente der Grafik bekommen einen weichen Schein (Kopie, Unschärfe 0,6 % der Höhe, Modus `screen`, 50 %). Kein Korn über 4 %.
- **Bausteine:**
  - Untertitel: `WortSpur` (Modus `haeppchen`, `proHaeppchen={3}`, `aktivArt="kasten"`, `aktivFarbe="#4FB8F0"`, `kastenText="#06111A"`, `zukunft="gedimmt"`, `platte={{farbe: 'rgba(8,10,14,0.9)', rand: 'rgba(120,140,160,0.45)'}}`, `size={2.6}`, `y={75}`, `uppercase={false}`, Schrift Inter Tight 800).
  - Zeigelinien mit Etikett: `Hinweis` (`punkt` am Objekt, `etikett` 8 bis 15 % daneben, Mono 1,1 %, Linie 0,1 %, zeichnet sich in 6 Bildern, Etikett tippt sich mit 2 Zeichen je Bild).
  - Stempelkasten: `Schild` mit `plate` in der Grundfarbe (`#03050F`, dann prüft der Wächter den Kontrast), `borderColor` gleich der Schriftfarbe, `border={0.3}`, `shadow={0}`, `rotate={-4}`, Space Grotesk 700 in gesperrten Versalien, `size={2.8}`; vor dem Wort mit Deckung 0,22 im Bild, auf `von` des Wortes Deckung 1; der zweite Stempel kommt mit `Wischer direction="glitch"` über 5 Bilder.
  - Karteikarte (Rezept, kein Baustein): eine `Flaeche` mit Rechteck `#ECE8DF` (58 % der Breite, 15 % der Höhe, Ecken 0,4 %), Reiter oben links (12 % breit, 2 % hoch) mit Mono-Aktennummer 1 %, Symbolkasten 5 % mit Haarlinie, Kleinzeile Mono 1 %, Name fett 5 % in `#1A1C22`, darunter Zeilen mit Haarlinie 0,08 % in `#BDB7AA`, Werte rechts bündig; schiebt in 8 Bildern 4 % von links ein (`easing="out"`), Zeilen tippen sich nacheinander (Zeichen je Bild 2, Start je Zeile auf ihr Wort), ein schräger Stempel in Cyan-Umriss (−8°) schlägt mit `Stempel` ein.
  - Kopfzeile: Strich 1,6 % lang, dann Mono-Versalien 1,3 %, gesperrt 0,2 em, bei x 6 %, y 10 %; Text als `Titelkarte` mit `text={voll.slice(0, n)}` (n = 2 Zeichen je Bild ab dem Wort), dahinter ein Block-Cursor (0,9 × 1,4 %) in Cyan, der alle 15 Bilder blinkt und 1 s nach dem letzten Zeichen verschwindet; Schlüsselwort als eigener Teil in Cyan.
  - Zähler und Balken: `ZahlWalze` in Mono mit kleiner Mono-Überschrift; Trefferbalken als Rechteck in Cyan, das in 18 Bildern auf seinen Wert wächst, Marke für den Zufallswert als senkrechte Haarlinie; Haken in Cyan mit `Kritzel` (4 Bilder).
  - Scanlinie: eine Linie über die Breite des Motivs, 0,15 % hoch in Cyan mit Schein, wandert in 40 Bildern von oben nach unten, daneben ein Mono-Zähler mit laufender Schichtnummer (`ZahlWalze` ohne Rollen oder Text je Bild).
  - Riesenwort mit Punkt: `Titelkarte` in Kleinschrift (`uppercase={false}`, Inter Tight 800, 13 %, Laufweite −0,03 em, `#E8E6E3`) und ein Kreis in Cyan mit Durchmesser 0,26 × Schriftgröße auf der Grundlinie direkt hinter dem letzten Buchstaben; Einstieg in 6 Bildern aus 2 % Unschärfe auf 0.
- **Typografie:** Zwei Stimmen. Fette Grotesk (frei: Inter Tight 800) für Untertitel, Riesenwort und Kartennamen; für Stempel eine technische Grotesk (frei: Space Grotesk 700) und für Etiketten, Kopfzeilen und Aktenzeilen eine Mono (frei: JetBrains Mono oder IBM Plex Mono), beide in gesperrten Versalien. Alles in Weiß, Grau, Papier und Cyan.
- **Bewegung:** Kamera im Material ruhig (Push-in 2 bis 4 % über die Einstellung, kleiner Orbit). Grafik hart oder in 4 bis 8 Bildern; nie schwebende Grafik. Jedes Element startet auf `von` seines Wortes. Harte Schnitte auf Satzanfänge.
- **Formate:** Quelle 9:16. In 16:9 Glaskörper rechts zwei Drittel, Akten- und Messebene in der linken Spalte (x 6 bis 40 %), Untertitel-Pille mittig bei y 82 %, Riesenwort links neben dem Motiv.
- **Eigene Kennungen (jetzt im Vokabular):** `aktivwort`: In einem Untertitel-Häppchen ist das gerade gesprochene Wort farbig oder in einem Kasten hervorgehoben. `akten-karte`: Eine helle Karteikarte mit Reiter, Feldern und schrägem Stempel liegt als Beweisstück über einem dunklen Bild, ihre Zeilen tippen sich. `satzzeichen-punkt`: Ein Riesenwort in Kleinschrift endet auf einem Punkt oder Fragezeichen in der Akzentfarbe, das Satzzeichen wird zur Grafik.

## Material
- **Bilder (Glaskörper):** `translucent glass x-ray [body part, organ or device], visible glassy inner structure, cool blue fresnel edges, a few glowing white-cyan light pathways running through it, near-black navy background with tiny floating dust particles, clean 3D render, cinematic, no text`
- **Bilder (Versuchsraum):** `bare grey test room with cold fluorescent light, a few simple objects on the floor, a smooth faceless grey figure in the middle, desaturated blue-grey, cinematic 3D render, no text`
- **Video:** Glaskörper und Versuchsraum als Standbild erzeugen und lokal zu 4 bis 6 s Bewegung animieren (langsamer Orbit oder Push-in, keine Schnitte im Clip).
- **Musik:** `Dark minimal science documentary bed, 60 BPM, deep sub drone, soft pulsing synth, subtle ticking texture, short glitch accents, tension rising slowly to 20 seconds, short drop-out at 16 seconds, gentle resolve at the end, instrumental, no vocals`
- **Geräusche:** Glitch auf Streifenversatz, Tippen auf getippte Zeilen, Klick auf Etiketten und Haken, Whoosh auf harte Schnitte, tiefer Impuls auf das Riesenwort; 10 bis 14 dB unter der Stimme, aber hörbar.

## Regler
- Akzentfarbe: Cyan, Eisgrün oder Bernstein, immer genau eine.
- Dichte der Ermittlungsebene: von nur Pille und Etiketten bis zur vollen Akte mit Zähler und Diagramm.
- Motiv: Glaskörper (Medizin, Technik, Gegenstände) oder Draufsicht-Szenen; Papier bleibt die einzige helle Fläche.
- Riesenwort: 0 bis 3 je Stück.
- Länge der Einstellungen 1,3 bis 20 s; mindestens ein Abschnitt mit schnelleren Schnitten.

## Abnahme
- `python -I starter/werkzeuge/abnahme.py <render.mp4> stilbibliothek/karten/glasroentgen-akte.md`.
- Standbild an drei Stellen: Cyan ist die einzige bunte Farbe, die Pille sitzt über den unteren 15 %, ein Element der Ermittlungsebene ist sichtbar.
- 12-fps-Streifen über 10 s: 4 bis 8 Grafik-Ereignisse, keine Grafik, die schwebt oder langsam einblendet.
- Whisper gegen Pille und Stempel: Aktivwort-Kasten und Aufleuchten innerhalb von zwei Bildern zur Silbe.

## Fallen
- Zweite Signalfarbe (Rot für Gefahr) → der Blick weiß nicht mehr, was zählt. Gefahr über Helligkeit oder Cyan-Puls zeigen.
- Pille unten bei 85 bis 90 % → verschwindet unter den Plattform-Knöpfen. Zeilenmitte bei 75 %, Unterkante über 85 %.
- Kommende Wörter weiß statt grau → das Aktivwort springt nicht heraus. Zukunft auf 45 % Helligkeit.
- Mono-Etiketten unter 1 % der Höhe → am Handy unlesbar. 1,1 % ist das Minimum, Laufweite 0,15 em hilft.
- Grafik erscheint ohne Wort → wirkt dekorativ. Jedes Element bekommt ein Wort aus der Transkription als Start.
- Karteikarte zu groß (über 60 % der Breite) → verdeckt den Glaskörper. 55 bis 60 % und an den Rand, Kopf bleibt sichtbar.
- Glas-Material mit Gesicht und Augen in Großaufnahme → wird unheimlich. Glasköpfe ohne Gesichtsdetails, Puppen ohne Gesicht.
- Studiennamen, Jahreszahlen und Zahlen in Akten wirken wie Belege → jede Zahl und jeder Name braucht eine echte Quelle.
- Riesenwort häufiger als dreimal → die Pointe nutzt sich ab.
- Runde Gefäßöffnungen in generierten Organen lesen sich als Auge (Befund im Testbau). Material vor dem Einbau ansehen, Varianten ohne runde dunkle Öffnung nehmen.
- Generierte Glas-Torsi zeigen schnell nackte Brust und Gesichter → für Plattformen heikel. Organ allein zeigen.
- Nahbild mit angehobenem Schwarzwert (milchig, Rand grau) → bricht die Dunkelwelt. Schwarzpunkt setzen, Rand fast schwarz.
- Herauszoomen unter 1,0 legt einen schwarzen Rand frei. Zoom nie unter 1.
- Schlussbild ohne Bewegung → Standbild. Herz schlägt mit (2 % Puls im EKG-Takt), EKG-Linie mindestens 0,35 % der Höhe dick mit Schein.
- Kopfzeile aus zwei Teilen in einem Flex-Container verliert das Leerzeichen vor dem Schlüsselwort. `white-space: pre`.
