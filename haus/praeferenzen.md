# Präferenzen: wie gebaut wird

> **BEISPIEL.** Vorbelegt für den erfundenen Kanal „Kleine Fragen“ (kurze Erklärstücke und Zitate, Bilder aus Code, mit Vorlesestimme und Musik über ElevenLabs), damit ein erster Durchlauf ohne Gespräch geht. Vor dem ersten echten Video im Gespräch ersetzen (leere Vorlagen in `_vorlagen/`). Solange diese Zeile hier steht, sagt Claude bei jeder Bestellung in einem Satz, dass noch Beispielwerte gelten.

Einmal im Gespräch gefüllt, bei jeder Bestellung gelesen. Ändert sich etwas, ändert Claude diese Datei und sagt es in einem Satz.

## Weg zum Material
- Standard: aus Code (Zitate mit `zitat.py --nur-code`, Erklärstücke nach dem Muster `AkkuWinter`)
- Bildmodell: keins
- Eigenes Material liegt in: keins
- Kostenrahmen je Video: wenige Cent (ElevenLabs: Musik rund 900 Credits je Minute, Stimme nach Zeichen); ohne Schlüssel keine Kosten, dann Stille statt Musik

## Stimme
- Weg: Vorlesestimme über ElevenLabs v4 (`stimme.py`), Wortzeiten aus der Aufnahme für `WortSpur`, Untertitel aus denselben Wortzeiten; ohne Stimme nur auf ausdrückliche Bestellung (dann `lesezeiten()`)
- Gewählte Stimme: noch keine gewählt; bis dahin nimmt `stimme.py` die erste Standardstimme des Kontos (Kennung hier eintragen, sobald gewählt)
- Kommt später eine Stimme dazu: drei Stimmen, die zum Kanal passen, je dieselbe Zeile, der Mensch hört und wählt eine. Nie eine Stimme ohne Einverständnis der Person klonen.

## Formate
- Hauptformat: 9:16
- Weitere Formate je Video: keine (Rückblick monatlich 16:9)

## Musik
- Weg: ElevenLabs Music über `musik.py` (Prompt aus der Karte), Schlag auf der Pointe aus `taktbauer.py --nur-schlaege`; ohne Schlüssel Stille
- Lautheit: −14 LUFS, True Peak höchstens −1 dBTP (`handy.py` setzt sie nach)

## Freigaben
- Was der Mensch vor dem Bau sieht: Skript mit Quelle, Look-Check (zwei Standbilder)
- Was ohne Rückfrage gebaut werden darf: zweite Folge derselben Rubrik im selben Stil
