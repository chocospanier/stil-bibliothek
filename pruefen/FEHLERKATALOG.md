# Fehlerkatalog (Pflichtlektüre vor jedem Bau)

> Ausgewertet am 16.10.2026 aus 24 Prüfberichten über 26 gebaute Kurzvideos: **59 Blocker, 273 Polish-Punkte**, dazu ein Befund aus der Abnahme (Figur verzerrt) und die Pannen im Ablauf. Die Fehler waren nicht zufällig. Sie haben acht Ursachen, und jede hat ein Gegenmittel. Wer baut, hakt die Liste „Vor dem Rendern“ selbst ab; der `pruefer` prüft danach dieselben Punkte. Neue Fehlerarten kommen hier hinein, nicht nur in einzelne Karten.

## Die acht Ursachen

| # | Ursache | Anteil der Blocker | Typische Fälle |
|---:|---|---:|---|
| 1 | **Avatare wie Rohbilder behandelt** | rund 20 | Gesicht invertiert (4×), Figur gestreckt oder gestaucht (Befund aus der Abnahme), Figurentafel schräg zur 3D-Kamera, Glanzoval als zweiter Mund, halb geschlossene Augen als Sonnenbrille, Lider aus anderer Pose geliehen, gerade Schnittkante am Brustbild (3×), Ganzkörper kindlich (3×), Freisteller mit weißen Inseln, Filter macht Haut braun, Klone verdecken sich |
| 2 | **Generiertes Material ungeprüft eingebaut** | rund 10 | Seilschlinge neben einsamer Figur, Schuh in Chucks-Form, Telefon eines bekannten Herstellers, Pseudo-Schrift und Abzeichen auf Rennwagen, Haken mit Ring in der Mauer, falsches Fundstück, Flakon je Bühne ein anderes Produkt, Schuhsohle „kocht“ im Videomodell |
| 3 | **Ränder, Zwischenbilder, Schutzzonen** | rund 14 | Wort im Überschwinger abgeschnitten („ONTAG“, „IM HEM“), Zahl im Ruckzoom am Rand, dunkle Randstreifen durch Wackeln, Inhalt in den unteren 15 %, Wort über den Augen, Text überlappt Text, Bild 0 kein Titelbild |
| 4 | **Zeit und Ton** | rund 7 | Blitze über 3 je Sekunde (3×), Handy-Fassung übersteuert (2×), Bett läuft über den Schnitt, Pointe trägt stumm nicht |
| 5 | **Bedeutung der Abfolge nicht gelesen** | rund 7 | Jenseits-Lesart (schlaflos, Dach, Licht über den Wolken, „ankommen“), Fakten-Logik falsch, Buchstaben bilden „ARD“, Höhepunkt kippt nach unten |
| 6 | **Halt und Dauer** | in 3 und 5 enthalten | Schluss als Standbild 4 s (Regel „keine Freezes“), Pointe nur 1,3 s, Wort 0,27 s (Flackern), 2 s leerer Rahmen vor dem Treffer |
| 7 | **Geprüft wurde zu spät und zu grob** | Querschnitt | Prüfer sah den fertigen Render statt das Storyboard; Stichproben-Standbilder statt jedes Bild; Messung statt Handy-Blick |
| 8 | **Ablauf und Werkzeuge** | Pannen | lokale Bildmaschine hing 1,5 h unbemerkt (Videomodell zwischen Bildläufen), Notmaßnahme Software-Rendern 6-mal langsamer, falsches Datum in 60 Dateien, Helfer las fremdes Storyboard aus geteiltem Arbeitsordner, Windows-Zeilenenden in einer Auftragsliste |

## Gegenmittel je Ursache

**1. Avatar-Kanon (gilt für jede gezeichnete oder freigestellte Figur)**
- Nur verschieben, gleichmäßig skalieren (scaleX gleich scaleY), drehen höchstens leicht, Deckkraft. Nie strecken, stauchen, scheren, perspektivisch verzerren; in 3D steht jede Figurentafel parallel zur Kamera-Bildebene.
- Spiegeln (scaleX gleich minus scaleY) ist erlaubt, außer bei Figuren mit Schrift (Aufdruck, Abzeichen) oder asymmetrischen Merkmalen (Scheitel, Muttermal, Narbe, einseitiger Schmuck): dort sieht der Zuschauer sofort, dass etwas nicht stimmt.
- Nie invertieren, nie Schwelle oder Duoton über Haut, nie Farb- oder Helligkeitsfilter auf die Figur (Filter nur auf Gründe). Bewegungsunschärfe im Übergang bis 6 Bilder ist erlaubt (Wischer), auch über der Figur.
- Nichts aus anderen Posen hineinmontieren (Lider, Brauen). Änderungen nur innerhalb der Augen- oder Mundöffnung.
- Kein Glanz unter dem Mund, keine Glanzpunkte in geschlossenen Augen; Zwinkern = ein Auge offen mit Pupille, eins als Bogen.
- Brustbild endet nie mit sichtbarer Kante im Bild (Kante unter den Bildrand oder unter ein Band). Ganzkörper nicht kindlich: lieber Brustbild, von hinten oder in Bewegung.
- Neue Posen (aus einem Bildmodell) gegen das Original abgleichen: Wangen glatt, Bart nur Mund und Kinn, Kappe, Hemd, Hautton, Kopfgröße, Linienbreite.
- Kein Kopf so oben angeschnitten, dass er platt wirkt; Münder geschlossen, wenn aus dem Off gesprochen wird.

**2. Material-Abnahme vor dem Einbau**
- Jedes generierte Bild (Bildmodell, Videomodell, 3D-Render; zum Beispiel Z-Image, LTX) in voller Größe ansehen, bevor es ins Stück kommt. Suchen nach: Schlingen, Seilen, Haken, Waffen, Blut, Flaggen, Zeichen, Logos, markentypischen Formen (Schuhe, Telefone, Autos, Flakons), lesbarer oder Pseudo-Schrift, Gesichtern im Hintergrund.
- Prompts nennen keine Gerätearten, die Marken herbeirufen (statt „smartphone photo“ den Blickwinkel beschreiben; statt „canvas sneaker“ „plain smooth leather sneaker“), kein „hook“.
- Ein Produkt = ein Master-Packshot; alle Bühnen daraus freistellen und setzen, nicht je Bühne neu generieren.
- Videomodelle (zum Beispiel LTX): Formtreue früh prüfen; wabert ein Objekt, 3D oder Code statt Videomodell.

**3. Ränder und Schutzzonen über alle Bilder, nicht nur Standbilder**
- Jede Animation mit Überschwinger, Zoom, Ruckzoom oder Wackeln: Extremwerte durchrechnen; Schrift bleibt auch im extremsten Bild 40 px vom Rand. Wackeln braucht überskalierten Grund (1 + 2,2 × Amplitude / Breite).
- Unten 15 % frei von Schrift und Bedeutungsträgern (Knöpfe der Plattformen), auch für Kalender, Tabellen und Füße, wenn sie etwas zeigen sollen. Körper und Flächen dürfen unten auslaufen (ein Brustbild endet sogar unter dem Bildrand).
- Bild 0 ist das Titelbild: Endgröße, nichts angeschnitten, Hauptmotiv mindestens 30 % der Höhe.
- Wörter in Nahaufnahmen auf Nasen- oder Kinnhöhe, nie über den Augen; Text nie über Text oder hellen Weltflächen ohne Kontrast.

**4. Zeit und Ton**
- Höchstens 3 harte Hell-Dunkel-Wechsel je Sekunde (lineare Helligkeit, Farbblitze zählen mit).
- Die Handy-Fassung übernimmt den Ton des Masters unverändert (`-c:a copy`), nie neu kodieren; Master und Handy beide −14 LUFS, True Peak höchstens −1 dBTP.
- −14 LUFS ist der Standard; nennt die Karte einen Bereich, gilt die Karte, solange sie innerhalb −14 ± 1 bleibt. Ein Kartenbereich ganz außerhalb davon ist kein Ziel (in `INDEX.md` markiert).
- Pointe: Musik hart stoppen, echte Stille vor dem Satz (mindestens 0,4 s), Satz zusätzlich als Etikett im Bild.
- Bett endet am Schnitt, läuft nicht über ein stilles Bild weiter.

**5. Abfolge als Zuschauer lesen**
- Nach dem Storyboard die ganze Folge einmal als Geschichte lesen: Kann ein Mensch in einer schlechten Phase darin einen Abschied sehen? Kann man es als Politik, Gewalt, Marke lesen? Ergibt die Logik Sinn (Fakten-Kette)?
- Lichte Auflösungen brauchen Boden, Alltagsding und lesbare Zeit oder Ort.
- Gestreute Buchstaben dürfen keine Abkürzungen bilden.

**6. Halt und Dauer**
- Kein Standbild über 1 s (Regel „keine Freezes“): Halt lebt mit Heranfahren, Glanzlicht, Lidschlag. Die Vorprüfung meldet Gelb an Shots von knapp über 1 s mit langsamer Bewegung; bei ruhigen Grafikstilen (große Einfarbflächen, 1 bis 2 % Drift je Sekunde) ist das normal und kein Befund. Rot über 2 s ist ein echter Halt ohne Leben. Ruhige Fahrten auf dunklen, kontrastarmen Bildern misst die Vorprüfung zusätzlich per Phasenkorrelation (Zoom und Versatz) und meldet sie grün; bleibt an einer ruhigen Fahrt trotzdem Rot stehen, entscheidet der Prüfer mit den Augen (Streifen ansehen).
- Pointen und Pflichtzeilen mindestens 2,3 s vollständig lesbar; einzelne Wörter mindestens 0,5 s.
- Vor dem Treffer kein leerer oder weicher Rahmen; Höhepunkt wird heller und größer, nicht dunkler.

**7. Prüfen früher und am Handy**
- **Automatische Vorprüfung zuerst (seit 16.10.2026):** `python -I werkzeuge/vorpruefung.py <video.mp4> --handy <video_handy.mp4> --out <ordner>` misst jedes Bild in rund 10 Sekunden: dunkle Randstreifen, kurz angeschnittene Kanten am Rand (Hinweis auf Überschwinger), Blitze (Bildhelligkeit und WCAG), Standbilder über 1 s, Kanten in den unteren 15 %, Bild 0, Lautheit und True Peak von Master und Handy. Ergebnis `<name>_vorpruefung.json` mit Zeit und Ampel, ohne Gesamturteil. Geeicht an bekannten Fällen aus echten Prüfberichten: findet Randstreifen, Blitze und eine übersteuerte Handy-Fassung und meldet an den reparierten Stücken kein Rot. Rot = sehr wahrscheinlich Blocker, Gelb = ansehen. Avatare, Material, Lesart und Ton-Gefühl prüft weiter nur das Auge.
- **Seit Runde 4 des Werkzeugkastens** misst die Vorprüfung auch: Schrift abgeschnitten, überlappend oder unter 50 px bei 1080 Breite (aus dem Text-Protokoll des Renders), den Höhepunkt nach der Stille, das Sprechtempo, ob der Held an seinem Platz bleibt, und ob die Bausteinprobe nach einer Änderung noch gleich aussieht (`werkzeuge/framehash.py`).
- Reihenfolge: Material-Abnahme → Look-Check (zwei bis vier Standbilder) → Storyboard in voller Größe → Selbstprüfung mit dieser Liste → `pruefer` auf das Storyboard und die Streifen → erst dann Vollrender → `pruefer` kurz auf den Render.
- Jedes Prüfbild auch auf 390 px Breite ansehen (so sieht der Zuschauer es auf dem Handy).
- Messung ist kein Urteil: Auge und Ohr des Auftraggebers entscheiden; Ton hört nur ein Mensch.

**8. Ablauf**
- Lokale Bildmaschine: Videomodelle nur einzeln laufen lassen, vorher den Grafikspeicher leeren; ein Wächter meldet nach 10 min ohne Fortschritt. Viele Helfer gleichzeitig: GPU-Aufträge früh bündeln.
- Remotion normal mit GPU rendern; Software-Rendern (`--gl=swangle`) nur als Notmaßnahme.
- Zu Beginn jeder Session das echte Datum per `date` prüfen, nie aus dem Gefühl datieren.
- Geteilter Arbeitsordner: jede Hilfsdatei mit einem Präfix je Stück.
- Messbilder und Sperrdateien gehören nicht in einen Cloud-Ordner. `video_schauen.py` legt Videokopie, Taktbilder, Einzelbilder und WAV in einen Cache außerhalb (Umgebungsvariable `VIDEO_SCHAUEN_CACHE`), sobald der Messordner in einem Cloud-Spiegel liegt (Google Drive, OneDrive, Dropbox, iCloud); im Projekt bleiben nur Bericht, Bögen und Zahlen. Prüfbilder des Prüfers liegen im Projekt unter `pruef/`.

## Checkliste vor dem Rendern (Bauende hakt ab, in STAND.md eintragen)
- [ ] Jedes generierte Bild angesehen, nichts Heikles, keine Marke, keine Schrift
- [ ] Avatare nur verschoben, gleichmäßig skaliert und (ohne Schrift, ohne asymmetrische Merkmale) gespiegelt, nichts invertiert, nichts gefiltert, gegen Original verglichen
- [ ] Extremwerte aller Bewegungen: kein Wort am Rand, keine Randstreifen
- [ ] Unten 15 % frei von Schrift und Bedeutungsträgern, Bild 0 ist Titelbild
- [ ] Blitze höchstens 3 je Sekunde
- [ ] Kein Standbild über 1 s, Pointe mindestens 2,3 s, Tonpause davor
- [ ] Treffer der Pointe in der Sprechpause, nie unter Sprache; Sprechtempo höchstens 3,5 Wörter je Sekunde (`vorpruefung.py --woerter --treffer`)
- [ ] Bild-Checkliste aus `stilbibliothek/GRAMMATIK.md` am Storyboard abgehakt (Konstante, eine Farbe eine Bedeutung, Medium am Handy, etwas Neues alle 2 bis 4 s)
- [ ] Abfolge als Zuschauer gelesen (Abschied, Politik, Marke, Logik)
- [ ] Handy-Fassung mit Master-Ton, beide −14 LUFS (oder Kartenbereich innerhalb −14 ± 1), höchstens −1 dBTP
