---
id: rotlicht-camcorder
name: Rotlicht-Camcorder
familie: filmlook
kurz: Nächtliche Camcorder-Aufnahmen einer Person, fast einfarbig in Rot bis Magenta getaucht, weich verwischt, darüber tippt sich eine Liedzeile Wort für Wort in kleiner weißer Schrift.
kern: [ein Farbkanal regiert das ganze Bild (Rot bis Magenta auf Schwarz), weiche Camcorder-Unschärfe mit Bewegungsschlieren statt harter Schnitte, Liedzeile tippt sich Wort für Wort mit weißem Störbalken]
energie: 2
format_quelle: "4:3"
laenge_s: [10, 18]
messung:
  shot_median_s: 9.07   # Messung erkennt nur einen harten Schnitt; sichtbar sind fünf Einstellungen von 2 bis 3,5 s, verbunden durch Schlieren und weiche Blenden
  schnitte_pro_s: 0.1
  schnitte_verlauf: [0.24, 0.0, 0.0]
  bpm: 110
  schnitt_auf_beat: niedrig
  lufs: -14.2
  helligkeit: 0.21
  kontrast: 0.18
  farbigkeit: 0.30
schnittmuster_16tel: [25, 66]
palette:
  grund: "#160315"
  tiefe: "#590623"
  licht_rot: "#A64659"
  spitze_magenta: "#E0458F"
  text: "#F4EEF0"
effekte: [blende, wischer, bewegungsunschaerfe, vhs, duoton, glow, vignette, handkamera, filmkorn, untertitel, schreibmaschine]
kamera: Handgeführter Camcorder, langsam und schwebend, folgt der Person, verliert sie in der Bewegung kurz in die Unschärfe.
ton: Langsamer, verträumter Gesang über einem weichen Beat um 110 BPM (Halbtempo-Gefühl), sehr gleichmäßig laut; die Schrift folgt den gesungenen Silben.
braucht: [fotos-figur, footage-ort]
motor_aufwand: mittel
einsatz: [musikvideo, hook, portrait]
abnahme:
  shot_median_s: [2.0, 9.5]
  schnitte_pro_s: [0.05, 0.4]
  helligkeit: [0.16, 0.26]
  farbigkeit: [0.24, 0.36]
  lufs: [-15.2, -13.2]
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Rotlicht-Camcorder

Fühlt sich an wie ein alter Camcorder-Abend, den jemand mit rotem Partylicht gefilmt und Jahre später wiedergefunden hat. Die Energie ist gedämpft: Sie kommt aus der verträumten Bewegung der Person, aus der Farbe und aus der Liedzeile, die sich Silbe für Silbe ins Bild schreibt.

## Kern
- **Ein Farbkanal regiert:** Alles außer Schwarz ist Rot, Rosa oder Magenta. Nur der erste Shot darf noch eine fremde Lichtfarbe (eine grelle Leuchtreklame) tragen, danach kippt alles in Rot. Mehrfarbige Bilder machen daraus einen normalen Nachtclip.
- **Weichheit statt Schnitt:** Die Einstellungen gehen über Bewegungsschlieren, Reißschwenk und Unschärfe ineinander über. Eine Schnitterkennung findet fast nichts, obwohl fünf Orte vorkommen. Harte Schnitte zerstören die Traumstimmung.
- **Die getippte Liedzeile:** Kleine weiße Grotesk mitten im Bild, die Wörter erscheinen einzeln im Silbentakt, vor dem nächsten Wort huscht ein heller Störbalken. Ohne die Zeile ist es nur ein Farbfilter.

## Erkennung
- **Bild:** dunkler Grund (Helligkeit 0,21, 40 % der Fläche fast schwarz), darin Haut und Kleidung in Rot bis Magenta (`#A64659` als Hauptton, 45 % der Fläche). Lichter blühen weich auf, Ränder vignettiert, Korn und leichte Camcorder-Weichzeichnung. In schnellen Passagen waagerechte Schlieren wie bei einem Bandfehler. Farbigkeit 0,30, also kräftig, aber eintönig.
- **Schnitt:** 12,5 s Vorlage. Gemessen zwei Shots (Wechsel bei 3,4 s), sichtbar fünf Einstellungen: Gang unter Leuchtreklame (0 bis 3 s), Rückenansicht im Dunkeln (3 bis 4 s), verwischte Drehung (4 bis 6 s), Nahaufnahme Gesicht mit Brille (6 bis 9 s), Halbnah am Geländer in Magenta (9 bis 12,5 s). Übergänge: Bewegungsunschärfe, kurze Weißschliere, weiche Blende von 6 bis 10 Bildern.
- **Ton:** −14,2 LUFS, Lautheitsspanne nur 0,6 LU, also völlig gleichmäßig. Gesang trägt das Stück; die Schrift folgt ihm, nicht dem Beat.
- **Text:** eine Rolle: Liedtext als mittige Einzelzeile, Höhe der Kleinbuchstaben 2,5 bis 3 % der Bildhöhe, weiß, schlichte Grotesk, klein geschrieben, ohne Kontur oder Kasten. Liegt bei 50 % der Bildhöhe (in der Nahaufnahme tiefer, bei 75 %, damit das Gesicht frei bleibt). Wörter erscheinen einzeln; ein Silbenstrich am Wortende zeigt an, dass das Wort weitergeht.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Person geht, Untersicht unter greller Leuchtreklame | 20 % | Figur halbnah von unten, Kopf bei 15 % der Bildhöhe, Körper füllt 90 % der Höhe, rechts der Mitte; links Lichtstreifen diagonal | 2,5 bis 3,5 s |
| Rückenansicht im Dunkeln | 10 % | Figur 60 % der Bildhöhe, mittig, fast nur Silhouette mit hellem Kopftuch oder Haar | 1 s |
| Verwischte Drehung | 15 % | Torso füllt 100 % der Höhe, starke Bewegungsunschärfe, Schlieren rechts | 1,5 bis 2 s |
| Nahaufnahme Gesicht, Blick an der Kamera vorbei | 30 % | Gesicht 70 bis 90 % der Bildhöhe, angeschnitten, links oder mittig; Hintergrund Schwarz mit roten Lichtstreifen | 2,5 bis 3 s |
| Halbnah am Geländer, Kopf im Nacken | 25 % | Figur rechts, Kopf bei 20 % der Bildhöhe, Arm auf Geländer im unteren Drittel, dunkle Tür im Hintergrund | 3 bis 4 s |

## Dramaturgie
- **Hook (0 bis 3 s):** der einzige Shot mit fremder Lichtfarbe: Person läuft unter greller Reklame, die erste Silbe tippt sich ins Bild.
- **Abtauchen (3 bis 6 s):** Rückenansicht, dann verwischte Drehung; die Farbe kippt komplett in Rot.
- **Nähe (6 bis 9 s):** Gesicht nah, die Liedzeile vollendet ihren ersten Satz.
- **Halt (9 bis 12,5 s):** Magenta, Person am Geländer, Kopf zurück, eine neue Zeile baut sich Wort für Wort auf und bleibt stehen.

## Schnittmuster
Kein Beat-Schnitt: in Sekunden denken. Bauplan für 18 s, sechs Einstellungen, Wechsel auf gesungene Phrasenenden.

| Slot | Sekunden | Bildtyp | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-3,2 | Person geht unter Leuchtreklame, Untersicht | Start | Gesang setzt ein, erstes Wort tippt bei 0,3 s |
| 2 | 3,2-4,4 | Rückenansicht im Dunkeln | weiche Blende 8 Bilder | Phrasenende |
| 3 | 4,4-6,2 | verwischte Drehung | Reißschwenk mit Schliere | Wort für Wort weiter |
| 4 | 6,2-9,2 | Nahaufnahme Gesicht | Bewegungsunschärfe löst sich auf | Satz endet bei 8,8 s |
| 5 | 9,2-12,6 | Halbnah am Geländer in Magenta | weiche Blende 10 Bilder | neue Zeile beginnt |
| 6 | 12,6-15,2 | Nahaufnahme Hände oder Haar im Licht | Wischer | Zeile wächst |
| 7 | 15,2-18 | Gesicht halbnah, Blick in die Kamera, Zeile bleibt stehen | weiche Blende | Phrase klingt aus |

## Rezept für einen Code-Motor
- **Grund:** kein eigener Grund; das Footage ist die Bühne. Wo Schwarz entsteht, auf `#160315` anheben (nie reines Schwarz, ein Hauch Violett).
- **Bildbehandlung:** Footage erst entsättigen, dann als Duoton einfärben: Schatten `#160315`, Mitten `#A64659`, Lichter `#F2A7C3`, in den Spitzen bis `#E0458F`. In SVG: `feColorMatrix` saturate 0, dann `feComponentTransfer` mit `tableValues` je Kanal (Rot 0,09 0,65 0,95; Grün 0,01 0,27 0,65; Blau 0,08 0,35 0,76). Glow: Lichter über 70 % Helligkeit herauslösen, mit `feGaussianBlur` stdDeviation 1,5 % der Bildhöhe weichzeichnen, mit 50 % `screen` zurücklegen. Weichzeichnung des ganzen Bildes 0,15 % der Bildhöhe. Vignette 35 % an den Ecken. Korn 6 %. VHS-Schlieren: in Bewegungsshots alle 0,5 bis 1 s für 3 bis 5 Bilder einzelne Bildstreifen von 1 bis 3 % Höhe waagerecht um 2 bis 6 % der Breite versetzen.
- **Bausteine:** Duoton-Filter, Glow, Schlieren-Generator, Tipp-Zeile. Die Tipp-Zeile setzt je gesungener Silbe ein Wort (oder Wortteil mit Silbenstrich), davor erscheint für 3 bis 4 Bilder ein weißer Balken in Breite des kommenden Wortes, 60 % der Zeichenhöhe hoch, leicht ausgefranst, dann steht das Wort. Zeilen bleiben bis zum Phrasenende stehen und verschwinden in einem Bild.
- **Typografie:** schlichte Grotesk, Regular, zum Beispiel Inter 400 oder Arimo 400, Weiß `#F4EEF0`, x-Höhe 2,5 bis 3 % der Bildhöhe, alles klein geschrieben, mittig auf 50 % der Bildhöhe, bei Nahaufnahmen auf 72 bis 78 %. Kein Schatten, keine Kontur; die Dunkelheit trägt die Lesbarkeit.
- **Bewegung:** Kamera schwebt: leichte Handkamera (±0,6 % Versatz, langsame Drift über 2 s), dazu in Übergängen ein Reißschwenk mit gerichteter Bewegungsunschärfe über 6 bis 10 Bilder. Blenden linear, 6 bis 10 Bilder. Keine harten Schnitte außer am Phrasenanfang, wenn die Musik einen Schlag hat.
- **Formate:** 4:3 ist das Original. In 9:16 rückt die Figur in die Mitte, Nahaufnahmen füllen die Breite, die Textzeile liegt bei 60 % der Höhe und bricht nie um (lieber weniger Wörter je Zeile). In 16:9 Figur ins rechte oder linke Drittel, Schwarz mit Vignette füllt die Seite, Textzeile bleibt mittig. Optional ein schmaler schwarzer 4:3-Rahmen links und rechts, wenn das Camcorder-Gefühl wichtiger ist als die Fläche.

## Material
- **Bilder:** `grainy 2000s camcorder still of [subject] at night under red party light, monochrome red and magenta tones, soft focus, light bloom, motion blur, dreamy candid mood, black background`
- **Bilder (Einstieg):** `low angle camcorder shot of [subject] walking at night past a glowing storefront sign, harsh fluorescent light streaks, grainy, slightly blurred, dreamy`
- **Musik:** `Dreamy bedroom R&B, 110 BPM with a half-time feel, muffled kick, lo-fi snare, warm Rhodes chords, soft sub bass, tape wobble; 0-3 s Rhodes alone, 3 s soft beat enters, steady and even to 15 s, last 3 s Rhodes alone with reverb tail, instrumental, no vocals`. Die Liedzeile im Bild gehört zum eigenen Gesang, der darübergelegt wird; ohne Gesang trägt eine gesprochene, geflüsterte Zeile.
- **Geräusche:** feines Bandrauschen durchgehend 30 dB unter der Musik, ein kurzes VHS-Schnarren in jedem Reißschwenk, 18 dB unter der Musik.

## Regler
- Farbkanal: Rot bis Magenta ist der Kern, Kobaltblau oder Giftgrün tragen genauso, solange es ein einziger Kanal bleibt.
- Weichheit: von leicht weich bis fast traumhaft verschmiert; Gesichter müssen in der Nahaufnahme scharf genug für die Augen bleiben.
- Text: Liedzeile, Gedankensatz oder ein einziges wiederholtes Wort; immer Wort für Wort.
- Länge: 10 bis 25 s; länger braucht eine zweite Farbe als Kapitelwechsel (zum Beispiel Rot zu Magenta wie in der Vorlage).

## Abnahme
- Render mit `video_schauen.py` messen: Helligkeit und Farbigkeit aus `abnahme`. Die Schnittzahl darf niedrig ausfallen, weil weiche Übergänge nicht erkannt werden; dann am Streifen zählen: fünf bis sieben Einstellungen auf 18 s.
- Standbild an drei Stellen: außer Schwarz nur Töne eines Farbkanals, Lichter blühen, keine knackscharfen Kanten.
- Streifen bei 12 fps: jedes Wort erscheint einzeln mit Balken davor, kein Wort springt ohne Gesang.

## Fallen
- Footage behält Eigenfarben (grüne Bäume, blaue Jeans) → Duoton zwingend über alles, nicht nur ein Rotfilter mit 50 % Deckung.
- Text mit Schatten oder Kasten → wirkt wie TikTok-Untertitel. Nackte weiße Zeile, Dunkelheit sorgt für Kontrast.
- Harte Schnitte im Beat → der Traum reißt. Wechsel nur über Unschärfe oder Blende.
- Zu viel Glow → Gesichter werden zu rosa Flecken. Glow nur auf Lichter über 70 % Helligkeit.
- Ganze Zeile auf einmal eingeblendet → Karaoke-Optik geht verloren. Wort für Wort, im Silbentakt.
- Reines Schwarz in den Schatten → wirkt digital. Schwarz auf einen dunklen Violettton anheben.
