---
name: stilbibliothek
description: Baut ein Kurzvideo in einem von 106 beschriebenen Video-Stilen (Lookbook, Noir, Kopierer, Glitch, Scrapbook, Musikvideo, Kinetik-Typo, Erklärstimme und mehr) mit einem Code-Motor wie Remotion. Nutzen, wenn jemand ein Video „im Stil von …“, einen Trailer, Hook, Intro oder Edit mit bestimmtem Look will, einen passenden Look für ein Thema sucht oder einen fertigen Render gegen einen Stil prüfen will.
---

# Stil-Bibliothek benutzen

## 1. Stil wählen
- Wirkung und Einsatz klären: Was soll das Video tun (Hook, Trailer, ganzes Kurzvideo, Übergang), wie viel Energie (1 ruhig bis 5 rasant), welches Material gibt es (Fotos einer Figur, Illustrationen, Ortsaufnahmen, Produkt, nur Typo, 3D)?
- In [FAMILIEN.md](FAMILIEN.md) die Familie wählen, dann nach `einsatz`, `energie`, `braucht` und `motor_aufwand` filtern: `python -I ../werkzeuge/bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook` (Tabelle; mehrere Werte mit Komma, `energie>=4`; nur mit Code baubar: `nur_code=ja` oder `braucht<=nur-typo,illustrationen`). Höchstens drei Karten vorschlagen, eine empfehlen.

## 2. Karte lesen, Kern zuerst
- Die drei `kern`-Merkmale sind nicht verhandelbar. Alles andere sind Regler.
- `Bildtypen` sagen, welche Einstellungen es gibt und wie groß das Motiv ist; `Schnittmuster` ist der Bauplan.

## 3. Raster vom echten Ton
- Musik zuerst fertig machen (Prompt aus `Material` über `starter/werkzeuge/musik.py`, ElevenLabs Music, oder eigene, lizenzierte Musik; der Taktbauer setzt nur einzelne Schläge darüber), jedes Stück mit Text mit Vorlesestimme (`stimme.py`), dann Tempo und ersten Schlag am fertigen Ton messen (`starter/werkzeuge/takt.py`). Die Sechzehntel des Schnittmusters auf dieses gemessene Raster umrechnen, nie auf die Zahl im Prompt.
- Bei Stilen mit Sprechstimme: Wortzeiten aus einer Transkription mit Wortstempeln, Schnitte und Wörter auf die Silben.

## 4. Bauen
- In Remotion im Starter bauen (`starter/`): die Bausteine aus `starter/BAUSTEINE.md` nehmen, nicht neu erfinden; wie eine Karte zur Komposition wird, steht in `starter/LIESMICH.md`, neun durchgebaute Beispiele liegen in `starter/src/beispiele/`.
- Nach `Rezept für einen Code-Motor` bauen: erst Grund und Bildbehandlung als Standbild prüfen, dann Bausteine, dann Bewegung.
- Teure Filter einmal vorrechnen und cachen, nicht je Frame.
- Formate: die Hinweise für 9:16 und 16:9 in der Karte befolgen; in 9:16 die unteren 15 % freihalten.
- Rohmaterial mit den Prompts aus `Material` erzeugen oder eigene Fotos nehmen. Nie Motive, Marken oder Texte einer Vorlage nachbauen.

## 5. Abnahme
- Den Render messen und gegen `abnahme` im Kopfblock halten: `python -I starter/werkzeuge/abnahme.py <video> <karte.md>` gibt je Wert ✓ oder ✗.
- Standbilder an drei zufälligen Stellen gegen den Kern prüfen; einen Streifen mit 12 Bildern je Sekunde ansehen.
- Jede neue Falle in der Karte unter `Fallen` ergänzen.

## Grenzen
- BPM in den Karten kann halb oder doppelt sein; die Karte sagt, wo.
- Eine Karte beschreibt, sie baut nicht. Ohne passende Bausteine im Motor dauert der erste Bau eines Stils deutlich länger als jeder weitere.
