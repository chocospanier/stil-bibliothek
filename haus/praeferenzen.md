# Präferenzen: wie gebaut wird

> **BEISPIEL.** Vorbelegt für den erfundenen Kanal „Kleine Fragen“ (kurze Erklärstücke und Zitate, Bilder aus Code, mit Vorlesestimme und Musik), damit ein erster Durchlauf ohne Gespräch geht. Vor dem ersten echten Video im Gespräch ersetzen (leere Vorlagen in `_vorlagen/`). Solange diese Zeile hier steht, sagt Claude bei jeder Bestellung in einem Satz, dass noch Beispielwerte gelten.

Einmal im Gespräch gefüllt, bei jeder Bestellung gelesen. Ändert sich etwas, ändert Claude diese Datei und sagt es in einem Satz.

## Weg zum Material
- Standard: aus Code (Zitate mit `zitat.py --nur-code`, Erklärstücke nach dem Muster `AkkuWinter`)
- Bildmodell: keins
- Eigenes Material liegt in: keins
- Kostenrahmen je Video: keine Kosten mit den lokalen Ton-Motoren (Musik aus Code oder ACE-Step, Stimme aus Qwen3-TTS oder eigener Aufnahme); mit ElevenLabs wenige Cent (Musik rund 900 Credits je Minute, Stimme nach Zeichen)

## Stimme
- Weg: Vorlesestimme aus `stimme.py` (von selbst: ElevenLabs v4, wenn ein Schlüssel da ist, sonst Qwen3-TTS auf dem eigenen Rechner), Wortzeiten aus der Aufnahme für `WortSpur`, Untertitel aus denselben Wortzeiten; ohne Stimme nur auf ausdrückliche Bestellung (dann `lesezeiten()`)
- Ton-Motor Stimme: auto (möglich: auto, qwen, elevenlabs; `stimme.py` hält sich daran, auch wenn ein Schlüssel in der Umgebung steht)
- Gewählte Stimme: noch keine gewählt; bis dahin nimmt `stimme.py` die erste Standardstimme des Kontos, bei Qwen `Uncle_Fu` (Kennung oder Name hier eintragen, sobald gewählt)
- Kommt später eine Stimme dazu: drei Stimmen, die zum Kanal passen, je dieselbe Zeile, der Mensch hört und wählt eine. Nie eine Stimme ohne Einverständnis der Person klonen.

## Formate
- Hauptformat: 9:16
- Weitere Formate je Video: keine (Rückblick monatlich 16:9)

## Musik
- Weg: Musikbett aus `musik.py` (Prompt aus der Karte; von selbst: ElevenLabs Music, wenn ein Schlüssel da ist, sonst ACE-Step, sonst Musik aus Code), Schlag auf der Pointe aus `taktbauer.py --nur-schlaege`
- Ton-Motor Musik: auto (möglich: auto, code, acestep, elevenlabs; `musik.py` hält sich daran, auch wenn ein Schlüssel in der Umgebung steht)
- Lautheit: −14 LUFS, True Peak höchstens −1 dBTP (`handy.py` setzt sie nach)

## Freigaben
- Was der Mensch vor dem Bau sieht: Skript mit Quelle, Look-Check (zwei Standbilder)
- Was ohne Rückfrage gebaut werden darf: zweite Folge derselben Rubrik im selben Stil

## Creator-Programm und Würfel
- creator_modus: aus
  (`tiktok`, wenn der Kanal im TikTok-Creator-Programm ist: dann würfelt `wuerfeln.py` nur Karten mit `creator: ja` oder `eingeschraenkt`, freie doppelt so oft; ausgeschnittene Figuren mit hartem Saum, Bild im Bild mit Rand und mehr als zwei Blitzbilder sind gesperrt; `vorpruefung.py --creator` prüft jedes Stück. Gesperrte Karten: `stilbibliothek/CREATOR_SPERRLISTE.md`.)
- eigene_stimme: nein
  (`ja`: Die Stimme kommt als eigene Aufnahme vom Handy, `stimme.py --eigene <datei> --text "…"`; im Creator-Modus empfohlen, weil ein menschlicher Anteil das Stück als Creator-Arbeit erkennbar macht. Ein eigenes Foto oder ein kurzer eigener Clip je Video hilft genauso.)
- KI-Kennzeichnung: bleibt an, wo KI-Material im Stück ist. Nie verstecken.
- register: zentral
  (`zentral`: jedes Video wird zusätzlich gegen die Videos aller Kunden geprüft, braucht `AUTOPILOT_REGISTER_SCHLUESSEL` aus dem Kauf in der Umgebung; `lokal`: nur gegen die eigenen Videos, jede Ausgabe sagt das dann. Schalter technisch: `"zentral": "aus"` in `haus/register.json`.)
- Mischung: `haus/mischung.json` (gewürfelt mit `wuerfeln.py mischung`, der Kunde wählt nichts); Verlauf der Videos `haus/verlauf.json`.
