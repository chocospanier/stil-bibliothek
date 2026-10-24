# Stil-Bibliothek für Kurzvideos aus Code

106 Video-Stile in 19 Familien, so beschrieben, dass ein Mensch oder eine KI sie mit einem Code-Motor (Remotion, Canvas, SVG, After Effects, Blender) nachbauen kann. Dazu das Prüf-Wissen aus 26 gebauten Stücken und 24 Prüfberichten, ein frischer Prüfer als Agent-Definition, Mess-Werkzeuge ohne Credits, Vorlagen für eigene Stile und Kanäle und ein Remotion-Starter mit 28 Bausteinen und neun durchgebauten Beispielen. Stand 17.10.2026.

## Für wen
Für alle, die Kurzvideos (9:16 und 16:9, 15 s bis einige Minuten) mit Code statt mit Schnittprogramm bauen und dabei nicht jedes Mal bei null anfangen wollen: Creator, kleine Agenturen, Marken mit eigenem Kanal, und jede KI, die für sie baut. Figuren und Material bringt jeder selbst mit; Stimme und Musik kommen über ElevenLabs mit eigenem Schlüssel (`musik.py`, `stimme.py`) oder aus eigener, lizenzierter Quelle. Das Paket enthält keine Figuren, keine Stimmen und keine fertigen Videos. Es enthält einen Starter-Motor für Remotion: Bausteine, Helfer und neun Beispiele im Quellcode (vier davon in der Familie erklaerstimme: die Wortzeiten liegen bei, die Stimme bringt jeder selbst).

## Was drin ist
| Ordner | Inhalt | Einstieg |
|---|---|---|
| [stilbibliothek/](stilbibliothek/LIESMICH.md) | 106 Stil-Karten (eine Datei je Stil, Kopfblock maschinenlesbar), 19 Familien, Effekt-Vokabular mit rund 180 Kennungen, `index.json` zum Filtern, die Anleitung `SKILL.md` für eine KI | [FAMILIEN.md](stilbibliothek/FAMILIEN.md) |
| [pruefen/](pruefen/FEHLERKATALOG.md) | Fehlerkatalog: acht Ursachen, Gegenmittel, Checkliste vor dem Rendern. Prüfer-Definition: ein zweites Modell prüft, was das erste gebaut hat | [FEHLERKATALOG.md](pruefen/FEHLERKATALOG.md) |
| [werkzeuge/](werkzeuge/INSTALL.md) | `video_schauen.py` (Schnitte, Kontaktbögen, Lautheit, Tempo), `vorpruefung.py` (Randstreifen, Blitze, Standbilder, Schutzzonen, Lautheit), `streifen.py` (12 Bilder je Sekunde), `kamera.py` (Kamerabewegung je Shot), `bibliothek_index.py` (Karten prüfen, Index bauen) | [INSTALL.md](werkzeuge/INSTALL.md) |
| [vorlagen/](vorlagen/HAUSSTIL_VORLAGE.md) | Formular für einen eigenen Hausstil, Formular für einen Kanal (Versprechen, Takt, Gates) | |
| [starter/](starter/LIESMICH.md) | Remotion-Projekt: 28 Bausteine plus Tonspur, Helfer (Raster vom Ton, Storyboard, Abnahme, Handy-Fassung, Musik und Stimme über ElevenLabs, Schläge, Mund nach Stimmpegel), neun Beispiele in 9:16, drei davon auch in 16:9 | [starter/LIESMICH.md](starter/LIESMICH.md) |
| [ABLAUF.md](ABLAUF.md) | Der Bauweg von der Stilwahl bis zur Abnahme | |
| [GLOSSAR.md](GLOSSAR.md) | Die Begriffe der Karten (Sechzehntel, Blitzregel, Schutzzone, Bild 0, Halt, Pointe …) | |
| [LIZENZ.md](LIZENZ.md) | Nutzungsbedingungen des Pakets, Lizenz des übernommenen Werkzeugteils | |

## In zehn Minuten zum ersten Stil
1. [FAMILIEN.md](stilbibliothek/FAMILIEN.md) öffnen, die Familie nach Wirkung und Einsatz wählen.
2. Eine Karte aus der Familie öffnen. Die drei `kern`-Merkmale sind nicht verhandelbar, alles andere sind Regler.
3. Den Abschnitt „Rezept für einen Code-Motor“ lesen: Grund, Bildbehandlung, Bausteine, Typografie, Bewegung, Formate. Das ist die Bauanleitung.
4. Mit den Prompts unter „Material“ eigene Bilder und Musik erzeugen oder eigenes Material nehmen. Jedes generierte Bild vor dem Einbau in voller Größe ansehen.
5. Bauen, dann prüfen: Checkliste im [Fehlerkatalog](pruefen/FEHLERKATALOG.md), `vorpruefung.py`, frischer Prüfer. Der ganze Weg steht in [ABLAUF.md](ABLAUF.md).

Wer in Remotion baut, beginnt im [Starter](starter/LIESMICH.md): `npm install`, dann `npm run storyboard`, `npm run render`, `npm run abnahme`. Die neun Beispiele zeigen, wie aus einer Karte eine Komposition wird.

Wer mit einer KI arbeitet (Claude Code, Cursor, ein anderer Agent), gibt ihr [SKILL.md](stilbibliothek/SKILL.md) als Anleitung und [PRUEFER.md](pruefen/PRUEFER.md) als zweite Rolle.

## Was eine Karte kann und was nicht
Eine Karte beschreibt einen Look mit Messzahlen (Shot-Länge, Schnittdichte, Tempo, Lautheit, Helligkeit, Farbigkeit), Schnittmuster in Sechzehnteln, Palette mit Rollen, Rezept, Material-Prompts, Abnahme-Zielwerten und erlebten Fallen. Sie ersetzt keinen Code: Wiederholbar wird ein Stil erst mit den passenden Bausteinen im Motor. Der Starter liefert die 28 Bausteine, die fast alle Karten tragen ([starter/BAUSTEINE.md](starter/BAUSTEINE.md)); der erste Bau eines Stils dauert trotzdem länger als jeder weitere.

## Herkunft
Jede Karte beruht auf der Messung eines öffentlich zugänglichen Vorschauvideos (Schnitterkennung, optischer Fluss, dominante Farben, Lautheit, Tempo) und auf dem Ansehen von Kontaktbögen. Beschrieben ist nur der Look: Rhythmus, Bildbehandlung, Komposition, Typografie, Ton. Keine Motive, Figuren, Marken, Texte oder Bilder der Quellen; die Karten enthalten kein fremdes Material. Die Fallen stammen aus 29 selbst gebauten Stücken (alle 19 Familien) und aus 27 Prüfberichten.

## Grenzen
- Tempo (BPM) ist aus der Tonspur geschätzt und kann halb oder doppelt sein; die Karten sagen, wo.
- Weiche Übergänge zählt die Schnitterkennung oft nicht; betroffene Karten nennen die Augen-Zählung.
- Messung ist kein Urteil. Am Ende entscheiden Auge und Ohr eines Menschen, am Handy.
