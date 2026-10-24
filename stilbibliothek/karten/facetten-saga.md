---
id: facetten-saga
name: Facetten-Saga
familie: malerei
kurz: Eine dunkle Sagenwelt aus kantigen Stein- und Papierfacetten in Blaugrau, mit einem einzigen warmen Licht, erzählt in ruhigen Einstellungen von je anderthalb Sekunden genau auf dem Raster, mit einem Akzent im Ton auf jedem Schnitt.
kern: [facettierte Welt (Scherben, Keile, kantige Figuren) wie gefaltetes Papier und gemalter Stein, kaltes Blaugrau mit einem warmen Lichtakzent, gleichmäßige Einstellungen von 1,25 bis 2 s, Schnitte exakt auf dem Sechzehntel-Raster mit Akzent im Ton auf jedem Schnitt]
energie: 2
format_quelle: "16:9"
laenge_s: [15, 30]
messung:
  shot_median_s: 1.42
  schnitte_pro_s: 0.7
  schnitte_verlauf: [0.7, 0.8, 0.5]
  bpm: 60
  schnitt_auf_beat: hoch
  lufs: -14.0
  helligkeit: 0.19
  kontrast: 0.17
  farbigkeit: 0.05
schnittmuster_16tel: [5, 6, 1, 6, 8, 6, 8, 6, 1, 8, 5, 10, 4]
palette:
  nacht: "#070F15"
  schiefer: "#2A3135"
  stein: "#696662"
  licht_stein: "#B6AFAA"
  ocker_stein: "#8E7B67"
  glut: "#A06A40"
effekte: [harter-schnitt, push-in, pull-out, ebenen-parallaxe, malerei, 3d-render, partikel, glow, vignette, titelkarte, beat-getrieben, facetten-welt, kinobalken]
kamera: Langsame Fahrten hinein oder heraus, oft fast stehend; in Totalen leichte Tiefenstaffelung, keine schnellen Bewegungen.
ton: Gleichmäßig ruhig gemischte, epische Musik (−14 LUFS, 1,7 LU Spanne), 60 BPM mit einem Schlag jede Sekunde; die Schnitte liegen genau auf dem Sechzehntel-Raster, und auf jedem Schnitt sitzt ein Akzent im Ton; Stimme nicht feststellbar.
braucht: [illustrationen, 3d, nur-typo]
motor_aufwand: mittel
einsatz: [intro, trailer, ganzes-kurzvideo, uebergang]
abnahme:
  shot_median_s: [1.15, 1.70]
  schnitte_pro_s: [0.5, 0.8]
  helligkeit: [0.15, 0.23]
  farbigkeit: [0.03, 0.07]
  lufs: [-15, -13]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Facetten-Saga

Eine Sage, erzählt in einer Welt aus gefalteten Steinscherben: Horizonte voller Keile, eine kantige Riesenfigur, Schluchten, in denen eine winzige Gestalt steht, und genau ein warmes Licht. Die Wirkung kommt aus der Ruhe und der Größe; geschnitten wird streng auf den langsamen Schlag.

## Kern
- **Facettierte Welt:** Alles besteht aus flachen, scharfkantigen Flächen wie gefaltetes Papier oder grob behauener Stein, gemalt, mit sichtbarer Pinselstruktur in den Flächen. Keine runden Formen außer wenigen Bögen.
- **Kalt mit einem warmen Licht:** Blaugrau und Schiefer, Farbigkeit nur 0,05. Ein Funke an einer Schnittkante, ein ockerfarbener Lichteinfall, eine warme Fläche je Bild höchstens.
- **Schnitt exakt auf dem Raster:** Einstellungen von fünf bis acht Sechzehnteln bei 60 BPM (1,25 bis 2 s), 67 % der Schnitte auf dem Raster gegen 16 % bei Zufall. Die Schnitte liegen auf Sechzehnteln, nicht alle auf Vierteln; hörbar „auf dem Schlag“ wird das, weil der Ton auf jeden Schnitt einen Akzent setzt. Dazu zwei Blitz-Inserts von 0,1 s als Akzent.

## Erkennung
- **Bild:** Nacht `#070F15`, Schiefer `#2A3135`, Stein `#696662`, Lichtstein `#B6AFAA`, Ocker `#8E7B67`, Glut `#A06A40`. Flächen mit leichter Pinselkörnung, harte Schlagschatten, Staub in Lichtkegeln, kleine Funken. Totalen mit Kinobalken oben und unten. Gemessen: Helligkeit 0,19, Kontrast 0,17, Farbigkeit 0,05, 35 % fast schwarz. Die Palette nennt Rollen, nicht Flächenanteile: Die Mitten liegen bei 0,19 Helligkeit, nur rund 35 % der Fläche ist fast schwarz. Wer die Hexwerte als Flächenfarben nimmt, landet bei 0,10 (Fremdtest); Mitten um rund 30 % anheben.
- **Schnitt:** 12 Schnitte in 18 Sekunden, Median 1,42 s, längste Einstellung 2,5 s. Dichte 0,7 → 0,8 → 0,5 Schnitte je Sekunde. Nur harte Schnitte; zwei Inserts von 0,1 s. Rundungsabweichung 0,15: sehr taktgenau.
- **Ton:** −14,0 LUFS, Lautheitsspanne 1,7 LU, True Peak −3,6 dBFS. Ruhig und gleichmäßig.
- **Text:** zwei Stellen: ein Wort in eine Steintafel graviert, mittig; Schlusskarte auf Schwarz, zwei Zeilen klein mittig (oben schmal und fett, unten dünn und gesperrt).

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Horizont mit Scherbenfeld | 20 % | Horizont auf 40 % der Bildhöhe, Struktur klein in der Mitte, Licht dahinter, Keile im Vordergrund, Kinobalken | 5 bis 10 Sechzehntel |
| Detail mit Lichtfunke | 15 % | Kante oder Keil diagonal, füllt das Bild, Funke oder Staub im Licht | 6 Sechzehntel |
| Steinfigur halbnah | 15 % | Kopf und Schultern rechts, 80 % der Bildhöhe, Seitenlicht, Scherben dahinter; oder zwei Hände um einen Keil | 6 Sechzehntel |
| Schlucht mit winziger Gestalt | 20 % | hohe Wände links und rechts, Gestalt unten mittig 3 % der Bildhöhe, Licht von oben oder unten | 8 Sechzehntel |
| Draufsicht auf Formation | 10 % | Spirale oder Ring aus Keilen, mittig, Gestalt in der Mitte | 8 Sechzehntel |
| Steintafel mit Wort | 8 % | Tafel mittig, 30 % der Bildhöhe, Wort eingraviert, Rest dunkel | 6 Sechzehntel |
| Insert | 4 % | Lichtkegel mit kleinem Wesen oder Hände | 0,1 s |
| Titelkarte | 8 % | Schwarz, zwei Zeilen klein mittig | 4 Sechzehntel |

## Dramaturgie
- **Hook (0 bis 1,25 s):** Horizont, in der Ferne eine Krone aus Scherben vor Licht.
- **Welt (1,25 bis 4,25 s):** ein Keil hebt sich mit Staub aus der Fläche, kurzer Blitz auf Hände, eine kantige Riesenfigur.
- **Weg (4,25 bis 7,75 s):** winzige Gestalt in der Schlucht, eine Klinge zieht einen Riss mit Funken.
- **Ordnung (7,75 bis 11,1 s):** Spirale von oben, Steintafel mit Wort.
- **Übergang (11,1 bis 14,5 s):** Blitz-Insert, Brücke über der Schlucht, zwei Steinhälften mit Lichtspalt.
- **Klammer (14,5 bis 17 s):** derselbe Horizont wie am Anfang, 2,5 s.
- **Schluss (17 bis 18 s):** Titelkarte.

## Schnittmuster
Bauplan für 18,5 s bei 60 BPM (74 Sechzehntel zu 0,25 s, ein Schlag jede Sekunde). Jeder Schnitt auf dem Sechzehntel-Raster, der Ton setzt auf jeden Schnitt einen Akzent (die Slot-Anfänge 5, 11, 18 … liegen nicht alle auf Vierteln).

Inserts zählen in Kopfblock und Tabelle gleich: als 1 Sechzehntel (0,25 s). Davon sind 0,1 s Insert, der Rest ist die Rückkehr in die vorige Einstellung, die mit derselben Fahrt weiterläuft (Insert mit Rückkehr). Im Starter: die vorige Einstellung um diesen Sechzehntel verlängern und `insert(slot, inhalt, bilder, nach16)` setzen, bei 30 fps 3 Bilder, zum Beispiel für Slot 2 und 3 `insert({len: 7, …}, <Haende />, 3, 6)`. Der Kopfblock zählte die Inserts früher als 0 (Summe 72); jetzt gilt 74 wie in der Tabelle.

| Slot | Sechzehntel | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-4 | Horizont mit Struktur in der Ferne, Licht dahinter | hart | Drone, Schlag |
| 2 | 5-10 | Keil hebt sich aus der Fläche, Staub | hart | Schlag |
| 3 | 11 | Insert: Hände um einen Keil, 0,1 s, dann zurück | hart | Akzent |
| 4 | 12-17 | Steinfigur halbnah, Seitenlicht | hart | Schlag |
| 5 | 18-25 | Schlucht, winzige Gestalt unten | hart | Schlag |
| 6 | 26-31 | Klinge zieht Riss, Funke | hart | Kratzen, Schlag |
| 7 | 32-39 | Spirale von oben, Gestalt in der Mitte | hart | Schlag |
| 8 | 40-45 | Steintafel mit eingraviertem Wort | hart | Schlag |
| 9 | 46 | Insert: Lichtkegel mit kleinem Wesen, 0,1 s, dann zurück | hart | Akzent |
| 10 | 47-54 | Brücke über Schlucht, Licht von unten | hart | Schlag |
| 11 | 55-59 | zwei Steinhälften, Lichtspalt | hart | Schlag |
| 12 | 60-69 | Horizont wie am Anfang, etwas näher | hart | Schlag, Swell |
| 13 | 70-73 | Titelkarte auf Schwarz | hart | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** keiner; jede Einstellung ist ein gemaltes Standbild oder ein kurzer Clip. Kinobalken in Totalen: oben und unten je 12 % der Bildhöhe Schwarz.
- **Bildbehandlung:** Grading: Schatten nach `#070F15` (nur die tiefsten Schatten, rund 35 % der Fläche), Mitten blaugrau um 0,19 Helligkeit, Sättigung −40 %, warme Töne nur in den Lichtern ab 80 % erlauben (selektiv Ocker und Glut stehen lassen). Feine Pinselkörnung als Textur (Rauschen 4 %, `overlay`). Vignette 30 %. Glow nur am Funken (Weichzeichner 1,5 % der Bildhöhe, `screen`).
- **Starter-Bausteine:** Ebenen-Parallaxe als zwei bis drei gestapelte `Kamera` (Rezept in `starter/BAUSTEINE.md`), Facetten als SVG in `Flaeche`, gemalte Kanten mit `Gemalt` (Verläufe nie darin), Lichteinfall mit `Partikel kind="schein"`, Funke mit `Partikel kind="funke"`, Staub mit `Partikel kind="dot"`, Gravur mit `Titelkarte variant="relief"`, Inserts mit `insert`, Ton mit `taktbauer.py --stil episch --bordun A --akzent …` (Akzent auf jeden Schnitt). Die Facettenwelt selbst bleibt Motivarbeit.
- **Bausteine:** Ebenen-Parallaxe (Standbild in zwei bis drei Tiefenebenen zerlegen, Vordergrund 3 %, Mitte 1,5 %, Hintergrund 0,5 % Verschiebung über die Einstellung); Staub (100 bis 200 Partikel im Lichtkegel, 0,1 bis 0,3 % der Bildhöhe, langsam steigend); Funke (heller Punkt mit fünf bis acht kurzen Strahlen, flackert); Steingravur (Wort in schmaler Grotesk, als Vertiefung: dunkle Kante oben links 0,2 %, helle unten rechts 0,2 %, 85 % Deckung); Titelkarte (zwei Zeilen mittig, 6 % und 3 % der Bildhöhe).
- **Typografie:** Gravur und erste Titelzeile in schmaler fetter Grotesk (frei lizenziert zum Beispiel Oswald 600 oder Bebas Neue), zweite Zeile dünn und gesperrt (zum Beispiel Inter 300, Laufweite +10 %).
- **Bewegung:** Jede Einstellung mit Push oder Pull von 3 bis 6 % über die ganze Dauer, Ease-in-out, oder Parallaxe. Schnitte genau auf dem Raster; Inserts zwei bis drei Frames.
- **Formate:** Quelle 16:9. In 9:16 Totalen hochkant neu komponieren (Horizont auf 55 % der Bildhöhe, Himmel mit Licht oben), Schluchten passen besonders gut, Kinobalken entfallen; Figuren auf 60 % der Bildhöhe. In 16:9 wie die Quelle.
- **Neue Kennungen:** `neu:facetten-welt`: Die ganze Welt besteht aus flachen, scharfkantigen Flächen wie gefaltetes Papier. `neu:letterbox`: Schwarze Kinobalken oben und unten.

## Material
- **Bilder (Welt):** `dark faceted geometric landscape with [subject], angular stone shards like folded paper, painterly flat facets with brush texture, cold blue-gray palette, a single warm amber light source, epic scale, tiny figure for scale, cinematic wide shot`
- **Bilder (Figur):** `colossal faceted stone figure of [subject], low-poly sculpted planes, hard side light, cold slate tones with one warm ochre highlight, painterly, dark background`
- **Musik:** `musik.py --karte facetten-saga.md` (ElevenLabs Music) oder eigene Musik, Raster mit `takt.py` am fertigen Bett; Akzente auf den Schnitten und der Schlag nach dem Atem als eigene Spur aus `taktbauer.py --nur-schlaege --schlag <n> --akzent <jeder Schnitt>` (die Musik im Atem stumm). Der Taktbauer ist keine Musikquelle mehr (18.10.2026).
- **Musik:** `Slow epic ambient score, 60 BPM, deep taiko hit on every second beat, low cello drone, distant choir pad, stone scraping textures, rising swell from fifteen seconds, final low hit at seventeen seconds, instrumental, no vocals`
- **Geräusche:** Steinschaben, Staubrieseln, Funkenknistern beim Riss, Wind in der Schlucht; 12 bis 18 dB unter der Musik.

## Regler
- Warmer Akzent: Ocker ist der Kern; Glutrot oder Gold gehen, immer nur eine warme Farbe.
- Einstellungslänge: 1,25 bis 2,5 s.
- Anteil Kinobalken: nur Totalen oder durchgehend.
- Für Sagen und Geschichte: Gestalt und Requisiten der Erzählung als Facettenfiguren.
- Mit Sprechstimme: Stimme setzt nach dem ersten Schlag ein, Schnitte bleiben auf dem Schlag.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen, besonders die niedrige Farbigkeit.
- Standbild-Prüfung: höchstens eine warme Fläche je Bild; keine weichen, runden Formen; Gestalt winzig gegen die Umgebung.
- Streifen bei 12 fps: jeder Schnitt auf dem Raster mit hörbarem Akzent; Inserts nicht länger als drei Frames.
- Schnitterkennung: Bei dunklen, kontrastarmen Bildern findet Schwelle 10 manchmal keinen Schnitt; dann die Gegenprobe `--schwelle 5` (`abnahme.py` weist selbst darauf hin), maßgeblich bleibt 10.
- Vorprüfung: Die ruhigen Fahrten (3 bis 6 % über bis 2,5 s) auf dunklen Bildern unterschreiten die Standbild-Schwelle der Blockdifferenz; die Phasenkorrelation der Vorprüfung meldet sie grün. Bleibt an Klammer oder Schlusskarte Rot stehen, entscheidet der Prüfer am Streifen.

## Fallen
- Glatte 3D-Optik ohne Pinselstruktur → wirkt wie Spielgrafik; Körnung und gemalte Kanten verlangen.
- Mehrere warme Farben → die Kälte und der Akzent gehen verloren.
- Schnitte neben dem Raster → bei diesem ruhigen Tempo fällt jede Abweichung auf; Musik vorher messen.
- Raster im Doppeltempo → `takt.py` meldet ein 60er-Bett mit Achtel-Hi-Hat oft als 120 (mit Halbtempo-Hinweis); mit `--min 50 --max 70` messen oder die `takt.json` des Taktbauers nehmen. Liegt eine eigene Fläche unter dem Bett, am Bett messen.
- Hexwerte der Palette als Flächenfarben → Bild zu dunkel (0,10 statt 0,19), die Abnahme erkennt dann keine Schnitte mehr. Die Palette nennt Rollen; Mitten anheben.
- RauFilter oder `Gemalt` über Lichtverläufen → Ringe und Bänder; Verläufe in eine eigene, ungefilterte Ebene.
- Zu viele Details → die Größe fehlt; viel dunkle Fläche lassen.
- Inserts länger als 0,1 s → werden zu eigenen Einstellungen und stören den Takt.
