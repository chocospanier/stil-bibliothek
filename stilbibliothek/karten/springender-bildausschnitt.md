---
id: springender-bildausschnitt
name: Springender Bildausschnitt
familie: bewegung
kurz: Ein einziges Handyvideo läuft in einem Bildfenster auf Schwarz; das Fenster selbst tanzt im Takt, wird breit, schmal, kippt in die Tiefe und schließt sich zum Schlitz, um am neuen Ort wieder aufzugehen.
kern: [Bildfenster auf schwarzer Fläche, das auf jedem Schlag Form, Breite und Kippung wechselt, Inhalt wird beschnitten statt skaliert (das Fenster ist ein Ausschnitt), Ortswechsel durch Zuklappen zum Schlitz statt Schnitt]
energie: 2
format_quelle: "3:4"
laenge_s: [10, 20]
messung:
  shot_median_s: 13.57
  schnitte_pro_s: 0.1
  schnitte_verlauf: [0.0, 0.0, 0.2]
  bpm: 64
  schnitt_auf_beat: niedrig   # nur ein erkannter Schnitt, nicht messbar; die Fensterbewegung folgt dem Takt
  lufs: -17.3
  helligkeit: 0.09
  kontrast: 0.15
  farbigkeit: 0.10
schnittmuster_16tel: [58, 6]
palette:
  flaeche: "#020101"
  raum_dunkel: "#1E1715"
  raum_mitte: "#564840"
  haut_licht: "#A28162"
  zweiter_ort: "#3A6FA0"
effekte: [harter-schnitt, masken-wechsel, bild-im-bild, zoom-schlag, handkamera, lippen-sync, tanz, outfit-wechsel, beat-getrieben, fenster-tanz]
kamera: Im Fenster eine Handy-Handkamera; die eigentliche Bewegung macht das Fenster (Breite, Höhe, Kippung um die senkrechte Achse), dazu ein, zwei Zoom-Schläge im Inhalt.
ton: Leise gemischter Song (−17,3 LUFS, 6,1 LU Spanne), gemessen 64 BPM, Fenster wechselt etwa jeden halben Takt eines Stücks um 128; die Figur singt sichtbar mit (Lippen-Sync).
braucht: [fotos-figur, footage-ort]
motor_aufwand: klein
einsatz: [musikvideo, portrait, uebergang, ganzes-kurzvideo]
abnahme:
  shot_median_s: [8, 16]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.07, 0.12]
  farbigkeit: [0.08, 0.12]
  lufs: [-15, -13]   # Vorlage −17,3; für Kanäle bewusst auf −14
quelle: Eigene Analyse einer öffentlichen Vorschau; nur der Look ist beschrieben, keine Motive, Texte oder Marken übernommen.
---

# Springender Bildausschnitt

Ein schlichtes Selfie-Video wird zum Musikvideo, weil sein Rahmen mittanzt. Auf schwarzer Fläche springt das Bildfenster im Takt von breit zu schmal, kippt nach links und rechts in die Tiefe und klappt zum Ortswechsel zu einem Schlitz zusammen. Die Energie kommt nur aus dem Fenster, der Inhalt bleibt ein einfacher Clip.

## Kern
- **Das Fenster tanzt:** Auf jedem Schlag eine neue Form: volle Breite, schmal und hoch, quadratisch, nach links oder rechts gekippt. Die Form hält bis zum nächsten Schlag.
- **Ausschnitt statt Skalierung:** Wenn das Fenster schmaler wird, bleibt die Figur gleich groß, nur der sichtbare Ausschnitt ändert sich. Dadurch wirkt es wie ein Fenster, nicht wie ein schrumpfendes Video.
- **Zuklappen statt Schneiden:** Ein Ortswechsel passiert, indem das Fenster in sechs Frames zum senkrechten Schlitz zusammenklappt und mit dem neuen Ort und neuem Outfit wieder aufgeht.

## Erkennung
- **Bild:** Schwarze Fläche `#020101` füllt 40 bis 60 % des Bildes. Im Fenster ein Handyvideo: dunkles Zimmer bei Nacht mit warmen und bläulichen Lichtern (`#1E1715`, `#564840`, Haut `#A28162`), später ein zweiter Ort mit kühlem Blau `#3A6FA0`. Kein Rahmen, keine Kontur, harte Kanten. Gemessen: Helligkeit 0,09, Kontrast 0,15, Farbigkeit 0,10, 72 % fast schwarz (die Fläche).
- **Schnitt:** praktisch keiner: ein harter Schnitt bei 13,6 s, ein Ortswechsel per Zuklappen bei rund 8,7 s. Die Fensterform wechselt etwa alle 0,4 bis 0,6 s.
- **Ton:** −17,3 LUFS, Lautheitsspanne 6,1 LU, True Peak −3,4 dBFS. Song mit Gesang, die Figur singt mit.
- **Text:** keiner.

## Bildtypen
| Bildtyp | Anteil | Komposition | Dauer typisch |
|---|---:|---|---|
| Fenster breit | 35 % | 100 % der Bildbreite, 55 bis 60 % der Bildhöhe, mittig; Figur halbnah, Kopf im oberen Drittel des Fensters | 1 bis 3 s am Stück |
| Fenster schmal und hoch | 20 % | 40 bis 55 % der Bildbreite, 60 bis 65 % der Bildhöhe, mittig oder leicht versetzt | ein Schlag |
| Fenster gekippt | 25 % | 60 bis 80 % der Breite, um die senkrechte Achse 10 bis 18° gedreht, nahe Kante 10 % höher als ferne | ein Schlag |
| Schlitz beim Ortswechsel | 5 % | Fenster 2 bis 10 % breit, volle Fensterhöhe | sechs Frames zu, sechs Frames auf |
| Zoom im Fenster | 15 % | Inhalt springt auf 150 %, Gesicht füllt das Fenster | ein bis zwei Schläge |

## Dramaturgie
- **Hook (0 bis 2,8 s):** Fenster breit, steht fast, die Figur singt die erste Zeile direkt in die Kamera.
- **Tanz (2,8 bis 8,5 s):** auf jedem Schlag eine neue Fensterform: schmal, gekippt, breit, quadratisch.
- **Wechsel (8,5 bis 8,9 s):** Fenster klappt zum Schlitz und geht am neuen Ort auf, Figur in neuem Outfit.
- **Zweiter Ort (8,9 bis 13,6 s):** Fenster wieder breit mit Kippungen, ein Zoom-Schlag aufs Gesicht.
- **Schluss (13,6 bis 15 s):** harter Schnitt auf eine zweite Einstellung desselben Ortes, Fenster steht.

## Schnittmuster
Hier gibt es kaum Schnitte; der Bauplan beschreibt die Fensterbewegung in Schlägen bei 128 BPM (ein Schlag 0,47 s, 38 Schläge für 18 s). Die Musik am fertigen Bett messen und jede Formänderung auf einen Schlag legen.

| Slot | Schläge | Fensterform und Inhalt | Übergang | Ton |
|---|---|---|---|---|
| 1 | 0-5 | breit, steht; Figur singt in die Kamera | keiner | Gesang setzt ein |
| 2 | 6 | schmal und hoch, mittig | Fenster-Sprung | Beat |
| 3 | 7 | gekippt nach links, 15° | Fenster-Sprung | Beat |
| 4 | 8 | quadratisch, leicht nach rechts versetzt | Fenster-Sprung | Snare |
| 5 | 9-10 | breit, leichte Kippung rechts | Fenster-Sprung | Beat |
| 6 | 11-17 | je Schlag eine der vier Formen, nie zweimal dieselbe hintereinander | Fenster-Sprung | Refrain |
| 7 | 18 | schließt sich zum Schlitz | Schlitz | Riser |
| 8 | 19 | öffnet am neuen Ort, neues Outfit | Schlitz | Drop |
| 9 | 20-27 | breit, zwei Kippungen links und rechts | Fenster-Sprung | Beat |
| 10 | 28-29 | Zoom-Schlag aufs Gesicht im Fenster | Zoom-Schlag | Hit |
| 11 | 30-31 | harter Schnitt auf zweite Einstellung | hart | Beat |
| 12 | 32-37 | Fenster wächst auf volle Breite und steht | keiner | Ausklang |

## Rezept für einen Code-Motor
- **Grund:** Fläche `#020101`, sonst nichts.
- **Bildbehandlung:** Clip unverändert, leichte Aufhellung der Schatten (+5 %), damit er sich von der Fläche löst. Der Clip liegt in einem Container mit `overflow: hidden`; der Clip selbst bleibt in Größe und Lage fest (mittig, Höhe 70 % der Bildhöhe), nur der Container ändert Breite und Höhe. So entsteht der Ausschnitt-Effekt.
- **Bausteine:** Fenster-Tanz (Container mit `perspective: 1200px` auf dem Elternteil; Formen als Liste: breit 100 % × 57 %, schmal 48 % × 63 %, quadratisch 62 % × 57 % mit +6 % Versatz, gekippt 72 % × 57 % mit `rotateY(±15deg)` und `rotateX(±3deg)`; Wechsel in vier Frames mit Ease-out, dann halten bis zum nächsten Schlag); Schlitz (Breite in sechs Frames auf 2 %, Clip tauschen, in sechs Frames zurück auf die Ausgangsform, Ease-in-out); Zoom-Schlag (Clip im Container in drei Frames auf 150 %, zwei Schläge halten, in sechs Frames zurück).
- **Typografie:** keine in der Vorlage. Wird ein Titel gebraucht: klein auf der schwarzen Fläche unter dem Fenster, schlichte Grotesk (frei lizenziert zum Beispiel Inter 600), 3 % der Bildhöhe, bewegt sich nicht mit.
- **Bewegung:** Formwechsel auf jedem Schlag, im Hook und am Schluss Ruhe. Nie dieselbe Form zweimal hintereinander. Kippung abwechselnd links und rechts.
- **Formate:** Quelle 3:4. In 9:16 dieselben Formen mit Fensterhöhe 45 bis 55 % der Bildhöhe, die schwarze Fläche oben und unten trägt Raum für Titel. In 16:9 Formen in der Breite schmaler (40 bis 70 %), damit links und rechts Fläche bleibt; Kippung wirkt dort am stärksten.
- **Neue Kennungen:** `neu:fenster-tanz`: Der Bildausschnitt ändert im Takt Größe, Seitenverhältnis und Kippung, der Inhalt bleibt fest.

## Material
- **Bilder (Ort 1):** `vertical phone video still of [subject] dancing and singing along in a dim bedroom at night, practical lamps, city lights in the window, candid, slight motion blur`
- **Bilder (Ort 2):** `vertical phone video still of [subject] in a playful costume in a surprising location, cool blue light, candid selfie angle, singing along`
- **Musik:** `Upbeat R&B pop, 128 BPM, punchy kick on every beat, finger snaps, warm bass, catchy vocal hook, soft intro for two point eight seconds, full beat from two point eight seconds, short riser at eight point five seconds, drop with new section at nine seconds, outro from fifteen seconds`
- **Geräusche:** keine nötig; ein leises Klack beim Zuklappen zum Schlitz (−16 dB).

## Regler
- Formwechsel je Schlag oder je halbem Takt; je halbem Schlag wird es hektisch.
- Kippwinkel 8 bis 20°.
- Anzahl Orte: einer bis vier, jeder Wechsel per Schlitz.
- Fensterrand: ohne ist der Kern; ein dünner weißer Rand macht daraus eine Polaroid-Variante.
- Für Erklärvideos: Fenster tanzt nur auf Schlüsselwörtern, sonst steht es.

## Abnahme
- Render mit `video_schauen.py` messen: Werte aus `abnahme` treffen; erwartet sind kaum erkannte Schnitte und sehr niedrige Helligkeit wegen der Fläche.
- Standbild-Prüfung: Figur hat in schmalem und breitem Fenster dieselbe Größe; Fensterkanten scharf.
- Streifen bei 12 fps: jede Formänderung liegt auf einem Schlag; das Zuklappen dauert höchstens sechs Frames je Richtung.

## Fallen
- Clip mit dem Fenster mitskaliert → wirkt wie ein schrumpfendes Video; Inhalt fest, nur Ausschnitt ändern.
- Formwechsel mit weicher, langer Animation → das Tanzen fehlt; vier Frames, dann stehen.
- Figur gerät beim schmalen Fenster aus dem Bild → Clip vorher so beschneiden, dass das Gesicht mittig liegt.
- Leise Vorlage übernehmen → auf Kanälen untergeht; Master auf −14 LUFS.
- Echte Gesichter fremder Personen → nur eigene Aufnahmen mit Einwilligung.
