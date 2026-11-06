---
id: formel-tafel
name: "Formel-Tafel"
familie: erklaergrammatik
kurz: "Formeln nach Art von 3Blue1Brown, gebaut mit Manim: eine Gleichung schreibt sich Glied für Glied, verwandelt sich, der Graph antwortet in derselben Farbe."
kern: [Formeln schreiben sich Glied für Glied und verwandeln sich ineinander, Graph und Formel teilen dieselben Farben, "dunkler Grund, ruhige Kamera, kaum Schnitte"]
energie: 2
format_quelle: "9:16"
laenge_s: [20, 90]
bauweg: animskill
animskill:
  motor: manim
  stil: "formel"
  quelle: "skills/manim-composer/SKILL.md"
  schrift: [serif, mono]
lizenz: "MIT (Manim Community und Skill); Urheberhinweis in LIZENZ.md"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 10
  schnitte_pro_s: 0.08
  ereignisse_pro_s: 0.8
  lufs: -14
  helligkeit: 0.34
  farbigkeit: 0.21
palette:
  grund: "#1C1C1C"
  text: "#FFFFFF"
  akzent: "#58C4DD"
  licht: "#F7D96F"
  rot: "#FC6255"
effekte: [sprechstimme, untertitel, aktivwort, geraeusche, formwandel, kamera-steht, diagramm-wachstum]
kamera: "Ruhig: steht oder fährt dem Argument nach, Bewegung kommt aus Verwandlung und Wachstum auf das Wort."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, hook]
zweck: [erklaeren, wissen]
branchen_passt: [bildung, technik, finanzen]
branchen_nie: [mode-beauty, lebensmittel-feinkost]
abnahme:
  shot_median_s: [4, 40]
  schnitte_pro_s: [0.0, 0.25]
  helligkeit: [0.16, 0.49]
  farbigkeit: [0.06, 0.45]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 3]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.3, 0.7]
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
  dunkel: grund
  hell: text
  licht: licht
quelle: Eigene Beschreibung eines offenen Zeichen-Motors (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken des Motors übernommen.
---
# Formel-Tafel

Formeln nach Art von 3Blue1Brown, gebaut mit Manim: eine Gleichung schreibt sich Glied für Glied, verwandelt sich, der Graph antwortet in derselben Farbe. Die Stimme trägt, das Bild antwortet auf jedes Stichwort und steht dann still; Verständnis ist die Energie.

## Kern
- Formeln schreiben sich Glied für Glied und verwandeln sich ineinander.
- Graph und Formel teilen dieselben Farben.
- Dunkler Grund, ruhige Kamera, kaum Schnitte.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Formeln und Graphen auf dunklem Grund, mit Manim gesetzt, Glied für Glied geschrieben und ineinander verwandelt. Farben: grund `#1C1C1C`, text `#FFFFFF`, akzent `#58C4DD`, licht `#F7D96F`, rot `#FC6255`.
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
- Gleiche Begriffe in Formel und Graph immer in derselben Farbe; eine Farbe für zwei Bedeutungen verwirrt sofort.
- Die Szene bringt ihre Länge selbst auf `ANIM_DAUER` und steht nie länger als 1 s still: lieber eine langsame Bewegung als `wait(3)`.
- Im Hochformat ist der Bildraum nur 4,5 Einheiten breit (16:9: 14,2): Formeln kleiner setzen oder untereinander, nie über den Rand.
- Formelsatz (MathTex) braucht das TinyTeX, das `einrichten.py` neben den Motor legt; fehlt es, bricht der Render mit Hinweis ab.
- Mehr als zwei Aussagen gleichzeitig machen aus der Grammatik eine Folienschau: Begriff für Begriff, der vorige wird Bild oder verschwindet.
- Jede Zahl braucht eine Quelle in `haus/fakten.md`; Beispieldaten der Motoren nie im Stück lassen.

## Ton
Dieser Motor liefert keinen Ton: das Bett kommt aus `musik.py` oder als Code-Musik eines anderen Motors, die Geräusche aus `taktbauer.py --nur-schlaege` oder eigenen Aufnahmen. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`.

## Bauweg
Zeichen-Motor `manim`, Stil `formel`, Quelle im Motor `skills/manim-composer/SKILL.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor manim --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/manim.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „the Pythagorean theorem rearranging squares“.

```json
{"szene": "manim/szene.py", "klasse": "Szene", "hintergrund": "#1C1C1C", "ende": "halten"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 4 bis 40 s, Schnitte je Sekunde 0,0 bis 0,25, Helligkeit 0,16 bis 0,49, Farbigkeit 0,06 bis 0,45, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei.
