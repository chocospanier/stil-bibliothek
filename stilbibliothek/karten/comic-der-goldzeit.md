---
id: comic-der-goldzeit
name: "Comic der Goldzeit"
familie: selbstzeichnend
kurz: "Ein Comic der Vierziger: Pinseltusche, Rasterpunkte, verrutschte Farben auf vergilbtem Papier."
kern: [Pinseltusche als Kontur, Rasterpunkte und verrutschte Farben, vergilbtes Zeitungspapier]
energie: 3
format_quelle: "9:16"
laenge_s: [10, 45]
bauweg: animskill
animskill:
  motor: zeichnen
  stil: "comic"
  quelle: "lib/comic.py"
  schrift: [hand, serif]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Beispielbilder und Beispielmotive des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 5
  schnitte_pro_s: 0.15
  ereignisse_pro_s: 1.1
  lufs: -14
  helligkeit: 0.71
  farbigkeit: 0.26
palette:
  grund: "#F2E8C8"
  text: "#141414"
  akzent: "#E2302A"
  licht: "#F7D33A"
  blau: "#2A5DB0"
effekte: [strich-fuer-strich, blende, push-in, geraeusche, halbton, comic-panel]
kamera: "Steht während der Stufen, danach langsame Fahrt oder Push-in über das Endbild (2 bis 5 %), am Schluss Rückzug aufs Ganze."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber das Werkzeug des Mediums je Stufe (Pinsel, Stift, Schere, Nadel, Tastatur), sehr leise, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, intro, uebergang]
zweck: [geschichte, kinder, event-teaser]
branchen_passt: [kinder-familie, musik-kultur]
branchen_nie: []
abnahme:
  shot_median_s: [1, 40]
  schnitte_pro_s: [0.0, 0.6]
  helligkeit: [0.53, 0.86]
  farbigkeit: [0.09, 0.56]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: eingeschraenkt
creator_ohne: [comic-panel, halbton]
spielraum:
  palette: akzent
  schrift: klasse
  blitzbild_bilder: [2, 4]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.4, 1.0]
  korn: [0.0, 0.04]
  vignette: [0.0, 0.3]
  beat_versatz_16tel: [0, 1]
  textgroesse_prozent: [-10, 10]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: text
  hell: grund
  licht: licht
quelle: Eigene Beschreibung eines offenen Zeichen-Motors (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken des Motors übernommen.
---
# Comic der Goldzeit

Ein Comic der Vierziger: Pinseltusche, Rasterpunkte, verrutschte Farben auf vergilbtem Papier. Ruhig und genau; die Spannung liegt im Warten auf das fertige Bild und im Detail, das die Kamera danach zeigt.

## Kern
- Pinseltusche als Kontur.
- Rasterpunkte und verrutschte Farben.
- Vergilbtes Zeitungspapier.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Pinseltusche, Ben-Day-Punkte, Vierfarbversatz, Zeitungspapier. Farben: grund `#F2E8C8`, text `#141414`, akzent `#E2302A`, licht `#F7D33A`, blau `#2A5DB0`.
- **Bewegung:** Das Bild malt sich in fünf bis zehn Stufen, jede wächst mit einer Pinselmaske über die vorige, danach hält eine langsame Kamera mit Lichtatmen das Endbild; manche Stile haben echte Bewegung (Formwandel, Bilderbuchfigur, Oberflächen).
- **Ton:** Leises Bett aus Code-Musik, darüber das Werkzeug des Mediums je Stufe (Pinsel, Stift, Schere, Nadel, Tastatur), sehr leise; die Stimme liegt vorn.
- **Text:** Ein bis vier Wörter als Untertitel der Brücke; Schrift im Bild nur, wo der Stil sie selbst trägt (Tafel, Heft, Plakat, Oberfläche).

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Stufe für Stufe | 50 % | der Motor malt Grund, Anlage, Flächen, Details, Licht; Motiv 40 bis 80 % der Bildhöhe | 0,6 bis 2 s je Stufe, Start auf Wortanfängen |
| Fahrt über das fertige Bild | 25 % | langsame Fahrt oder Push-in über das Endbild, nie über 1 s ohne Bewegung | 2 bis 4 s |
| Detail im Ausschnitt | 15 % | Nahaufnahme einer Stelle mit sichtbarem Material | 1 bis 2 s |
| Wort auf dem Bild | 10 % | ein bis vier Wörter, unteres Sechstel frei | 1,5 bis 3 s |

## Regler
Zahl der Stufen (5 bis 10), Länge der Fahrt, Details im Ausschnitt, Akzent und Licht aus dem Zug. Fest bleiben Malweise, Grund und Reihenfolge der Stufen. Der Zug tauscht nur Akzent und Licht, Grund und Linie bleiben die des Stils.

## Fallen
- Bewegung entsteht nur aus Stufen: der Motor lässt jede Stufe mit einer Pinselmaske über die vorige wachsen und hält das Endbild mit Kameraschub und Lichtatmen. Mit zwei oder drei Stufen wirkt es wie eine Diashow: fünf bis zehn Stufen je Bild planen, ihre Starts auf Wortanfänge legen (`an_woerter`).
- Die Bibliotheken nutzen Systemschriften (Arial, Georgia, Segoe Print, KaiTi): für Schrift im Bild eine eigene OFL-Schrift über `INKPAINT_FONT_<STIL>` setzen und Umlaute am Standbild prüfen.
- `beispiel` im motor_spec ist nur ein Test mit fester 16:9-Größe; für echte Stücke immer ein eigenes Skript, das die Größe aus `ANIM_W` und `ANIM_H` liest.
- Ein Bild braucht je nach Stil 0,1 bis 30 s Rechenzeit: Stufenbilder einmal rechnen und zwischenspeichern, nie je Videobild neu malen.
- Große Verläufe zeigen nach starker Kompression Farbstufen: das leichte Raster oder Korn des Motors drinlassen.
- Das Beispielmotiv einer Malweise im Motor ist nur ein Stichwort: das eigene Thema in derselben Malweise neu komponieren, Motive und Texte der Beispiele nie übernehmen.
- Creator-Modus: ohne `comic-panel`, `halbton` bauen; geht der Stil dann nicht mehr, eine andere Karte würfeln.

## Ton
Dieser Motor liefert keinen Ton: das Bett kommt aus `musik.py` oder als Code-Musik eines anderen Motors, die Geräusche aus `taktbauer.py --nur-schlaege` oder eigenen Aufnahmen. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: das Werkzeug des Mediums je Stufe (Pinsel, Stift, Schere, Nadel, Tastatur), sehr leise. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`.

## Bauweg
Zeichen-Motor `zeichnen`, Stil `comic`, Quelle im Motor `lib/comic.py`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor zeichnen --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/zeichnen.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a rocket launch in three panels“.

```json
{"skript": "zeichnen/bild.py", "stil": "comic", "kamera": "schub", "an_woerter": true}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 1 bis 40 s, Schnitte je Sekunde 0,0 bis 0,6, Helligkeit 0,53 bis 0,86, Farbigkeit 0,09 bis 0,56, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
