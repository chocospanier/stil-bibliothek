# Stil-Bibliothek: Anleitung für Claude

> Diese Datei lädt automatisch, wenn Claude Code in diesem Ordner gestartet wird. Sie sagt dir, was hier liegt, in welcher Reihenfolge du liest und nach welchen Regeln du baust. Der Mensch, mit dem du arbeitest, will Kurzvideos in einem bestimmten Look; dieser Ordner ist das Wissen und der Werkzeugkasten dafür.

## Was hier liegt
| Ordner | Inhalt |
|---|---|
| `stilbibliothek/` | 106 Stil-Karten in 19 Familien. Einstieg `FAMILIEN.md`, Anleitung für dich `SKILL.md`, Erzählformen und Bild-Checkliste `GRAMMATIK.md`, Filter über `werkzeuge/bibliothek_index.py --filter` |
| `starter/` | Remotion-Projekt mit 28 Bausteinen plus Tonspur, 13 Helfern und 9 fertigen Beispielen. Einstieg `starter/LIESMICH.md`, Bausteine `starter/BAUSTEINE.md` |
| `pruefen/` | `FEHLERKATALOG.md` (acht Ursachen, Checkliste vor dem Rendern) und `PRUEFER.md` (die Rolle des frischen Prüfers) |
| `werkzeuge/` | Video vermessen, Vorprüfung, Streifen, Kamerabewegung, Kartenfilter. Einrichtung `werkzeuge/INSTALL.md` |
| `ABLAUF.md`, `GLOSSAR.md`, `LIESMICH.md` | der Bauweg, die Begriffe, die Übersicht |
| `haus/` | Der Betrieb, für den du baust: `look.md` (Farben, Schrift, Stil-Familien), `rubriken.md` (feste Formate mit Länge, Kanal, Familie), `tabus.md` (was nie vorkommt), `fakten.md` (jede Zahl mit Quelle), `themen.md` (Vorrat), `praeferenzen.md` (Weg zum Material, Stimme, Formate). Lies alle sechs bei jeder Bestellung. Fehlen sie, lege sie aus `haus/LIESMICH.md` im Gespräch an, bevor du das erste Video baust |
| `projekte/` | Ein Unterordner je Video (`JJJJ-MM-TT_<slug>/`): Skript, Storyboard, Prüfbericht, Render, `STAND.md`. Nie etwas darin löschen |

## Lies zuerst, in dieser Reihenfolge
1. `LIESMICH.md` (5 Minuten)
2. `ABLAUF.md` (der Weg von der Stilwahl bis zur Abnahme)
3. `stilbibliothek/SKILL.md` (wie du mit den Karten baust) und `stilbibliothek/GRAMMATIK.md` (acht Erzählformen, vier Regeln, Bild-Checkliste)
4. `starter/LIESMICH.md` (wie der Werkzeugkasten läuft)
5. `pruefen/FEHLERKATALOG.md` (die Fehler, die schon passiert sind; die Checkliste hakst du vor jedem Render ab)

## Beim ersten Start einmalig
- `haus/` ist mit einem erfundenen Beispielkanal („Kleine Fragen“) vorbelegt, jede Datei trägt oben die Zeile **BEISPIEL**; damit läuft ein erster Durchlauf auch ohne Gespräch. Vor dem ersten echten Video füllst du die sechs Dateien im Gespräch mit dem Menschen neu (leere Vorlagen in `haus/_vorlagen/`; Farben aus dem Logo, drei Stil-Familien als Zehn-Sekunden-Probe mit dem Firmennamen, fünf Rubriken, zehn Tabus, zehn Fakten mit Quelle, zwanzig Themen) und löschst die Beispielzeile. Solange sie steht, sagst du bei jeder Bestellung in einem Satz, dass noch Beispielwerte gelten.
- Lege die Prüfer-Rolle an: Kopiere `pruefen/PRUEFER.md` nach `.claude/agents/pruefer.md` in diesem Ordner. **Die Rolle wirkt erst in einer neuen Sitzung, die in diesem Ordner startet**; danach startest du den Prüfer mit dem Agent-Werkzeug („Prüfe <Projektordner>“). In der laufenden Sitzung startest du stattdessen einen allgemeinen Agenten, gibst ihm `pruefen/PRUEFER.md` als Rollenbeschreibung und beschränkst ihn auf den Projektordner. Der Prüfer darf nie dieselbe Instanz sein, die gebaut hat.
- Prüfe, ob Node.js, Python, ffmpeg und ffprobe da sind (`werkzeuge/INSTALL.md`). Fehlt ffmpeg im PATH, setze die Umgebungsvariablen `FFMPEG` und `FFPROBE`.
- Prüfe den ElevenLabs-Schlüssel für Stimme und Musik: `python -I starter/werkzeuge/stimme.py --stimmen` listet die Stimmen des Kontos. Fehlt er, bitte den Menschen, `ELEVENLABS_API_KEY` in der Umgebung zu setzen (nie in eine Datei des Pakets); ohne Schlüssel gibt es keine Musik und die Stimme nur von Hand.
- Im Ordner `starter`: `npm install`, dann `npm run storyboard -- TitelblattNoir beispiele/titelblatt-noir/beats.json out/`. Liegt nach einer Minute ein Storyboard in `out/`, ist alles eingerichtet.

## Bestellungen verstehen
Der Mensch bestellt in einem Satz: Art (Kurzvideo, Erklärvideo, Teaser), Thema, Länge, Format, Kanal, optional Rubrik und Pointe. Alles andere (Farben, Schrift, Familie, Tabus, Fakten) nimmst du aus `haus/`. Sage ihm, was du vorhast, in drei Zeilen, und frage nur, wenn verschiedene Antworten zu wirklich anderen Videos führen würden. Weitere Sätze, die er benutzt: „Fülle den Wochenplan“ (je Rubrik das nächste Thema aus `haus/themen.md`, je Zeile ein Bestellsatz, Datei `projekte/wochenplan.md`), „Bau die Woche“ (alle Zeilen nacheinander, je mit Storyboard zuerst), „Ändern: …“ (genau eine Sache, eine Runde), „Verwerfen, anderer Stil“, „Werte die Woche aus“ (liest `projekte/wochenuebersicht.md`, nennt besten und schwächsten Beitrag, schlägt EINE Änderung vor).
- **„Bau mir ein Zitat-Video: „<Satz>“ (<Name>, <Werk und Stelle>)“**, optional „als Strom“ (Karte `verwandlungsstrom`, Satz steht, Bilder verwandeln sich, Musik) oder „mit Stimme“ (Karte `umkehrwort-monolog`, Wort für Wort, Stimme aus `haus/praeferenzen.md`); ohne Angabe: Satz bis 12 Wörter als Strom, längere mit Stimme. Dann: Projektordner `projekte/JJJJ-MM-TT_<slug>/`, Quelle prüfen und mit Beleg in `FAKTEN.md` (nur gemeinfreie Wortlaute oder eigene Sätze), `bestellung.json` (`python -I starter/werkzeuge/zitat.py --vorlage <ordner>`), Szenenplan `szenen.json` schreiben (vier bis sechs Szenen, englisch, Pass nach `stilbibliothek/GRAMMATIK.md`), dann `python -I starter/werkzeuge/zitat.py <ordner>/bestellung.json`. **Ohne Bild- und Videodienste** (nur Code, oder eigene Bilder aus einem Ordner): `--vorlage <ordner> --nur-code` und `zitat.py <bestellung.json> --nur-code`; dann ist jede Szene eine Form der Code-Bühne (`form`, `farbe`, Formen in `src/beispiele/codebuehne.tsx`) oder mit `material.ordner` ein eigenes Bild, gerendert mit 30 fps, Stimme und Musik kommen aus ElevenLabs (eingebaut, Schlüssel in der Umgebung); ohne Schlüssel Stille statt Musik und die Stimme von Hand. Nach dem Schritt `bilder` den Bogen ansehen, nach `pruefen` den frischen Prüfer, eine Reparatur mit `--neu`, dann zeigen. Ablauf und Adapter für Bild-, Video- und Stimmdienste: `ABLAUF.md`, Abschnitt „Zitat in einem Rutsch“.

- **„Bau mir ein Kurzvideo über <Frage>“ (Erklärstück, 15 bis 30 s)**: Das Muster ist das Beispiel `AkkuWinter` ([starter/src/beispiele/AkkuWinter.tsx](starter/src/beispiele/AkkuWinter.tsx) mit `starter/beispiele/akku-winter/`, Karte `neon-symbolbuehne`): Frage und Antwort, drei bis fünf Bühnen mit je einem Symbol aus Code, Wörter im Differenzmodus, Stimme aus `stimme.py` (der Teil nach dem Treffer als eigene Zeile mit `pause_vor`), Musik aus `musik.py` unter der Stimme leiser und im Atem stumm, der Schlag aus `taktbauer.py --nur-schlaege`, gelber Lichtblitz auf dem Treffer nach der Stille. Kopiere die Datei, tausche Bühnen, Text und Belege. Die Wortzeiten kommen aus der Aufnahme (`stimme.py` schreibt sie); nur auf ausdrückliche Bestellung **ohne Stimme** aus `lesezeiten(text, {wps: 2.3})`, den Teil nach dem Treffer mit `ab: treffer + 0.15`, und `WortSpur` bekommt `bisEnde` (Pointe bis zum letzten Bild) und `wechsel` (Bühnenwechsel und Treffer). Material und Musik eines Projekts liegen in seinem Ordner, Render und Storyboard mit `--public-dir <ordner>`.

## So baust du ein Video (Kurzfassung von ABLAUF.md)
1. Absicht in einem Satz klären: Was soll das Video tun, für wen, welche Länge, 9:16 oder 16:9, welches Material gibt es. `haus/` lesen.
2. Erzählform aus `stilbibliothek/GRAMMATIK.md` wählen, dann Stil: `FAMILIEN.md`, Filter, nur Familien aus `haus/look.md`, höchstens drei Karten vorschlagen, eine empfehlen. Entscheidung des Menschen abwarten; bei der zweiten Bestellung derselben Rubrik nicht mehr fragen.
3. Karte lesen, die drei `kern`-Merkmale sind Pflicht, die `Fallen` liest du vor dem Bau.
4. Skript locken, dann **Look-Check**: zwei bis vier verschiedene Beats als Standbild, je Bild Ja oder Nein vom Menschen. Erst danach das ganze Storyboard; Abfolge einmal als Zuschauer lesen (Abschied, Politik, Marke, Logik). Treffer der Pointe in die Sprechpause, nie unter Sprache.
5. Material erzeugen und jedes Bild in voller Größe ansehen, bevor es ins Stück kommt. Figuren nur verschieben, gleichmäßig skalieren, leicht drehen; nie strecken, filtern, invertieren.
6. Musik zuerst, dann Takt messen (`npm run takt`), Raster vom echten Ton.
7. Bauen mit den Bausteinen aus `starter/BAUSTEINE.md`. Baue nur selbst, was kein Baustein kann.
8. Storyboard exportieren, Checkliste abhaken, `npm run vorpruefung`, dann den frischen Prüfer auf Storyboard und Streifen.
9. Render, Handy-Fassung (`npm run handy`), `npm run abnahme` gegen die Karte. Genau eine Reparaturrunde, dann entscheidet der Mensch mit Auge und Ohr.

## Regeln, die immer gelten
- **Musik und Stimme (Hausregel seit 18.10.2026):** Musik ist immer echte Musik: ElevenLabs Music über `starter/werkzeuge/musik.py` (Prompt aus dem Abschnitt `Material` der Karte, Länge aus der Bestellung, rund 900 Credits je Minute) oder eigene, lizenzierte Musik. Der Taktbauer ist keine Musikquelle; er setzt nur einzelne Schläge und Klicks über die Musik (`taktbauer.py --nur-schlaege`). Ohne Schlüssel: Stille mit Hinweis, nie ein Ersatzbett. Jedes Stück mit Text bekommt eine Vorlesestimme (`starter/werkzeuge/stimme.py`, ElevenLabs v4, Wortzeiten für `WortSpur`, Untertitel); „ohne Stimme“ nur auf ausdrückliche Bestellung. Schlüssel nur in der Umgebung (`ELEVENLABS_API_KEY` oder `ELEVENLABS_KEY_DATEI`), nie in einer Datei des Pakets.
- Nie `cd` in Befehlen; immer absolute Pfade oder `npm --prefix`. Python immer mit `python -I`.
- Stimme und Musik über den ElevenLabs-Schlüssel des Menschen sind der Hausweg (wenige Cent je Stück; ist kein Schlüssel gesetzt, fragst du einmal). Alle anderen bezahlten Dienste und jeder Upload nur mit ausdrücklichem Ja des Menschen. Bilder aus Code, aus dem Starter oder aus freien Quellen reichen für jeden Stil; die Beispiele und die Fremdtests sind so entstanden.
- Messung ist kein Urteil. Die Werkzeuge melden, der Mensch entscheidet. Ton hört nur ein Mensch.
- Wortzeiten nie von Hand schätzen: mit Stimme aus der Transkription, ohne Stimme aus `lesezeiten()`.
- Höchstens 3 harte Hell-Dunkel-Wechsel je Sekunde, kein Standbild über 1 s, unten 15 % frei (4:5: 10 %, 1:1: 8 %), Bild 0 ist das Titelbild, Pointe mindestens 2,3 s mit Tonpause davor, Sprechtempo höchstens 3,5 Wörter je Sekunde.
- Jede neue Falle, die du erlebst, trägst du in die Karte unter `Fallen` ein. So wird die Bibliothek besser.
- Liefern heißt: Video, Handy-Fassung, Storyboard, Prüfbericht und eine kurze `STAND.md` im Projektordner. Ein Ergebnis, das der Mensch nicht in einem Klick ansehen kann, ist nicht geliefert.

## Wenn etwas unklar ist
Entscheide selbst, notiere die Lücke in `STAND.md` und mach weiter. Frag den Menschen nur, wenn verschiedene Antworten zu wirklich anderen Videos führen würden (Stilwahl, Thema, Länge).
