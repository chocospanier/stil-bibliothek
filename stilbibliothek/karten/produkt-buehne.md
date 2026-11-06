---
id: produkt-buehne
name: Produkt-Bühne
familie: produktspot
kurz: Social-Media-Anzeige aus einem echten Produktfoto; groß gesetzte Frage auf der Markenfarbe, dann steht das freigestellte Produkt auf einem dunklen oder hellen Studioboden, ein Lichtstreif läuft darüber, Vorteile bauen sich als Liste auf, das Preisschild springt an, Schluss mit Logo und Knopf.
kern: [das echte Produktfoto als Held auf einem Studioboden mit weichem Kontaktschatten und Lichthof, Hook als gestapelte Plakatzeile auf der Akzentfarbe in Bild 0, Preis und Handlungsaufforderung als gestaltete Elemente in den Markenfarben]
energie: 3
format_quelle: "9:16"
laenge_s: [15, 25]
messung:
  shot_median_s: 17.5
  schnitte_pro_s: 0.0
  schnitte_verlauf: [0.0, 0.0, 0.0]
  bpm: 120
  schnitt_auf_beat: hoch
  lufs: stumm gemessen
  helligkeit: 0.174
  kontrast: 0.201
  farbigkeit: 0.279
schnittmuster_16tel: [8, 12, 8, 10, 8, 12, 14]
palette:
  grund: "#111111"
  text: "#FFFFFF"
  akzent: "#E3120B"
effekte: [push-in, titelkarte, kamera-steht, neu:lichtstreif, neu:kontaktschatten, neu:preisschild, neu:aufzaehlung]
kamera: Eine Bühne ohne Schnitt; das Produkt steigt auf seinen Boden und wandert zwischen drei Posen (Reveal, Vorteile, Preis), dazu ein langsamer Push-in auf Hook und Schlusskarte.
ton: Optional eine fertige Mischung (Musik mit oder ohne Stimme) über das Prop ton; Szenenwechsel auf dem Schlag, wenn takt gegeben ist, sonst auf einem 0,5-s-Raster.
braucht: [produkt]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo, hook]
zweck: [produktwerbung, angebot]
branchen_passt: [werkstatt-auto, lebensmittel-feinkost, handwerk, technik, mode-beauty, sport, gastro]
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
  push_in_prozent: [2, 5]
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
quelle: Eigener Entwurf nach dem Handwerk gängiger Produktanzeigen in sozialen Netzen (Hook, Packshot, Vorteile, Preis, Schlusskarte); keine Vorlage, keine Motive, Texte oder Marken übernommen.
---

# Produkt-Bühne

Die Standardanzeige eines Ladens, gut gemacht: eine Frage, die den Kunden abholt, dann das echte Produkt im Licht, drei Gründe, der Preis, wo es das gibt. Die Energie kommt nicht aus Effekten, sondern aus einer einzigen durchgehenden Bühne, auf der das Produkt seinen Platz wechselt, während die Information sich um es herum aufbaut.

## Kern
- **Echtes Produktfoto als Held:** freigestellt, nie gefiltert oder umgefärbt, auf einem Boden aus der Grundfarbe mit weichem Kontaktschatten, Lichthof dahinter und optional einer Spiegelung. Der Lichtstreif ist eine Ebene über dem Foto, auf seinen Umriss begrenzt. So sieht es nach Studioaufnahme aus, nicht nach ausgeschnittenem Bild.
- **Hook als Plakatzeile in Bild 0:** die Frage oder das Problemwort in einer kräftigen schmalen Grotesk, jede Zeile auf volle Breite gesetzt, auf der vollen Akzentfarbe. Das ist das Titelbild und der Daumenstopper.
- **Preis und Handlungsaufforderung gestaltet:** Preisschild auf dem Akzent, leicht gedreht, Cent hochgestellt, springt mit einer Feder an; Schlusskarte mit Logo, Produkt, Knopf in Akzentfarbe und Webadresse. Alle Farben aus drei Rollen (grund, text, akzent) und Mischungen davon.

## Erkennung
- **Bild:** zwei Flächen: die Akzentfläche des Hooks und die Bühne in der Grundfarbe mit Lichthof aus Text-Anteil (16 % auf dunklem Grund). Boden als weicher ovaler Schein unter dem Produkt, feine Bodenkante. Keine Texturen außer sehr leichtem Korn (3 %).
- **Schnitt:** genau zwei Wechsel: die Bühne schiebt sich von unten über den Hook (0,45 s), die Schlusskarte blendet über die Bühne (0,35 s). Dazwischen keine Schnitte, nur Umstellungen des Produkts (0,7 s, ease-in-out).
- **Ton:** nach Bestellung; eine fertige Mischung über `ton`. Szenengrenzen auf dem Schlag (`takt`).
- **Text:** Hook in Versalien, gestapelt, bis 21 % der Bildhöhe je Zeile; Produktname über dem Produkt (5,8 %); Vorteile als Liste mit Akzent-Quadrat (5 %), die aktuelle Zeile in Textfarbe, frühere gedämpft; Preis groß (10 % Höhe des Schilds); Webadresse in der Lauftextschrift.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Hook-Plakat | 12 % | Akzentfläche, zwei bis drei Zeilen links bündig, Block um 42 % der Höhe, Linie darunter | 2,0 bis 2,5 s |
| Reveal | 15 % | Produkt mittig, 40 % der Bildhöhe (schlanke Produkte 56 %), Name darüber, Lichtstreif | 2,5 bis 3,5 s |
| Vorteile | 35 % | breite Produkte oben (30 % Höhe), Liste darunter; schlanke Produkte rechts, Liste links | je Vorteil 2,0 bis 3,0 s |
| Preis | 15 % | Produkt links der Mitte, Schild rechts auf dem Boden | 2,6 bis 3,0 s |
| Schlusskarte | 20 % | Logo oben, Produkt klein, Knopf, Webadresse | 3,2 bis 4,0 s |

## Dramaturgie
0 bis 2 s Hook (Frage, Bild 0 fertig), 2 bis 5 s das Produkt steigt auf, Name, Lichtstreif; 5 bis 12 s Vorteile Zeile für Zeile; 12 bis 15 s Preis mit zweitem Lichtstreif; ab 15 s Schlusskarte mit langsamem Push-in bis zum Ende.

## Schnittmuster
Bei 120 BPM in Sechzehnteln (ein Schlag = vier Sechzehntel); ohne `takt` gilt ein 0,5-s-Raster. Wachsen dürfen Reveal und Schluss.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 8 | Hook-Plakat | Bühne schiebt sich von unten darüber | Einsatz |
| 2 | 12 (wächst) | Reveal | weich, Produkt steigt | erster Schlag auf der Landung |
| 3 | 8 | Vorteil 1 | Produkt fährt nach oben, Zeile gleitet ein | Schlag |
| 4 | 10 | Vorteil 2 | Zeile gleitet ein | Schlag |
| 5 | 8 | Vorteil 3 | Zeile gleitet ein | Schlag |
| 6 | 12 | Preis | Liste geht, Schild springt | Akzent |
| 7 | 14 (wächst) | Schlusskarte | Blende 0,35 s | Ausklang, Ton 0,5 s ausgeblendet |

## Rezept für einen Code-Motor
- **Grund:** Fläche in der Grundrolle, Lichthof als radialer Verlauf aus der Textrolle (Deckkraft über `color-mix`), Boden als ovaler Schein unter dem Produkt; optional ein Hintergrundfoto mit einem Schleier aus der Grundfarbe als eigener Ebene.
- **Bildbehandlung:** keine am Produkt und am Logo. Schatten zwei radiale Ellipsen in Schwarz; Spiegelung eine gespiegelte Kopie mit Maskenverlauf (20 %); Lichtstreif ein Verlauf im Mischmodus Screen, maskiert mit dem Alpha des Fotos.
- **Bausteine:** `Buehne`, `Korn`; eigene Teile in `gemeinsam_p1.tsx` (Grund, ProduktBild, Preisschild, Schlusskarte, Fehlerhinweis, Palette, Raster).
- **Typografie:** Barlow Condensed 800/700 (Titel, Würfelklasse schmal), Inter 500/700 (Lauftext, Klasse grotesk). Größen in Prozent der Bildhöhe, Breite gemessen und eingepasst.
- **Bewegung:** drei Kurven (Auftritt 0.16,1,0.3,1; Abgang 0.7,0,0.84,0; Fahrt 0.65,0,0.35,1), drei Dauern (0,35 / 0,6 / 1,0 s); keine linearen Bewegungen außer dem Lichtstreif (sanfte Kurve).
- **Formate:** 9:16 Pflicht (`ProduktBuehne`); 16:9 (`ProduktBuehne-16x9`) und 1:1 (`ProduktBuehne-1x1`): Hook links, Produkt rechts, Liste links neben dem Produkt, Schlusskarte mit Produkt links.

## Material
- **Bilder:** echtes Produktfoto, freigestellt (PNG mit Alpha, eng beschnitten, mindestens 1000 px hoch). Freistellen mit `werkzeuge/freistellen.py` oder rembg (Modell isnet-general-use). Logo als PNG oder SVG; Logos, die auf dunklem Grund untergehen, mit `logoPlatte: true`.
- **Musik:** "Confident modern advertising track, 120 BPM, tight punchy kick and clap, muted electric guitar stabs, warm bass, short riser into a clear drop at 2 seconds, steady groove for 12 seconds, small break at 13 seconds, clean ending with a final hit at 17 seconds, instrumental, no vocals"
- **Geräusche:** ein kurzer Akzent (Klick oder Hit) auf dem Preisschild, leise unter der Musik.

## Regler
Hook als Frage oder Problemwort; zwei bis vier Vorteile; Preis optional (fehlt er, entfällt die Szene); Spiegelung an oder aus; Hintergrundfoto optional; Produkthöhe (`produktHoehe`). Hell oder dunkel: der Motor trägt beide Gründe, Kontrast Text zu Grund wird auf mindestens 4,5 gehalten.

## Abnahme
Zielwerte aus `abnahme` (gemessen an der eigenen Basis, Beispiel Feldflasche, stumm). Die Fenster für Helligkeit und Farbigkeit sind weit, weil Markenfarben den Grund bestimmen (Werkstatt dunkel, Feinkost hell). Augen-Prüfung am Standbild: Produkt nirgends gefiltert oder verzerrt, Preis und Webadresse fehlerfrei, kein Text in den unteren 15 %, Hook in Bild 0 vollständig.
Formatfest sind Schnitte je Sekunde, Shot-Median und LUFS. Helligkeit und Farbigkeit hängen vom Format ab.

## Fallen
- Freisteller mit Rand oder Resten der weißen Fläche → am dunklen und am hellen Grund in voller Größe ansehen, bevor es ins Stück kommt (Fremdtest 6: ausgefranster LED-Ring war der einzige gemeinsame Blocker).
- Schwarzes Produkt auf schwarzem Grund verschwindet → Lichthof und Boden tragen es; bei sehr dunklen Produkten die Grundfarbe nicht unter #0E0E0E wählen.
- Beispieltext in der Kundenfassung → das Beispiel steht in `props.json` unter `beispiel`; sobald eigener Inhalt oben steht, gilt nur er, fehlende Pflichtfelder zeigen einen roten Hinweis.
- Preis ohne Beleg → nur Preise aus `haus/fakten.md` oder der Bestellung; ohne Preis bleibt `preis` weg.
- Remotion mischt `defaultProps` mit eigenen Props → darum liegt das Beispiel nie oben in den Props (sonst rutscht ein Beispielpreis in ein Video ohne Preis; erster Testlauf 05.11.2026).
- Lange Vorteile werden klein → höchstens fünf Wörter je Vorteil; bei schlanken Produkten bricht der Motor in zwei Zeilen um.
- Gleichzeitiges Rendern mit demselben `--public-dir` → beim ersten Lauf kopiert render.mjs die Korn-Kacheln; zwei Läufe zugleich stoßen beim Kopieren zusammen (EBUSY). Erst einen Lauf starten.
- Bild 0 nur Schrift auf der Akzentfläche wirkt leer (Prüfrunde 1) → das Produkt steht schon im Hook unter dem Textblock; der Motor rechnet seine Höhe aus dem Platz unter dem Text (bei drei Hook-Zeilen wird es klein: Hook kurz halten).
- Vorteile als stehende Liste wirken wie eine Folie (Prüfrunde 1) → je Vorteil rückt das Produkt (seitlich 7 %, näher 8 %), dazu ein Lichtstreif; das Produkt schwebt sanft.
- Spiegelung bei Produkten mit Schrift zeigt Spiegelschrift → `spiegelung` nur bei Produkten ohne Aufdruck.
- Liste zu nah am schlanken Produkt (Prüfrunde 1: 20 px) → Listenbreite endet 7 % der Bildbreite vor der Produktkante.
