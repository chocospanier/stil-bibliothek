---
id: kopierer-pegel
name: Kopierer-Pegel
familie: kopierer
kurz: Körnige Schwarzweiß-Kopien mit Messgeräte-Einblendungen und einem knalligen Magenta, eine Zahl im Stempel steigt Bild für Bild, bis die Farbe einmal das ganze Bild flutet.
kern: [eine steigende Zahl als Erzählfaden in Stempel und Messetikett, Magenta als plane Füllung von Objekten und einmal als Vollbild, gleichmäßig dichter Schnitt ohne Ausklang]
energie: 5
format_quelle: "4:3"
laenge_s: [15, 25]
messung:
  shot_median_s: 0.25
  schnitte_pro_s: 3.8
  schnitte_verlauf: [3.3, 4.1, 4.1]
  bpm: 60
  schnitt_auf_beat: hoch
  lufs: -14.2
  helligkeit: 0.36
  kontrast: 0.29
  farbigkeit: 0.12
schnittmuster_16tel: [2, 1, 1, 0, 0, 3, 1, 2, 1, 2, 1, 0, 0, 3, 1, 2, 1, 1, 3, 1, 3, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 0, 0, 3, 1, 1, 1, 1, 0, 0]
palette:
  grund: "#E9E2DA"
  tusche: "#14110F"
  mittelton: "#564F4D"
  akzent: "#FD2092"
effekte: [harter-schnitt, stottern, wiederholung, kamera-steht, schwarzweiss, schwellwert, ein-akzent, papier, filmkorn, glow, kritzel, stempel, mono-zeile, zahl-walze, titelkarte, partikel, beat-getrieben, farbfuellung, hud]
kamera: Steht; Bewegung kommt aus dem Inhalt (Druckwelle, fliegende Dinge, wehende Haare) und aus dem Schnitt.
ton: Laut und dicht, −14 LUFS mit Spitzen bis über 0 dBFS, Raster 0,25 s (gemessen 60 BPM, fühlt sich wie Achtel bei 120 an); Stimme in den Bildern nicht erkennbar.
braucht: [fotos-figur, footage-ort, illustrationen, produkt, nur-typo]
motor_aufwand: mittel
einsatz: [trailer, hook, intro, produkt, musikvideo]
abnahme:
  shot_median_s: [0.20, 0.30]
  schnitte_pro_s: [3.0, 4.6]
  helligkeit: [0.29, 0.43]
  farbigkeit: [0.09, 0.15]
  lufs: [-15.2, -13.2]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Kopierer-Pegel

Ein Kopierstapel, der lauter wird. Jedes Bild zeigt eine Wirkung von Druck oder Schall, eine Zahl im Stempel und ein Messetikett klettern nach oben, und Magenta füllt das Objekt, um das sich alles dreht. Die Energie bleibt bis zum Schluss oben, es gibt keinen ruhigen Ausklang.

## Kern
- **Steigende Zahl als Erzählfaden:** Ein Stempel mit einer Zahl taucht alle zwei bis drei Sekunden auf, jedes Mal höher, dazu ein kleines Mono-Etikett mit Messwert, das ebenfalls steigt. Ohne dieses Zählen ist es nur eine Bilderfolge.
- **Magenta als plane Füllung und einmal als Vollbild:** Das zentrale Objekt ist immer flach magenta ausgemalt, Wellen und Bögen sind magenta gekritzelt. Auf dem Höhepunkt wird der ganze Grund magenta und ein Stich steht darauf.
- **Gleichmäßig dichter Schnitt:** 3,3 Schnitte je Sekunde am Anfang, 4,1 in der Mitte und am Ende. Kein Shot länger als 0,8 s, die Schlusskarte steht nur eine halbe Sekunde.

## Erkennung
- **Bild:** Papier `#E9E2DA` mit grobem Korn und feinen senkrechten Schlieren, Tusche `#14110F`, viele dunkle Mitteltöne um `#564F4D`. Fotos in hartem, körnigem Schwarzweiß mit Gegenlicht und ausbrennenden Spots. Stiche (anatomische und technische Illustration, Tier) auf Papier. Magenta `#FD2092` füllt Objekte plan, zieht Wellen-Ovale um Gegenstände, große Kreisbögen über Personen und färbt Stempel, Zeiger, Wellenform und Schlusswort. Gemessen: Helligkeit 0,36, Kontrast 0,29, Farbigkeit 0,12, 44 % der Fläche fast schwarz.
- **Schnitt:** 84 Schnitte in 22 Sekunden, Median 0,25 s, Mittel 0,28 s, längster Shot 0,75 s. 40 % der Schnitte sitzen auf dem Raster gegen 16 % bei Zufall, Rundungsabweichung 0,16: sehr taktgenau. Übergänge: harter Schnitt, Stottern (dasselbe Bild zwei Sechzehntel mit Versatz), Stempel bleibt stehen, während darunter vier Bilder wechseln. Keine Blenden.
- **Ton:** −14,2 LUFS, Lautheitsspanne 3,0 LU, True Peak +1,3 dBFS (übersteuert). Durchgehend laut, keine Pause erkennbar.
- **Text:** Text ist Messinstrument. Vier Rollen: Gummistempel mit Wort und steigender Zahl, schief, oben links oder mittig; kleines Mono-Etikett in weißem Kästchen unten links mit Messwert; Messleiste unten über die volle Breite mit Wellenform und Zeitstempel; Schlusswort in fetter schmaler Grotesk magenta auf Papier, darunter eine Mono-Zeile, die sich Buchstabe für Buchstabe tippt.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Objekt mit Magenta-Füllung | 15 % | Detail nah, Objekt füllt 60 bis 100 % der Bildhöhe, oft angeschnitten, Hand im Bild | 1 bis 3 Sechzehntel |
| Gegenstand unter Schall oder Druck | 25 % | Gegenstand mittig, 40 bis 70 % der Bildhöhe, Tischkante oder Platte als Diagonale; Wellen-Ovale drumherum; Partikel, Sand, Tropfen | 1 bis 3 Sechzehntel |
| Raum oder Fassade mit Messleiste | 15 % | weit, starke Fluchtlinie, Gegenlicht durch Fenster; Messleiste über die unteren 9 % | 2 bis 3 Sechzehntel |
| Person im Druck | 15 % | Gesicht frontal 70 bis 90 % der Bildhöhe mit wehenden Haaren und geschlossenen Augen, oder Gruppe quer durchs Bild, die nach hinten gedrückt wird | 1 bis 2 Sechzehntel |
| Stich-Illustration | 10 % | 70 bis 90 % der Bildhöhe, mittig auf Papier, mit gezeichneten Schalllinien; einmal auf Vollbild-Magenta | 1 bis 2 Sechzehntel |
| Figur im Spot | 7 % | Figur 50 bis 70 % der Bildhöhe, mittig im Lichtkegel, Objekt in Magenta, Kritzel-Kreis | 1 bis 2 Sechzehntel |
| Grafik und Typo (Drehregler, Stempel, Schlusswort) | 13 % | Drehregler mittig 55 % der Bildhöhe auf Papier; Schlusswort mittig 20 % der Bildhöhe | 1 bis 2 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1 s):** das magenta gefüllte Objekt ganz nah, eine Hand dreht daran, Stempel mit der kleinsten Zahl oben links; drei Details im Sechzehntel.
- **Aufbau (1 bis 8 s):** Stich mit Schalllinien, Gegenstand mit Wellen-Ovalen und niedrigem Messwert, Stempel mit höherer Zahl, Raum mit Messleiste, Figur im Spot, Gesicht im Druck. Alle zwei bis drei Sekunden steigt die Zahl.
- **Erster Schlag (um 8 s):** eine Gruppe wird quer durchs Bild nach hinten gedrückt.
- **Steigerung (9 bis 13,5 s):** Membran mit Partikeln, gezeichneter Drehregler, Sandmuster im Stottern, dann derselbe Stempel mit hoher Zahl über vier wechselnden Bildern je Sechzehntel, Drehregler auf Anschlag.
- **Hauptschlag (14 s):** Vollbild Magenta mit Stich und der höchsten Zahl, danach eine Lichtquelle, die zerplatzt, mit dem höchsten Messwert.
- **Verdichtung (14 bis 20 s):** Einzel-Sechzehntel aus allen Bildtypen, Zielscheiben-Ringe in Magenta um eine Figur von oben.
- **Schluss (20 bis 22 s):** Stich zweimal, Schlusswort eine halbe Sekunde, das Objekt mit aufgeklebtem Regler, eine Hand daran, Tusche.

## Schnittmuster
Bauplan für 20 s auf dem gemessenen Raster von 0,25 s (80 Sechzehntel bei 60 BPM, gleich Achtel bei 120 BPM). Inhalt austauschbar, Rhythmus bleibt. Raster immer am fertigen Musikbett messen.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-1 | Objekt nah mit Magenta, Hand dreht, Stempel mit Zahl 1 | hart | Akkord setzt ein |
| 2 | 2, 3 | zwei weitere Details desselben Objekts | hart | Beat |
| 3 | 4 | Stich mit Schalllinien | hart | Tick |
| 4 | 5-7 | Gegenstand mit Wellen-Ovalen, Etikett mit niedrigem Wert | hart | Brummen |
| 5 | 8-9 | Objekt im Raum, Stempel springt eine Zahl höher, Kritzel-Bogen | hart | Stempel |
| 6 | 10-13 | Reihe gleicher Gegenstände, Etikett höher; der letzte kippt | hart | Klirren |
| 7 | 14-19 | Raum mit Messleiste, Stempel höher; dann Figur im Spot, fliegende Blätter | hart | Beat |
| 8 | 20-27 | Gesicht im Druck, Magenta-Bogen; Regal oder Fassade, Messleiste läuft weiter | hart | Beat voller |
| 9 | 28-31 | Schlag 1: Gruppe wird nach hinten gedrückt | hart | Hit |
| 10 | 32-37 | Membran mit Partikeln, Drehregler mit springendem Zeiger | hart | Basswelle |
| 11 | 38-41 | Stempel mit hoher Zahl steht, darunter vier Bilder je Sechzehntel | Stottern | Tick je Bild |
| 12 | 42-45 | Sandmuster zweimal, Drehregler auf Anschlag | Stottern | Knarzen |
| 13 | 46-47 | Schlag 2: Vollbild Magenta mit Stich, höchste Zahl | Blitzbild | Hit und Aufprall |
| 14 | 48-51 | Lichtquelle zerplatzt, höchster Messwert | hart | Knall |
| 15 | 52-67 | Verdichtung: Einzel-Sechzehntel aus allen Bildtypen, zwei Flackerbilder, Zielscheiben-Ringe | hart | Beat voll |
| 16 | 68-69 | Stich zweimal | Stottern | Hall |
| 17 | 70-71 | Schlusswort in Magenta, Mono-Zeile tippt | hart | Beat |
| 18 | 72-77 | Objekt mit aufgeklebtem Regler, dann Hand daran | hart | letzter Akkord |
| 19 | 78-79 | Leerbild Tusche | hart | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Papier `#E9E2DA` aus Rauschen mit festem Seed, grobes Korn (Deckung 8 bis 12 %), zwei bis vier senkrechte Schlieren von 1 px, je Sechzehntel neu. Tusche-Grund `#14110F` mit weicher Vignette.
- **Bildbehandlung:** Fotos entsättigen, harte Kurve (Schwarzpunkt 15 %, Weißpunkt 82 %), Glow nur auf Lichtern ab 85 % Helligkeit (Weichzeichner 3 % der Bildhöhe, `screen`, 50 %). Mit `multiply` aufs Papier. Stiche mit Schwellwert bei 55 % und `multiply`. Magenta-Füllung: Objektmaske plan in `#FD2092`, Kante mit `feTurbulence` baseFrequency 0,8 und `feDisplacementMap` scale 3 leicht ausgefranst, Glanzlichter der Vorlage als Papierweiß ausgespart (Maske der hellsten 8 % abziehen). Vollbild-Magenta: Fläche `#FD2092`, Stich mit `multiply` darauf.
- **Bausteine:** Zahl-Stempel (Rahmen, Strich 0,8 % der Bildhöhe, Höhe 12 bis 15 % der Bildhöhe, Drehung −5° bis +4°, Rand aufgeraut, Rauschmaske 80 bis 100 % Deckung; schlägt in drei Bildern ein, Skala 1,4 → 0,96 → 1,0); Mono-Etikett (weißes Kästchen 3,5 % der Bildhöhe hoch, 1 px Rahmen, 4 % vom Rand unten links); Messleiste (Papierstreifen über die unteren 9 % der Bildhöhe, Wellenform in Magenta mit Strich 0,3 % und Amplitude bis 3 % der Bildhöhe, aus der echten Hüllkurve der Musik, scrollt; links klein Einheit und Zeitstempel in Mono, 1,5 % der Bildhöhe); Wellen-Ovale (zwei bis drei konzentrische Ellipsen, Seitenverhältnis 3:1, Strich 0,4 %, Breite 40 bis 60 % der Bildbreite, zeichnen sich in vier Bildern); Kreisbogen (Teilkreis mit Radius 60 bis 90 % der Bildhöhe, Strich 0,4 %); Drehregler (Tusche-Kreis 55 % der Bildhöhe, Skala 0 bis 10 in Mono, Zeiger in Magenta, springt je Sechzehntel); Zielscheibe (drei bis vier Ringe in Magenta um einen Punkt).
- **Typografie:** Stempel und Schlusswort in fetter schmaler Grotesk, Versalien (frei lizenziert zum Beispiel Archivo Narrow 700 oder Oswald 700), Schlusswort 20 bis 24 % der Bildhöhe. Mono für Etikett, Messleiste und Schlusszeile (zum Beispiel IBM Plex Mono 400 oder JetBrains Mono 400), Schlusszeile 3,5 % der Bildhöhe, tippt mit zwei Bildern je Buchstabe.
- **Bewegung:** Raster 0,25 s; im Aufbau wechselt das Bild alle ein bis drei Raster-Schritte, Flackerbilder (drei Frames) nur in der Verdichtung. Zahl im Stempel steigt nur, nie zurück, in fünf bis sechs Stufen über das Stück. Kamera steht; Bewegung entsteht in den Clips selbst (Druckwelle, wehende Haare, fliegende Dinge). Kopier-Jitter ±2 px je Raster-Schritt.
- **Formate:** In 9:16 rückt das Objekt in die Mitte, 45 bis 60 % der Bildhöhe; Messleiste rutscht über die unteren 15 % (Bedienelemente), Stempel ins obere Drittel, Wellen-Ovale werden schmaler und höher (2:1). In 16:9 bleibt alles wie in 4:3, die Messleiste läuft über die volle Breite.
- **Neue Kennungen:** `neu:farbfuellung`: Ein Objekt wird plan in der Akzentfarbe ausgemalt, als hätte jemand es mit dem Marker gefüllt. `neu:messleiste`: Eine Leiste am unteren Rand zeigt Wellenform, Einheit und Zeitstempel wie ein Messgerät.

## Material
- **Bilder (Foto):** `grainy black and white photocopy of a [subject] hit by a shockwave of sound, dust and particles flying, harsh spotlight from above, crushed blacks, coarse paper grain, faint vertical copier streaks, no color`
- **Bilder (Stich):** `vintage scientific engraving of a [subject] with drawn sound wave lines radiating outward, fine hatching, black ink on cream paper, centered, isolated, no color`
- **Musik:** `Loud distorted garage rock instrumental, 120 BPM, driving eighth-note guitar riff, pounding floor tom and kick, feedback swells, energy rises in steps every four bars, short feedback squeal at thirteen point five seconds, full band hit at fourteen seconds, last chord rings out at nineteen seconds, instrumental, no vocals`
- **Geräusche:** Stempel, Glasklirren, Basswelle, Knall, Knarzen eines Drehreglers, Rückkopplung; 10 bis 16 dB unter der Musik.

## Regler
- Akzentfarbe: Magenta ist der Kern; jede einzelne grelle Farbe trägt (Signalgelb, Kobaltblau).
- Was steigt: Lautstärke, Preis, Temperatur, Zähler. Die Zahl muss nur sichtbar steigen.
- Anteil Bilder mit Magenta-Füllung: 10 bis 20 %, Vollbild-Magenta höchstens einmal.
- Messleiste: in 30 bis 50 % der Bilder; ohne sie fehlt der Messgeräte-Charakter.
- Für Erklärkanäle: Raster auf 0,5 s strecken, Zahl-Stempel und Messleiste bleiben.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` im Kopf dieser Karte treffen.
- Standbild-Prüfung: höchstens eine Farbe; die Zahl im Stempel ist an jeder Stelle höher als an der vorigen; Messleiste und Etikett lesbar bei 600 px Breite.
- Streifen bei 12 fps: kein Shot über 0,8 s, das Vollbild-Magenta sitzt auf dem stärksten Downbeat, die Dichte fällt zum Ende nicht ab.

## Fallen
- Zu viel Magenta-Fläche macht aus der Kopie ein Plakat → Füllung nur auf dem einen Objekt, Vollbild nur einmal.
- Wellenform als Zufallslinie wirkt falsch, sobald man die Musik hört → aus der echten Hüllkurve rechnen.
- Übersteuerung aus der Vorlage übernehmen → eigenes Master auf −14 LUFS und höchstens −1 dBTP.
- Zahl springt zurück oder bleibt gleich → die Steigerung bricht; jede Stufe neu und höher.
- Schlusswort zu lange stehen lassen nimmt den Druck → eine halbe bis eine Sekunde, danach noch zwei kurze Bilder.
- Druckwelle mit Kamera-Wackeln nachbauen → wirkt billig; die Bewegung gehört ins Motiv, die Kamera steht.
- Stempel in der Akzentfarbe über dem ausgemalten Objekt ist unsichtbar (Akzent auf Akzent) → das Motiv im Bild nach unten schieben und den Stempel über eine dunkle Stelle im oberen Drittel setzen.
- Wellen-Ovale im Hochformat hoch statt breit gezeichnet sehen aus wie Schlaufen → auch in 9:16 flach bleiben (Breite zu Höhe etwa 2:1 bis 3:1), wie Ringe auf einer Wasserfläche um das Objekt.
- Grafiken auf Papier (Drehregler, Kurve) heben die Helligkeit über die Abnahme → Drehregler als aufgeklebte Papierscheibe auf Tusche, Kurven invertiert auf Tusche; die Akzentfarbe leuchtet dort zusätzlich stärker.
- Warme Akzente (Gold, Gelb) tragen auf Papier deutlich schwächer als Magenta → Stempel und Füllungen vor allem auf dunkle Bilder legen, Schlusswort auf Tusche statt auf Papier.
- Hinweiszeile am Schluss tippt zu langsam und steht über wechselnden Bildern zu kurz → zwei Zeichen je Bild, danach mindestens 2 s vollständig stehen lassen, Kästchen mit Tusche-Rahmen, damit es auf hellem wie dunklem Grund lesbar bleibt; notfalls das Stück um eine halbe Sekunde verlängern.
- Helle Stiche auf Papier zwischen dunklen Grafiken ergeben mehr als drei harte Hell-Dunkel-Wechsel je Sekunde → in solchen Passagen Stiche invertiert auf Tusche setzen und die Wechsel je Bild messen, nicht schätzen.
- Eine Figur mit offenem Mund auf einem gesprochenen Wort wirkt, als spräche sie → offene Münder nur in Sprechpausen, sonst geschlossener Mund oder Hände vor dem Mund.
- Generierte Kalender, Schilder und Etiketten tragen Fantasie-Schrift → Schrift im Ausgangsbild wegschließen (helles Max-/Min-Filter über der Fläche) oder einen Ausschnitt ohne Schrift wählen.
- Mit Erzählerstimme: der Stempel schlägt auf dem gesprochenen Zahlwort ein (Wortzeit, nicht Raster), das Bild darunter wechselt weiter im Raster. Eine Erklärgrafik (Kurve) läuft als Stottern zwischen anderen Bildern und zeichnet sich über die Wiederholungen hinweg weiter, so bleibt kein Shot über 0,8 s.
