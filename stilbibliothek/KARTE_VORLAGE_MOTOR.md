---
id: <kurzname-mit-bindestrich, eigener deutscher Name, nie der Name eines Motors, Studios, einer Serie oder Marke>
name: <Anzeigename auf Deutsch>
familie: <strichzeichnung | malstil | erklaergrammatik | selbstzeichnend | andere Familie aus FAMILIEN.md>
kurz: <ein Satz: was man sieht und wie es wirkt>
kern: [<Merkmal 1>, <Merkmal 2>, <Merkmal 3>]   # ohne diese drei ist es nicht der Stil
energie: <1 ruhig bis 5 rasant>
format_quelle: "9:16"          # der Motor rendert jedes Format; die Sollwerte gelten formatfest
laenge_s: [<von>, <bis>]
bauweg: animskill               # ein Zeichen-Motor malt das Bild aus Code; kein Remotion-Bau, kein Handbau
animskill:
  motor: <huashu | anidoodle | zeichnen | handzeichnung | manim | pinsel | jsanim>
  stil: "<Kennung des Stils im Motor, genau wie der Motor sie erwartet>"
  quelle: "<Datei im Motor, relativ zu seinem Ordner, in der der Stil beschrieben ist>"
  schrift: [<Klasse für Titel>, <Klasse für Satz>]   # Klassen aus starter/src/wuerfel/schriftklassen.json; der Zug wählt die Schrift darin
lizenz: "<Kurzhinweis: Lizenz des Motors und was in LIZENZ.md oder den Abspann muss, verbotene Figuren oder Beispielbilder>"
sollwerte:                      # statt messung: keine Vorlage gemessen, Zielwerte für den eigenen Render
  shot_median_s: <Sekunden>
  schnitte_pro_s: <je Sekunde>
  ereignisse_pro_s: <Bildereignisse je Sekunde: neuer Strich, Form, Wort>
  lufs: -14
  helligkeit: <0..1, aus der Palette geschätzt>
  farbigkeit: <0..1, aus der Palette geschätzt>
palette:
  <rolle>: "<#HEX>"             # Rollen: grund, text, akzent, licht, dazu eigene (blau, gruen, nacht ...)
effekte: [<Kennungen aus EFFEKT_VOKABULAR.md; für Zeichen-Motoren oft strich-fuer-strich, formwandel, diagramm-wachstum>]
kamera: <ein Satz>
ton: <ein Satz: leises Code-Bett, Geräusche des Mediums, Stimme trägt, heller Schluss>
braucht: [nur-typo]             # der Motor zeichnet alles; nur, wenn echtes Material Kern ist: fotos-figur, footage-ort, produkt
motor_aufwand: <klein, wenn der Motor den Stil fertig kann | mittel bei Forschungsständen oder eigener Figur>
einsatz: [<trailer | hook | intro | uebergang | ganzes-kurzvideo | musikvideo | produkt | portrait>]
zweck: [<Wörter aus ZWECKE.md>]
branchen_passt: [<Wörter aus ZWECKE.md>]
branchen_nie: [<Wörter aus ZWECKE.md>]
abnahme:                        # realistische Spannen für abnahme.py; Helligkeit und Farbigkeit aus der Palette gerechnet
  shot_median_s: [<min>, <max>]
  schnitte_pro_s: [<min>, <max>]
  helligkeit: [<min>, <max>]
  farbigkeit: [<min>, <max>]
  lufs: [-15, -13]
# Würfel-Felder: wie in KARTE_VORLAGE.md (creator, creator_ohne oder creator_grund, spielraum, palettenrolle), gefüllt von
# werkzeuge/karten_wuerfelfelder.py; Familien-Standard der Zeichen-Familien: palette akzent (erklaergrammatik: nachbarn)
creator: <ja | eingeschraenkt | nein>
spielraum: {}
palettenrolle: {}
quelle: Eigene Beschreibung eines offenen Zeichen-Motors (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken des Motors übernommen.
---

# <Name>

<Ein bis zwei Sätze: was man sieht und woher die Energie kommt.>

## Kern
Die drei Merkmale aus `kern`, je ein Satz. Wer nur diese drei trifft, ist zu 80 % da.

## Erkennung
- **Bild:** <Medium und Machart in Worten, Farben mit Rollen>
- **Bewegung:** <wie das Bild entsteht oder lebt: Strich für Strich, Stufen, Verwandlung, Leitmotiv>
- **Ton:** <Bett, Geräusche des Mediums, Stimme>
- **Text:** <wie viel Text, wo, ob der Motor ihn zeichnet oder die Brücke ihn als Untertitel setzt>

## Bildtypen
| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|

## Regler
<was sich ändern darf, ohne dass der Stil kippt; was der Zug an Farbe tauscht>

## Fallen
- <aus der Quelle des Motors und aus eigenen Proben; je Falle die Lösung>

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems.

## Bauweg
Motor, Stil-Kennung, Quelle im Motor; die Befehle (`animskill.py --vorlage`, `animskill.py <bestellung.json>`) und ein kurzes Beispiel für `motor_spec`. Der Würfel (`wuerfeln.py zug`) schreibt bei diesen Karten `bauweg: animskill`, `animskill` und `motor_spec_entwurf` in `stil.json`.

## Abnahme
Sollwerte statt Messung, Prüfung mit `starter/werkzeuge/abnahme.py <video> <karte.md>`, dazu drei Standbilder gegen den Kern und die Prüfwerkzeuge des Motors, wenn er welche hat.

<!--
Was gegenüber KARTE_VORLAGE.md wegfällt: messung (es gibt keine gemessene Vorlage), schnittmuster_16tel und die Abschnitte
Dramaturgie, Schnittmuster, Rezept und Material (die macht der Motor). Neu: bauweg, animskill, lizenz, sollwerte und die
Abschnitte Ton und Bauweg. bibliothek_index.py prüft beides: Pflichtfelder und Abschnitte je nach bauweg.
Erste Karten dieser Form (06.11.2026) erzeugt aus den Stil-Dateien der Motoren und stichprobenartig von Hand gelesen.
-->
