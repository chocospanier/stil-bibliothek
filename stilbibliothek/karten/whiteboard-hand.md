---
id: whiteboard-hand
name: Whiteboard mit zeichnender Hand
familie: erklaerstimme
kurz: Eine Hand mit schwarzem Marker schreibt und zeichnet Strich für Strich auf eine große weiße Tafel, die Kamera fährt mit der Erklärung von Gruppe zu Gruppe und zieht am Schluss zurück, bis die ganze Tafel als Landkarte des Gedankens zu sehen ist.
kern: [Hand mit Marker im Bild zeichnet jeden Strich und schreibt jedes Wort sichtbar mit der Stiftspitze am Strichende, eine große Tafel mit Kamerafahrten zwischen den Gruppen und Gesamtansicht am Schluss, schwarze Tinte auf Weiß mit genau einem Akzent für Schlagwörter und Flächen]
energie: 2
format_quelle: "9:16"
laenge_s: [15, 90]
bauweg: animskill
animskill:
  motor: handzeichnung
  stil: "whiteboard"
  quelle: "starter/src/beispiele/WhiteboardHand.tsx"
  schrift: [hand, grotesk]
lizenz: "Komposition und Hand eigene Umsetzung des Pakets; Handschrift Caveat SIL OFL 1.1 (OFL.txt im Starter); Szenen-Idee nach HandDraw-Skill, MIT"
sollwerte:        # Zielwerte für den eigenen Render (Probe 06.11.2026 und Routinetest 1.5)
  shot_median_s: 25
  schnitte_pro_s: 0.0
  ereignisse_pro_s: 1.4
  lufs: -14
  helligkeit: 0.95
  farbigkeit: 0.062
messung:
  shot_median_s: 25.0          # eine einzige Einstellung, die Kamera fährt nur
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm: 100                      # Bett aus Code, liegt leise unter der Stimme
  schnitt_auf_beat: niedrig
  lufs: -14.0
  helligkeit: 0.95
  kontrast: 0.12
  farbigkeit: 0.062
  ereignisse_pro_s: 1.4         # neuer Strich, Buchstabe oder Kamerafahrt (Probe 06.11.2026: 34 Elemente in 25 s)
  woerter_pro_s: 1.8
schnittmuster_16tel: [400]
palette:
  grund: "#FBFBFB"
  tinte: "#0A0503"
  akzent: "#EF7226"
  flaeche: "#F4B08A"
  haut: "#F2CBAA"
  aermel: "#DCE5F0"
effekte: [handschrift, strich-fuer-strich, push-in, sprechstimme, untertitel, aktivwort, diagramm-wachstum, neu:zeichnende-hand, neu:tafel-gesamtansicht]
kamera: Eine durchgehende Einstellung über einer großen Tafel; weiche Fahrten (0,7 bis 1,2 s, sinus) von Gruppe zu Gruppe, für weite Sprünge ein Schwenk mit Bewegungsunschärfe (0,8 s), am Schluss Rückzug auf die ganze Tafel.
ton: Ruhige Erzählstimme trägt, Marker kratzt hörbar auf jedem Strich, leises Musikbett aus Code (allein um −24 LUFS) mit Atem vor der Pointe, heller Glockenton beim Rückzug am Schluss.
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, hook, intro]
zweck: [erklaeren, wissen, kinder]
branchen_passt: [bildung, kinder-familie, gesundheit, finanzen, technik, handwerk]
branchen_nie: [mode-beauty, musik-kultur]
abnahme:
  shot_median_s: [8, 120]
  schnitte_pro_s: [0.0, 0.12]
  helligkeit: [0.86, 0.98]
  farbigkeit: [0.02, 0.14]
  lufs: [-15, -13]
creator: ja
spielraum:
  palette: akzent
  schrift: fest
  blitzbild_bilder: [0, 0]
  stottern_wiederholungen: [0, 0]
  push_in_prozent: [2, 4]
  wackeln_faktor: [0, 0]
  korn: [0.0, 0.04]
  vignette: [0.0, 0.2]
  beat_versatz_16tel: [0, 0]
  textgroesse_prozent: [-8, 8]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: tinte
  akzent: akzent
  dunkel: tinte
  hell: grund
  licht: grund
quelle: Eigene Beschreibung nach der Whiteboard-Grammatik (RSA-Typ, offene Erklär-Grammatik, MIT) und der Probe vom 06.11.2026; keine Motive, Texte oder Marken übernommen.
---

# Whiteboard mit zeichnender Hand

Das klassische Erklärvideo, bei dem man der Hand beim Denken zusieht: Jemand sagt einen Satz, und die Hand schreibt ihn mit oder zeichnet das Bild dazu. Die Energie kommt nicht aus Schnitten (es gibt keinen), sondern daraus, dass ständig ein Strich entsteht und die Kamera der Erklärung über die Tafel folgt. Am Ende sieht man die ganze Tafel als eine Landkarte des Gedankens.

## Kern
- **Die Hand zeichnet sichtbar.** Jeder Strich und jedes Wort entsteht an der Stiftspitze, die Hand tritt von rechts unten ein und geht wieder, wenn nichts zu zeichnen ist. Ohne Hand ist es eine Animation, kein Whiteboard.
- **Eine große Tafel, eine Kamera.** Gruppen liegen nebeneinander auf derselben Tafel; die Kamera fährt dorthin, wo der nächste Gedanke steht, und zeigt am Schluss alles. Kein Seitenwechsel, kein harter Schnitt zu leerem Papier.
- **Schwarz und ein Akzent.** Tinte fast schwarz, ein einziger Akzent (Standard Orange) nur für Schlagwörter, Zahlen und helle Schraffur; rund ein Fünftel der Striche.

## Erkennung
- **Bild:** Fast weiße Tafel (#FBFBFB) mit leichtem Korn, Glanzfleck oben links und blassen alten Wischspuren, Marker rund 0,6 % der Bildhöhe stark, Handschrift (Caveat, OFL) ohne Kontur, Akzentflächen als helle Füllung oder Schraffur. Echte Hand (Foto) oder Cartoon-Hand freigestellt, Stift zwischen Daumen und Zeigefinger, Spitze links, Arm im Hemdärmel läuft nach rechts unten aus dem Bild; weicher Schatten nach rechts unten, gleiche Größe im ganzen Stück.
- **Schnitt:** Keine Schnitte. Kamerafahrten zwischen Gruppen etwa alle 3 bis 5 s im Kurzvideo (alle 6 bis 7 s im langen Stück), Schwenk mit Unschärfe für weite Sprünge.
- **Ton:** Erzählstimme, ruhig, rund 2 Wörter je Sekunde; Markerkratzen auf jedem Strich, leises Wischen bei Fahrten; Musik leise oder gar keine; heller Glockenton beim Rückzug.
- **Text:** Wenig schreiben, viel zeichnen: höchstens eine Zeile Handschrift je Satz, Schlagwörter in Akzent, Zahlen groß. Untertitel unten in einer hellen Pille, Aktivwort im Akzent.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Frage als Handschrift mit einem kleinen Symbol | 15 % | drei Zeilen à 6 % der Bildhöhe, Symbol darunter, Mitte | 3 bis 4 s |
| Skizze mit Beschriftung (Ort, Gerät, Ablauf) | 45 % | Titel oben, Zeichnung 35 bis 45 % der Höhe, Beschriftung daneben | 4 bis 5 s |
| Rechnung oder Gleichung in Handschrift | 20 % | Zeilen untereinander, Ergebniszeile im Akzent | 3 bis 4 s |
| Pointe groß, unterstrichen | 10 % | eine Zeile bildfüllend breit (über 80 % der Bildbreite) | 2,3 s und mehr |
| Gesamtansicht der Tafel | 10 % | alle Gruppen, leicht grau getönt | 0,6 bis 3 s |

## Dramaturgie
Hook als geschriebene Frage (0 bis 3,5 s, Bild 0 zeigt die Frage fertig), dann je Gedanke eine Gruppe (3 bis 5 s), Atem vor der Pointe (Musik 0,8 s stumm), Pointe groß und unterstrichen, dann Rückzug auf die ganze Tafel mit Glocke.

## Schnittmuster
Kein Schnittraster; der Takt kommt aus den Wortanfängen der Stimme. Bauplan für 25 s:

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| Hook (wächst) | 0 bis 3,5 | Frage als Handschrift | Bild 0 = fertige Frage | Stimme, Marker |
| Gruppe 1 | 3,5 bis 8 | Skizze | Fahrt 0,7 bis 1,2 s | Wischen |
| Gruppe 2 | 8 bis 13 | Skizze | Fahrt | Wischen |
| Gruppe 3 | 13 bis 16 | Rechnung | Schwenk 0,8 s mit Unschärfe | Wischen |
| Gruppe 4 | 16 bis 20 | Rechnung | Fahrt | Marker |
| Atem | 0,8 s | steht | keiner | Musik stumm |
| Pointe (wächst) | 20 bis 23,4 | Pointe groß | Fahrt heran | Stimme |
| Schluss (wächst) | 23,4 bis Ende | Gesamtansicht | Rückzug 1,1 s | Glocke hell |

## Rezept für einen Code-Motor
Fertig im Starter: Komposition `WhiteboardHand` (9:16) und `WhiteboardHand-16x9`, Inhalt komplett über Props, Beispiel `starter/beispiele/whiteboard-hand/props.json`. Zeichen-Motor dazu: `handzeichnung` (`starter/werkzeuge/animskills/motoren/handzeichnung.py`, Bestellung über `animskill.py`).
- **Grund:** Fläche #FBFBFB, Korn aus Code (0,5), Glanzfleck oben links, Wischspuren auf der Tafel (bewegen sich mit der Kamera).
- **Bildbehandlung:** Striche als SVG-Pfade mit leichtem Zittern quer zur Linie (niederfrequent), runde Enden; gestrichelt für Strahlen und Pläne, gepunktet für Hilfslinien.
- **Bausteine:** Elemente `text`, `zahl`, `pfad`, `linie`, `pfeil`, `kreis`, `bogen`, `rechteck`, `punkt`, `symbol` (22 Symbole), `schraffur` (auch `voll`), `unterstrich`, Start mit `ab_wort` (0,3 s nach dem Wort) oder nach dem vorigen; `mitsprechen` legt jedes Wort eines Textes auf sein gesprochenes Wort.
- **Typografie:** Handschrift Caveat SemiBold (OFL) aus Glyphen-Umrissen, Buchstabe für Buchstabe über eine Maske entlang der Kontur aufgedeckt; Text 100 bis 150 Tafelpunkte, Fließtext 13 Zeichen je Sekunde, Titel 8.
- **Bewegung:** Hand folgt der Stiftspitze, gleitet zwischen nahen Strichen im Bogen, verlässt das Bild nach rechts unten bei Pausen über 0,45 s, kommt 0,32 s vor dem nächsten Strich wieder. Kamera aus den Rahmen der Gruppen gerechnet (nie von Hand), langsames Hineinschieben um 3,5 % je Halt.
- **Formate:** 9:16 und 16:9 aus denselben Props; die Kamera passt jeden Rahmen ins Bildfeld des Formats (unten Platz für Untertitel).

## Material
- **Bilder:** keine; alles aus Code.
- **Musik:** "light acoustic explainer bed, 100 BPM, celesta, pizzicato strings, soft ticks, major key, steady and unobtrusive, short pause before the final line, bright bell at the end, instrumental, no vocals"; aus Code: Partitur der Stimmung `hell` des Musikmotors.
- **Geräusche:** Marker auf der Tafel je Strich, Kratzen beim Schreiben, leises Wischen bei Fahrten, Glocke beim Rückzug; aus dem Motor (`geraeusche`), um −20 LUFS.

## Regler
Akzentfarbe, Hand echt (Foto) oder cartoon (gezeichnet), Hand links oder rechts, Handgröße (fest im ganzen Stück), Tempo für Text und Linien, Korn, Glanz, Wischspuren, Fahrt, Schwenk oder Schnitt je Gruppe, Haltezeit vor jeder Fahrt (`stehen`), Gesamtansicht an oder aus.

## Ton
Der Motor liefert Geräusche aus Code (Marker, Kratzen, Wischen, Glocke beim Rückzug) als ungemasterten Stem; Musik aus Code holt die Bestellung von einem anderen Motor (`"musik": {"weg": "code", "motor": "huashu"}`, Stimmung hell). Bett allein um −24 LUFS, Atem vor der Pointe über `ton_standard.atem`, Gesamt −14 LUFS, True Peak −1 dBTP, Schluss hell. Jedes Stück mit Text bekommt eine Stimme.

## Bauweg
Zeichen-Motor `handzeichnung` (Remotion-Komposition `WhiteboardHand` im Starter). `wuerfeln.py zug` schreibt `bauweg: animskill` und `motor_spec_entwurf` in `stil.json`; die Palette des Zugs geht nach `farben` in `whiteboard/szenen.json`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor handzeichnung --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

Szenen-Datei nach `starter/beispiele/whiteboard-hand/props.json`; Felder je Element in `starter/src/beispiele/whiteboard/plan.ts`. Vor dem Render die Warnungen des Zeitplans lesen (`--nur look` gibt sie aus).

```json
{"szenen": "whiteboard/szenen.json"}
```

## Abnahme
Zielwerte aus `abnahme`. Dazu am Standbild: Hand mit fünf Fingern, Stiftspitze sitzt am Strichende; jede Zahl steht mindestens 1 s fertig, bevor die Kamera fährt; keine angeschnittene Schrift am oberen Rand eines Halts; Pointe über 80 % der Bildbreite und mindestens 2,3 s groß; Bild 0 zeigt die fertige Frage.

## Fallen
- Eine gezeichnete Hand mit falschem Griff (Stift waagerecht aus der Zeigefingerspitze, Faust, starrer Arm) macht das ganze Stück kaputt; seit 06.11.2026 kommt die Hand als Bild (`hand.stil` echt oder cartoon), Ankerpunkt Filzspitze, fester Maßstab, nie an die Kamera gekoppelt.
- Die Kamera fährt los, während die letzte Zahl noch entsteht: `stehen` an der nächsten Szene (Standard 0,4 s, für Zahlen 0,9 s). Gefunden in der Probe vom 06.11.2026.
- Beschriftung der vorigen Gruppe steht direkt über der nächsten und liest sich als deren Überschrift: Trennlinie zeichnen oder den Rahmen der neuen Gruppe so setzen, dass die alte Zeile ganz draußen ist (`rahmen`), nie halb.
- Eine Rechnung, deren Zwischenschritt fehlt, sieht falsch aus (5.000 × 50 über 40.000): jeden Schritt an die Tafel, auch wenn die Stimme ihn auslässt.
- Ein Stab mit Spitze liest sich als Pfeil oder Antenne, ein gefülltes Dreieck am Stab als Leitkegel: Schatten nur als Bodenlinie im Akzent.
- Überzeichnete Winkel (für das Handy) beschriften, die wahre Größe steht als Zahl; im Schaubild mit dem Kreis den echten Winkel zeichnen, sonst passt der Keil nicht zur Zahl daneben.
- Schrift unter 90 Tafelpunkten wird am Handy in der Gesamtansicht unlesbar; die Pointe deshalb mit eigenem engem `rahmen` heranholen, bevor die Kamera zurückzieht.
- Die Hand verdeckt rechts unten: Wichtiges nicht in die rechte untere Ecke eines Rahmens legen, Zahlen links neben die Zeichnung.
- Zu viele Elemente mit Hand: die Hand hinkt der Stimme sekundenlang hinterher (im Routinetest 5,7 s, Zeichnen endete nach der Dauer). `--nur look` zeigt das nicht; die Warnungen stehen nur im Zeitplan (`handzeichnung.zeitplan`). Nebensachen mit `hand: false`, `tempo.text` 18, `stehen` 0,3 (Routinetest 1.5).
- Der Würfel kann einen hellen Akzent ziehen (im Test #9ED7FD, 1,5:1 auf Weiß); Zahlen und Schlagwörter dann in Tinte, der Akzent nur für Flächen, Kreise und Linien.
- Schraffur über der Pointe-Zahl zerschneidet die Ziffern: Fläche nie über die Zahl legen (Prüferbefund).
- Kurven in Schaubildern nach der Rechnung setzen, nicht frei Hand: eine Zinseszinskurve unter der Geraden des einfachen Zinses ist sachlich falsch (Prüferbefund).
