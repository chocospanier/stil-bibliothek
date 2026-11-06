---
id: formwandel-dunkel
name: "Formwandel im Dunkeln"
familie: erklaergrammatik
kurz: "Mathematik und Begriffe nach Art von 3Blue1Brown: auf Schwarz steht nur das, wovon gerade die Rede ist, und verwandelt sich ohne Schnitt ins Nächste."
kern: ["auf Schwarz steht nur das eine Ding, von dem gerade die Rede ist", ein Begriff verwandelt sich ohne Schnitt in den nächsten, "Farbe ist der Name eines Begriffs, höchstens vier Farben"]
energie: 2
format_quelle: "9:16"
laenge_s: [20, 90]
bauweg: animskill
animskill:
  motor: huashu
  stil: "t1_3b1b"
  quelle: "references/动画语法/t1_3b1b.md"
  schrift: [grotesk, mono]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Figuren, Stimmen und Beispielbilder des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 10
  schnitte_pro_s: 0.08
  ereignisse_pro_s: 0.8
  lufs: -14
  helligkeit: 0.3
  farbigkeit: 0.21
palette:
  grund: "#0E1116"
  text: "#ECEFF4"
  akzent: "#58C4DD"
  licht: "#FFD166"
  rot: "#FC6255"
effekte: [sprechstimme, untertitel, aktivwort, geraeusche, formwandel, kamera-steht]
kamera: "Ruhig: steht oder fährt dem Argument nach, Bewegung kommt aus Verwandlung und Wachstum auf das Wort."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, hook]
zweck: [erklaeren, wissen]
branchen_passt: [bildung, technik, finanzen]
branchen_nie: [mode-beauty, lebensmittel-feinkost]
abnahme:
  shot_median_s: [4, 40]
  schnitte_pro_s: [0.0, 0.25]
  helligkeit: [0.12, 0.45]
  farbigkeit: [0.06, 0.46]
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
# Formwandel im Dunkeln

Mathematik und Begriffe nach Art von 3Blue1Brown: auf Schwarz steht nur das, wovon gerade die Rede ist, und verwandelt sich ohne Schnitt ins Nächste. Die Stimme trägt, das Bild antwortet auf jedes Stichwort und steht dann still; Verständnis ist die Energie.

## Kern
- Auf Schwarz steht nur das eine Ding, von dem gerade die Rede ist.
- Ein Begriff verwandelt sich ohne Schnitt in den nächsten.
- Farbe ist der Name eines Begriffs, höchstens vier Farben.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Schwarzer Grund, nur das eine Ding, von dem die Rede ist, weiche Verwandlungen, Farbe als Name eines Begriffs. Farben: grund `#0E1116`, text `#ECEFF4`, akzent `#58C4DD`, licht `#FFD166`, rot `#FC6255`.
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
- Wer den Satz „was wird zu was“ nicht schreiben kann, nimmt eine andere Grammatik (Schlagwortbühne oder Tafelbild).
- Zu wenig Bewegung im Bild ist die häufigste Schwäche des Motors: vor der Abgabe `film_gate.py` des Motors laufen lassen; unter 0,06 schnellen Bewegungsbildern wirkt das Stück wie eine Folienschau.
- Ein Grund aus Blau und Violett über ein Drittel der Bilder fällt im `film_gate.py` durch; nur wenn der Stil es selbst verlangt, mit Begründung freigeben.
- Mehr als zwei Aussagen gleichzeitig machen aus der Grammatik eine Folienschau: Begriff für Begriff, der vorige wird Bild oder verschwindet.
- Jede Zahl braucht eine Quelle in `haus/fakten.md`; Beispieldaten der Motoren nie im Stück lassen.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `huashu`, Stil `t1_3b1b`, Quelle im Motor `references/动画语法/t1_3b1b.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor huashu --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/huashu.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a square grid bending into a circle“.

```json
{"grammatik": "t1_3b1b", "cues": [{"wort": "<Stichwort>", "kind": "draw", "text": "<Wort>"}], "safe": {"bottom": 300}}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 4 bis 40 s, Schnitte je Sekunde 0,0 bis 0,25, Helligkeit 0,12 bis 0,45, Farbigkeit 0,06 bis 0,46, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei. Dazu `film_gate.py` des Motors grün oder gelb.
