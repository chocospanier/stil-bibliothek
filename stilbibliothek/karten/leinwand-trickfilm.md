---
id: leinwand-trickfilm
name: "Leinwand-Trickfilm"
familie: erklaergrammatik
kurz: "Ein kleiner Trickfilm, ganz aus Code gezeichnet, mit eigener Wendung oder als Erklärstück, Musik im selben Code."
kern: ["alles ist gezeichneter Code, keine Bilddatei", "ein Look je Film aus der Zeichenbibliothek (Tusche, Bilderbuch, Schmuckfarbe, Einlinienstich, Wortformen, Marker)", eine kleine Geschichte mit Wendung oder ein Erklärstück mit Bildern]
energie: 3
format_quelle: "9:16"
laenge_s: [20, 90]
bauweg: animskill
animskill:
  motor: jsanim
  stil: "canvas"
  quelle: "skills/javascript-animation/SKILL.md"
  schrift: [hand, grotesk]
lizenz: "MIT; Urheberhinweis in LIZENZ.md"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 4
  schnitte_pro_s: 0.2
  ereignisse_pro_s: 1.0
  lufs: -14
  helligkeit: 0.75
  farbigkeit: 0.22
palette:
  grund: "#F6F1E7"
  text: "#22201C"
  akzent: "#E4572E"
  licht: "#F3B33D"
  blau: "#3B6EA8"
effekte: [sprechstimme, untertitel, aktivwort, geraeusche, strich-fuer-strich]
kamera: "Ruhig: steht oder fährt dem Argument nach, Bewegung kommt aus Verwandlung und Wachstum auf das Wort."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, hook]
zweck: [geschichte, erklaeren, kinder]
branchen_passt: [bildung, technik, kinder-familie]
branchen_nie: []
abnahme:
  shot_median_s: [2, 20]
  schnitte_pro_s: [0.03, 0.5]
  helligkeit: [0.57, 0.9]
  farbigkeit: [0.07, 0.47]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 3]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.4, 1.0]
  korn: [0.0, 0.03]
  vignette: [0.0, 0.2]
  beat_versatz_16tel: [0, 0]
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
# Leinwand-Trickfilm

Ein kleiner Trickfilm, ganz aus Code gezeichnet, mit eigener Wendung oder als Erklärstück, Musik im selben Code. Die Stimme trägt, das Bild antwortet auf jedes Stichwort und steht dann still; Verständnis ist die Energie.

## Kern
- Alles ist gezeichneter Code, keine Bilddatei.
- Ein Look je Film aus der Zeichenbibliothek (Tusche, Bilderbuch, Schmuckfarbe, Einlinienstich, Wortformen, Marker).
- Eine kleine Geschichte mit Wendung oder ein Erklärstück mit Bildern.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Jedes Bild in JavaScript auf eine Leinwand gezeichnet, ohne Bilddateien: Tuschlinie, Bilderbuch, Schmuckfarbendruck, Einlinienstich, Wörter als Formen oder Marker. Farben: grund `#F6F1E7`, text `#22201C`, akzent `#E4572E`, licht `#F3B33D`, blau `#3B6EA8`.
- **Bewegung:** Was gesagt wird, erscheint oder verwandelt sich genau auf dem Wortanfang und steht dann; die Umgebung darf leise weiterleben.
- **Ton:** Leises Bett aus Code-Musik, darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung; die Stimme liegt vorn.
- **Text:** Höchstens zwei Aussagen gleichzeitig im Bild, Schlagwort oder Zahl groß, Untertitel wortgenau mit Aktivwort.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Begriff als Bild | 45 % | genau ein Ding in der Mitte, 30 bis 60 % der Bildhöhe, alles andere leise | 2 bis 6 s |
| Verwandlung oder Wachstum | 25 % | das Bild ändert sich auf das Stichwort (Form wird Form, Balken wächst, Hand schreibt) | 0,6 bis 2 s |
| Zahl oder Schlagwort | 15 % | ein großes Wort oder eine Zahl mit Einheit und Quelle | 1 bis 3 s |
| Rückzoom aufs Ganze | 15 % | alle Teile des Arguments in einem Bild, zum Schluss | 2 bis 4 s |

## Regler
Tempo der Stimme (2 bis 3,5 Wörter je Sekunde), Begriffe je Minute, Hauspalette aus dem Zug (passt der Grund nicht, nur Akzent und Licht), Schriftpaar des Hauses. Fest bleiben ein Begriff je Bild und höchstens vier Bedeutungsfarben. Der Zug nimmt die Hauspalette; trägt der Stil einen hellen Grund und das Haus einen dunklen (oder umgekehrt), tauscht er nur Akzent und Licht.

## Fallen
- Die Musik synthetisiert der Motor im selben HTML: nur als Stem ausgeben, ohne Mastering; das Bett liegt leise unter Stimme und Geräuschen.
- Keine Bilddateien im Stück: Fotos und Logos nur als eigene Eingabe des Menschen, nie aus dem Netz.
- Mehr als zwei Aussagen gleichzeitig machen aus der Grammatik eine Folienschau: Begriff für Begriff, der vorige wird Bild oder verschwindet.
- Jede Zahl braucht eine Quelle in `haus/fakten.md`; Beispieldaten der Motoren nie im Stück lassen.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `jsanim`, Stil `canvas`, Quelle im Motor `skills/javascript-animation/SKILL.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor jsanim --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/jsanim.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a cat chasing a vacuum cleaner around a flat“.

```json
{"seite": "jsanim/szene.html"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 2 bis 20 s, Schnitte je Sekunde 0,03 bis 0,5, Helligkeit 0,57 bis 0,9, Farbigkeit 0,07 bis 0,47, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
