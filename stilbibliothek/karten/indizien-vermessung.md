---
id: indizien-vermessung
name: Indizien-Vermessung
familie: noir
kurz: Ruhige, fast farblose Einstellungen von Gegenständen und Orten in einem Rahmen mit runden Ecken, überzogen von einem Netz aus Messpunkten und gestrichelten Linien; leise Satzfetzen benennen die Indizien, nur Gold leuchtet.
kern: [lange ruhige Einstellungen um zwei Sekunden mit Schnitt auf dem Satz, Mess-Overlay aus Koordinaten-Etiketten und gestrichelten Linien über jedem Bild, entsättigte Kälte mit einem einzigen warmen Gold für das gesuchte Objekt]
energie: 2
format_quelle: "16:9"
laenge_s: [18, 25]
messung:
  shot_median_s: 1.5      # selbst nachgemessen ohne die Schluss-Flackerkette; Messung sah 2.0
  schnitte_pro_s: 1.0     # Messung 0.5, hat dunkle Schnitte übersehen
  schnitte_verlauf: [0.5, 0.6, 2.0]
  bpm: 102
  schnitt_auf_beat: niedrig
  lufs: -14.2
  helligkeit: 0.18
  kontrast: 0.17
  farbigkeit: 0.06
schnittmuster_16tel: [10, 14, 10, 12, 15, 14, 11, 7, 9, 11, 7, 10, 1, 0, 0, 0, 0, 1, 0, 1, 2]   # nachgemessen bei 102 BPM; messung.json: [46, 15, 14, 18, 9, 28, 1, 1, 1, 3]
palette:
  grund: "#050505"
  nacht: "#132528"
  grau: "#585651"
  hell: "#CBC9C8"
  gold: "#C9963F"
  etikett: "#B0A292"
effekte: [harter-schnitt, bild-im-bild, hud, vignette, filmkorn, push-in, pull-out, partikel, titelkarte, mono-zeile, untertitel, atem-vor-schlag, wort-schnitt, tracking-etiketten, rahmen-rund]
kamera: Langsame Push-ins und Pull-outs von 1 bis 4 % über die ganze Einstellung, nie Handkamera; erst im Schluss ein paar ruckartige Digitalzooms auf das Objekt.
ton: Gleichmäßige dunkle Spannungsfläche um 102 BPM, ab 10 s ein Anschwellen mit Bass, bei 13,5 s eine Sekunde fast Stille, dann der Wiedereinsatz; Satzfetzen wirken wie leise gesprochene Erzählung.
braucht: [footage-ort, produkt, nur-typo]
motor_aufwand: klein
einsatz: [trailer, intro, ganzes-kurzvideo]
abnahme:
  shot_median_s: [1.2, 1.9]
  schnitte_pro_s: [0.8, 1.2]
  helligkeit: [0.14, 0.22]
  farbigkeit: [0.04, 0.08]
  lufs: [-15.2, -13.2]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Indizien-Vermessung

Ein Ermittlungsfilm in zwanzig Sekunden: Ein Gegenstand wandert durch Orte und Hände, und jede Einstellung wird vermessen wie ein Beweisfoto. Die Spannung kommt aus Ruhe, aus dem Netz der Messpunkte und aus dem einen goldenen Objekt, das in kalten, fast farblosen Bildern als einziges warm leuchtet.

## Kern
- **Ruhe und Satzschnitt:** Einstellungen stehen 1 bis 2 s, geschnitten wird, wenn ein Satzfetzen fertig ist, nicht auf dem Beat. Erst im Schluss bricht eine Flackerkette von acht Bildern in einer halben Sekunde aus.
- **Mess-Overlay auf jedem Bild:** Zehn bis zwölf Koordinaten-Etiketten mit Punkt, zwei, drei gestrichelte Verbindungslinien und ein Fadenkreuz liegen über jeder Einstellung. Sie machen aus schönen Bildern Beweismaterial.
- **Kälte und ein Gold:** Nacht in Petrol-Schwarz, Tagesbilder in kühlem Hellgrau, das Objekt und seine Welt (Rahmen, Saal) in Gold. Farbigkeit nur 0,06; Gold ist der einzige warme Ton.

## Erkennung
- **Bild:** Das Bild sitzt in einem Rahmen mit runden Ecken (2 % Rand, Eckradius 3 % der Bildhöhe), außen Schwarz, innen Vignette und feines Korn, wie ein Sucher oder alter Monitor. Drei Lichtwelten: Nacht (#132528 Petrol in Schwarz, Nebel, nasse Straße), Galerie (kühles Hellgrau #CBC9C8, Weißraum, Gips, Handschuhe), Gold (#C9963F, Münze, Bilderrahmen, Kronleuchtersaal). Gemessen: Helligkeit 0,18, Kontrast 0,17, Farbigkeit 0,06, 55 % der Fläche fast schwarz.
- **Schnitt:** 20 s, nachgemessen 21 Shots: zwölf ruhige Einstellungen von 1,0 bis 2,2 s, dann bei 19 s eine Flackerkette aus acht Bildern von ein bis drei Frames, letztes Bild 0,3 s. Die automatische Messung hat die dunklen Schnitte im ersten Drittel übersehen (sie fand den ersten Schnitt erst bei 6,8 s). Übergänge: nur harte Schnitte; ein Staubausbruch als Bewegungs-Höhepunkt um 13 s.
- **Ton:** −14,2 LUFS, Lautheitsspanne 4,8 LU. Bis 10 s gleichmäßig um −14 dB, dann Anschwellen mit viel Bass bis 12,5 s, bei 13,5 bis 14,5 s fast Stille (−38 dB), Wiedereinsatz bei 15 s, Ende bei 19,5 s. Ob eine Stimme spricht, ist nicht sicher; die Satzfetzen im Bild wirken wie Untertitel einer leisen Erzählung.
- **Text:** Drei Ebenen. Messetiketten in Monospace, etwa 1,8 % der Bildhöhe, Form „x: Zahl y: Zahl“ mit Punkt, Grau mit 70 % Deckung. Satzfetzen in schlichter Grotesk, Kleinbuchstaben, 3 % der Bildhöhe, direkt neben dem Objekt, weiß auf Dunkel oder dunkel auf Hell. Titelkarte in feiner Serif, Versalien, 7 % der Bildhöhe, auf fast schwarzem Bild mit Overlay.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Objekt-Makro in Gold | 15 % | Objekt 40 bis 50 % der Bildhöhe, mittig, schwarzer Grund, warmes Streiflicht | 1,0 bis 1,5 s |
| Hand am Objekt | 15 % | behandschuhte Hand füllt 60 % des Bilds von oben, Objekt am Kontaktpunkt im unteren Drittel, kühles Licht | 2,0 s |
| Ort in der Nacht | 20 % | Figur von hinten 25 bis 40 % der Höhe, Gasse oder Straße, Nebel, Petrol-Licht, Neon-Reste | 1,5 bis 2,1 s |
| Weißer Raum | 20 % | Fluchtpunkt-Gang oder Studio, Figur oder Fahrzeug 20 bis 35 % der Höhe, viel helles Grau | 1,3 bis 2,2 s |
| Skulptur oder Porträt | 15 % | Büste im Profil rechts, 70 % der Höhe; gemaltes Porträt im goldenen Ovalrahmen, angeschnitten | 1,0 bis 1,7 s |
| Titelkarte | 5 % | Serif-Zeile mittig links auf fast Schwarz, Overlay sichtbar | 1,0 s |
| Flackerkette | 10 % | Objekt, Skulptur und Schatten im Wechsel, Digitalzoom | 1 bis 3 Frames je Bild |

## Dramaturgie
- **Hook (0 bis 1,5 s):** ein Gegenstand im Dunkeln, ganz nah, Messpunkte erscheinen.
- **Spur (1,5 bis 7 s):** Figur in nächtlicher Gasse, erster Satzfetzen; das goldene Objekt; Fahrzeug mit Scheinwerfer.
- **Katalog (7 bis 13 s):** weißer Gang, Hand mit Handschuh legt das Objekt ab (Satzfetzen), Büste. Ton schwillt an.
- **Schlag und Stille (13 bis 15 s):** Staubausbruch, dann eine Sekunde fast Stille über einem Fahrzeug im weißen Raum.
- **Herkunft (15 bis 18,5 s):** goldener Saal mit Hand, gemaltes Porträt im Goldrahmen (Satzfetzen), Titelkarte.
- **Schluss (19 bis 20 s):** Flackerkette mit Digitalzooms aufs Objekt, letztes Bild, Ton aus.

## Schnittmuster
Bauplan für 20 s; gedacht in Sekunden, weil der Schnitt dem Satz folgt (Raster nur zur Orientierung: 102 BPM, Sechzehntel = 0,147 s).

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0,0 bis 1,5 | Objekt-Detail im Dunkeln, Messpunkte blenden einzeln ein | hart | Fläche setzt ein |
| 2 | 1,5 bis 3,6 | Ort in der Nacht, Figur von hinten, erster Satzfetzen | hart | Stimme 1 |
| 3 | 3,6 bis 5,0 | Objekt in Gold, Fadenkreuz wandert hinein | hart | |
| 4 | 5,0 bis 6,8 | Ort in der Nacht mit Lichtquelle | hart | |
| 5 | 6,8 bis 9,0 | weißer Raum, Fluchtpunkt | hart | Stimme 2 |
| 6 | 9,0 bis 11,0 | Hand am Objekt, Satzfetzen daneben | hart | |
| 7 | 11,0 bis 12,7 | Skulptur im Profil | hart | Anschwellen |
| 8 | 12,7 bis 13,7 | Staubausbruch | hart | Schlag |
| 9 | 13,7 bis 15,0 | weißer Raum mit Fahrzeug, fast still | hart | Stille |
| 10 | 15,0 bis 16,6 | goldener Saal, Hand greift | hart | Wiedereinsatz, Stimme 3 |
| 11 | 16,6 bis 17,6 | gemaltes Porträt im Goldrahmen, Satzfetzen | hart | |
| 12 | 17,6 bis 19,1 | Titelkarte in Serif | hart | |
| 13 | 19,1 bis 19,7 | Flackerkette aus acht Bildern, Digitalzoom aufs Objekt | hart | Ticks |
| 14 | 19,7 bis 20,0 | letztes Bild, Objekt | hart | Ton aus |

## Rezept für einen Code-Motor
- **Grund:** Schwarz #050505 außerhalb des Rahmens. Rahmen: Bildfläche um 2 % eingerückt, Ecken mit 3 % der Bildhöhe gerundet (`border-radius` oder `clip-path: inset(2% round 3vh)`), innen Vignette mit 35 % zu den Ecken.
- **Bildbehandlung:** Sättigung 0,35 als Grundzustand; Nachtbilder mit Petrol tönen (Schatten 30 % #132528 beimischen); Tagesbilder kühl (Weißabgleich leicht blau, Sättigung 0,2); Goldbilder mit voller Sättigung im Farbton 30° bis 45°, Rest entsättigt. Korn 3 %, leichtes Halation-Glühen um helle Kanten (Gauß 1 %, `screen`, 20 %).
- **Bausteine:** Mess-Overlay (10 bis 12 Punkte von 0,4 % der Höhe, je ein Etikett „x: … y: …“ mit vierstelligen Zahlen daneben, 2 bis 3 gestrichelte Linien von 1 px mit Strichlänge 0,6 % zwischen Punkten, ein Fadenkreuz aus Kreis und vier Strichen mit 2,5 % der Höhe; Punkte erscheinen nacheinander im Abstand von 3 Frames, Linien zeichnen sich in 8 Frames per `stroke-dashoffset`; je Einstellung neue Positionen, ein Punkt liegt immer auf dem Objekt); Satzfetzen; Titelkarte; Flackerkette (acht Bilder zu ein bis drei Frames, jedes mit Digitalzoom von 110 auf 140 %).
- **Typografie:** Etiketten in Monospace (frei lizenziert zum Beispiel IBM Plex Mono 400), 1,8 % der Bildhöhe, Grau #B0A292 mit 70 %. Satzfetzen in neutraler Grotesk, Kleinbuchstaben, 3 % der Bildhöhe (zum Beispiel Inter 400), mit 6 Frames Einblendung. Titel in feiner Serif mit Versalien (zum Beispiel Cormorant Garamond 500 oder Cinzel 400), 7 % der Bildhöhe, Weiß 90 %.
- **Bewegung:** Push-in oder Pull-out über die ganze Einstellung, 1 bis 4 % Skalierung, Ease linear. Overlay bewegt sich nicht mit dem Bild, sondern liegt fest auf dem Rahmen. Schnitt nach Satzende plus 0,3 bis 0,5 s.
- **Formate:** 16:9 ist das Original. In 9:16 den Rahmen behalten (2 % Rand, gleiche Rundung), Objekt in die obere Hälfte, Satzfetzen darunter, Etiketten über die ganze Höhe streuen, aber die unteren 15 % freilassen. Titel zweizeilig.

## Material
- **Bilder (Objekt):** `macro photograph of a [subject] made of old gold on a black velvet background, warm raking light, museum evidence photo, shallow depth of field, fine grain`
- **Bilder (Ort):** `desaturated cinematic still of [subject], cold teal night light, fog, wet ground, figure seen from behind, low key, muted colors, film grain`
- **Musik:** `Dark investigative thriller underscore, 102 BPM, steady low pulse with soft ticking and distant metallic textures, a slow swell with deep bass from 10 to 12.5 seconds, a hit at 12.7 seconds followed by one second of near silence, the pulse returns at 15 seconds, quick ticks at 19 seconds, hard end at 20 seconds, instrumental, no vocals`
- **Geräusche:** Handschuh auf Oberfläche, Münzklang oder Klick beim Ablegen, Staubausbruch auf dem Schlag, leises Datenpiepen beim Erscheinen der Messpunkte; 15 bis 20 dB unter der Fläche. Eine eigene Erzählstimme flüstert die Satzfetzen.

## Regler
- Akzent: Gold ist der Kern; ein einzelnes Rot für ein anderes Beweisstück geht auch, aber nie zwei warme Töne.
- Dichte des Overlays: 6 bis 14 Punkte je Bild.
- Erzählung: nur Satzfetzen im Bild oder mit gesprochener Stimme; beides trägt.
- Länge: 18 bis 40 s; bei längeren Stücken alle 15 s eine Titelkarte.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen. Achtung: Die automatische Schnitterkennung übersieht dunkle Schnitte; Schnitte zusätzlich am Streifen zählen.
- Standbild an drei Stellen: Rahmen mit runden Ecken vorhanden, Overlay mit mindestens acht Etiketten, nur Gold als warmer Ton.
- Ton: eine Sekunde fast Stille vor dem Wiedereinsatz ist vorhanden.

## Fallen
- Overlay bewegt sich mit dem Bild → wirkt wie Tracking-Effekt, nicht wie Vermessung. Fest auf dem Rahmen lassen und je Schnitt neu setzen.
- Zu viele Linien → Spinnennetz. Zwei bis drei gestrichelte Verbindungen genügen.
- Satzfetzen zu groß oder mittig → wird Untertitel statt Indiz. Klein, neben das Objekt.
- Gold auch in der Nacht- oder Galerie-Welt → das Objekt verliert seine Sonderrolle.
- Flackerkette zu früh → verbraucht die Ruhe. Erst in der letzten Sekunde.
- (erlebt beim Bau, 16.10.2026) Ein berühmtes Fundstück aus dem Bildmodell → Z-Image erfindet ein eigenes Muster. Nackte Platte erzeugen, die Goldauflagen aus Code nach belegter Beschreibung zeichnen, im Bild „abb.: nachbildung“.
- Goldwelt mit fast null Restsättigung macht grüne Patina grau, das Objekt wirkt wie Blech. Rest um 30 % Sättigung und dunkler, dann bleibt die Patina petrol und das Gold trägt allein.
- Eine Figur, die halb durchsichtig einblendet, zeigt das Gold durch den Körper. Figuren nur einschieben, nie überblenden.
- Labor- und Galeriebilder heben die mittlere Helligkeit über das Fenster der Karte (gemessen 0,245 gegen 0,14 bis 0,22), obwohl sie zur Welt gehören. Galerie um 10 % dunkler graden, den Rest bewusst dunkel halten.
- Zufallspunkte des Overlays legen ihr Etikett über Inhalts-Etiketten. Sperrflächen für Satzfetzen, Figur und feste Etiketten, geprüft über die ganze Etikettbreite.
- (erlebt in der Prüfrunde) Eine Z-Image-Platte trug am Rand einen hellen Fetzen mit Loch, der im Detail-Shot wie ein Fremdkörper aussah. Platte vor dem Bau am ganzen Rand absuchen; Patina aus einer um die Scheibenmitte gedrehten Kopie klonen (der Rand bleibt auf demselben Radius), eine Beschädigung als dunkle, gezackte Kerbe zeichnen.
- „Indiz“ als Zwischenzeile nur für Belege, die genau die gestellte Frage stützen. Die Herkunft eines Metalls stützt das Alter, nicht den Fundort; dort „und das gold?“ statt „indiz 3“.
- Das Etikett am Fadenkreuz lief am rechten Rand aus dem Bild. Etiketten, die rechts nicht passen, links vom Punkt setzen.
- Inhalts-Etiketten (Preise, Daten, Streitfragen) am Handy lesbar: 30 bis 34 px in einem dunklen Kasten mit feinem Rand; die x/y-Etiketten bleiben Textur.
- Warme Reste neben dem Gold (Blatt, Moos) konkurrieren mit dem einen Gold. Gold nur in einer Ellipse um das Objekt zulassen, außerhalb fast farblos.
