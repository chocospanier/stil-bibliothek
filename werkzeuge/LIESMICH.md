# Werkzeuge in der freien Hälfte

Hier liegt nur der **Kartenfilter** `bibliothek_index.py`. Er prüft die Karten (Pflichtfelder, Effekt-Kennungen), baut `index.json`, `INDEX.md` und `EFFEKTE.md` neu und filtert die 106 Karten nach deinen Bedingungen.

```bash
pip install PyYAML
python -I werkzeuge/bibliothek_index.py --bib stilbibliothek --filter braucht=nur-typo motor_aufwand=klein
python -I werkzeuge/bibliothek_index.py --bib stilbibliothek --nur-pruefen
```

Listen-Felder treffen, wenn ein Element passt; Komma heißt „eins davon“; Zahlen auch mit `>=`, `<=`, `!=`.

Die übrigen Werkzeuge (Video vermessen, Vorprüfung, Bewegungsstreifen, Kamerabewegung, Abnahme gegen die Karte, Takt messen, Musik aus Code) gehören zum Werkzeugkasten: https://content-autopilot.de
