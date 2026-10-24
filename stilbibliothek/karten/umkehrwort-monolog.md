---
id: umkehrwort-monolog
name: Umkehrwort-Monolog
familie: kinetik-typo
kurz: Eine schnelle Stimme spricht einen Gedanken, und genau das gesprochene Wort steht riesig in Versalien in der Bildmitte, eins nach dem anderen hart getauscht, in der Umkehrfarbe des Bildes darunter, über einer sehr bunten, flachen Trickwelt, die alle drei Sekunden auf einem Wortanfang wechselt.
kern: [jedes gesprochene Wort einzeln groß in der Mitte und hart getauscht ohne Animation, weiße Schrift im Differenzmodus nimmt die Gegenfarbe des Bildes an, harte Szenenwechsel auf Wortanfängen alle 2 bis 5 s über gesättigter flacher Trickwelt]
energie: 3
format_quelle: "16:9"
laenge_s: [20, 70]
messung:
  shot_median_s: 3.17
  schnitte_pro_s: 0.25
  schnitte_verlauf: [0.30, 0.17, 0.26]
  bpm: 167                  # aus den Sprechsilben, das Bett hat keinen Puls; Schnitte folgen den Wörtern
  schnitt_auf_beat: niedrig
  lufs: -16.3
  helligkeit: 0.32
  kontrast: 0.21
  farbigkeit: 0.38
  woerter_pro_s: 4.0
  schnitt_auf_wortanfang: 0.94   # Anteil der Schnitte höchstens 0,1 s neben einem Wortanfang
schnittmuster_16tel: [15, 35, 25, 24, 35, 53, 20, 92, 24, 55, 57, 78, 26, 28, 30, 48, 69, 55]   # bei 167 BPM, nur Umrechnung der Sekunden
palette:
  nachtviolett: "#1F1951"
  indigo: "#2D1E72"
  magenta: "#9D04A4"
  sattgruen: "#18C751"
  tuerkis: "#2DD8D9"
  orange: "#E28627"
  rot: "#B51B30"
  tiefnacht: "#040023"
  text: "#FFFFFF"            # weiß im Mischmodus Differenz, sichtbar ist die Gegenfarbe
effekte: [sprechstimme, wort-schnitt, harter-schnitt, differenz-schrift, farbwelt-je-shot, push-in, geringe-schaerfentiefe, neu:wort-zur-zeit, neu:vektor-trickwelt]
kamera: Je Szene entweder stehend oder eine langsame Fahrt hinein oder heraus um 3 bis 8 % mit leichtem Versatz, nie ein Schwenk oder Wackeln, damit das Wort in der Mitte ruhig liegt.
ton: Eine schnelle Sprechstimme in Ich-Form von Bild 0 bis kurz vor Schluss, rund 4 Wörter je Sekunde, darunter ein tiefes, pulsloses Musikbett rund 9 dB leiser, keine Geräusche.
braucht: [illustrationen, nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, hook, intro]
abnahme:
  shot_median_s: [2.5, 4.5]
  schnitte_pro_s: [0.18, 0.4]
  helligkeit: [0.25, 0.42]
  farbigkeit: [0.30, 0.50]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Umkehrwort-Monolog

Ein Gedanke, gesprochen und gleichzeitig Wort für Wort riesig gezeigt. Das Auge muss mitlesen und kann nicht weg; die Farbe jedes Wortes kommt aus dem Bild darunter, dadurch gehören Schrift und Bild zusammen, ohne Kasten und ohne Gestaltungsaufwand. Die Energie kommt aus dem Wortwechsel (vier je Sekunde), die Ruhe aus den langen, bunten Szenen darunter.

## Kern
- **Ein Wort zur Zeit, hart.** Jedes gesprochene Wort erscheint allein, in derselben Größe, an derselben Stelle, und springt beim nächsten Wort ohne Zwischenbild weg. Kein Pop, keine Blende, kein Zoom: bei vier Wörtern je Sekunde wäre jede Animation Flimmern. Wer Wörter auslässt oder zu Häppchen bündelt, landet bei Untertiteln.
- **Umkehrfarbe.** Weiße Schrift im Mischmodus Differenz zeigt in jedem Buchstaben die Gegenfarbe des Bildes (Grün auf Magenta, Blau auf Orange, Hellgelb auf Nachtviolett), oft mehrere Farben in einem Wort. Eine feste Schriftfarbe macht daraus ein gewöhnliches Wort-Video.
- **Szene je Satz, Schnitt auf Wortanfang.** Harte Schnitte zwischen flachen, sehr bunten Trickwelt-Szenen, je eine Farbwelt, alle 2 bis 5 s, immer genau mit einem gesprochenen Wort, oft mit einem neuen Satz. So wirkt jeder Schnitt wie ein neuer Gedanke.

## Erkennung
- **Bild:** Flache Vektor-Trickwelt mit satten Farben (Sättigung im Mittel 0,74), weichen Verläufen, sauberen Formen, gelegentlich unscharfem Hintergrund und kleinen Glanzsternen. Mittel hell (0,32), wenig Schwarz (24 %). Jede Szene hat eine eigene Grundfarbe: Nachtviolett und Indigo, Magenta mit Pastellgelb, Nachtblau mit Sattgrün, Orange mit Türkis, Tiefnacht mit Magenta.
- **Schnitt:** 0,25 Schnitte je Sekunde, Median 3,2 s, keine Szene unter 1,3 s, längste 8,3 s; dichter am Anfang und am Ende, ruhiger in der Mitte (0,30 / 0,17 / 0,26). Nur harte Schnitte. 94 % der Schnitte liegen höchstens 0,1 s neben einem Wortanfang, rund die Hälfte auf einem Satzanfang.
- **Ton:** Eine Stimme trägt alles, schnell und dicht (4 Wörter je Sekunde, kaum Pausen über 0,25 s). Darunter ein pulsloses Bett mit tiefem Grundton rund 9 dB leiser. Kein Abbinder, die Stimme endet kurz vor dem letzten Bild. Vorlage −16,3 LUFS mit True Peak an der Grenze; eigene Stücke auf −14 LUFS, True Peak höchstens −1 dBTP.
- **Text:** Eine Rolle: das gesprochene Wort. Versalien in einer schweren, runden Grotesk, Versalhöhe 13,6 % der Bildhöhe in 16:9, Mitte des Wortes genau in der Bildmitte, Breite nach Wortlänge (30 bis 75 % der Bildbreite). Keine Kontur, kein Schatten, kein Kasten.

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Innenraum mit Figur, flach und farbig (Draufsicht oder Bühne von vorn) | 35 % | Figur 30 bis 60 %, leicht neben der Mitte, damit das Wort auf ruhiger Fläche liegt; Raum in einer Grundfarbe | 2 bis 6 s |
| Weite Landschaft in Sattfarben (Wasser, Wald, Himmel) | 25 % | Horizont im unteren Drittel oder Blattwerk über das ganze Bild, langsame Fahrt | 4 bis 8 s |
| Einzelnes Objekt auf dunklem Grund (isometrisch oder frontal) | 15 % | Objekt 50 bis 70 % mittig, Grund dunkel, das Wort liegt quer über dem Objekt | 3 bis 7 s |
| Nachtszene mit Sternen und kleinem Licht | 15 % | Figuren klein im unteren Drittel, Mitte dunkel, Wort am besten lesbar | 4 bis 7 s |
| Weichgezeichnete Szene in rundem Rahmen auf Schwarz | 10 % | Rahmen 80 % der Höhe, Inhalt unscharf und warm, Glanzsterne | 3 bis 5 s |

## Dramaturgie
0 bis 1 s Hook: Stimme und Wort laufen ab Bild 0, gerne mitten im Satz; das erste Wort steht schon, bevor man scrollen kann. 1 bis 20 s Aufbau: kurze Szenen (2 bis 3 s), Alltagsbilder, dicht geschnitten. Mitte: längere Szenen (5 bis 8 s), weite Landschaften, der Gedanke wird größer. Letztes Drittel: wieder dichter, Rückkehr zu einem Innenraum. Schluss: eine ruhige Nachtszene mit kleinem Licht, die Stimme endet 0,3 bis 0,5 s vor dem letzten Bild, keine Abblende. Der Neustart wirkt wie Weitersprechen.

## Schnittmuster
Bauplan für ein eigenes Stück von 20 s ohne Beat, in Sekunden. Jeder Schnitt wird auf den nächsten Wortanfang gerastet, bevorzugt auf einen Satzanfang.

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0,0 bis 2,5 | Innenraum mit Figur | harter Schnitt auf Wortanfang | Stimme ab Bild 0, Bett ab Bild 0 |
| 2 | 2,5 bis 5,0 | Einzelnes Objekt auf dunklem Grund | harter Schnitt auf Satzanfang | Stimme |
| 3 | 5,0 bis 8,5 | Innenraum mit Figur, andere Grundfarbe | harter Schnitt auf Wortanfang | Stimme |
| 4 | 8,5 bis 14,0 | Weite Landschaft, langsamer Push-in | harter Schnitt auf Satzanfang | Stimme, Bett etwas voller |
| 5 | 14,0 bis 20,0 | Nachtszene mit kleinem Licht, Mitte dunkel | Ende ohne Abblende | letztes Wort 0,4 s vor Schluss, Bett klingt bis zum letzten Bild |

## Rezept für einen Code-Motor
- **Grund:** Folge von Standbildern oder Clips je Szene, harte Schnitte. Schnittbilder aus den Wortzeiten berechnen: geplanten Schnitt auf den nächstgelegenen Wortanfang ziehen, bei Abstand unter 0,6 s den Satzanfang bevorzugen.
- **Bildbehandlung:** keine Filter. Wo der Videomotor nichts liefert, je Szene eine Fahrt über das Standbild (Skalierung 1,00 auf 1,05 bis 1,08 oder umgekehrt, Easing linear oder sehr weich, dazu 1 bis 2 % Versatz). Hintergrund darf unscharf sein; das Motiv bleibt scharf.
- **Bausteine:** Wort-Ebene über allem (ein Wort zur Zeit, Differenzmodus), Szenenfolge darunter, Tonspur aus Stimme und Bett. Das Wort liegt in derselben Ebenengruppe direkt über dem Bild, ohne Filter oder isolation auf den Elternebenen, sonst mischt die Differenz nicht. Im Starter fertig als Komposition `UmkehrwortMonolog` (Props von außen); vom Zitat bis zum geprüften Stück in einem Rutsch mit `starter/werkzeuge/zitat.py` (ABLAUF.md, „Zitat in einem Rutsch“), samt Lesbarkeitsprüfung des Grundes unter jedem Wort.
- **Typografie:** schwere, runde Grotesk in Versalien (frei lizenziert: Rubik ExtraBold 800), Laufweite 0 bis +1 %. 16:9: Schriftgröße rund 19 % der Bildhöhe (Versalhöhe 13 bis 14 %). 9:16: Schriftgröße 9 bis 11 % der Bildhöhe, lange Wörter auf 86 % der Breite verkleinern statt umbrechen. Wortmitte bei 50 % Höhe (9:16 auch 45 %). Weiß `#FFFFFF`, Mischmodus Differenz.
- **Bewegung:** Wort hart, ohne Ein- und Ausblendung, sichtbar vom Wortanfang bis zum nächsten Wortanfang; in Pausen über 1,5 s darf es verschwinden. Das Wort springt 0 bis 0,1 s nach dem Wortanfang aus der Transkription, nie davor (ein Wort vor der Silbe wirkt vorgelesen). Kamera nur als langsame Fahrt.
- **Formate:** 16:9 wie die Vorlage. 9:16 nativ: Szenenbilder hochkant komponieren, Motive ins obere und untere Drittel, die Bildmitte als ruhige dunkle oder sehr helle Fläche für das Wort.
- **Neue Kennungen:** `neu:wort-zur-zeit`: Jedes gesprochene Wort steht allein und groß in der Bildmitte und wird beim nächsten Wort hart ausgetauscht, ohne Animation und ohne Auslassen. `neu:vektor-trickwelt`: Flache, stark gesättigte Vektor-Trickfilmszenen mit weichen Verläufen, je Szene eine Grundfarbe.

## Material
- **Bilder:** „Flat vector animation still, [scene of the sentence], one dominant saturated colour world with a single warm light source, clean rounded shapes, soft gradients, the subject off-centre, a calm dark area in the centre of the frame, no text, no letters.“ · „Flat vector animation wide shot, [landscape of the sentence] in two saturated complementary colours, smooth shapes, slight background blur, the centre of the frame is a quiet very dark or very bright area, no text.“
- **Musik:** „Low, warm ambient piano and soft synth pad, no drums and no clear pulse, steady from the first second, slightly fuller from 8 to 14 seconds, continues to the last frame without a fade, 20 seconds, instrumental, no vocals.“ Unter der Stimme rund 9 dB leiser mischen.
- **Geräusche:** keine.

## Regler
Sprechtempo (2,5 bis 4,5 Wörter je Sekunde), Szenenlänge (2 bis 8 s), Trickwelt (Vektor, Papierschnitt, gemalt, auch Fotos, solange die Bildmitte hell oder dunkel ist), Schrift (runde Grotesk, schmale Versalien, ruhige Antiqua für edlere Marken), Füllwörter auslassen (aus für Bekenntnis, an für Erklärung), Bettlautstärke (6 bis 12 dB unter der Stimme). Fest bleibt: ein Wort zur Zeit, Differenzmodus, Wort in der Mitte, harte Schnitte auf Wörtern.

## Abnahme
Zielwerte aus `abnahme` mit `video_schauen.py` und `--whisper` messen; zusätzlich prüfen, dass mindestens 80 % der Schnitte höchstens 0,1 s neben einem Wortanfang liegen. Augen-Prüfungen: Steht in jedem Bild genau ein Wort, und ist es auf 390 px Breite lesbar? Liegt an jeder Stelle, wo das Wort steht, ein Grund mit Helligkeit unter 0,35 oder über 0,65 (mittlere Töne lassen die Differenz verschwinden)? Springt das Wort nie vor der Silbe? Wechselt die Szene auf einem Wort und nicht mitten in einer Silbe?

## Fallen
- Wort auf mittlerem Grund (Helligkeit 0,35 bis 0,65) → Gegenfarbe ist fast dieselbe, das Wort verschwindet. Bildmitte beim Bildprompt als ruhige dunkle oder sehr helle Fläche verlangen und am Standbild prüfen.
- Differenz mischt nicht, das Wort steht einfach weiß → Filter, Schatten oder isolation auf einer Elternebene. Wort direkt über dem Bild in derselben Gruppe.
- Wort springt vor der Silbe → Wortzeiten aus der echten Stimme, 0 bis 0,1 s nachziehen, nie schätzen.
- Wort-Animation (Pop, Zoom, Blende) → bei 4 Wörtern je Sekunde Flimmern. Hart tauschen.
- Schnitt mitten im Wort → wirkt wie ein Fehler. Schnitte auf Wortanfänge rasten.
- Bild illustriert Wort für Wort → wird zur Bilderrätsel-Folge. Eine Szene je Satz oder Gedanken.
- Monolog endet in Ausweglosigkeit, letzte Szene eine einsame Figur im Dunkel → kann als Abschied gelesen werden. Schluss mit Wende, Halt oder Frage, Licht im letzten Bild.
- True Peak bis an die Grenze, wie in der Vorlage → Hausnorm −14 LUFS, höchstens −1 dBTP.
- Videomotor zoomt trotz „locked-off“ weiter heran (ein Gegenstand in der Bildmitte wächst über die Szene auf das Doppelte) → Buchstaben werden vom Motiv angeschnitten. Gegenstände ins untere Drittel setzen und die Szene kürzer halten; die erlaubte Fahrt von 3 bis 8 % im Schnitt machen, nicht im Motor bestellen.
- Erstes Wort im Ton angeschnitten → Stimme am gemessenen Einsatz der Aufnahme schneiden, nie an der Zeichenzeit des Dienstes; sonst fehlt der Anlaut und jeder Neustart knackt.
- Schluss zu lang (mehrere Sekunden ohne Stimme hinter dem Namen) → letztes Wort 2,5 s halten, Name und Herkunft 2,8 s, dann Ende. Eine Herkunftszeile unter 0,45 der Wortgröße ist am Handy nicht lesbar.
- Ein schäumender, türkiser Bach in der Bildmitte liegt im Mittelton und lässt einzelne Buchstaben der Differenzschrift verschwinden (gemessen 20 bis 27 % schwache Pixel); Wasser in die Ränder, die Mitte als tiefen Schatten oder hellen Himmel.
