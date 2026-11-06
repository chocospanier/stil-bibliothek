---
id: buehnenoberflaeche
name: "Bühnenoberfläche"
familie: erklaergrammatik
kurz: "Eine Produktvorstellung wie auf großer Bühne: ein Ding je Bild, das echte Produkt groß, Namen und Zahlen setzen sich genau auf das Wort."
kern: ["eine Sache je Bild, das Produkt füllt mindestens 80 % der Breite", Namen und Zahlen landen genau auf dem gesprochenen Wort, "Schrift eng gesetzt, Federn ohne oder mit leichtem Rückschwung"]
energie: 3
format_quelle: "9:16"
laenge_s: [20, 90]
bauweg: animskill
animskill:
  motor: huashu
  stil: "t2_keynote_ui"
  quelle: "references/动画语法/t2_keynote_ui.md"
  schrift: [grotesk, mono]
lizenz: "MIT; Urheberhinweis in LIZENZ.md, Figuren, Stimmen und Beispielbilder des Motors nicht verwenden"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 4
  schnitte_pro_s: 0.2
  ereignisse_pro_s: 1.0
  lufs: -14
  helligkeit: 0.76
  farbigkeit: 0.3
palette:
  grund: "#F5F5F7"
  text: "#1D1D1F"
  akzent: "#0A84FF"
  licht: "#FF9F0A"
effekte: [sprechstimme, untertitel, aktivwort, geraeusche, ui-attrappe, push-in, zahl-walze]
kamera: "Ruhig: steht oder fährt dem Argument nach, Bewegung kommt aus Verwandlung und Wachstum auf das Wort."
ton: "Leises Bett aus Code-Musik (allein um −24 LUFS), darüber kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung, die Stimme trägt; gesamt −14 LUFS, der Schluss klingt hell statt mit einem Schlag."
braucht: [nur-typo, produkt]
motor_aufwand: klein
einsatz: [ganzes-kurzvideo, hook]
zweck: [produktwerbung, erklaeren, event-teaser]
branchen_passt: [technik, finanzen, bildung]
branchen_nie: [kinder-familie]
abnahme:
  shot_median_s: [2, 20]
  schnitte_pro_s: [0.03, 0.5]
  helligkeit: [0.58, 0.91]
  farbigkeit: [0.1, 0.62]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: eingeschraenkt
creator_ohne: [ui-attrappe]
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
# Bühnenoberfläche

Eine Produktvorstellung wie auf großer Bühne: ein Ding je Bild, das echte Produkt groß, Namen und Zahlen setzen sich genau auf das Wort. Die Stimme trägt, das Bild antwortet auf jedes Stichwort und steht dann still; Verständnis ist die Energie.

## Kern
- Eine Sache je Bild, das Produkt füllt mindestens 80 % der Breite.
- Namen und Zahlen landen genau auf dem gesprochenen Wort.
- Schrift eng gesetzt, Federn ohne oder mit leichtem Rückschwung.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** Eine Sache je Bild, Bildschirmaufnahme oder Gegenstand groß, Namen und Zahlen landen auf das Wort, Glas und Lichtflecken nur sparsam. Farben: grund `#F5F5F7`, text `#1D1D1F`, akzent `#0A84FF`, licht `#FF9F0A`.
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
- Lichtfleck-Grund, Milchglas, Verlaufsschrift, Aufblühen aus der Unschärfe und schwebende Karten zusammen sehen aus wie eine Vorlage: höchstens zwei davon je Stück.
- Zu wenig Bewegung im Bild ist die häufigste Schwäche des Motors: vor der Abgabe `film_gate.py` des Motors laufen lassen; unter 0,06 schnellen Bewegungsbildern wirkt das Stück wie eine Folienschau.
- Ein Grund aus Blau und Violett über ein Drittel der Bilder fällt im `film_gate.py` durch; nur wenn der Stil es selbst verlangt, mit Begründung freigeben.
- Mehr als zwei Aussagen gleichzeitig machen aus der Grammatik eine Folienschau: Begriff für Begriff, der vorige wird Bild oder verschwindet.
- Jede Zahl braucht eine Quelle in `haus/fakten.md`; Beispieldaten der Motoren nie im Stück lassen.
- Creator-Modus: ohne `ui-attrappe` bauen; geht der Stil dann nicht mehr, eine andere Karte würfeln.

## Ton
Der Motor liefert Musik und Geräusche aus Code als getrennte Stems. Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS) und schweigt im Atem vor der Pointe. Geräusche: kurzer Klick oder Plopp auf jedes erscheinende Element, ein Wisch auf jeder Verwandlung. Jedes Stück mit Text bekommt eine Stimme (Wortzeiten aus der Aufnahme, Szenen auf Wortanfänge). Gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell (Glocke, Akkord, Glanz). Gemischt wird mit `ton_standard.py`, aus den ungemasterten Stems des Motors.

## Bauweg
Zeichen-Motor `huashu`, Stil `t2_keynote_ui`, Quelle im Motor `references/动画语法/t2_keynote_ui.md`. Kein Remotion-Bau: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf` mit Palette und Schrift des Zugs.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor huashu --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec`, Gerüst wie im Würfel-Entwurf (alle Schlüssel im Kopf von `starter/werkzeuge/animskills/motoren/huashu.py`). Die genannte Datei schreibst du nach dieser Karte, mit Palette und Schrift aus `motor_spec_entwurf.vorgabe`; Bildidee für den Anfang: „a phone screen zooming into one button“.

```json
{"grammatik": "t2_keynote_ui", "cues": [{"wort": "<Stichwort>", "kind": "draw", "text": "<Wort>"}], "safe": {"bottom": 300}}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 2 bis 20 s, Schnitte je Sekunde 0,03 bis 0,5, Helligkeit 0,58 bis 0,91, Farbigkeit 0,1 bis 0,62, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Die Spannen sind aus der Palette gerechnet: fällt ein Wert knapp heraus, entscheidet das Auge. Am Standbild: drei zufällige Bilder zeigen alle drei Kern-Merkmale, in jeder Sekunde ändert sich etwas, das untere Sechstel ist frei. Dazu `film_gate.py` des Motors grün oder gelb.
