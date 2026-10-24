---
id: projektor-farbsprung
name: Projektor-Farbsprung
familie: glitch
kurz: Rasante Drei-Frame-Schnitte aus einfarbig getönten Aufnahmen, Lichtlecks, Flares und kinetischen Wörtern, anfangs im Fenster eines Filmprojektors, mit Messkurven über Gesichtern und einem langen, stillen Ausklang.
kern: [jede Einstellung in einer anderen Tönung (Türkis, Rot, Violett, Blau, Sepia) oder invertiert, Drei-Frame-Schnitt auf Worte statt auf den Beat, Typo als Bildmaterial (Riesenwort, Pixelschrift, Zeilenwiederholung, Glitch-Wort)]
energie: 5
format_quelle: "16:10"
laenge_s: [12, 20]
messung:
  shot_median_s: 0.10
  schnitte_pro_s: 4.9
  schnitte_verlauf: [5.7, 6.6, 2.2]
  bpm: 91
  schnitt_auf_beat: niedrig
  lufs: -7.9
  helligkeit: 0.24
  kontrast: 0.22
  farbigkeit: 0.11
schnittmuster_16tel: [2, 0, 0, 2, 2, 3, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 2, 3, 1, 2, 0, 0, 0, 1, 0, 3, 0, 1, 1, 2, 1, 1, 0, 0, 1, 0, 1, 4, 0, 2]
palette:
  schwarz: "#070607"
  grau: "#6B6A6E"
  hell: "#DAE2E1"
  tuerkis: "#7EC6BD"
  rot: "#B61219"
  violett: "#3B227A"
  blau: "#3566A8"
  sepia: "#B58762"
effekte: [harter-schnitt, blitzbild, glitch-uebergang, wischer, stottern, filmriss, masken-wechsel, bild-im-bild, wort-schnitt, invertieren, chroma-versatz, glow, vignette, filmkorn, bewegungsunschaerfe, hud, freisteller, ausschnitt-kante, text-hinter-figur, handschrift, wortkolonne, mono-zeile, titelkarte, sprechstimme, rahmen-rund, farbwelt-je-shot]
kamera: Kaum eigene Bewegung; Dynamik aus verwischten Clips, Lichtstreifen, leichtem Bildstandwackeln im Projektor-Fenster und Zoom-Wischern.
ton: Extrem laut gemischt (−7,9 LUFS, Spitzen über 0 dBFS), Raster um 91 BPM, Schnitte folgen eher Worten; nach den eingeblendeten Begriffen vermutlich eine Sprechstimme über einem Beat.
braucht: [fotos-figur, footage-ort, nur-typo]
motor_aufwand: mittel
einsatz: [hook, trailer, intro]
abnahme:
  shot_median_s: [0.08, 0.13]
  schnitte_pro_s: [3.9, 5.9]
  helligkeit: [0.19, 0.29]
  farbigkeit: [0.09, 0.14]
  lufs: [-8.9, -6.9]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Projektor-Farbsprung

Ein Technik-Trailer, der wie ein Filmprojektor im Fieber aussieht: jede Einstellung in einer anderen Farbe getönt, drei Frames lang, dazwischen Lichtlecks, Flares und Wörter, die das Gesagte groß ins Bild stellen. Die Energie kommt aus der Dichte und dem Farbwechsel; die Wirkung aus dem langen stillen Schluss.

## Kern
- **Tönungswechsel:** Fast jede Einstellung ist einfarbig getönt: Türkis, Rot, Violett, Blau oder Sepia, oder invertiert. Zwei aufeinanderfolgende Einstellungen haben nie dieselbe Tönung.
- **Drei-Frame-Schnitt auf Worte:** Median 0,10 s, also drei Frames bei 30 fps. Die Schnitte liegen kaum auf dem Beat (30 % gegen 24 % Zufall), sondern auf gesprochenen Begriffen, die zugleich als Text erscheinen.
- **Typo als Bild:** Ein Riesenwort über die ganze Breite, Pixelschrift, eine Zeile, die sich wiederholt, ein Wort mit Glitch-Versatz, ein Pinselwort hinter einer freigestellten Figur. Text ist Material, keine Untertitelung.

## Erkennung
- **Bild:** Grund Schwarz `#070607`. Tönungen: Türkis `#7EC6BD`, Rot `#B61219`, Violett `#3B227A`, Blau `#3566A8`, Sepia `#B58762`, dazu Grau `#6B6A6E` und Hell `#DAE2E1`. Die ersten zwei Sekunden laufen in einem Projektor-Fenster mit abgerundeten Ecken, roten Randmarken und kleiner senkrechter Randschrift. Dünne gestrichelte Kurven, Koordinaten und eine Namenszeile liegen über Gesichtern. Lichtlecks in Orange, ein Lichtpunkt mit langem waagerechtem Flare in Violett, Bokeh, Bewegungsunschärfe als Farbfläche. Zeilen-Glitch (rote Zeilenstreifen, versetzte Bänder). Einmal eine freigestellte Figur mit weißem Rand auf Papier vor einem Pinselwort, daneben ein kleines gerahmtes Foto. Gemessen: Helligkeit 0,24, Kontrast 0,22, Farbigkeit 0,11, 58 % fast schwarz.
- **Schnitt:** 66 Schnitte in 13,6 Sekunden, Median 0,10 s, Mittel 0,23 s; die letzte Einstellung steht 3,7 s. Dichte 5,7 → 6,6 → 2,2 Schnitte je Sekunde. Übergänge: harter Schnitt, Invertier-Blitz, Zeilen-Glitch, Lichtleck, Kreisvignette, Weißbild, Stottern (dieselbe Einstellung in drei Tönungen hintereinander).
- **Ton:** −7,9 LUFS, Lautheitsspanne 4,1 LU, True Peak +3,0 dBFS (übersteuert). Schnitte auf Worte, nicht aufs Raster.
- **Text:** Riesenwort in breiter Grotesk über die volle Breite, angeschnitten; Pixelschrift-Wörter mit Person daneben; wiederholte Textzeile über einem Bild; Wort mit Glitch-Versatz auf Rot; Namenszeile neben dem Gesicht (zweites Wort in Rot); kleines kursives Wort auf Schwarz; Pinselwort hinter Figur; Schlusszeile klein mittig auf dunklem Rauch.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Getöntes Gesicht mit Messkurven | 25 % | Gesicht oder Profil 60 bis 100 % der Bildhöhe, links oder mittig, gestrichelte Kurven, Koordinaten und Namenszeile rechts | 3 bis 15 Frames |
| Kinetisches Wort | 15 % | Wort füllt 90 % der Breite oder Pixelschrift neben Person; wiederholte Zeile oben links | 3 bis 9 Frames |
| Lichtereignis | 15 % | Lichtleck, Flare-Punkt mittig mit waagerechtem Streifen, Lichtband, Lichtkreis | 2 bis 4 Frames |
| Farbfläche aus Bewegungsunschärfe | 10 % | ganzes Bild verwischt in einer Tönung | 2 bis 9 Frames |
| Insert Gerät oder Fahrzeug | 15 % | Objekt füllt 60 bis 100 % der Bildhöhe, oft angeschnitten, dreifach getönt | 2 bis 3 Frames je Tönung |
| Freisteller auf Papier | 5 % | Figur mittig 75 % der Bildhöhe mit weißem Rand, Pinselwort dahinter über die Breite, kleines Foto unten links | 12 Frames |
| Saal-Totale | 5 % | weit, Bühne mittig, im Rahmen oder invertiert | 3 bis 15 Frames |
| Leerbild und kleiner Text | 5 % | Schwarz, Weiß oder Papier, ein kleines Wort mittig | 2 bis 21 Frames |
| Ruhiger Ausklang | 5 % | dunkler Rauch, eine kleine Zeile mittig | 3,7 s |

## Dramaturgie
- **Hook (0 bis 2,3 s):** 0,4 s Schwarz, dann im Projektor-Fenster: Naturmotiv mit Zeilen-Glitch, Riesenwort, Insert, wiederholte Textzeile über einer Fahrt, Profil mit Glitch, Messkurven, Wort auf Rot.
- **Personen (2,3 bis 4,4 s):** Lichtleck, Pixelwort mit Person, Sepia-Porträt mit Namenszeile, Blau-Porträt, Flare-Punkt dreimal.
- **Rausch (4,4 bis 6,4 s):** Lichtstreifen, Bokeh, rote Unschärfe, Inserts, Pixel-Zahlen. Dichteste Stelle.
- **Atem (6,5 bis 7,2 s):** Schwarz mit kleinem Wort.
- **Ort (7,2 bis 9,9 s):** Papier, Freisteller vor Pinselwort, Saal in drei Tönungen, Person in Blau und invertiert, Kreisvignette, Lichtband, Gerät dreifach getönt, Weiß.
- **Ausklang (9,9 bis 13,6 s):** dunkler Rauch, eine kleine Zeile, dann zwei Namen. Kein Schnitt mehr.

## Schnittmuster
Bauplan für 15 s in Sekunden, weil der Stil auf Worte schneidet: Wortanfänge der Sprechstimme markieren, dann Bilder von drei bis neun Frames dazwischen setzen.

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0,0-0,4 | Schwarz | hart | Stille |
| 2 | 0,4-1,2 | Projektor-Fenster: Naturmotiv mit Zeilen-Glitch, Riesenwort, Insert | hart | erstes Wort |
| 3 | 1,2-2,0 | Fahrt mit wiederholter Textzeile, Profil mit Glitch-Bändern | Glitch | Stimme |
| 4 | 2,0-2,4 | Profil mit Wort auf der Wange und Messkurven, Glitch-Wort auf Rot | hart | Schlüsselwort |
| 5 | 2,4-3,1 | Lichtleck, Pixelwort neben Person, zweimal | Filmriss | Beat |
| 6 | 3,1-4,1 | Porträt Sepia mit Namenszeile, dann Blau | hart | Name |
| 7 | 4,1-4,5 | Flare-Punkt dunkel, invertiert, dunkel | Blitzbild | Hits |
| 8 | 4,5-5,5 | Lichtstreifen, Bokeh, rote Unschärfe | Wischer | Beat |
| 9 | 5,5-6,5 | Inserts, Pixel-Zahlen in Türkis und Gelb | hart | Ticks |
| 10 | 6,5-7,2 | Schwarz mit kleinem Wort | hart | Atem, Stimme |
| 11 | 7,2-7,7 | Papier, Freisteller mit Pinselwort dahinter | hart | Hit |
| 12 | 7,7-8,4 | Saal im Rahmen, invertiert, violett | Stottern | Stimme |
| 13 | 8,4-9,0 | Person blau, invertiert, Kreisvignette türkis | Stottern | Beat |
| 14 | 9,0-9,9 | Lichtkreis, Lichtband, Gerät dreifach getönt, Weiß | Blitzbild | Hits |
| 15 | 9,9-15,0 | dunkler Rauch, kleine Zeile, dann Schlusskarte | Blende | Stimme allein, Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Schwarz `#070607`, Korn 5 %, leichtes Helligkeitsflimmern ±4 % je Frame.
- **Bildbehandlung:** Entsättigen, dann je Einstellung eine Tönungstabelle Schwarz → Tönung → Weiß (`feComponentTransfer` mit `type="table"`), Reihenfolge so wählen, dass nie zweimal dieselbe folgt; 20 % der Einstellungen invertiert. Chroma-Versatz an Kanten (Rot +0,3 %, Blau −0,3 % waagerecht). Vignette 25 %.
- **Bausteine:** Projektor-Fenster (Bild in abgerundetem Rechteck 85 % × 90 %, Eckenradius 2 % der Bildhöhe, auf Schwarz; links senkrechte rote Randschrift 1 % der Bildhöhe, rechts kleine rote Dreiecke; Bildstand wackelt ±0,3 % je Frame); Zeilen-Glitch (zwei bis vier Bänder 5 bis 20 % der Bildhöhe versetzt, dazu ein Feld roter waagerechter Striche am linken Rand, zwei Frames); Messkurven (zwei bis drei gestrichelte Bézierkurven 1 px weiß 60 %, Koordinaten-Paare in Mono 1 % der Bildhöhe an den Enden); Namenszeile (breite Grotesk 4 % der Bildhöhe, zweites Wort in Rot); Lichtleck (zwei bis drei orange Flecken, `screen` 60 %, wandern); Flare-Punkt (weißer Kern 2 %, waagerechter Streifen 60 % der Breite in `#7B3FD0`); Freisteller (weißer Rand 0,6 %, Papiergrund mit Verlauf, Pinselwort dahinter 40 % der Bildhöhe, kleines Foto mit weißem Rahmen 15 % der Breite unten links); Letterbox-Balken 8 % oben und unten bei jeder dritten Einstellung.
- **Typografie:** Riesenwort in breiter fetter Grotesk (frei lizenziert zum Beispiel Archivo Expanded 800), türkis auf Weiß, angeschnitten. Pixelwörter in Pixelschrift (zum Beispiel Silkscreen 700), 7 % der Bildhöhe. Wiederholte Zeile in schmaler Grotesk, drei bis vier Zeilen, mit Bewegungsunschärfe. Pinselwort (zum Beispiel Permanent Marker). Kleine Wörter in Kursiv (zum Beispiel Inter Italic 400), 2 % der Bildhöhe.
- **Bewegung:** Zustände drei bis neun Frames, im Rausch nur drei. Wörter erscheinen hart mit dem gesprochenen Wort. Ausklang ohne Schnitt mindestens 3 s, Rauch driftet langsam.
- **Formate:** Quelle 16:10. In 9:16 Projektor-Fenster hochkant (80 % × 70 %), Riesenwort zweizeilig, Messkurven über das Gesicht im oberen Drittel, Namenszeile darunter; Letterbox-Balken weglassen. In 16:9 wie die Quelle.
- **Neue Kennungen:** `neu:projektor-fenster`: Das Bild läuft in einem abgerundeten Rahmen mit Randmarken wie in einem Projektor. `neu:toenung-wechsel`: Jede Einstellung hat eine andere einfarbige Tönung.

## Material
- **Bilder (Person):** `grainy 16mm film still of [subject] speaking on stage, side light, shallow depth of field, slight motion blur, dark background, documentary feel`
- **Bilder (Insert):** `close-up of [subject] in motion with strong motion blur and light streaks, night, grainy film, shallow depth of field`
- **Musik:** `Driving dark electronic bed for a spoken-word tech trailer, 91 BPM, pulsing bass, glitchy percussion, tape stops, risers, very dense for the first six seconds, short drop to silence at six point five seconds, second burst from seven point two seconds, from nine point nine seconds only an airy pad, instrumental, no vocals`
- **Geräusche:** Projektor-Rattern unter dem Fenster (−20 dB), Glitch-Zirpen bei Zeilenversatz, Whoosh bei Lichtstreifen; 8 bis 12 dB unter Stimme und Musik.

## Regler
- Tönungen: drei bis sechs; zwei Tönungen machen es ruhiger, mehr als sechs wirkt bunt.
- Länge des Projektor-Fensters: nur Hook bis ganzes Stück.
- Schnittdichte: drei bis sechs Frames je Zustand; unter drei flimmert es nur.
- Mit eigener Sprechstimme wird es ein Kanal-Hook; Schlüsselwörter der Stimme als kinetische Wörter.
- Ausklang: 2 bis 4 s; ohne ihn fehlt die Landung.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; die Lautheit nur so hoch, wie der Kanal verträgt (siehe Fallen).
- Standbild-Prüfung: zwei Nachbar-Einstellungen nie in gleicher Tönung; jedes kinetische Wort entspricht einem gesprochenen Wort.
- Streifen bei 12 fps: im Rausch kein Zustand unter drei Frames; der Ausklang steht still.

## Fallen
- Drei-Frame-Schnitte mit Invertierung über Sekunden sind eine Epilepsie-Gefahr → Rausch-Strecken kürzer als 2 s, Invertier-Blitze höchstens drei je Sekunde.
- Übersteuerung der Vorlage übernehmen → laut ja, aber höchstens −1 dBTP; für Plattformen mit Lautheitsnormalisierung bringt mehr als −9 LUFS nichts.
- Echte Personen, Firmennamen und Logos → nur eigene Aufnahmen oder Figuren, Namen nur mit Rechten.
- Tönung als halbtransparenter Farbfilter → wirkt matschig; erst entsättigen, dann Tabelle.
- Wörter auf den Beat statt aufs Wort → passt nicht zur Stimme; hier entscheidet die Sprache.
