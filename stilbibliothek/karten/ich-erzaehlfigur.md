---
id: ich-erzaehlfigur
name: "Ich-Erzählfigur"
familie: erklaergrammatik
kurz: "Die Stimme erzählt eine eigene Geschichte, eine einfache Figur springt zwischen Posen und friert, die Pointe sitzt im Schnitt auf das Gesicht."
kern: ["die Stimme ist Hauptdarsteller, das Bild antwortet", "Posenwechsel in 0,1 s, dann Halt", "Pointe als Schnitt auf die Reaktion, kurz Stille"]
energie: 4
format_quelle: "9:16"
laenge_s: [20, 90]
bauweg: animskill
animskill:
  motor: huashu
  stil: "y4_storytime"
  quelle: "references/动画语法/y4_storytime.md"
  schrift: [grotesk, mono]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Figuren, Stimmen und Beispielbilder des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 1.6
  schnitte_pro_s: 0.6
  ereignisse_pro_s: 1.4
  lufs: -14
  helligkeit: 0.78
  farbigkeit: 0.22
palette:
  grund: "#F7F7F2"
  text: "#1A1A1A"
  akzent: "#F25F5C"
  licht: "#FFE066"
effekte: [sprechstimme, untertitel, aktivwort, geraeusche, erzaehlerfigur, posen-auf-beat, harter-schnitt, ton-stopp]
kamera: "Ruhig: steht oder fährt dem Argument nach, Bewegung kommt aus Verwandlung und Wachstum auf das Wort."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, hook]
zweck: [geschichte, person-vorstellen]
branchen_passt: [bildung, musik-kultur]
branchen_nie: []
abnahme:
  shot_median_s: [0.5, 6]
  schnitte_pro_s: [0.15, 1.5]
  helligkeit: [0.6, 0.93]
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
# Ich-Erzählfigur

Die Stimme erzählt eine eigene Geschichte, eine einfache Figur springt zwischen Posen und friert, die Pointe sitzt im Schnitt auf das Gesicht. Die Stimme trägt, das Bild antwortet auf jedes Stichwort und steht dann still; Verständnis ist die Energie.

## Kern
- Die Stimme ist Hauptdarsteller, das Bild antwortet.
- Posenwechsel in 0,1 s, dann Halt.
- Pointe als Schnitt auf die Reaktion, kurz Stille.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Einfache gezeichnete Figur, Posenwechsel in 0,1 s, dann Halt; Pointe als Schnitt auf die Reaktion in Großaufnahme mit Schweigen. Farben: grund `#F7F7F2`, text `#1A1A1A`, akzent `#F25F5C`, licht `#FFE066`.
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
- Für dichte Anleitungen und Zahlen falsch: der Zuschauer wartet auf den Lacher und merkt sich keine Zahl.
- Die Grammatik braucht eigene Figurenbilder (Posen, Münder, Reaktion); ohne sie zeichnet der Motor nur Platzhalter. Eigene Figur aus Code oder eigene Bilder mitbringen.
- Zu wenig Bewegung im Bild ist die häufigste Schwäche des Motors: vor der Abgabe `film_gate.py` des Motors laufen lassen; unter 0,06 schnellen Bewegungsbildern wirkt das Stück wie eine Folienschau.
- Ein Grund aus Blau und Violett über ein Drittel der Bilder fällt im `film_gate.py` durch; nur wenn der Stil es selbst verlangt, mit Begründung freigeben.
- Mehr als zwei Aussagen gleichzeitig machen aus der Grammatik eine Folienschau: Begriff für Begriff, der vorige wird Bild oder verschwindet.
- Jede Zahl braucht eine Quelle in `haus/fakten.md`; Beispieldaten der Motoren nie im Stück lassen.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `huashu`, Stil `y4_storytime`, Quelle im Motor `references/动画语法/y4_storytime.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor huashu --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/huashu.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a tiny avatar realising the oven is still on“.

```json
{"grammatik": "y4_storytime", "cues": [{"wort": "<Stichwort>", "kind": "draw", "text": "<Wort>"}], "safe": {"bottom": 300}}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 0,5 bis 6 s, Schnitte je Sekunde 0,15 bis 1,5, Helligkeit 0,6 bis 0,93, Farbigkeit 0,07 bis 0,47, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei. Dazu `film_gate.py` des Motors grün oder gelb.
