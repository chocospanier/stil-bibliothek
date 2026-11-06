---
id: detail-zoom
name: Detail-Zoom
familie: produktspot
kurz: Eine ruhige Kamerafahrt über ein echtes Produktfoto; Bild 0 zeigt das ganze Produkt mit dem Hook, dann fährt die Kamera nacheinander in Ausschnitte, ein Ring markiert die Stelle, eine dünne Linie führt zum Merkmal im Infofeld; Rückzug aufs ganze Produkt mit Preis und Schlusskarte.
kern: [eine einzige Kamera über einem unveränderten Produktfoto mit Makro-Ausschnitten und sanftem Push, je Ausschnitt Ring plus dünne Hinweislinie zu einem Merkmal in großer schmaler Grotesk, Rückzug aufs ganze Produkt vor Preis und Schlusskarte]
energie: 2
format_quelle: "9:16"
laenge_s: [15, 25]
messung:
  shot_median_s: 22.5
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm: 100
  schnitt_auf_beat: hoch
  lufs: stumm gemessen
  helligkeit: 0.162
  kontrast: 0.197
  farbigkeit: 0.066
schnittmuster_16tel: [10, 12, 12, 12, 12, 14]
palette:
  grund: "#111111"
  text: "#FFFFFF"
  akzent: "#E3120B"
effekte: [push-in, kamera-steht, neu:kamerafahrt-foto, neu:hinweislinie, neu:preisschild, neu:infofeld]
kamera: Eine virtuelle Kamera über dem Foto; Fahrten von 0,75 s (ease-in-out, Zoom logarithmisch) zwischen den Merkmalen, in jedem Halt ein Push um 6 %, am Ende Rückzug in einer Sekunde.
ton: Optional eine fertige Mischung über das Prop ton; jede Fahrt beginnt auf dem Schlag, wenn takt gegeben ist, sonst auf einem 0,5-s-Raster.
braucht: [produkt]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo]
zweck: [produktwerbung, angebot]
branchen_passt: [werkstatt-auto, lebensmittel-feinkost, handwerk, technik, mode-beauty, sport]
branchen_nie: []
abnahme:
  shot_median_s: [10, 26]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.04, 0.93]
  farbigkeit: [0.0, 0.4]
  lufs: [-15, -13]
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 2]
  stottern_wiederholungen: [2, 2]
  push_in_prozent: [4, 8]
  wackeln_faktor: [0.0, 0.0]
  korn: [0.02, 0.04]
  vignette: [0.0, 0.2]
  beat_versatz_16tel: [0, 0]
  textgroesse_prozent: [-8, 8]
  textlage: regel
  musik: fest
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: grund
  hell: text
  licht: text
quelle: Eigener Entwurf nach dem Handwerk gängiger Detailanzeigen (Makrofahrt mit Merkmalen) in sozialen Netzen; keine Vorlage, keine Motive, Texte oder Marken übernommen.
---

# Detail-Zoom

Die Anzeige für Produkte, die man aus der Nähe verkaufen muss: Wer die Stelle sieht, glaubt das Merkmal. Die Energie ist ruhig und genau; sie kommt aus der Kamera, die sich Stelle für Stelle an das Produkt heranarbeitet, und aus dem Ring, der genau dort aufgeht, wo das Merkmal sitzt.

## Kern
- **Eine Kamera über dem echten Foto:** das Produktfoto wird nur verschoben und gleichmäßig skaliert, nie gefiltert. Der Zoom ist auf 2,2-fache Pixelvergrößerung des Fotos begrenzt, damit es scharf bleibt.
- **Ring und Hinweislinie:** auf der Stelle ein Ring in der Akzentfarbe mit Punkt und feinem Außenring, eine dünne Linie in der Textfarbe zieht zum Infofeld; dort das Merkmal in großer schmaler Grotesk, darunter eine kleine Erklärzeile.
- **Rückzug aufs Ganze:** nach den Merkmalen zieht die Kamera zurück, der Name steht über dem Produkt, das Preisschild springt an; danach die Schlusskarte mit Logo, Produkt, Knopf und Webadresse.

## Erkennung
- **Bild:** Bühne in der Grundfarbe mit Lichthof, das Produkt groß; in den Merkmalen ein festes Infofeld (Hochformat: untere 40 %, quer: rechte 45 %) in der Grundfarbe mit Haarlinie und kurzem Akzentbalken an der Kante.
- **Schnitt:** keine harten Schnitte; Fahrten, ein Rückzug und die Blende zur Schlusskarte.
- **Ton:** nach Bestellung; eine fertige Mischung über `ton`.
- **Text:** Hook über dem Produkt in Bild 0 (8,5 % der Bildhöhe), Merkmale 5,2 % in Versalien, Erklärzeile 2,6 % in der Lauftextschrift, gedämpfte Textfarbe.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Ganzes Produkt mit Hook | 12 % | Hook oben, Produkt 50 % der Höhe unten mittig | 2,2 bis 2,5 s |
| Makro mit Merkmal | 55 % | Stelle bei 31 % der Höhe (quer 28 % der Breite), Infofeld unten oder rechts | je 2,5 bis 3,5 s |
| Rückzug mit Preis | 15 % | Produkt links der Mitte, Name darüber, Schild rechts unten | 2,8 bis 3,0 s |
| Schlusskarte | 18 % | Logo, Produkt klein, Knopf, Webadresse | 3,2 bis 4,0 s |

## Dramaturgie
0 bis 2,5 s Hook mit ganzem Produkt (Bild 0), dann drei Merkmale zu je rund 3 s, jedes mit Fahrt, Ring, Linie, Text; 12 bis 15 s Rückzug, Name, Preis, Lichtstreif; ab 15 s Schlusskarte mit langsamem Push-in.

## Schnittmuster
Bei 100 BPM in Sechzehnteln; ohne `takt` ein 0,5-s-Raster. Wachsen dürfen die Merkmale und der Schluss.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 10 | Ganzes Produkt mit Hook | Hook geht nach oben, Kamera fährt | Einsatz |
| 2 | 12 (wächst) | Merkmal 1 | Fahrt 0,75 s, Infofeld steigt | Schlag auf der Ankunft |
| 3 | 12 (wächst) | Merkmal 2 | Fahrt | Schlag |
| 4 | 12 (wächst) | Merkmal 3 | Fahrt | Schlag |
| 5 | 12 | Rückzug mit Preis | Rückzug 1 s, Infofeld geht | Akzent auf dem Schild |
| 6 | 14 (wächst) | Schlusskarte | Blende 0,35 s | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** wie Produkt-Bühne (Grundfläche, Lichthof aus der Textrolle).
- **Bildbehandlung:** keine am Foto. Kamera als `translate(a - p·z) scale(z)` auf einer Weltebene; z wird logarithmisch gemischt, Stelle und Anker linear.
- **Bausteine:** `Buehne`, `Korn`; Ring und Linie als SVG; Infofeld, Preisschild, Schlusskarte aus `gemeinsam_p1.tsx`.
- **Typografie:** Barlow Condensed 800 (Merkmale, Hook), Inter 500 (Erklärzeile, Webadresse).
- **Bewegung:** Fahrt 0,75 s (0.65,0,0.35,1), Ring 0,35 s, Linie 0,4 s, Text 0,6 s, Abgang 0,3 s vor der nächsten Fahrt; Push 6 % mit sanfter Kurve.
- **Formate:** 9:16 Pflicht (`DetailZoom`), 16:9 und 1:1 (`DetailZoom-16x9`, `DetailZoom-1x1`): Stelle links, Infofeld rechts, waagerechte Hinweislinie.

## Material
- **Bilder:** echtes Produktfoto, freigestellt, möglichst groß (über 1500 px Höhe für tiefe Zooms); Merkmale als `x`, `y` in Prozent des freigestellten Bilds (eng beschnitten) angeben.
- **Musik:** "Calm premium product advertising track, 100 BPM, soft analog synth pulse, felt piano chords, light shaker, warm sub bass, gentle build from 2 seconds, a soft accent every 3 seconds for each detail shot, small lift at 13 seconds, clean resolved ending at 18 seconds, instrumental, no vocals"
- **Geräusche:** ein leiser Klick, wenn der Ring aufgeht.

## Regler
Zwei bis vier Merkmale; Zoom je Merkmal (1,2 bis 3; begrenzt durch die Bildgröße); Preis optional; Spiegelung im Rückzug; Hintergrundfoto optional.

## Abnahme
Zielwerte aus `abnahme` (eigene Basis, Beispiel Feldflasche, stumm). Augen-Prüfung: der Ring sitzt wirklich auf der Stelle, das Foto ist in der tiefsten Fahrt noch scharf, der Merkmaltext passt zum Ausschnitt, nichts in den unteren 15 %.

## Fallen
- Kleine Produktfotos werden in der Fahrt weich → der Motor begrenzt den Zoom auf 2,2-fache Pixelvergrößerung; ein Foto von 700 px Höhe erlaubt kaum mehr als 1,6-fach. Größere Fotos liefern.
- Ein Verlauf über dem Foto als Textgrund wäscht das Produkt aus (erster Testlauf 05.11.2026, helle Flasche wirkte milchig) → festes Infofeld in der Grundfarbe statt Schleier.
- Merkmal-Lage in Prozent bezieht sich auf das eng beschnittene Freistellbild, nicht auf das Originalfoto → nach dem Freistellen messen.
- Beispieltext in der Kundenfassung → das Beispiel steht unter `beispiel` in `props.json`; eigener Inhalt oben schaltet es ab.
- Merkmale, die man im Foto nicht sieht (Zertifikat, Datum) → als Erklärzeile zu einer sichtbaren Stelle (Siegel, Etikett) setzen, nicht auf leere Fläche.
- Ring neben dem Produkt auf leerem Grund (Testlauf Öl: x 30, y 30 lag neben der Flaschenschulter) → Lage am eng beschnittenen Freisteller messen, Ring auf eine sichtbare Stelle setzen.
- Leeres Infofeld während der Fahrt (Prüfrunde 1) → der Merkmaltext erscheint schon während der Fahrt, Ring und Linie nach der Ankunft.
- Standbild-Meldung der Vorprüfung auf glatten dunklen Flächen → im Halt schwenkt die Kamera zusätzlich 3 % seitlich, abwechselnd.
