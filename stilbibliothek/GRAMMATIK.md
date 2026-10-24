# Grammatik: wie ein Kurzvideo erzählt

Die Karten sagen, wie ein Stil aussieht und schneidet. Diese Datei sagt, wie die Geschichte darin läuft. Ein Stück besteht aus vier Entscheidungen: **eine Erzählform** (unten, acht Kurzformate), **ein Stil** (eine Karte), **ein Thema** (etwas Wahres, mit Quelle in `haus/fakten.md`) und **ein Takt** (Musik, Stimme oder gleich lange Stationen). Erst die Form wählen, dann die Karte: Die Form entscheidet, ob ein Stück schneidet, verwandelt oder stehen bleibt.

## Die acht Kurzformate

| # | Form | Was die Handlung antreibt | Wie es von Bild zu Bild geht | Woran man sie erkennt | Passt zu |
|---:|---|---|---|---|---|
| 1 | **Chronologie mit Verwandlung** | echte Zeitfolge, oft mit sichtbarem Zähler (Jahr, Uhrzeit, Stufe) | Formverwandlung: ein Gegenstand der alten Welt wird zum Gegenstück der neuen (Baustein `Bruecke`, sobald er da ist; sonst Maske oder Blende) | kaum harte Schnitte, ein Zähler, am Ende ein Rückgriff auf das erste Bild | Geschichte eines Produkts, eines Handwerks, einer Idee |
| 2 | **Auftrag mit Beat-Schnitten** | jemand will etwas und schafft es Schritt für Schritt, ein Helfer löst je Schritt ein Problem | harte Schnitte auf dem Raster, Wechsel weit und nah, ein wiederkehrender Gegenstand misst die Zeit | kurzer Vorgriff auf das Ziel am Anfang, eine Eilstrecke von vier kurzen Schnitten, Stille vor der Frist, Treffer auf dem Ziel | Kundenfall, Lieferung, „so lösen wir das“ |
| 3 | **Fester Held** | ein Held reist durch Welten oder Zeit | harte Schnitte, der Held bleibt in der schnellsten Strecke genau an seinem Platz, die Welt wechselt um ihn | Schnitte werden schneller (Schlag, Achtel, Sechzehntel), der Held steht still im Bild | ein Paket, eine Nachricht, ein Gericht auf dem Weg zum Kunden |
| 4 | **Katalog** | eine Frage geht hinaus, die Antwort ist eine Liste, ein Punkt je Schlag | harte Schnitte, je Punkt eine Karte in eigener Farbe, am Ende alles in einem Bild versammelt | die Karten werden schneller, ein Sammelbild von mindestens 1,5 s | „fünf Gründe“, Sortiment, Leistungen |
| 5 | **Gegenüberstellung** | zwei Seiten (vorher und nachher, kalt und warm, wir und die anderen) | geteilte Bühne oder Wechsel im Schlag, dieselbe Bildposition auf beiden Seiten | dieselbe Einstellung zweimal, nur eine Sache ändert sich | Vergleich, Mythos und Wahrheit |
| 6 | **Frage und Antwort** | eine Frage im ersten Bild, die Antwort im letzten Drittel | Aufbau in ruhigen Bühnen, Stille vor der Antwort, die Antwort als lautester Moment | die Frage steht als Satz im Bild, die Antwort als Bild und Wort | Erklärstück, Wissensfrage |
| 7 | **Vorher und nachher** | ein Ergebnis, dann zurück zum leeren Anfang, dann die echten Schritte | eine feste Einstellung, Schichten kommen dazu, ein einziger Übergang ins Leere | das letzte Bild gleicht dem ersten bis aufs Pixel, frühe Schritte schnell, späte langsam | Handwerk, Renovierung, Gericht, Software von leer bis fertig |
| 8 | **Ablauf** | ein Gegenstand wandert durch Stationen, jede Station tut genau eine Sache mit ihm | eine große Zeichnung, eine weiche Fahrt von Station zu Station, am Ende eine Rückfahrt aufs Ganze | keine Schnitte, Stationen gleich lang oder nach der Stimme, die Rückfahrt zeigt ein Muster | Prozess, Bestellweg, Produktion |

**Wie die Spalten zusammenhängen:** Wege (Stationen, eine Maschine) bekommen eine Fahrt über eine Zeichnung und keinen Schnitt. Zeit, die vergeht, wird verwandelt, nicht geschnitten. Figuren und Listen schneiden hart auf dem Raster. Eine Stimme übernimmt den Takt: Das Bild wechselt am Satzende, nicht auf dem Schlag.

**Erprobt:** Form 6 trägt das Beispiel `akku-winter` im Starter, Form 1 hat in einem Vergleichsbau ein Stück getragen, das alle Messungen bestand. Die übrigen Formen sind aus Messungen fremder Stücke beschrieben und hier noch nicht gebaut. Wer eine davon wählt, sagt es dem Menschen.

## Die vier Regeln (gelten in jeder Form)
1. **Eine Konstante.** Etwas bleibt, während sich alles andere ändert: ein Held, eine Bühne, eine Seite, ein Gegenstand. Das Auge braucht einen Halt.
2. **Eine Farbe, eine Bedeutung.** Eine reservierte Farbe für das, dem die Geschichte folgt (der Held, die Energie, das Geld), und nie für Schmuck. Zwei Bedeutungen in einer Farbe verwirren.
3. **Stille vor der Pointe, Lautestes auf der Pointe.** 0,5 bis 4 s fast Stille auf einem stehenden Bild, dann der eine lauteste Treffer auf der Wendung. Das dichteste Stück ist nicht das lauteste: Die größte Dichte kommt kurz vor der Stille.
4. **Das Ende ist der Anfang, verändert.** Zurück zum ersten Bild, mit dem Unterschied, den die Geschichte gemacht hat. Daraus entsteht von selbst eine Schleife.

Dazu ein Satz, der das Stück trägt und sich sagen lässt („der Akku friert ein und wacht im Warmen wieder auf“). Wer den Satz nicht sagen kann, hat noch keine Geschichte.

## Treffer in die Sprechpause
Mit einer Stimme ist die Stimme die Uhr. Jeder neue Beat beginnt rund 0,3 s nach dem Satzende. **Der Treffer der Pointe gehört in die Pause vor dem Satz, der sie nennt, nie unter Sprache:** Unter der Stimme wird die Musik abgesenkt und der Treffer verschluckt. Sprechtempo höchstens 3,5 Wörter je Sekunde; wo das Bild Zeit zum Ankommen braucht (eine Zahl, ein Etikett, die Stille vor der Pointe), bekommt die Zeile eine längere Pause. Die Vorprüfung misst beides: `--woerter <wortzeiten.json> --treffer <sekunde>`.

## Die Bild-Checkliste (jedes Schlüsselbild, jeder Stil)
Wer baut, hakt sie am Storyboard ab, bevor der Prüfer es sieht.
1. **Die Konstante ist im Bild** und an ihrem Platz.
2. **Die reservierte Farbe** steht nur auf dem, wofür sie reserviert ist.
3. **Das Medium zeigt sich am Handy:** Papierkante, Raster, Korn, Strich, Pixel. Ein Bild, das jeder Stil sein könnte, ist Clipart.
4. **Die Idee ist gespielt, nicht beschriftet:** „Kälte bremst“ heißt Eis an den Rändern und langsame Teilchen, nicht das Wort „Kälte“ auf einem Verlauf.
5. **Etwas passiert:** jedes Bild ist ein Moment einer Bewegung. Auch stehende Bilder haben kleines Leben (ein Blinzeln, Dampf, ein blinkendes Licht, fallender Schnee). Etwas Neues alle 2 bis 4 s: eine Bewegung, eine Enthüllung, ein Schnitt, eine Reaktion.
6. **Schrift gehört zur Welt** (auf einem Schild, einer Platte, einem Etikett) oder ist gesetzt wie die Schrift der Karte. Höchstens eine kurze Zeile je Beat, mindestens 50 px bei 1080 Breite, Wichtiges mindestens 100 px.
7. **Die Größe wechselt:** weit, halbnah und mindestens eine extreme Nahaufnahme im Stück. Lauter gleiche Einstellungen sind eine Diashow.
8. **Ein Faden zieht sich durch:** ein Gegenstand, eine Farbe, eine Form, die verändert wiederkommt.
9. **Handy-Maßstab:** in 9:16 alles Wichtige zwischen x 60 und 940 und y 250 bis 1500 (oben und unten liegt die Oberfläche der Plattform); unten 15 % frei.

**Standardlösungen, die nach Massenware aussehen:** ein zentrierter Titel auf einem Farbverlauf; alles blendet ein; Beschriftungen oder Rahmen in den Ecken; Glühen auf Bedienelementen; Partikelwolken ohne Anlass; ein Logo als einziges Ende.

## Der Look-Check (vor dem Storyboard)
Zwei bis vier der verschiedensten Beats als Standbild in Endgröße, nebeneinander gezeigt, bevor das ganze Storyboard entsteht. Je Bild fragt man: Ja oder Nein, und warum. So kostet ein falscher Look ein paar Minuten statt eines ganzen Storyboards. Der Code dieser Standbilder wird der Code des Videos; nichts wird später neu gezeichnet. Ablauf und Befehl: [ABLAUF.md](../ABLAUF.md) Schritt 3a.
