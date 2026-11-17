# Präferenzen: wie gebaut wird

Einmal im Gespräch gefüllt, bei jeder Bestellung gelesen. Hier steht, auf welchem Weg Material, Stimme und Musik entstehen und in welchen Formaten geliefert wird. Ändert sich etwas, ändert Claude diese Datei und sagt es in einem Satz.

## Weg zum Material
- Standard: [aus Code | eigenes Material | Bildmodell]
- Bildmodell, falls genutzt: [Name des Dienstes oder „lokal“], Objekte immer mit transparentem Hintergrund (Weg in `starter/LIESMICH.md`, Abschnitt „Objekte mit transparentem Hintergrund“)
- Eigenes Material liegt in: [Ordner]
- Kostenrahmen je Video: [Betrag oder „keine Kosten“]; Kosten vorher schätzen und nachher nennen

## Stimme
- Weg: [eigene Aufnahme | Sprachdienst | keine Stimme, nur Schrift]
- Gewählte Stimme: [Name oder Kennung], ausgewählt am [Datum] aus drei Hörproben mit demselben Satz
- Auswahl, wenn noch keine gewählt ist: drei Stimmen, die zur Marke passen, je dieselbe Zeile aus dem ersten Skript, der Mensch hört und wählt eine. Nie eine Stimme ohne Einverständnis der Person klonen.
- Sprechtempo höchstens 3,5 Wörter je Sekunde; Zahlen und Namen so ins Skript schreiben, wie sie gesprochen werden

## Formate
- Hauptformat: [9:16 | 16:9 | 4:5 | 1:1]
- Weitere Formate je Video: [Liste]; jedes Format wird eigens angeordnet, nie beschnitten (Schutzzonen in `starter/BAUSTEINE.md`)

## Musik
- Weg: [ElevenLabs Music über `musik.py` | freie Musik mit geprüfter Lizenz | eigene Musik]; der Taktbauer setzt nur Schläge, kein Bett
- Lautheit: −14 LUFS, True Peak höchstens −1 dBTP

## Freigaben
- Was der Mensch vor dem Bau sieht: [Skript, Look-Check, Storyboard]
- Was ohne Rückfrage gebaut werden darf: [zum Beispiel zweite Folge derselben Rubrik im selben Stil]

## Creator-Programm und Würfel
- creator_modus: aus
  (`tiktok`, wenn der Kanal im TikTok-Creator-Programm ist: dann würfelt `wuerfeln.py` nur Karten mit `creator: ja` oder `eingeschraenkt`, freie doppelt so oft; ausgeschnittene Figuren mit hartem Saum, Bild im Bild mit Rand und mehr als zwei Blitzbilder sind gesperrt; `vorpruefung.py --creator` prüft jedes Stück. Gesperrte Karten: `stilbibliothek/CREATOR_SPERRLISTE.md`.)
- eigene_stimme: nein
  (`ja`: Die Stimme kommt als eigene Aufnahme vom Handy, `stimme.py --eigene <datei> --text "…"`; im Creator-Modus empfohlen, weil ein menschlicher Anteil das Stück als Creator-Arbeit erkennbar macht. Ein eigenes Foto oder ein kurzer eigener Clip je Video hilft genauso.)
- KI-Kennzeichnung: bleibt an, wo KI-Material im Stück ist. Nie verstecken.
- register: zentral
  (`zentral`: jedes Video wird zusätzlich gegen die Videos aller Kunden geprüft, braucht `AUTOPILOT_REGISTER_SCHLUESSEL` aus dem Kauf in der Umgebung; `lokal`: nur gegen die eigenen Videos, jede Ausgabe sagt das dann. Schalter technisch: `"zentral": "aus"` in `haus/register.json`.)
- Mischung: `haus/mischung.json` (gewürfelt mit `wuerfeln.py mischung`, der Kunde wählt nichts); Verlauf der Videos `haus/verlauf.json`.
