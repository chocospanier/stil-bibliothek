---
id: bonbon-3d
name: "Bonbon-3D"
familie: selbstzeichnend
kurz: "Bonbonfarbene Kugeln in weichem Licht, eine prall aufgeblasene Schrift, der Hintergrund verschwimmt."
kern: [weiche Kugeln in Bonbonfarben, "prall aufgeblasene, weiche Schrift", Tiefenunschärfe und weiches Licht]
energie: 3
format_quelle: "9:16"
laenge_s: [10, 45]
bauweg: animskill
animskill:
  motor: zeichnen
  stil: "soft3d"
  quelle: "lib/soft3d.py"
  schrift: [hand, serif]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Beispielbilder und Beispielmotive des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 5
  schnitte_pro_s: 0.15
  ereignisse_pro_s: 1.1
  lufs: -14
  helligkeit: 0.77
  farbigkeit: 0.22
palette:
  grund: "#F6E6F0"
  text: "#3A2A4A"
  akzent: "#FF6FA8"
  licht: "#FFD84A"
  blau: "#7FC8F8"
effekte: [strich-fuer-strich, blende, push-in, geraeusche, "3d-render", geringe-schaerfentiefe, "3d-schrift"]
kamera: "Steht während der Stufen, danach langsame Fahrt oder Push-in über das Endbild (2 bis 5 %), am Schluss Rückzug aufs Ganze."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber das Werkzeug des Mediums je Stufe (Pinsel, Stift, Schere, Nadel, Tastatur), sehr leise, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, intro, uebergang]
zweck: [marke-image, event-teaser]
branchen_passt: [mode-beauty, technik, kinder-familie]
branchen_nie: [finanzen]
abnahme:
  shot_median_s: [1, 40]
  schnitte_pro_s: [0.0, 0.6]
  helligkeit: [0.59, 0.92]
  farbigkeit: [0.07, 0.47]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
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
# Bonbon-3D

Bonbonfarbene Kugeln in weichem Licht, eine prall aufgeblasene Schrift, der Hintergrund verschwimmt. Ruhig und genau; die Spannung liegt im Warten auf das fertige Bild und im Detail, das die Kamera danach zeigt.

## Kern
- Weiche Kugeln in Bonbonfarben.
- Prall aufgeblasene, weiche Schrift.
- Tiefenunschärfe und weiches Licht.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Raygetracetes Meer aus Bonbonkugeln, prall weiche Schrift, Tiefenunschärfe. Farben: grund `#F6E6F0`, text `#3A2A4A`, akzent `#FF6FA8`, licht `#FFD84A`, blau `#7FC8F8`.
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

## Ton
Dieser Motor liefert keinen Ton: das Bett kommt aus `musik.py` oder als Code-Musik eines anderen Motors, die Geräusche aus `taktbauer.py --nur-schlaege` oder eigenen Aufnahmen. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: das Werkzeug des Mediums je Stufe (Pinsel, Stift, Schere, Nadel, Tastatur), sehr leise. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`.

## Bauweg
Zeichen-Motor `zeichnen`, Stil `soft3d`, Quelle im Motor `lib/soft3d.py`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor zeichnen --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/zeichnen.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a word rising out of a sea of candy spheres“.

```json
{"skript": "zeichnen/bild.py", "stil": "soft3d", "kamera": "schub", "an_woerter": true}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 1 bis 40 s, Schnitte je Sekunde 0,0 bis 0,6, Helligkeit 0,59 bis 0,92, Farbigkeit 0,07 bis 0,47, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
