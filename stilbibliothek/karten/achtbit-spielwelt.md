---
id: achtbit-spielwelt
name: "Achtbit-Spielwelt"
familie: malstil
kurz: "Eine Achtbit-Spielwelt: grobe Pixel, vierzehn Farben, ein Herz blinkt in der Anzeige, ein Block wirft eine Münze."
kern: ["240 mal 135 Pixel, nur vierzehn Farben", jedes Teil mit einem Pixel schwarzer Kante, Bewegung in Schritten wie auf einer alten Konsole]
energie: 4
format_quelle: "9:16"
laenge_s: [10, 60]
bauweg: animskill
animskill:
  motor: huashu
  stil: "14_8bit"
  quelle: "references/风格配方/14_8bit.md"
  schrift: [serif, grotesk]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Figuren, Stimmen und Beispielbilder des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 4.5
  schnitte_pro_s: 0.2
  ereignisse_pro_s: 1.2
  lufs: -14
  helligkeit: 0.39
  farbigkeit: 0.51
palette:
  grund: "#0838A8"
  text: "#FBE2A6"
  akzent: "#E04030"
  licht: "#AAE9FB"
effekte: [malerei, push-in, geraeusche, pixelgrafik, hud, stop-motion]
kamera: "Langsame Fahrt oder Push-in über die gemalte Szene (2 bis 5 %), Wechsel über den eigenen Übergang des Stils."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, intro, uebergang]
zweck: [kinder, wissen, event-teaser]
branchen_passt: [technik, kinder-familie, bildung]
branchen_nie: [finanzen, gesundheit]
abnahme:
  shot_median_s: [2, 20]
  schnitte_pro_s: [0.03, 0.5]
  helligkeit: [0.21, 0.54]
  farbigkeit: [0.19, 0.9]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: eingeschraenkt
creator_ohne: [hud, pixelgrafik]
spielraum:
  palette: akzent
  schrift: klasse
  blitzbild_bilder: [2, 4]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.4, 1.0]
  korn: [0.03, 0.06]
  vignette: [0.3, 0.5]
  beat_versatz_16tel: [0, 1]
  textgroesse_prozent: [-10, 10]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: grund
  hell: licht
  licht: licht
quelle: Eigene Beschreibung eines offenen Zeichen-Motors (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken des Motors übernommen.
---
# Achtbit-Spielwelt

Eine Achtbit-Spielwelt: grobe Pixel, vierzehn Farben, ein Herz blinkt in der Anzeige, ein Block wirft eine Münze. Getragen wird es vom Wiedererkennen einer Epoche, ohne dass ein bekanntes Bild nachgestellt wird.

## Kern
- 240 mal 135 Pixel, nur vierzehn Farben.
- Jedes Teil mit einem Pixel schwarzer Kante.
- Bewegung in Schritten wie auf einer alten Konsole.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 240 mal 135 Pixel mit 14 Farben, jedes Teil mit einem Pixel schwarzer Kante, Bewegung in Schritten bei 15 bis 30 Bildern. Farben: grund `#0838A8`, text `#FBE2A6`, akzent `#E04030`, licht `#AAE9FB`.
- **Bewegung:** Das Leitmotiv des Stils bewegt sich die ganze Zeit (Wirbel, Lichtfleck, Tusche, Goldglanz, Punkte); Szenen wechseln über den eigenen Übergang des Stils.
- **Ton:** Leises Bett aus Code-Musik, darüber leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang; die Stimme liegt vorn.
- **Text:** Ein bis vier Wörter in einer Leerfläche der Szene oder als Untertitel der Brücke; Schrift aus der Zeit des Stils, wenn sie lesbar bleibt.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Gemalte Szene lebt | 50 % | eigene Komposition für das Thema, Leitmotiv bewegt sich, Motiv 40 bis 70 % der Bildhöhe | 3 bis 6 s |
| Eintritt in den Stil | 15 % | der Übergang des Stils trägt den Wechsel | 0,6 bis 1,5 s |
| Nahaufnahme der Malspur | 15 % | Detail mit sichtbarem Material (Strich, Punkt, Blattgold, Tusche) | 1 bis 3 s |
| Weite mit Wort | 20 % | Landschaft oder Raum mit Leerfläche für ein bis vier Wörter, unteres Sechstel frei | 2 bis 4 s |

## Regler
Stärke der Leitmotiv-Bewegung, Länge je Szene, Anteil Nahaufnahme, Akzent und Licht aus dem Zug. Fest bleiben Pinselführung, Farblogik und Übergang des Stils. Der Zug tauscht nur Akzent und Licht, Grund und Linie bleiben die des Stils.

## Fallen
- Zu wenig Bewegung im Bild ist die häufigste Schwäche des Motors: vor der Abgabe `film_gate.py` des Motors laufen lassen; unter 0,06 schnellen Bewegungsbildern wirkt das Stück wie eine Folienschau.
- Ein Grund aus Blau und Violett über ein Drittel der Bilder fällt im `film_gate.py` durch; nur wenn der Stil es selbst verlangt, mit Begründung freigeben.
- Die Musterszenen des Motors zeigen alle dasselbe Zimmer (Fenster oben links, Katze unten, Figur mit Tasse): Pinselführung, Farblogik und Leitmotiv mitnehmen, Raum, Möbel und Figuren neu bauen.
- Motive bekannter Gemälde nie nachstellen: Malweise, Farblogik und Bewegung des Leitmotivs mitnehmen, den Bildinhalt für das eigene Thema neu komponieren.
- Creator-Modus: ohne `hud`, `pixelgrafik` bauen; geht der Stil dann nicht mehr, eine andere Karte würfeln.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: leiser Raumklang der Szene (Wind, Wasser, Feuer, Stadt), ein Pinselwisch auf jedem Übergang. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `huashu`, Stil `14_8bit`, Quelle im Motor `references/风格配方/14_8bit.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor huashu --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/huashu.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a tiny hero jumping over a river of numbers“.

```json
{"szenen": "huashu/film.js", "rezept": "14_8bit"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 2 bis 20 s, Schnitte je Sekunde 0,03 bis 0,5, Helligkeit 0,21 bis 0,54, Farbigkeit 0,19 bis 0,9, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei. Dazu `film_gate.py` des Motors grün oder gelb.
