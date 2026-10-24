# Der Haus-Ordner: das, was jedes Video über den Betrieb wissen darf

Sechs Dateien, einmal gefüllt, bei jeder Bestellung gelesen. Claude legt sie beim ersten Start im Gespräch an; Sie können sie jederzeit selbst ändern. Was hier nicht steht, weiß kein Video. Was hier nie hineinkommt: Kundennamen, Kundendaten, Passwörter, Schlüssel, Bilder von Personen ohne Ja.

| Datei | Inhalt |
|---|---|
| `look.md` | Farben mit Rollen, Schriften, Logo-Datei, drei passende Stil-Familien, drei, die nie passen |
| `rubriken.md` | Die festen Formate: Name, Frage, Länge, Format, Kanäle, Uhrzeit, Stil-Familie |
| `tabus.md` | Wörter, Themen, Vergleiche, die nie vorkommen |
| `fakten.md` | Jede Zahl, die ein Video nennen darf, mit Quelle und Datum |
| `themen.md` | Der Vorrat: ein Satz je Zeile; Claude nimmt die nächste freie Zeile, wenn der Wochenplan eine Lücke hat |
| `praeferenzen.md` | Wie gebaut wird: Weg zum Material (aus Code, eigenes Material, Bildmodell), Stimme (eigene Aufnahme oder Sprachdienst, ausgewählt aus drei Hörproben), Formate (9:16, 16:9, 4:5, 1:1), Musikweg, Kostenrahmen |

Die sechs Dateien sind mit einem erfundenen Beispielkanal („Kleine Fragen“) vorbelegt, damit ein erster Durchlauf ohne Gespräch geht; jede trägt oben die Zeile **BEISPIEL**. Die leeren Vorlagen mit Platzhaltern in eckigen Klammern liegen in `_vorlagen/`. Beim ersten echten Start füllt Claude die Dateien im Gespräch neu und löscht die Beispielzeile; solange sie steht, sagt Claude bei jeder Bestellung, dass noch Beispielwerte gelten.
