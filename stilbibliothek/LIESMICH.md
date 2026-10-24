# Stil-Bibliothek

106 Video-Stile für Kurzvideos, so beschrieben, dass ein Mensch oder eine KI sie in einem Code-Motor (Remotion, Canvas, SVG) nachbauen kann: mit Messzahlen, Schnittmuster, Rezept, Material-Prompts, Abnahme-Werten und bekannten Fallen. Stand 16.10.2026.

## Was drin ist
| Datei | Inhalt |
|---|---|
| [FAMILIEN.md](FAMILIEN.md) | Einstieg: 18 Stil-Familien, je Wirkung, Regler, Einsatz und Karten |
| [karten/](karten/) | 106 Stil-Karten, eine Datei je Stil, Kopfblock maschinenlesbar (YAML) |
| [INDEX.md](INDEX.md) · [index.json](index.json) | Übersicht je Familie, alle Kopfblöcke als JSON zum Filtern |
| [EFFEKT_VOKABULAR.md](EFFEKT_VOKABULAR.md) | rund 180 feste Kennungen für Techniken (Schnitt, Kamera, Look, Text, Figur, Ton, Dramaturgie) |
| [EFFEKTE.md](EFFEKTE.md) | wie oft jede Technik über alle Karten vorkommt |
| [KARTE_VORLAGE.md](KARTE_VORLAGE.md) | das Formular für neue Karten |
| [SKILL.md](SKILL.md) | Anleitung für eine KI, die mit der Bibliothek ein Video baut |

## Aufbau einer Karte
Kopfblock mit Kern (drei Merkmale, ohne die es nicht der Stil ist), Energie, Messung (Shot-Länge, Schnittdichte, Tempo, Lautheit, Helligkeit, Farbigkeit), Schnittmuster in Sechzehnteln, Palette mit Rollen, Effekt-Kennungen, Aufwand, Einsatz und Abnahme-Zielwerte. Darunter: Erkennung, Bildtypen mit Komposition, Dramaturgie, Schnittmuster als Bauplan, Rezept für einen Code-Motor (mit Filter-Parametern, Maßen, Timing, Formaten 9:16 und 16:9), Material (englische Prompts für Bilder und Musik), Regler, Abnahme, Fallen.

## So wurde sie gebaut
Jede Karte beruht auf der Messung eines öffentlich zugänglichen Vorschauvideos (Schnitterkennung, optischer Fluss je Shot, dominante Farben, Lautheit, Tempo) und auf dem Ansehen von Kontaktbögen mit einem Bild je Sekunde. Beschrieben ist nur der Look: Rhythmus, Bildbehandlung, Komposition, Typografie, Ton. Keine Motive, Figuren, Marken, Texte oder Bilder der Quellen; die Karten enthalten kein fremdes Material. Die Fallen sind teils vorhergesagt, teils erlebt: Erlebt sind die aus 26 selbst gebauten Stücken (alle 19 Familien) und 24 Prüfberichten; bei Karten, nach denen noch nicht gebaut wurde, sind sie aus der Messung vorhergesagt. Sie werden besser, sobald jemand nach der Karte baut.

## Werkzeuge
- `video_schauen.py`: macht ein Video ansehbar (Schnitte, Kontaktbögen, Kurven, Lautheit, Tempo).
- `kamera.py`: Kamerabewegung und Look je Shot (teilweise übernommen aus einem MIT-lizenzierten Projekt, Lizenzhinweis liegt bei).
- `bibliothek_index.py`: prüft die Karten (Pflichtfelder, Effekt-Kennungen, Gedankenstriche, verbotene Namen) und baut Index und Auszählung.

## Grenzen
- Das Tempo (BPM) wird aus der Tonspur geschätzt und kann halb oder doppelt sein; die Karten weisen darauf hin, wo es so ist.
- Weiche Übergänge (Blenden, Masken, Wischer) zählt die Schnitterkennung oft nicht mit; betroffene Karten nennen die Augen-Zählung.
- Eine Karte ersetzt keinen Code. Wiederholbar wird ein Stil erst mit den passenden Bausteinen im Motor; der Remotion-Starter im Paket (`starter/`) liefert sie.
