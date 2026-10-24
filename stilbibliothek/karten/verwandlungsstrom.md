---
id: verwandlungsstrom
name: Verwandlungsstrom
familie: malerei
kurz: Ein einziger Satz steht von Bild 0 bis zum Ende unbewegt in warmem Gelb in der Bildmitte, darunter fließen handgemalte Motive auf Schwarz ohne Schnitt ineinander, jedes verwandelt sich ins nächste.
kern: [ein Satz fest ab Bild 0 in der Mitte, ohne Kasten und ohne Animation, Verwandlung statt Schnitt alle 1 bis 3 s bei stehender Kamera, gemalte Motive auf fast schwarzem Grund]
energie: 2
format_quelle: "16:9"
laenge_s: [15, 22]
messung:
  shot_median_s: 2.7
  schnitte_pro_s: 0.1
  schnitte_verlauf: [0.17, 0.0, 0.17]
  bpm: 63
  schnitt_auf_beat: niedrig
  lufs: -16.8
  helligkeit: 0.14
  kontrast: 0.21
  farbigkeit: 0.22
schnittmuster_16tel: [8, 9, 4, 6, 13, 5, 5, 11, 11]
palette:
  grund: "#060708"
  nacht: "#272E53"
  glut: "#AC2731"
  licht: "#E0CE75"
  mond: "#BAC786"
  text: "#F2CD41"
effekte: [kamera-steht, malerei, papier, welten-folge, blende, neu:verwandlung, neu:standzitat]
kamera: Steht in jeder Einstellung still, kein Schwenk, kein Zoom; alle Bewegung entsteht im gemalten Motiv selbst.
ton: Ruhiges Instrumentalbett um 63 BPM ohne Stimme, fast ohne Dynamik (LRA 1 LU), in der Vorlage leiser als die Plattform-Norm.
braucht: [illustrationen, nur-typo]
motor_aufwand: mittel
einsatz: [ganzes-kurzvideo, hook]
abnahme:
  shot_median_s: [2.0, 20.0]
  schnitte_pro_s: [0.0, 0.25]
  helligkeit: [0.10, 0.24]
  farbigkeit: [0.15, 0.35]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Verwandlungsstrom

Ein Satz, der stillsteht, über Bildern, die nie stillstehen. Die Ruhe kommt aus der Schrift, die Spannung aus der Frage, was als Nächstes aus dem Motiv wird. Für jeden kurzen Text über schönem Bewegtbild in jeder Nische: ein Zitat, ein Leitsatz, ein Titel, eine Frage, ein Satz einer Marke. Alles, was einmal gelesen und dann gefühlt werden soll.

## Kern
- **Ein Satz fest ab Bild 0.** Das Auge liest ihn in den ersten zwei Sekunden und schaut danach frei. Wird der Satz animiert, eingeblendet oder wortweise gezeigt, kippt der Stil zur Lyric-Typo.
- **Verwandlung statt Schnitt.** Ein Motiv wird zum nächsten (Form fließt, Linie wird Welle, Flamme wird Sonne). Die Schnitterkennung sieht fast nichts, das Auge zählt einen Wechsel alle 1 bis 3 s. Harte Schnitte zerstören den Strom.
- **Gemalt auf Schwarz.** Gouache, Kreide, Tusche mit sichtbarem Pinsel und Papierkorn, rund zwei Drittel des Bildes fast schwarz. Das Motiv leuchtet aus der Mitte, die Schrift liegt ohne Kasten lesbar darauf.

## Erkennung
- **Bild:** fast schwarzer Grund (Mittel 0,14 Helligkeit, bis 73 % Dunkelanteil), darauf ein einzelnes leuchtendes Motiv in satten Malfarben (Glutrot, Nachtblau, warmes Licht, blasses Mondgrün). Sichtbare Pinselstriche, leichtes Papier- oder Kreidekorn, keine Fotografie, keine glatten Computerflächen.
- **Schnitt:** 2 erkannte Schnitte in 17,6 s, Median 2,7 s laut Messung; nach Augen rund zehn Motive, je 1,2 bis 3,2 s. Übergänge sind Verwandlungen und weiche Überblendungen, die zwei längsten Motive kommen am Ende.
- **Ton:** instrumentales Bett ohne Stimme, gleichmäßig, kein Drop, keine Geräusche. Lautheit der Vorlage −16,8 LUFS, für eigene Stücke auf −14 LUFS mastern.
- **Text:** ein Satz in zwei Zeilen, zentriert, Blockmitte auf halber Bildhöhe, Blockbreite rund 76 % des Bildes. Neutrale Grotesk halbfett in warmem Gelb `#F2CD41`, keine Kontur, kein Schatten, keine Bewegung über die ganze Dauer. Wirkt wie die einfache Textfunktion der App, nicht wie Markendesign.

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Einzelmotiv leuchtet auf Schwarz (Hand, Flamme, Vogel, Gestirn) | 50 % | Motiv 50 bis 80 % der Höhe, mittig oder leicht versetzt, Rest Schwarz | 1 bis 2 s |
| Gemalte Landschaft in Nachtfarben (Meer, Himmel mit Formen) | 25 % | Horizont im unteren Drittel, Formen oben, Motiv klein in der Mitte | 2 bis 3 s |
| Verwandlung im Gange (zwei Formen gleichzeitig, halb das eine, halb das andere) | 15 % | dieselbe Lage wie das ausgehende Motiv, damit das Auge folgt | 0,5 bis 1 s |
| Ruhebild am Schluss (ein Gestirn oder Zeichen mit Restflimmern) | 10 % | Motiv 40 bis 60 % der Höhe, mittig, Schrift liegt quer darüber | 2,5 bis 3 s |

## Dramaturgie
0 bis 2 s Hook: Schrift steht, das erste Motiv ist schon in Bewegung (keine Schwarzblende am Anfang). 2 bis 12 s Strom: alle 2 bis 3 s eine Verwandlung, Farben wechseln von warm zu kalt oder umgekehrt. 12 bis 17 s Atem: Motive werden länger, ruhiger, ein großes Licht. Letzte 2,5 bis 3 s Halt: ein Ruhebild mit Eigenbewegung (Flimmern, Glühen), kein Abspann. Bestes Ende: das Schlussbild verwandelt sich zurück ins Anfangsbild, damit der Neustart wie eine Fortsetzung wirkt.

## Schnittmuster
Bauplan für 18 bis 20 s ohne Beat-Bindung, in Sekunden.

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0,0 bis 3,5 | Einzelmotiv auf Schwarz, schon in Bewegung | Verwandlung ins Motiv 2 | Bett beginnt sofort, kein Einzählen |
| 2 | 3,5 bis 7,0 | Einzelmotiv, verwandt mit 1 in Form oder Farbe | Verwandlung | Bett gleichmäßig |
| 3 | 7,0 bis 11,0 | Gemalte Landschaft | Verwandlung | Bett gleichmäßig |
| 4 | 11,0 bis 15,0 | Einzelmotiv, großes Licht | Verwandlung | Bett etwas voller |
| 5 | 15,0 bis 19,5 | Ruhebild, am besten zurück zum Anfangsmotiv | weiche Abblende nur des Tons, Bild bleibt | Bett klingt aus |

## Rezept für einen Code-Motor
- **Grund:** Videoclips je Motiv als unterste Ebene, Grund `#060708`; zwischen zwei Clips eine Überblendung von 0,5 bis 0,8 s, wenn der Videomotor keine echte Verwandlung mit Start- und Endbild liefert.
- **Bildbehandlung:** leichtes Korn 3 bis 4 % Deckkraft, sonst nichts. Keine Vignette nötig, das Schwarz liegt im Motiv selbst.
- **Bausteine:** im Starter fertig als Baustein 28 (`BildStrom` für den Strom aus Clips mit Kreuzblende, Tempo und Start im Clip; `StandZitat` für den stehenden Satz mit Unterzeile, Schatten und Wächtern), Beispiel `src/beispiele/verwandlungsstrom/`, Komposition über Props `ZitatStrom`; den ganzen Weg vom Zitat bis zum geprüften Stück macht `starter/werkzeuge/zitat.py` (ABLAUF.md, „Zitat in einem Rutsch“). Dazu bei Bedarf ein dezentes KI-Zeichen nach der Hausregel des Kanals.
- **Typografie:** neutrale Grotesk halbfett (frei lizenziert: Inter SemiBold), warmes Gelb `#F2CD41`. Hochkant 1080 × 1920: Schriftgröße 64 bis 72 px, Zeilenabstand 1,15, Blockbreite höchstens 86 % (Rand ≥ 75 px), Blockmitte bei 45 bis 50 % der Höhe. Höchstens zwei, ausnahmsweise drei Zeilen. Ein dezenter, weicher Schatten (Weichheit 8 px, 35 %) ist nur erlaubt, wenn ein Motiv hell unter der Schrift liegt.
- **Bewegung:** Schrift 0 Bewegung, sichtbar ab Bild 0 bis zum letzten Bild. Kamera steht. Verwandlungen im Videomotor mit Start- und Endbild; im Code nur Überblendung, kein Zoom, kein Wackeln.
- **Formate:** 9:16 nativ, Motiv füllt das Bild, Schrift Mitte; 16:9 wie die Vorlage, Schrift dann rund 11 % der Bildhöhe, Blockbreite 76 %.

## Material
- **Bilder:** „A single [motif] painted in thick gouache and ink on black paper, glowing warm colours against deep black, visible brush strokes and dry paper grain, the motif fills the middle of the frame, two thirds of the picture is near black, hand-painted animation still, no text, no letters.“ · „A quiet night landscape painted in gouache on black paper, deep blue water, a thin pale horizon line, soft red cloud shapes, visible brush texture, hand-painted animation still, no text.“
- **Musik:** „Calm instrumental piano and soft strings, 63 BPM, warm and hopeful but restrained, steady from the first second with no intro and no drop, gentle swell from 12 to 16 seconds, fades out over the last 3 seconds, 20 seconds, instrumental, no vocals.“
- **Motoren (gemessen 17.10.2026, Zitat-Probe):** Standbild lokal (Z-Image) liefert klare, gemalte Illustration, bringt öfter einen weißen Papierrand mit (beschneiden); ein Cloud-Bildmodell mit dem ersten Bild als Stil-Referenz trifft dunkle Gouache auf Schwarz sicher. Verwandlung mit Start- und Endbild: Cloud (Kling 3.0) fließt von selbst, hält aber am Clipanfang 1 bis 2 s still; lokal (LTX 2.5) übernimmt bei gemaltem Material den Zeichentrick-Takt und ruckelt, außer die Bewegung wird ausdrücklich als fließende Echtzeit-Aufnahme bestellt („in one smooth, fluid, continuous motion, like real time-lapse footage filmed at full frame rate … every frame moves a little, evenly, with no pauses and no jumps“) und das Startbild liegt im Latent statt als Führung. Danach war lokal 0 von 308 bewegten Bildern stehend. Jeden Clip vor dem Einbau auf Ruckeln messen. Clips nie im Schnitt verlangsamen; die Länge im Motor bestellen, Stille vorne und in der Mitte herausschneiden. Ein Motiv, das sich bewegt, nie quer durch die Satzmitte führen.
- **Geräusche:** keine. Wer will, legt sehr leise Papierrascheln oder Wind unter die Verwandlungen, mindestens 18 dB unter dem Bett.

## Regler
Motivwelt (Natur, Gestirne, Wasser, Hände, Tiere), Farbwärme (Glutrot bis Nachtblau), Länge der Abschnitte (1 bis 4 s), Anzahl der Motive (4 bis 10), Schriftfarbe (warmes Gelb, Creme, Hausfarbe der Marke), Schriftcharakter (neutrale Grotesk wie die App oder eine ruhige Antiqua für edlere Marken), Herkunftszeile klein unter dem Satz (aus oder an). Fest bleibt: Satz steht, Kamera steht, kein harter Schnitt.

## Abnahme
Zielwerte aus `abnahme` mit `video_schauen.py` messen (die Schnitterkennung soll fast nichts finden). Augen-Prüfungen: Ist der Satz in Bild 0 vollständig lesbar? Bleibt er in jedem Bild an derselben Stelle? Ist an jeder Stelle, an der ein helles Motiv unter der Schrift liegt, jeder Buchstabe lesbar (auf 390 px Breite ansehen)? Verwandeln sich die Motive, statt hart zu springen? Wirkt das Ende wie ein Ruhebild mit Eigenbewegung und nicht wie ein Standbild?

## Fallen
- Schrift wird animiert oder wortweise eingeblendet → Stil kippt zur Lyric-Typo. Satz steht ab Bild 0.
- Harte Schnitte zwischen den Motiven → Strom reißt. Start- und Endbild im Videomotor oder Überblendung mit Formverwandtschaft.
- Videomotor fährt die Kamera → Kamerazeile als eigener letzter Block, nicht im Fließtext.
- Helles Motiv genau unter der Schrift → Buchstaben verschwinden. Motive so setzen, dass die Mitte dunkel bleibt, oder weichen Schatten erlauben.
- Glatte Computerflächen statt Malerei → wirkt wie Werbung. Pinsel, Papierkorn, Unregelmäßigkeit im Prompt verlangen und am Standbild prüfen.
- Einsame Figur, die in ein Licht geht → kann als Abschied gelesen werden. Lichte Auflösungen brauchen Boden und Alltag, oder ohne Figur arbeiten.
- Letztes Bild steht still → Freeze. Ruhebild mit Eigenbewegung (Flimmern, Glühen) oder Rückverwandlung zum Anfang.
- Verwandlung ruckelt (Bild ändert sich nur jedes zweite oder dritte Bild) → der Videomotor imitiert Zeichentrick. Fließende Echtzeit-Bewegung bestellen, messen, bei Rot neu rendern; Interpolation hilft nicht.
- (Fremdtest 4, 18.10.2026, nur aus Code) Flamme als Polarform mit einer Spitze liest sich als Oval, Ei oder Glut → schmaler Fuß und zwei bis drei Zungen, die versetzt flackern. Alle Motive aus derselben Ringscheibe wirken wie Umfärben statt Verwandlung → jedem Motiv eine eigene Silhouette geben (die Code-Bühne `src/beispiele/codebuehne.tsx` hat zehn Formen mit eigener Silhouette; eine Sichel ist dort eine Scheibe mit Schattenscheibe, als Polarform wird sie zur Niere).
- (Fremdtest 4) Ein Stück von genau 20 s misst als ein Shot 20,01 s (Ton 11 ms länger) und fällt aus `shot_median_s` [2, 20] → Stück auf 19,9 s bauen (`zitat.py` begrenzt bei Code und eigenen Bildern selbst).
- (Fremdtest 4) Die Unterzeile von `StandZitat` war fest 0,4 der Schriftgröße (26 px) und fiel unter die 50-px-Grenze der Vorprüfung → behoben in Runde 5: Standard mindestens 52 px bei 1080 Breite (`unterzeileSize`); nicht kleiner stellen.
- (Runde 5) Im Hochformat widersprechen sich „Motiv 50 bis 80 % der Höhe“ und „Satz in der dunklen Mitte“. Es gilt: Motiv 30 bis 40 % der Höhe (Bild 0 Pflicht 30 %), Mitte bei rund 70 % der Höhe, der helle Kern unter dem Satz, nur der dunkle Rand darf unter die Schrift; die Lesbarkeit misst es (`zitat.py`, Schritt `lesbarkeit`). Ganz unter den Satz geschoben war der Stein in Bild 0 nur 19,5 % hoch (Blocker des Prüfers).
- (Runde 5) GRAMMATIK verlangt eine extreme Nahaufnahme, die Karte eine stehende Kamera → die Kamera steht; die Nähe entsteht, wenn ein Motiv in der Verwandlung groß wird, nie durch Zoom.
- (Runde 5) Blasse Motivfarben auf fast Schwarz drücken die Farbigkeit unter das Soll (gemessen 0,14 mit Sandstein und Mondgrün, 0,20 bis 0,23 mit satten Farben) → Farben mit Sättigung ab 0,5; `zitat.py` meldet blasse Farben.
- (Runde 5) Taktbauer `episch` legt alle zwei Schläge eine Pauke ins Bett (Fremdtest 4: alle 1,9 s ein Paukenschlag) → seit 18.10.2026 kein Taktbauer-Bett mehr: Musik aus ElevenLabs (`zitat.py` eingebaut oder `musik.py`), die Stimme liest den Satz vor, die Musik wird unter ihr leiser.
