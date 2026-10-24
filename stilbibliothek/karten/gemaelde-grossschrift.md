---
id: gemaelde-grossschrift
name: Gemälde-Großschrift
familie: malerei
kurz: Alte Gemälde und Druckgrafiken gleiten langsam durchs Bild, riesige schmale Wörter stehen hinter den gemalten Figuren, jedes Kapitel hat eine eigene Tönung, gerahmt von einer feinen Museums-Beschriftung in den Ecken.
kern: [riesige schmale Versalwörter hinter den gemalten Figuren, eine Tönung je Kapitel (Sepia, Rot-Duoton, Papierweiß, Grau), feine Ecken-Beschriftung mit Werkangaben und Kapitelzähler]
energie: 2
format_quelle: "16:9"
laenge_s: [20, 30]
messung:
  shot_median_s: 1.67
  schnitte_pro_s: 0.5
  schnitte_verlauf: [0.33, 0.55, 0.55]
  bpm: 157
  schnitt_auf_beat: niedrig
  lufs: -14.0
  helligkeit: 0.28
  kontrast: 0.18
  farbigkeit: 0.13
schnittmuster_16tel: [1, 1, 25, 81, 52, 17, 1, 15, 1, 17, 27, 46]
palette:
  grund_sepia: "#4D2F1E"
  sepia_licht: "#8E6246"
  tiefe: "#190D09"
  papier: "#D5CBC4"
  wort_creme: "#E8C9A8"
  wort_rot: "#D24B3A"
  wort_schwarz: "#1B1714"
effekte: [text-hinter-figur, schwenk, push-in, blende, wischer, glitch-uebergang, duoton, schwarzweiss, filmkorn, vignette, mono-zeile, titelkarte, kapitel-zaehler, typo-raster]
kamera: Langsame Fahrten über die Bildflächen (Schwenk, Push-in), als ginge jemand mit der Nase am Gemälde entlang; zwischen Werken verwischt die Fahrt.
ton: Ruhiges, atmosphärisches Stück um 78 BPM (gemessen 157, Doppeltempo), mittellaut mit moderater Dynamik; die Wörter erscheinen im Satzrhythmus, vermutlich zu einer Stimme oder einem Zitat.
braucht: [illustrationen, nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, intro, trailer]
abnahme:
  shot_median_s: [1.3, 2.0]
  schnitte_pro_s: [0.35, 0.6]
  helligkeit: [0.22, 0.34]
  farbigkeit: [0.10, 0.16]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Gemälde-Großschrift

Ein Zitat, das durch ein Museum spaziert. Die Energie ist gering, aber dicht: Sie kommt aus den riesigen Wörtern, die hinter gemalten Menschen stehen, und aus dem Kapitelwechsel, bei dem die ganze Farbwelt umschlägt.

## Kern
- **Wort hinter Figur:** Ein Wort in schmaler, fetter Versalschrift nimmt 35 bis 50 % der Bildhöhe ein und liegt hinter der wichtigsten gemalten Figur. Die Figur schneidet Buchstaben ab. Das verbindet Text und Bild zu einer Ebene; Text davor wäre nur Untertitel.
- **Eine Tönung je Kapitel:** Vier Kapitel, vier Farbwelten: warmes Sepia, Rot-Schwarz-Duoton, reine Typo auf Papierweiß, Graustufen. Der Wechsel ist der Höhepunkt jedes Abschnitts.
- **Museums-Beschriftung:** In allen vier Ecken feine Angaben: links oben Stücktitel, rechts oben Zähler wie „Kapitel von zwölf“, links unten Künstler und Werk in Kleinversalien, rechts unten die Jahreszahl, dazu Eckwinkel. Sie gibt dem Ganzen Ordnung und Wert.

## Erkennung
- **Bild:** Gemälde und Grafiken als Vollbild, stark beschnitten, nie ganz zu sehen. Kapitel 1 in Sepia (Hauptfarben `#4D2F1E`, `#8E6246`), Kapitel 2 als Rot-Duoton auf Tiefbraun, Kapitel 3 Papierweiß `#D5CBC4` mit feinen Rasterlinien, Kapitel 4 Graustufen. Leichtes Korn, weiche Vignette. Helligkeit 0,28, Farbigkeit 0,13.
- **Schnitt:** 12 erkannte Shots in 27,2 s, Median 1,7 s. Innerhalb der langen Shots (bis 7,7 s) wechseln die Werke über Wischer und Blenden, sichtbar alle 1 bis 2 s ein neues Werk. Ein harter Glitch mit gezackter Bildspalte beim Wechsel zu Kapitel 4. Am Anfang zwei Blitzbilder in Creme.
- **Ton:** −14 LUFS, Lautheitsspanne 5,1 LU. Gemessen 157 BPM, gefühlt halb so schnell. Ob eine Stimme spricht, zeigen die Bilder nicht; die Wörter bilden zusammen ein Zitat, das nahe legt, dass sie einer Stimme folgen.
- **Text:** drei Rollen. Großwort: schmale fette Grotesk, 35 bis 50 % der Bildhöhe, Farbe je Kapitel (Creme mit 80 % Deckung, Rot, Schwarz, Dunkelgrau), hinter der Figur. Raster-Typo im weißen Kapitel: vier Zeilen in drei Größen (8 bis 11 % der Bildhöhe, Füllwörter klein mit 3 %), versetzt an dünnen Rasterlinien ausgerichtet. Ecken-Beschriftung: Monospace oder schmale Grotesk, 1,2 bis 1,6 % der Bildhöhe, 3 % vom Rand.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Gemälde Innenraum mit Figuren, Sepia | 25 % | Ausschnitt einer Szene, Figur stehend 40 bis 60 % der Bildhöhe, Großwort im oberen Drittel dahinter | 1 bis 2,5 s |
| Gemälde Doppelporträt oder Halbfigur | 15 % | zwei Köpfe je 30 % der Bildhöhe, Wort links hinter der ersten Figur | 1,5 bis 2 s |
| Detail-Fahrt über Gegenstände | 10 % | Glas, Tisch, Stoff füllen das Bild, Fahrt nach rechts, endet im Wischer | 1 bis 1,5 s |
| Porträt im Rot-Duoton | 15 % | Kopf rechts, 50 bis 60 % der Bildhöhe, drei Textzeilen links, Rot `#D24B3A` auf Tiefbraun | 2 bis 5 s |
| Raster-Typo auf Papier | 10 % | nur Wörter und dünne Linien, Zeilen treppenartig versetzt | 1,5 s |
| Graustufen-Gemälde oder Druckgrafik | 20 % | Figur 50 bis 80 % der Bildhöhe, Großwort in Dunkelgrau dahinter oder im oberen Drittel | 1,5 bis 2,5 s |
| Schlusskarte | 5 % | Schwarz, Titel klein mittig in weit gesperrten Versalien, darunter eine Zeile mit Namen in 1 % Höhe | 3 bis 4,5 s |

## Dramaturgie
- **Hook (0 bis 0,2 s):** zwei Blitzbilder in Creme, auf denen das erste Großwort schon durchscheint.
- **Kapitel 1, Sepia (0,2 bis 10,3 s):** Innenräume und Paare, Großwörter wechseln je Phrase, Fahrten über Details, ein Wischer verbindet zwei Werke.
- **Kapitel 2, Rot (10,3 bis 15,3 s):** ein Porträt im Duoton, Text wächst Zeile für Zeile links daneben.
- **Kapitel 3, Papier (15,3 bis 17 s):** reine Typo im Raster, der stärkste Satz des Zitats.
- **Glitch (16,9 s):** gezackte Spalte reißt das Raster auf.
- **Kapitel 4, Grau (17 bis 22,8 s):** Porträts und Grafiken in Graustufen, Wörter in Dunkelgrau, das letzte Wort zerfällt.
- **Schluss (22,8 bis 27,2 s):** Schwarz mit kleinem, weit gesperrtem Titel.

## Schnittmuster
Kein Beat-Schnitt: in Sekunden denken, Wechsel auf Phrasen des Zitats. Bauplan für 20 s, vier Kapitel.

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-0,2 | zwei Blitzbilder Creme, Großwort scheint durch | Blitzbild | Ton setzt ein |
| 2 | 0,2-2,2 | Sepia: Innenraum mit Figuren, Großwort 1 hinter Figur | hart | erste Phrase |
| 3 | 2,2-4 | Sepia: zweite Szene, Großwort 2 | Wischer | |
| 4 | 4-5,2 | Sepia: Detail-Fahrt über Gegenstände | Blende 8 Bilder | |
| 5 | 5,2-7 | Sepia: Doppelporträt, Großwort 3 | Wischer | Phrasenende |
| 6 | 7-10,5 | Rot-Duoton: Porträt rechts, drei Zeilen erscheinen links nacheinander | hart | Kapitelwechsel, tiefer Ton |
| 7 | 10,5-12 | Papier: Raster-Typo, Zeilen erscheinen versetzt | hart | Kernsatz |
| 8 | 12-12,1 | Glitch-Spalte | Glitch | Störgeräusch |
| 9 | 12,1-13,6 | Grau: Porträt sitzend, Großwort dahinter | hart | |
| 10 | 13,6-15,3 | Grau: Druckgrafik, Großwort oben | Blende | |
| 11 | 15,3-17 | Grau: Kopfporträt nah, langsamer Push-in | hart | letzte Phrase |
| 12 | 17-20 | Schwarz: Titel weit gesperrt, Namenszeile darunter | Blende 12 Bilder | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** das Werk selbst. Für Kapitel 3 Papier `#D5CBC4` mit leichtem Rauschen (3 %) und einem Raster aus dünnen Linien (0,1 % der Bildhöhe, `#1B1714` mit 35 % Deckung) in unregelmäßigen Abständen.
- **Bildbehandlung:** je Kapitel ein Filter: Sepia (entsättigen, dann Duoton `#190D09` zu `#E8C9A8`, 85 % Deckung über dem Original), Rot (entsättigen, Duoton `#1E0806` zu `#D86A4E`), Grau (entsättigen, Kontrast +15 %). Korn 4 %, Vignette 25 %. Für Text hinter Figur die Hauptfigur einmal freistellen (Maske vorrechnen) und als oberste Ebene über das Großwort legen.
- **Bausteine:** Großwort, freigestellte Figur, Ecken-Beschriftung (vier Felder plus Eckwinkel aus zwei Linien à 2 % der Bildhöhe, 3 % vom Rand), Kapitelzähler (zweistellig mit Schrägstrich), Raster-Typo, Glitch-Spalte (senkrechter Streifen 8 % der Bildbreite, darin waagerechte Versätze mit gezackter Kante über 3 Bilder, dazu Rot-Blau-Versatz von 0,5 %), Schlusskarte.
- **Typografie:** Großwort in schmaler, fetter Grotesk, zum Beispiel Anton oder Oswald 700, Versalien, Zeilenabstand 0,85, Höhe 35 bis 50 % des Bildes. Raster-Typo in fetter Grotesk, zum Beispiel Inter 800, Füllwörter in derselben Schrift sehr klein. Ecken in Monospace, zum Beispiel IBM Plex Mono 400, Versalien. Schlusstitel in Inter 500, Versalien, Sperrung 40 %, 2 % der Bildhöhe.
- **Bewegung:** Fahrt über jedes Werk mit 3 bis 6 % der Bildbreite je Sekunde, `linear`, oder Push-in von 100 auf 108 % über den Shot. Großwörter erscheinen in drei Bildern (Deckung 0 auf 100 %), Raster-Zeilen nacheinander alle 6 Bilder. Wischer: gerichtete Bewegungsunschärfe 8 % der Bildbreite über 6 Bilder.
- **Formate:** 16:9 ist das Original. In 9:16 das Großwort vertikal stapeln (Buchstabenblock in zwei Zeilen) oder in der oberen Hälfte über die volle Breite; die Figur rückt in die untere Hälfte, Ecken-Beschriftung bleibt, aber über den unteren 15 %. Raster-Typo als vier gestapelte Zeilen linksbündig.

## Material
- **Bilder:** gemeinfreie Gemälde und Druckgrafiken (älter als 70 Jahre nach dem Tod des Künstlers) aus offenen Museumsarchiven; für eigene Motive: `oil painting in the style of late 19th century impressionism of [subject] in a dim interior, visible brush strokes, warm lamp light, muted palette`
- **Bilder (Grafik):** `etching of [subject], fine crosshatching, black ink on aged paper, 18th century printmaking style, high detail`
- **Musik:** `Atmospheric neo-classical piece, 78 BPM, soft felt piano motif, warm cello line, distant choir pad, subtle low pulse; 0-7 s piano alone, 7 s cello enters with a deeper tone for the second chapter, 10 s silence for half a beat then piano high register, 12 s low swell, 17-20 s piano resolves and fades, instrumental, no vocals`
- **Geräusche:** Papierrascheln beim Kapitel Papier, ein digitales Knacken auf dem Glitch, leises Museumsraum-Ambiente 30 dB unter der Musik. Für ein Zitat eine ruhige Sprechstimme, die Großwörter folgen ihren betonten Wörtern.

## Regler
- Kapitelzahl: drei bis fünf.
- Tönungen: frei, aber je Kapitel genau eine.
- Wortgröße: 30 bis 55 % der Bildhöhe.
- Mit Sprechstimme wird es ein Zitat-Video; ohne ein Lyrik-Clip.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen.
- Standbild an drei Stellen: Großwort liegt hinter der Figur (Figur schneidet Buchstaben), Ecken-Beschriftung vollständig, eine Tönung im Bild.
- Streifen bei 12 fps: Kapitelwechsel klar als Farbwechsel, Fahrten ruhig ohne Ruckeln.

## Fallen
- Großwort vor der Figur → wird zum Untertitel. Immer dahinter, Figur freistellen.
- Gemälde ohne Rechteprüfung → nur gemeinfreie Werke oder eigene Bilder.
- Alle Kapitel in Sepia → kein Höhepunkt. Mindestens ein harter Farbwechsel.
- Ecken-Beschriftung zu groß → überlädt. Höchstens 1,6 % der Bildhöhe.
- Wort zu lang für die Breite → nicht verkleinern, sondern anschneiden lassen; angeschnittene Buchstaben gehören zum Stil.
- In 9:16 erreicht ein Wort mit sechs Buchstaben einzeilig nur rund 20 % der Bildhöhe (Anton ist etwa 2,5 Geviert breit), 35 bis 50 % schaffen nur Wörter bis vier Buchstaben. Zweizeilig (KAI/SER) verschwindet die untere Zeile hinter dem Körper. Besser: eine Zeile über die volle Breite, Ränder leicht angeschnitten, der Kopf schneidet die Unterkante von ein bis zwei Buchstaben.
- Freistellung auf Radierungen nimmt glatten Himmel oder Horizontstreifen mit in die Maske, das Wort wirkt dann mit einer geraden Kante abgeschnitten → Maske oberhalb der echten Figur verwerfen.
- Pflanzen, Disteln oder ein zu großer Kopf in der oberen Bildhälfte verdecken das halbe Wort → schon im Bild-Prompt die Aufteilung festlegen („the upper half is completely plain, nothing in it“).
- Dunkles Wort auf dunklem Gemälde verschwindet, helles auf heller Öffnung auch → helles Grau mit Mischmodus Differenz, dann bleibt es über beiden lesbar.
- Ecken-Beschriftung über unruhigen Stichen ist unlesbar → Halo in der Gegenfarbe, bei sehr dichten Blättern eine weiche Papier-Platte dahinter.
- Ein Großwort, das erst kurz vor dem Schnitt erscheint, sieht niemand → jedes Großwort mindestens 1 s stehen lassen, Schnitt notfalls hinter die nächste Phrase legen (J-Schnitt), aber nie hinter das nächste Großwort, sonst kommt dieses zu spät.
- Raster-Typo auf zwei Seiten verteilt lässt ein Wort aufblitzen oder eine Seite leer stehen → den Kernsatz auf einer Seite aufbauen, Zeile für Zeile, Block über die halbe Bildhöhe.
- Ein Shot, dessen Wort erst nach über 0,5 s kommt, wirkt leer → später anfangen oder das vorige Wort länger halten.
- Starker Ausschnitt mit Parallaxe verschiebt das Großwort mit (bei Skala 1,45 rutschte es um 160 px nach oben) → bei engen Ausschnitten das Wort ohne Parallaxe setzen.
- Radierungen haben unten oft eine Plattenkante mit Pseudo-Signatur → beim Ausschnitt die Unterkante prüfen.
- Ein Mönch in Kutte unter „KAISER“ kippt den Hook → Figuren mit eindeutigen Zeichen ihres Standes malen lassen (Mantel mit Fibel, keine Kapuze).
