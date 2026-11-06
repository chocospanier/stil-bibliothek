# Stil-Bibliothek: Index

289 Stil-Karten in 24 Familien. Maschinenlesbar: `index.json`.

So liest man die Felder: `braucht` heißt „eins davon reicht“; ob das eigene Material trägt, entscheidet der Kern der Karte (Beispiel: ein Kern ohne Fotos lässt sich mit Illustrationen oder nur Typo bauen). `abnahme` gilt im Format der Quelle (`format_quelle`). Formatfest sind Schnitte je Sekunde, Shot-Median und LUFS; Helligkeit und Farbigkeit dürfen im Hochformat um 0,03 höher liegen, außer die Karte hat einen eigenen Block `abnahme_9x16`. Gemessen wird mit `starter/werkzeuge/abnahme.py`.

Lautheit: −14 LUFS ist der Standard. Nennt die Karte einen Bereich, gilt die Karte, solange er innerhalb −14 ± 1 bleibt (Ziel dann im gemeinsamen Teil, etwa −13,5). ⚠ LUFS hinter einer Karte heißt: Ihr Bereich liegt ganz außerhalb von −14 ± 1; die Messwerte der Vorlage bleiben stehen, gebaut wird trotzdem mit −14 ± 1, und dieser eine Wert fällt in der Abnahme durch.

Filtern: `python -I werkzeuge/bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook` gibt die passenden Karten als Tabelle aus. Nur mit Code baubar (braucht nur `nur-typo` oder `illustrationen`): `--filter nur_code=ja` oder `--filter braucht<=nur-typo,illustrationen`.

✎ hinter einer Karte heißt: Ein Zeichen-Motor malt den Stil aus Code (`bauweg: animskill`, Motor-Kennung dahinter, Vorlage `KARTE_VORLAGE_MOTOR.md`); die Karte hat Sollwerte statt einer Messung. Nur diese Karten: `--filter bauweg=animskill`, je Motor `--filter zeichen_motor=huashu`.

## selbstzeichnend (77)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Bilderbuch in Bewegung](karten/bilderbuch-in-bewegung.md) ✎ `zeichnen` | Eine kleine Figur im Bilderbuchstil bewegt sich wirklich, staucht und streckt sich beim Hüpfen. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bonbon-3D](karten/bonbon-3d.md) ✎ `zeichnen` | Bonbonfarbene Kugeln in weichem Licht, eine prall aufgeblasene Schrift, der Hintergrund verschwimmt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Chromsonne](karten/chromsonne.md) ✎ `zeichnen` | Eine gestreifte Sonne sinkt hinter ein Neongitter, Chromschrift glänzt, das Bild rauscht wie Videoband. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Comic der Goldzeit](karten/comic-der-goldzeit.md) ✎ `zeichnen` | Ein Comic der Vierziger: Pinseltusche, Rasterpunkte, verrutschte Farben auf vergilbtem Papier. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Diagonalplakat](karten/diagonalplakat.md) ✎ `zeichnen` | Ein Plakat der Zwanziger: Rot und Schwarz, Schrägbalken, Keile, große Schrift und ein Rasterfoto. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Handschuhfigur 1930](karten/handschuhfigur.md) ✎ `zeichnen` | Eine Trickfigur mit weißen Handschuhen am Morgen, schwarzweiß wie auf altem Film. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Heimvideo](karten/heimvideo.md) ✎ `zeichnen` | Ein Geburtstag wie auf altem Heimvideo, warmes Licht, Farben bluten, oben eine Aufnahmeanzeige. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kartenwand](karten/kartenwand.md) ✎ `zeichnen` | Auf einer Punktrasterwand fallen Karten mit Rückfedern ein, Linien verbinden sie, Häkchen setzen sich. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Marktzettel](karten/marktzettel.md) ✎ `zeichnen` | Ein Wochenmarkt als Stickercollage: Bon, gestanzte Sticker mit weißem Rand, Klebeband, Anhänger und Stempel. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Notiz-App](karten/notiz-app.md) ✎ `zeichnen` | Eine erfundene dunkle Notiz-App: eine Seite schreibt sich, ein Diagramm tippt sich Zeile für Zeile. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Pastelloberfläche](karten/pastelloberflaeche.md) ✎ `zeichnen` | Eine erfundene App wird in Pastell vorgestellt: Karten springen auf, Häkchen setzen sich, eine Lupe fliegt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Regennacht Neon](karten/regennacht-neon.md) ✎ `zeichnen` | Eine Straße bei Nacht im Regen: Neonröhren, schwebende Werbung, alles spiegelt sich im nassen Asphalt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Rotstiftkorrektur](karten/rotstiftkorrektur.md) ✎ `zeichnen` | Eine Klassenarbeit wird rot korrigiert: Haken, Kringel, Wellenlinie, Randnotiz und ein Stempel. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schablonen-Spray](karten/schablonen-spray.md) ✎ `zeichnen` | Ein Motiv wird Schablone für Schablone auf Beton gesprüht, mit Sprühnebel und Laufnasen. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Siebdruck-Pop](karten/siebdruck-pop.md) ✎ `zeichnen` | Dasselbe Motiv vier- oder neunmal in grellen Farbfeldern, die schwarze Platte leicht versetzt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Wandernde Kontur](karten/wandernde-kontur.md) ✎ `zeichnen` | Eine Kontur verwandelt sich Form für Form, Nachbilder zeigen den Weg, ideal für Kreisläufe und Abläufe. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zeitungscollage](karten/zeitungscollage.md) ✎ `zeichnen` | Eine Collage aus Packpapier und alter Zeitung, Rasterfotos, Buchstaben zusammengeklebt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zitterlinien-Cartoon](karten/zitterlinien-cartoon.md) ✎ `zeichnen` | Ein Cartoon mit kochender Linie: unter der Pinsellinie die Blaustiftskizze, Farben leicht versetzt, alles zittert lebendig. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Aufnäher](karten/aufnaeher.md) ✎ `zeichnen` | Ein gestickter Aufnäher auf Jeans, Füllstich, Plattstich, dicker Rand. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Blaues Bilderbuch](karten/blaues-bilderbuch.md) ✎ `zeichnen` | Eine Bilderbuchseite in Blau mit Tuschelinie, Korallrot und weißer Kreide, die Buchmitte ist zu sehen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bleisatzplakat](karten/bleisatzplakat.md) ✎ `zeichnen` | Ein Plakat aus Holzlettern in Rot und Schwarz, leicht versetzt gedruckt, mit einem Holzschnitt. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bügelperlen](karten/buegelperlen.md) ✎ `zeichnen` | Ein Motiv aus Bügelperlen, Perle für Perle gesteckt, dann gebügelt, bis die Röhrchen verschmelzen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Dämmerungsminiatur](karten/daemmerungsminiatur.md) ✎ `zeichnen` | Der Tag kippt in die Nacht über Flickenhügeln, eine kleine Figur trägt ein Glas voller Glühwürmchen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Durchleuchtung](karten/durchleuchtung.md) ✎ `zeichnen` | Ein Koffer im Durchleuchter, Konturen leuchten, Materialien in Falschfarben. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Farbenstädtchen](karten/farbenstaedtchen.md) ✎ `zeichnen` | Ein buntes Städtchen an Treppen, Wimpel spannen sich, der nasse Platz spiegelt alles. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Feder und Lavis](karten/feder-und-lavis.md) ✎ `zeichnen` | Kleine Karten mit Fineliner-Figuren, die Farbe verrutscht lässig über die Linie. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Flache Ebenen](karten/flache-ebenen.md) ✎ `zeichnen` | Ein Nachtlager aus flachen Farbflächen, sieben Farben, kleine Schatten zwischen den Ebenen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Grünschirm](karten/gruenschirm.md) ✎ `zeichnen` | Ein alter Röhrenschirm zeigt grüne Zeichengrafik, Zeilen flimmern, Licht leuchtet nach. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Heftrandkritzel](karten/heftrandkritzel.md) ✎ `zeichnen` | Ein Brettspiel als Kulizeichnung im Heft, blaue und rote Linien, Kleckse und Randkritzel. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Herbstaquarell](karten/herbstaquarell.md) ✎ `zeichnen` | Ein Herbstsee in Aquarell: Bäume werden lasiert, das Wasser spiegelt, Trockenränder und Spritzer bleiben stehen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Ideen-Illustration](karten/ideen-illustration.md) ✎ `zeichnen` | Eine Idee als Zeitschriftenillustration: Handlinie, zwei Druckfarben, ein Begriff wird zu einem einfachen Bild. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kinderkreide](karten/kinderkreide.md) ✎ `zeichnen` | Ein Picknick, wie ein Kind es malt: Wachsmalstift, krumme Formen, kräftige Farben. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Knetfigur](karten/knetfigur.md) ✎ `zeichnen` | Eine Szene aus Knete: Fingerspuren im Himmel, gerollte Wellen, ein Leuchtturm unter Studiolicht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kreidelektion](karten/kreidelektion.md) ✎ `zeichnen` | Eine Tafel erklärt eine Frage: Titel, Skizze mit Pfeilen, farbige Kreide, darunter die Reste der letzten Stunde. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Laborheft](karten/laborheft.md) ✎ `zeichnen` | Ein Versuch im Karoheft: Bleistifttabellen, eine Kurve, Textmarker, ein roter Kreis und eine Haftnotiz mit dem Ergebnis. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Linolschnitt](karten/linolschnitt.md) ✎ `zeichnen` | Ein verschneites Dorf als Linolschnitt, mit Messerspuren, Fehlstellen und versetzter Farbe. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Milchglas](karten/milchglas.md) ✎ `zeichnen` | Weiche Farbverläufe leuchten hinter Milchglaskarten, eine ruhige, moderne Oberfläche. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Miniaturinsel](karten/miniaturinsel.md) ✎ `zeichnen` | Eine Insel als isometrisches Modell, drei Seiten im Licht einer Sonne, kleine Datenkarten schweben darüber. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Morgenrot-Holzschnitt](karten/morgenrot-holzschnitt.md) ✎ `zeichnen` | Ein Berg im Morgenrot als Farbholzschnitt, der Himmel gewischt, Wellen als Muster, die Maserung sichtbar. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Papierstadt](karten/papierstadt.md) ✎ `zeichnen` | Eine fröhliche Stadt aus farbigem Papier legt sich Teil für Teil, Ballons, Sonne und Wolken schweben. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Pastoses Sternfeld](karten/pastoses-sternfeld.md) ✎ `zeichnen` | Ein Sternenhimmel über einem Feld in dicker Ölfarbe, die Striche folgen dem Wind, das Relief glänzt im Seitenlicht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Polygon 1999](karten/polygon-neunundneunzig.md) ✎ `zeichnen` | Eine Schlucht wie in einem Spiel von 1999: grobe Polygone, verzerrte Texturen, Nebel und Dither. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Radiofront der Sechziger](karten/radiofront.md) ✎ `zeichnen` | Die Front eines Radios der Sechziger baut sich auf, Teak, Aluminium, Skala leuchtet, Knöpfe drehen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Regenpixel](karten/regenpixel.md) ✎ `zeichnen` | Ein Café im Regen als Pixelbild: Neon spiegelt sich in Pfützen, Bayer-Raster in den Verläufen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Retro-Gouache](karten/retro-gouache.md) ✎ `zeichnen` | Eine Figur im Regen in Retro-Gouache, wenige Tonstufen, Strickmuster und trockene Glanzlichter. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schattenbühne](karten/schattenbuehne.md) ✎ `zeichnen` | Schattenfiguren aus gefärbtem Leder spielen vor einem leuchtenden Tuch, lösen sie sich, wird der Schatten doppelt. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schraffurnacht](karten/schraffurnacht.md) ✎ `zeichnen` | Eine Nacht aus schrägen Strichen, ein Vulkan glüht, Lava spiegelt sich im Meer. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Siebdruck-Geometrie](karten/siebdruck-geometrie.md) ✎ `zeichnen` | Ein Plakat aus Kreis, Quadrat und Dreieck in Grundfarben, gedruckt im Sieb mit leichtem Versatz. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Sommerhimmel](karten/sommerhimmel.md) ✎ `zeichnen` | Ein Sommertag wie im Anime: riesige Quellwolken, eine Landstraße mit Strommasten, eine kleine Figur von hinten. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Stilles Gruselchen](karten/stilles-gruselchen.md) ✎ `zeichnen` | Eine Figur mit Porzellangesicht hält ein kleines Gespenst im Glas, auf dunklem Brett, Strick und Karo. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Stromlinie](karten/stromlinie.md) ✎ `zeichnen` | Ein Zug rast auf einem Plakat der Dreißiger, Strahlenfächer, Stufenhochhäuser, goldene Schrift. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Tintenpapier](karten/tintenpapier.md) ✎ `zeichnen` | Auf warmem Papier steigen Karten auf, ein Ablauf zeichnet sich Linie für Linie, ein orangefarbener Rahmen setzt den Fokus. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Transparentlagen](karten/transparentlagen.md) ✎ `zeichnen` | Ein Stadtplan entsteht auf dem Leuchttisch: Grundzeichnung, darüber Folie für Folie in einer Farbe. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Trockenpinsel-Flächen](karten/trockenpinsel-flaechen.md) ✎ `zeichnen` | Ein Mann an einer Nudeltheke aus wenigen Farbblöcken, mit der Rolle aufgetragen, ein rotes Quadrat signiert. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Wärmebild](karten/waermebild.md) ✎ `zeichnen` | Eine Küche als Wärmebild: heiß leuchtet gelb, kalt liegt violett. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Warmes Buntstiftbuch](karten/warmes-buntstiftbuch.md) ✎ `zeichnen` | Eine Schildkröte mit einem Garten auf dem Rücken quert einen Bach, in warmen Buntstiftschichten. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zeichendrucker](karten/zeichendrucker.md) ✎ `zeichnen` | Ein Bild aus Buchstaben und Zeichen, Zeile für Zeile auf grün gestreiftes Endlospapier gedruckt. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bleiglasfenster](karten/bleiglasfenster.md) ✎ `zeichnen` | Ein Spitzbogenfenster aus farbigem Glas leuchtet im Gegenlicht, Bleiruten zeichnen die Formen. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bleistiftstudie](karten/bleistiftstudie.md) ✎ `zeichnen` | Ein Fahrrad als Bleistiftstudie, schraffiert, gewischt, die Ränder bleiben bloße Linie. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Delfter Fliese](karten/delfter-fliese.md) ✎ `zeichnen` | Eine Grachtenszene in Kobaltblau auf weißer Fliese, von Hand gemalt. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Ein Strich](karten/ein-strich.md) ✎ `zeichnen` | Ein Bild in einer einzigen Linie, ohne einmal abzusetzen, auf dunklem Grund mit einer Akzentfarbe. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Ein-Bit-Malprogramm](karten/einbit-malprogramm.md) ✎ `zeichnen` | Ein Garten in Schwarzweiß wie aus einem frühen Malprogramm, Flächen mit Mustern gefüllt. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Erfinderskizze](karten/erfinderskizze.md) ✎ `zeichnen` | Eine Maschine zerlegt sich im Notizbuch eines Erfinders: braune Tinte, Rötel, Spiegelschrift am Rand. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Fackelhöhle](karten/fackelhoehle.md) ✎ `zeichnen` | Eine Jagdszene in Ocker auf Höhlenfels, gesprühte Handabdrücke, Fackellicht. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Felsritzung](karten/felsritzung.md) ✎ `zeichnen` | Tiere und Menschen werden in dunklen Wüstenfels gepickt, alte Spuren verblassen neben frischen. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Grabwand in Registern](karten/grabwand-register.md) ✎ `zeichnen` | Eine ägyptische Grabwand füllt sich Streifen für Streifen über rotem Vorzeichnungsraster. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kieselmosaik](karten/kieselmosaik.md) ✎ `zeichnen` | Ein Hafen als Mosaik, Reihe um Reihe entlang der Konturen gesetzt, mit Inschrifttafel. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kreuzstich](karten/kreuzstich.md) ✎ `zeichnen` | Ein Stickbild im Kreuzstich wächst Kreuz für Kreuz auf Aida-Stoff, mit Rückstich-Konturen und Knoten. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Pastellvignette](karten/pastellvignette.md) ✎ `zeichnen` | Ein Porträt mit Katze in Pastellkreide, Haut verwischt, Haar in Strähnen, viel Papier ringsum. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Pausblau-Werkplan](karten/pausblau-werkplan.md) ✎ `zeichnen` | Ein technischer Plan in Weiß auf Blau, mit Maßen und Schnitten. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Profilschatten](karten/profilschatten.md) ✎ `zeichnen` | Ein Mensch im Profil als Scherenschnitt aus schwarzem Papier, Goldstaub, ein ovaler Rahmen. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Sonnendruck](karten/sonnendruck.md) ✎ `zeichnen` | Pflanzen erscheinen als weiße Schatten auf preußischblauem Sonnendruck, daneben feine Handnotizen. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Tuschlandschaft](karten/tuschlandschaft.md) ✎ `zeichnen` | Eine weite Tuschlandschaft malt sich in Lagen, der Mond bleibt ausgespart, ein Boot treibt im Leerraum. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Vasenfries](karten/vasenfries.md) ✎ `zeichnen` | Ein Wettkampf als abgerollter Vasenfries, schwarze Figuren auf Tongrund. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Wassergarten](karten/wassergarten.md) ✎ `zeichnen` | Ein südchinesischer Garten im Frühling, weiße Mauern, Mondtor, Weiden und Wasser, zuletzt ein Siegel. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zarter Buntstift](karten/zarter-buntstift.md) ✎ `zeichnen` | Ein Stillleben in zartem Buntstift, weich schraffiert, pastellig, mit kleinen Glanzlichtern. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zierinitiale](karten/zierinitiale.md) ✎ `zeichnen` | Eine Buchseite des Mittelalters: Goldinitiale, gotische Schrift, rote Überschriften auf Pergament. | 1 | klein | ganzes-kurzvideo, intro, uebergang |

## malstil (54)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Achtbit-Spielwelt](karten/achtbit-spielwelt.md) ✎ `huashu` | Eine Achtbit-Spielwelt: grobe Pixel, vierzehn Farben, ein Herz blinkt in der Anzeige, ein Block wirft eine Münze. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kosmischer Comic](karten/kosmos-comic.md) ✎ `huashu` | Superheldencomic der Sechziger: Vierfarbraster, verrutschter Druck, knisternde Energiepunkte, Lautmalerei in Riesenbuchstaben. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Neonwelle](karten/neonwelle.md) ✎ `huashu` | Neonwelle der Zehnerjahre: ein Gitter rollt in die Tiefe, eine gestreifte Sonne steigt, Schilder flackern, Bandrauschen läuft durch. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Nudelarm-Revue](karten/nudelarm-revue.md) ✎ `huashu` | Zeichentrick um 1930: Figuren mit Nudelarmen und weißen Handschuhen wippen im Takt, der alte Film flackert und kratzt. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Rasterpunkt-Pop](karten/rasterpunkt-pop.md) ✎ `huashu` | Pop-Art der Sechziger: Rasterpunkte, dicke Konturen, ein Bild viermal in wechselnden Farben, Denkpunkte blinken. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Roter Keil](karten/roter-keil.md) ✎ `huashu` | Konstruktivismus der Zwanziger nach Art von Lissitzky: ein roter Keil schlägt in den Kreis, Rasterfotos, Parolen stempeln sich Wort für Wort. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Tanzende Strichfiguren](karten/tanzende-strichfiguren.md) ✎ `huashu` | Straßenkunst der Achtziger: dicke Linien, Strahlen um tanzende Figuren, alles hüpft im Takt. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Aquarell-Figur](karten/aquarell-figur.md) ✎ `pinsel` | Eine eigene gezeichnete Figur spielt eine kleine Szene in Pinselstrichen und Aquarell, die Linie kocht leicht, jede Szene hat einen Übergang. | 3 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Barockwolke](karten/barockwolke.md) ✎ `huashu` | Barocke Deckenmalerei nach Art von Pietro da Cortona: Figurengruppen fließen über Wolken in einen goldenen Himmel. | 3 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Facettenbruch](karten/facettenbruch.md) ✎ `huashu` | Analytischer Kubismus um 1912: der Raum zerfällt in halbtransparente Facetten, Buchstaben springen, Zeitungspapier zittert. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Farbige Scherenschnitte](karten/farbige-scherenschnitte.md) ✎ `huashu` | Späte Scherenschnitte nach Art von Matisse: satte Papierformen mit unruhiger Scherenkante treiben wie Algen über Blau. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Flachgrafik von heute](karten/flachgrafik-heute.md) ✎ `huashu` | Heutige Flachillustration: Farbflächen ohne Kontur, körnige Schatten, eine Figur spielt mit Nachschwingen, am Ende eine Pointe. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Frühe Rechenbilder](karten/fruehe-rechenbilder.md) ✎ `huashu` | Rechenbilder der frühen Neunziger: glänzender Kunststoff, Chromkugel, Schachbrettboden, erst Drahtgitter, dann Zeile für Zeile berechnet. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Glubschaugen-Trick](karten/glubschaugen-trick.md) ✎ `huashu` | Zeichentrick für Erwachsene der Zehnerjahre: dünne runde Konturen, Glubschaugen, flache Farben, fleckige Kulissen. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Grundformen-Plakat](karten/grundformen-plakat.md) ✎ `huashu` | Ein Plakat der Bauhaus-Zeit: Kreis, Quadrat und Dreieck in Grundfarben, eine Gliederpuppe, Rasterfelder wechseln die Farbe. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Papierschnitt-Trick](karten/papierschnitt-trick.md) ✎ `huashu` | Zeichentrick für Erwachsene der Neunziger: Figuren aus wenigen ausgeschnittenen Teilen, steife Bewegung, Münder klappen. | 3 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Punkte ohne Ende](karten/punkte-ohne-ende.md) ✎ `huashu` | Unendliche Punkte: handgezogene Kreise wachsen ringweise aus der Mitte, ein Spiegelraum vervielfacht sie. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schattenspiel aus Leder](karten/schattenspiel-leder.md) ✎ `huashu` | Chinesisches Schattentheater: durchbrochene Lederfiguren an Stäben, steife Gelenke, die Öllampe glimmt hinter dem Schirm. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Trockenputz-Fresko](karten/trockenputz-fresko.md) ✎ `huashu` | Grottenmalerei der Nördlichen Dynastien: Mineralfarben auf trockenem Lehm, schnelle Linien fliegen quer durch das Bild. | 3 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Weiche Rundkörper](karten/weiche-rundkoerper.md) ✎ `huashu` | Familienfilm aus dem Computer: weiche runde Körper, Glanz auf Kunststoff und Stoff, Figuren spielen mit dem ganzen Körper. | 3 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Wirbelstrich](karten/wirbelstrich.md) ✎ `huashu` | Nach Art von van Gogh: Pinselstriche folgen einem Strömungsfeld, Sternwirbel drehen sich, Lichthöfe dehnen sich, Flammen flackern. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Wogender Schrei](karten/wogender-schrei.md) ✎ `huashu` | Expressionismus nach Art von Munch: lange geschwungene Striche, die ganze Welt wellt sich, ein blutroter Himmel fließt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Blattgold-Handschrift](karten/blattgold-handschrift.md) ✎ `huashu` | Eine gotische Buchseite: Blattgold glänzt schräg auf, Ranken schwingen, eine Schnecke kriecht am Rand. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Farbpunkt-Mosaik](karten/farbpunkt-mosaik.md) ✎ `huashu` | Pointillismus nach Art von Seurat: reine Farbpunkte mischen sich erst im Auge, das Bild kristallisiert aus Punkten. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Freskenblöcke](karten/freskenbloecke.md) ✎ `huashu` | Frühe Freskomalerei nach Art von Giotto: schwere Gestalten als Blöcke, klare Gruppen erzählen, der Himmel ist eine blaue Fläche. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Goldornament](karten/goldornament.md) ✎ `huashu` | Goldene Periode nach Art von Klimt um 1907: Spiralen und Augenmuster im Blattgold, ein echtes Gesicht im flachen Goldmantel. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Grabkammerfresko](karten/grabkammer-fresko.md) ✎ `huashu` | Altägyptische Grabmalerei: Figuren im Profil mit frontalem Auge, flache Farben, Hieroglyphen schreiben sich Strich für Strich. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Grottenfresko](karten/grottenfresko.md) ✎ `huashu` | Höhlenmalerei der Tang-Zeit aus den Mogao-Grotten: Mineralfarben auf Erdrot, fliegende Himmelswesen mit Bändern, Blüten fallen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Harte Lichtkante](karten/harte-lichtkante.md) ✎ `huashu` | Amerikanischer Realismus der Vierziger: harte Sonnenflächen wandern über Wand und Gesicht, ein Schatten trinkt mit. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Höhlenwand](karten/hoehlenwand-ocker.md) ✎ `huashu` | Tiere laufen in zwei Posen über eine fackelbeleuchtete Felswand aus Ocker und Holzkohle, die Glut flackert. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Jugendstilplakat](karten/jugendstil-plakat.md) ✎ `huashu` | Ein Jugendstilplakat nach Art von Mucha: schwellende Linien, ein Kreis hinter dem Kopf dreht sich, Blumen und Locken schwingen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kerzendunkel](karten/kerzendunkel.md) ✎ `huashu` | Helldunkel nach Art von Rembrandt: Kerze und Fenster schneiden Gesichter aus dem Dunkel, Staub tanzt im Lichtkegel. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Körper unter Spannung](karten/koerper-unter-spannung.md) ✎ `huashu` | Nach Art von Michelangelo: Körper wie aus Marmor gehauen, in gedrehter Spannung, große Gesten. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Lagunenluft](karten/lagunenluft.md) ✎ `huashu` | Venezianische Vedute nach Art von Guardi: die Luft flirrt, Licht bricht sich, Fassaden und Gondeln lösen sich an den Rändern. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Lesbare Stadt](karten/lesbare-stadt.md) ✎ `huashu` | Gotische Stadtmalerei nach Art von Ambrogio Lorenzetti: eine ganze Stadt mit vielen kleinen Szenen, die man nacheinander liest. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Lichtflecken](karten/lichtflecken-garten.md) ✎ `huashu` | Impressionismus um 1874 nach Art von Monet: kurze Pastellstriche, Lichtflecken wandern, Mohn wiegt sich, Wolken ziehen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Lichtstrahl-Himmel](karten/lichtstrahl-himmel.md) ✎ `huashu` | Japanischer Anime-Hintergrund der Zehnerjahre: Quellwolken, Strahlen durch Dunst, Lichtteilchen schweben, ein Lichtstreif zieht schräg durch. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Persische Buchmalerei](karten/persische-buchmalerei.md) ✎ `huashu` | Persische Buchmalerei: Räume stapeln sich übereinander statt in die Tiefe, feine Figuren erzählen, Lapisblau und Gold. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Schwarzfigurige Vase](karten/schwarzfigur-vase.md) ✎ `huashu` | Attische Vasenmalerei: schwarze Silhouetten auf Terrakotta, Ritzlinien, ein Mäanderband läuft gegen die Richtung. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schwebendes Dorf](karten/schwebendes-dorf.md) ✎ `huashu` | Dorf-Traumbilder des frühen zwanzigsten Jahrhunderts: Erinnerung als Raum, Liebende schweben über Dächern, Farben aus dem Gefühl. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Seerosenteich](karten/seerosenteich.md) ✎ `huashu` | Nach Art von Monets Seerosen um 1899: Striche spiegeln sich, Seerosen treiben, Weidenschatten wiegen, Ringe breiten sich aus. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Sfumato](karten/sfumato.md) ✎ `huashu` | Hochrenaissance nach Art von Leonardo: weiche Übergänge ohne Kontur, Craquelé und Firnisgelb, Licht fällt durchs Fenster. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Sommerwind-Aquarell](karten/sommerwind-aquarell.md) ✎ `huashu` | Japanischer Zeichentrickfilm mit Aquarellhintergrund: Vorhänge blähen sich, Gras wogt in Feldern, Laub wirft Lichtflecken. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Steinmosaik](karten/steinmosaik.md) ✎ `huashu` | Ein römisches Fußbodenmosaik: Steinchen folgen der Kontur, eine Wellenbordüre fließt im Uhrzeigersinn, ein Vulkan raucht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Straßenleben](karten/strassenleben.md) ✎ `huashu` | Nach Art von Pissarro: Menschen im Strom des Alltags, ein Boulevard oder ein Feld, Figuren gehören zu ihrem Ort. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Symbolfarbe](karten/symbolfarbe.md) ✎ `huashu` | Nach Art von Gauguin: flache, kräftige Flächen mit dunkler Kontur, Farbe steht für Gefühl und Bedeutung. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Tuschhauch](karten/tuschhauch.md) ✎ `huashu` | Chinesische Freihand-Tuschmalerei nach Art von Bada Shanren: Striche schreiben sich selbst, Tusche verläuft, Leerraum trägt, ein Siegel drückt sich ein. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Warme Haut](karten/warme-haut.md) ✎ `huashu` | Nach Art von Renoir: warme und kalte Töne verweben sich, Licht fällt durch Laub auf Gesichter, Menschen haben Wärme. | 2 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Zerfließende Zeit](karten/zerfliessende-zeit.md) ✎ `huashu` | Surrealismus der Dreißiger: Uhren zerfließen, Schatten werden länger, ein Elefant auf Stelzenbeinen zieht vorbei. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Blaue Schwermut](karten/blaue-schwermut.md) ✎ `huashu` | Melancholische Blaumalerei um 1903: alles in Blau, breite Striche, gestreckte Gestalten atmen langsam. | 1 | klein | ganzes-kurzvideo, intro, uebergang |
| [Eine Ecke](karten/eine-ecke.md) ✎ `huashu` | Song-zeitliche Landschaft nach Art von Ma Yuan: alles drängt in eine Ecke, der Rest ist Nebel und Leerraum. | 1 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Klares Maß](karten/klares-mass.md) ✎ `huashu` | Frührenaissance nach Art von Piero della Francesca: geometrische Ordnung, helle stille Körper, klares Morgenlicht. | 1 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Stille Harmonie](karten/stille-harmonie.md) ✎ `huashu` | Hochrenaissance nach Art von Raffael: ausgewogene Gruppen im Dreieck vor weicher Landschaft, Blicke verbinden die Figuren. | 1 | mittel | ganzes-kurzvideo, intro, uebergang |
| [Wetterhimmel](karten/wetterhimmel.md) ✎ `huashu` | Nach Art von Sisley: der Himmel nimmt die halbe Leinwand, Wetter zieht über eine zusammenhängende Flusslandschaft. | 1 | mittel | ganzes-kurzvideo, intro, uebergang |

## strichzeichnung (32)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Gummiarm-Trick](karten/gummiarm-trick.md) ✎ `anidoodle` | Eine Trickfigur mit Schlaucharmen wippt im Takt, schwarzweiß mit Graustufen und Filmkorn wie ein Kurzfilm von 1930. | 4 | klein | ganzes-kurzvideo, intro, uebergang |
| [Flächenvektor](karten/flaechen-vektor.md) ✎ `anidoodle` | Flache Vektorformen schließen sich Pfad für Pfad, Füllung springt ein, lange Schlagschatten und feines Korn geben Tiefe. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Fünfziger Gouache](karten/fuenfziger-gouache.md) ✎ `anidoodle` | Reduzierte Fünfziger-Farbflächen auf warmem Karton, trocken gemalt, die Tuschelinie sitzt bewusst neben der Fläche. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Isometrischer Schnitt](karten/isometrie-schnitt.md) ✎ `anidoodle` | Ein aufgeschnittenes Haus oder Gerät zeigt sein Inneres auf einem isometrischen Raster, drei Töne je Material. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Klemmbausteine](karten/klemmbaustein.md) ✎ `anidoodle` | Ein Haus, Fahrzeug oder Diagramm setzt sich Stein für Stein aus Klemmbausteinen mit Noppen zusammen. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Marker-Comic](karten/marker-comic.md) ✎ `anidoodle` | Comicfiguren in Markerfarbe mit harter Schattenkante und einer Kontur, die auf der Schattenseite anschwillt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Papierschnitt](karten/papierschnitt-stapel.md) ✎ `anidoodle` | Eine Szene wird aus Papier gelegt, Stück für Stück von hinten nach vorn, jedes schwebt erst und wird dann angedrückt. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Papiertheater](karten/papiertheater.md) ✎ `anidoodle` | Eine Geschichte spielt in einem Theater aus Karton, Kulissen in Ebenen, Figuren mit weißem Rand wie ausgeschnitten. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Sechzehn-Farben-Pixel](karten/pixelraster-16.md) ✎ `anidoodle` | Eine kleine Pixelwelt füllt sich Zelle für Zelle in genau sechzehn Farben, ganzzahlig vergrößert und ohne Glättung. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Risodruck](karten/risodruck.md) ✎ `anidoodle` | Zwei bis drei leuchtende Schmuckfarben drucken übereinander, leicht versetzt, Ton nur aus Raster, Weiß ist das Papier. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Wachskreide](karten/wachskreide-kritzel.md) ✎ `anidoodle` | Ein Motiv entsteht in kräftiger Wachskreide auf rauem Papier, Kritzelfüllung für Kritzelfüllung, mit doppelter Kontur und weißen Glanzstellen. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Zeitungsraster](karten/zeitungsraster.md) ✎ `anidoodle` | Ein Bild wie aus der Tageszeitung, nur aus Rasterpunkten in Schwarz und einer orangen Schmuckfarbe auf gelblichem Papier. | 3 | klein | ganzes-kurzvideo, intro, uebergang |
| [Archivalbum](karten/album-archiv.md) ✎ `anidoodle` | Eine vergilbte Albumseite füllt sich mit Karten, Stichen und Schreibmaschinentext, Klebeband hält, Stempel und roter Stift kommentieren. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bilderbuchfigur](karten/bilderbuch-figur.md) ✎ `anidoodle` | Eine kleine wiederkehrende Figur in weichem Aquarell über feiner Bleistiftlinie, in jeder Szene gleich gezeichnet. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Bleistift und Aquarell](karten/bleistift-aquarell.md) ✎ `anidoodle` | Ein zartes Motiv in Bleistift und Aquarell, die Farbe bleibt knapp neben der Linie, viel weißes Papier steht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Buntstift-Schraffur](karten/buntstift-schraffur.md) ✎ `anidoodle` | Ein Motiv wächst aus Buntstiftschraffur in einer Richtung, Farbe über Farbe, mit sichtbarem Papierkorn. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Einlinienstich](karten/einlinien-stich.md) ✎ `anidoodle` | Ein Porträt oder Gegenstand spult sich aus einer einzigen Linie ab, deren Breite allein Licht und Schatten macht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Facettenlandschaft](karten/facetten-tal.md) ✎ `anidoodle` | Eine Landschaft aus flachen Dreiecken, jede Facette in einem Ton nach der tiefen Sonne, Dunst trennt die Ebenen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Farbholzschnitt](karten/farbholzschnitt.md) ✎ `anidoodle` | Ein japanischer Farbholzschnitt druckt sich Platte für Platte, schwarze Kontur, flache Farbe, gewischter Himmel. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Gebrochene Farbe](karten/gebrochene-farbe.md) ✎ `anidoodle` | Eine Landschaft oder ein Platz baut sich aus unvermischten Öltupfern auf grundiertem Leinen auf, das Auge mischt das Licht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kohle und Radierer](karten/kohle-radiert.md) ✎ `anidoodle` | Kohle wird gezeichnet, weggewischt und neu gesetzt, sodass jede frühere Fassung als grauer Geist im Blatt bleibt. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Kugelschreiber-Skizze](karten/kuli-skizze.md) ✎ `anidoodle` | Eine genaue Skizze in einem einzigen blauen Kugelschreiber, Ton nur aus Schraffur, mit Tintenklecksen an den festen Strichen. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Lichtpause](karten/lichtpause-bauplan.md) ✎ `anidoodle` | Ein Gerät oder Bauwerk zeichnet sich als weißer Werkplan auf tiefem Preußischblau, Grundriss, Schnitt und Maßlinien mit Lineal und Zirkel. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Märchenbuch](karten/maerchenbuch.md) ✎ `anidoodle` | Eine Märchenszene, vorne in deckender Gouache, nach hinten immer blasser bis zur bloßen Bleistiftlinie. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Öl auf Leinwand](karten/oel-impasto.md) ✎ `anidoodle` | Ein Bild wird in Öl gemalt, erst mager angelegt, dann mit fettem Impasto und sichtbaren Borstenspuren. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schabkarton](karten/schabkarton.md) ✎ `anidoodle` | Aus einer schwarzen Fläche wird Licht herausgekratzt, feine weiße Schraffuren formen Tier, Ast oder Gesicht. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Schiefertafel](karten/schiefertafel.md) ✎ `anidoodle` | Auf einer Schiefertafel entsteht in gebrochener Kreide eine Lektion, über den Resten früherer Stunden. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Stickrahmen](karten/stickrahmen.md) ✎ `anidoodle` | Ein Bild entsteht Stich für Stich in Baumwollgarn auf Leinen, mit Fadenglanz und sichtbaren Stichlöchern. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Traumlasur](karten/traumlasur.md) ✎ `anidoodle` | Eine weite, unwirklich klare Ebene unter tiefer Sonne, strichlos glatt gemalt, mit harten Kanten und langen Schatten. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Feder und Lavur](karten/tusche-lavur.md) ✎ `anidoodle` | Eine Straßenecke oder ein Garten, erst als nasse Farbe, die über die Ränder läuft, dann mit schwellender Federlinie gezeichnet. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Tuschpinsel](karten/tuschpinsel.md) ✎ `anidoodle` | Bambus, Zweig oder Vogel entstehen in einzelnen Pinselgesten aus Tusche, jede einmal gesetzt, zuletzt drückt sich ein rotes Siegel ins Blatt. | 2 | klein | ganzes-kurzvideo, intro, uebergang |
| [Punktierte Tusche](karten/punktiertusche.md) ✎ `anidoodle` | Ein Gegenstand verdichtet sich Punkt für Punkt aus feiner Tusche wie eine wissenschaftliche Tafel. | 1 | klein | ganzes-kurzvideo, intro, uebergang |

## lookbook (15)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Beton-Fischauge](karten/beton-fischauge.md) ⚠ LUFS -11.5 bis -9.5 | Ein Look in grauer Betonarchitektur, fast nur mit Fischauge aus der Froschperspektive, kühler Analogfilm mit Korn, alle Drittelsekunde ein Schnitt, dazwischen Störbilder in Falschfarbe, Negativ, Rasterpunkt und Bewegungsecho, am Rand ein gedrehtes Datenblatt. | 5 | mittel | hook, ganzes-kurzvideo, trailer |
| [Dunkelkammer-Abzug](karten/dunkelkammer-abzug.md) | Porträts und Kleidungsdetails in ochsenblutrotem Dunkel, dazwischen Material aus der Dunkelkammer (rosa Negative, Filmstreifen, gerissene Abzüge auf Papier) und Weißblitze; Stotter-Negative peitschen, Porträts stehen ruhig. | 4 | mittel | hook, portrait, ganzes-kurzvideo, intro |
| [Kampagnen-Großschrift](karten/kampagnen-grossschrift.md) ⚠ LUFS -17.5 bis -15.5 | Modekampagne aus flachen Signalfarben, riesiger schmaler Großschrift und Freistellern mit weißem Stickerrand, dazwischen Studio-Makros, ein Papierriss und ein Fischauge. | 4 | mittel | produkt, trailer, hook, ganzes-kurzvideo |
| [Neunziger Anzug und Sport](karten/neunziger-anzug-sport.md) | Eine Figur im weiten Anzug spielt allein in einer dunklen Halle Sport, gedreht wie ein Werbespot der späten Neunziger auf Diafilm (sattes Rot, getönte Brille, Spot von oben), getragen von Blitzbildern, Lichtstreifen und Untersichten unter dem Ziel. | 4 | mittel | ganzes-kurzvideo, trailer, hook |
| [Weißblitz-Kampagne](karten/weissblitz-kampagne.md) ⚠ LUFS -11.9 bis -9.9 | Überbelichtete Modefotos auf gleißendem Weiß in Rosa und Eisblau, gekippte Foto-Karten schweben im Raum, dazwischen Raster-, Zeilen- und Tiefenbild-Blitze und harte Wischer, dazu ein schwarzes Namensetikett. | 4 | mittel | produkt, trailer, hook, ganzes-kurzvideo |
| [Auswahl-Lookbook](karten/auswahl-lookbook.md) | Aus einer Reihe von Outfits wird eines gewählt und dann Ort für Ort vorgeführt; eine riesige Schlagzeile tippt sich Buchstabe für Buchstabe als Selbstgespräch, Orte wechseln durch die Silhouette der Figur, Sticker-Klone stehen daneben. | 3 | mittel | ganzes-kurzvideo, hook, portrait |
| [Drei Farbwelten](karten/drei-farbwelten.md) ⚠ LUFS -9 bis -7 | Ein Look wandert durch drei streng getrennte Farbwelten (goldene Wüste, blauer Tunnel, weißer Raum); jede Welt bekommt ein Etikett in Pixelschrift und ein Paar Foto-Kacheln, danach springen Kacheln über die Vollbilder und eine Sonnen-Silhouette setzt den Drop. | 3 | mittel | ganzes-kurzvideo, portrait, hook |
| [Guckloch und Weinstreifen](karten/guckloch-weinstreifen.md) | Ein Look im hellen Treppenhaus und vor kaltem Himmel, gefilmt mit Fischauge; ein Streifen in der Farbe des Hauptstücks wischt diagonal durchs Bild und teilt es, dazwischen runde Guckloch-Bilder auf Schwarz und ein Kamerasucher. | 3 | mittel | ganzes-kurzvideo, hook, portrait |
| [Kobalt und Kalk](karten/kobalt-kalk.md) | Eine Figur in hellem Leinen auf einer weißgekalkten Insel, nur Weiß und Kobaltblau, Makro-Details, Meer und Möwen wechseln mit kobaltblauen Blitzbildern, dazu ein selbstverliebtes Selbstgespräch in kleiner fetter Kleinschrift. | 3 | mittel | ganzes-kurzvideo, hook, portrait |
| [Laternen-Klone](karten/laternen-klone.md) ⚠ LUFS -8.5 bis -6.5 | Eine Figur in Schwarz mit glitzerndem Schmuck auf einer nächtlichen Straße unter einer Laterne, umgeben von ihren eigenen Klonen; Schnitt im Wechsel ein Schlag nah, zwei Schläge weit, nach einer Pause ein Abschnitt in grünem Licht, am Ende ein langes Porträt in Stille. | 3 | mittel | ganzes-kurzvideo, musikvideo, portrait |
| [Blaue Stunde flanieren](karten/blaue-stunde-flanieren.md) ⚠ LUFS -10.6 bis -8.6 | Eine Figur schlendert in der blauen Stunde durch eine alte Stadt, lange ruhige Bilder der Figur wechseln regelmäßig mit kurzen leeren Orten (warmes Fenster, Wasser, Laterne), ohne Text, weich und filmisch. | 2 | klein | ganzes-kurzvideo, portrait, uebergang |
| [Farbfächer-Drehung](karten/farbfaecher-drehung.md) | Eine Figur dreht sich auf Weiß, mit dem Rücken zur Kamera wechselt sie das Outfit, und von vorn erscheint sie in Farbe, eingerahmt von drei gekippten Farbmusterkarten und einem Farbfächer am Boden. | 2 | mittel | ganzes-kurzvideo, produkt, portrait |
| [Goldene Nacht](karten/goldene-nacht.md) | Eine Figur im hellen Anzug zieht durch eine Großstadtnacht voller Gold und Nachtblau, Prachtsäle, roter Teppich und Cabrio, kinohaft und symmetrisch, mit wenigen kleinen Serifenwörtern wie Liedzeilen. | 2 | mittel | ganzes-kurzvideo, intro, portrait |
| [Kassenbon-Wechsel](karten/kassenbon-wechsel.md) | Eine müde Figur auf Weiß, dann rauscht sie per senkrechtem Wisch durch eine Reihe hochkanter Kassenbons und Speisekarten, jede in eigener Farbwelt, und trägt jedes Mal das passende Outfit. | 2 | klein | ganzes-kurzvideo, produkt, hook, portrait |
| [Titelblatt-Zimmer](karten/titelblatt-zimmer.md) | Ein Raum ganz aus Zeitungspapier, eine Person springt alle zwei Sekunden in ein neues Outfit, und jedes Outfit landet als Magazin-Titelblatt an der Wand. | 2 | klein | ganzes-kurzvideo, hook, produkt, portrait |

## erklaergrammatik (11)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Ich-Erzählfigur](karten/ich-erzaehlfigur.md) ✎ `huashu` | Die Stimme erzählt eine eigene Geschichte, eine einfache Figur springt zwischen Posen und friert, die Pointe sitzt im Schnitt auf das Gesicht. | 4 | klein | ganzes-kurzvideo, hook |
| [Schlagwortbühne](karten/schlagwortbuehne.md) ✎ `huashu` | Wörter sind die Darsteller: jedes Schlüsselwort schlägt auf eine Betonung ein, groß genug für einen Blick, die anderen steigen aus Schlitzen. | 4 | klein | ganzes-kurzvideo, hook |
| [Beweistisch](karten/beweistisch.md) ✎ `huashu` | Ein Argument nach Art von Vox: echtes Material liegt auf einem Tisch, die Kamera sucht wie ein Reporter, Stift und Linien ziehen ruckweise. | 3 | klein | ganzes-kurzvideo, hook |
| [Bühnenoberfläche](karten/buehnenoberflaeche.md) ✎ `huashu` | Eine Produktvorstellung wie auf großer Bühne: ein Ding je Bild, das echte Produkt groß, Namen und Zahlen setzen sich genau auf das Wort. | 3 | klein | ganzes-kurzvideo, hook |
| [Erklärfigur mit Zahlen](karten/erklaerfigur-zahlen.md) ✎ `huashu` | Eine Erklärfigur führt durch Wirtschaft und Technik, wechselt zwischen Zahl im Vollbild, Vergleich und Reaktion. | 3 | mittel | ganzes-kurzvideo, hook |
| [Leinwand-Trickfilm](karten/leinwand-trickfilm.md) ✎ `jsanim` | Ein kleiner Trickfilm, ganz aus Code gezeichnet, mit eigener Wendung oder als Erklärstück, Musik im selben Code. | 3 | mittel | ganzes-kurzvideo, hook |
| [Leuchtende Erklärwelt](karten/leuchtende-erklaerwelt.md) ✎ `huashu` | Wissenschaft nach Art von Kurzgesagt: ein abstrakter Begriff wird ein Ding in einer leuchtenden Welt, die Kamera reist zwischen Größenordnungen. | 3 | klein | ganzes-kurzvideo, hook |
| [Wachsendes Tafelbild](karten/wachsendes-tafelbild.md) ✎ `huashu` | Eine Hand schreibt Satz für Satz auf eine große weiße Tafel, die Kamera folgt, am Ende sieht man das ganze Argument als ein Bild. | 3 | klein | ganzes-kurzvideo, hook |
| [Zahlen, die wachsen](karten/zahlen-wachsen.md) ✎ `huashu` | Ein Diagramm baut sich auf das Wort: Achsen, dann wachsen Balken oder Linien, zuletzt wird genau eine Sache markiert. | 3 | klein | ganzes-kurzvideo, hook |
| [Formel-Tafel](karten/formel-tafel.md) ✎ `manim` | Formeln nach Art von 3Blue1Brown, gebaut mit Manim: eine Gleichung schreibt sich Glied für Glied, verwandelt sich, der Graph antwortet in derselben Farbe. | 2 | mittel | ganzes-kurzvideo, hook |
| [Formwandel im Dunkeln](karten/formwandel-dunkel.md) ✎ `huashu` | Mathematik und Begriffe nach Art von 3Blue1Brown: auf Schwarz steht nur das, wovon gerade die Rede ist, und verwandelt sich ohne Schnitt ins Nächste. | 2 | klein | ganzes-kurzvideo, hook |

## noir (11)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Hochweiß Rotglut](karten/hochweiss-rotglut.md) | Helles, fast weißes Schwarzweiß voller Bewegung, durchschossen von Bildern in glühendem Rot-Orange; Schnitte im Zwei-Frame-Stakkato auf einer Musikwand ohne Pause. | 5 | mittel | trailer, hook, intro, uebergang |
| [Rotes Requisit](karten/rotes-requisit.md) ⚠ LUFS -10.2 bis -8.2 | Grobkörniges Straßen-Schwarzweiß mit hartem Kopflicht und schnellen, unregelmäßigen Schnitten, in dem ein einziger roter Gegenstand von Person zu Person wandert; am Ende landet das Rot auf der Haut und ein Tiefbass klingt aus. | 5 | klein | trailer, hook, produkt, musikvideo |
| [Negativ und Zeitlupe](karten/negativ-zeitlupe.md) ⚠ LUFS -20.6 bis -18.6 | Graustufen-Sportfilm in drei Texturen, erst rohes überbelichtetes Handkamera-Flackern mit Negativbildern, dann saubere Zeitlupe im Spotlicht mit einem stotternden Treffer, am Ende Sprungschnitte im Konfetti. | 4 | mittel | trailer, ganzes-kurzvideo, portrait |
| [Titelblatt-Noir](karten/titelblatt-noir.md) | Mode-Porträt in Schwarzweiß als bewegtes Magazin, Titelseiten-Layouts, rote Rahmen, Riesenwörter hinter der Figur, Fotos auf einem Perspektivraster und eine Collage, in der rote Buchstaben im Takt einschlagen; Rot ist hier zweite Hauptfarbe, nicht nur Akzent. | 4 | mittel | trailer, intro, ganzes-kurzvideo, portrait |
| [Chrom-Makro-Noir](karten/chrom-makro-noir.md) | Mode-Porträt in tiefem Schwarzweiß, geschnitten mit Makros aus gebürstetem Chrom, Lautsprechergittern und Wassertropfen; Papierweiß-Blitze und Zeilenrisse markieren die Schläge, nur die Lippen bleiben rot. | 3 | mittel | trailer, intro, produkt, portrait |
| [Neo-Noir-Steckbrief](karten/neonoir-steckbrief.md) ⚠ LUFS -18.2 bis -16.2 | Eine Figur wird wie im Kinotrailer vorgestellt, in sehr dunklem Petrol mit Bernstein-Praktikallicht, Schnitt auf jeder Zählzeit, und am Ende steht nur ihr Name klein auf Schwarz über einem tiefen Bass-Schlag. | 3 | klein | trailer, intro, portrait |
| [Sieger-Mantra](karten/sieger-mantra.md) | Schwarzweiß-Doku im Kinobalken, getragen von zwei Schriftstimmen, einer leisen kursiven Serif-Zeile und einem riesigen Schlagwort in Gelb oder Kobalt, auf einem Schlag je Takt. | 3 | klein | trailer, intro, ganzes-kurzvideo, portrait |
| [Tiefschwarz-Datamosh](karten/tiefschwarz-datamosh.md) | Schwarzweißes Nachtmaterial, drei Viertel des Bildes abgesoffen, dazwischen ausgebrannte Weißflächen, Weitwinkel und verschmierte Kompressionsfehler; endet auf einem Auge und langer Schwärze. | 3 | mittel | hook, trailer, intro, musikvideo |
| [Indizien-Vermessung](karten/indizien-vermessung.md) | Ruhige, fast farblose Einstellungen von Gegenständen und Orten in einem Rahmen mit runden Ecken, überzogen von einem Netz aus Messpunkten und gestrichelten Linien; leise Satzfetzen benennen die Indizien, nur Gold leuchtet. | 2 | klein | trailer, intro, ganzes-kurzvideo |
| [Störbild-Noir](karten/stoerbild-noir.md) | Ruhiges, hart beleuchtetes Schwarzweiß einer einzelnen Figur, durchbrochen von Ein-Frame-Störbildern (Kontur, Kachelzerfall, Streifenversatz, geschwärztes Rauschblatt) und kurzen Schwarzbildern, auf einem langsamen 60er-Puls. | 2 | mittel | trailer, intro, hook, portrait |
| [Untertitel-Thriller](karten/untertitel-thriller.md) | Ein erzählter Psychothriller in tiefem Schwarzweiß, Nebel, Regen und Gegenlicht, getragen von kleinen Untertiteln, die sich wie auf einer Schreibmaschine aufbauen, und von Fragetiteln, die sich aus Zeichensalat entschlüsseln; ruhige Einstellungen um zwei Sekunden. | 2 | klein | trailer, ganzes-kurzvideo, intro |

## aura-portrait (9)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Funken-Aura](karten/funken-aura.md) ⚠ LUFS -12.3 bis -10.3 | Status-Montage aus Glanzobjekten, Fahrzeugen und grinsenden Gesichtern in kaltem Teal-Monochrom, in das rot-orange Glut, Funkenregen, Blitze und Lichtstreifen einschlagen; Schnitte im Zwei-Frame-Takt auf einer lauten Wand. | 5 | mittel | hook, trailer, produkt, uebergang |
| [Giftgrün-Stakkato](karten/giftgruen-stakkato.md) | Ein Hauptfiguren-Edit ganz in Schwarz und Giftgrün, mit Kontaktstreifen, Fingerabdruck-Silhouetten, Tracking-Linien und Weitwinkel von unten, im Zwei-Frame-Takt bis zum glühenden Titelwort. | 5 | mittel | hook, intro, trailer, portrait |
| [Sportheld mit Kinobalken](karten/sportheld-kinobalken.md) | Spielszenen eines Sporthelden in entsättigtem Petrol-Grün mit schwarzen Kinobalken, grobem Korn und winzigen Tracking-Koordinaten, unterbrochen von dunklen Nachtfahrt-Zwischenbildern, ausgebrannten Weißbildern und einem 1-Bit-Moment; am Ende funkeln Sterne im Schwarz. | 4 | mittel | hook, trailer, portrait, ganzes-kurzvideo |
| [Tinte auf Weiß](karten/tinte-auf-weiss.md) | Helles Lyric-Porträt auf fliederweißem Grund, Silhouetten in tiefem Tintenblau, pastellige Beauty-Makros und Liedwörter in schmaler Grotesk mit Chrom-Füllung, die hinter Gesicht und Schmuck liegen; zwei Stroboskop-Salven zwischen Silhouette und Titelkarte. | 4 | mittel | musikvideo, portrait, hook |
| [Anzug-Monolog](karten/anzug-monolog.md) ⚠ LUFS -20.7 bis -18.7 | Eine Figur im Anzug redet selbstbewusst in die Kamera, Wort für Wort untertitelt, Schlüsselwörter groß in Glasschrift; nach dem Monolog kippt es in eine schnelle Montage derselben Figur in vielen Büroszenen. | 3 | gross | ganzes-kurzvideo, portrait, hook |
| [Augenbalken-Grünnacht](karten/augenbalken-gruennacht.md) | Handkamera-Nacht in olivgrünem Laternenlicht, eine Figur meist von hinten oder mit verdeckten Augen, unterbrochen von Röntgenbild, Schlüsselloch und einem Negativ mit leuchtend roten Augen im Balken; am Drop ein einzelnes rotes Serifenwort. | 3 | klein | hook, intro, portrait, musikvideo |
| [Erkennungs-Porträt](karten/erkennung-portraet.md) | Eine einzige gehaltene Einstellung einer Figur in Abendblau, über die ab dem Drop ein Erkennungssystem läuft (Negativ-Streifen mit Suchmeldung, Datenspalte, Kreuz, Wärmebild-Kipp), während Wortpaare in Pink links und rechts am Kopf vorbei stehen. | 3 | klein | portrait, hook, musikvideo, intro |
| [Hauptfigur-Wende](karten/hauptfigur-wende.md) | Hochformat-Handyclip im grauen Tageslicht, eine Figur im eigenen Garten aus Froschperspektive und Weitwinkel, erst untertreibend betextet, dann kippt es auf dem Drop in große kursive Behauptungen und Viertel-Schnitt; Polaroid-Stapel, Freisteller auf Schwarz und Dreifach-Bild als Würze. | 3 | klein | portrait, hook, ganzes-kurzvideo |
| [Wortflanke Goldstunde](karten/wortflanke-goldstunde.md) | Heldenplakat im Gegenlicht der tiefen Sonne, eine Figur in kühler Kleidung vor warmer Weite, die Kamera driftet langsam zurück; ab dem Drop stehen Liedzeilen als pinke Wortpaare beidseits des Kopfes, kurz unterbrochen von kalten Negativ-Streifen und einem Glutkipp. | 2 | klein | portrait, hook, intro, musikvideo |

## auto-beat (9)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Burnout-Countdown](karten/burnout-countdown.md) ⚠ LUFS -11.7 bis -9.7 | Körniger Nullerjahre-Film über Straßenrennen, Reifenqualm und tanzende Menge, eröffnet mit einem leuchtenden 3-2-1 neben Gesichtern, danach leuchtende Einwortbefehle mit Punkt und eine schmutzige Titelkarte zum Schluss. | 5 | mittel | hook, trailer, intro, ganzes-kurzvideo |
| [Sechziger-Hafenrennen](karten/sechziger-hafenrennen.md) | Ein Gentleman-Fahrer im Stil der Sechziger, ein alter Rennwagen auf einem Stadtkurs am Hafen, warmes Creme, Ocker und Weinrot, schnelle Schnitte von Handschuh, Helm, Kurve und Feier, Bilder kippen kurz in Schwarzweiß, ein roter Streifen wischt durch. | 5 | mittel | trailer, ganzes-kurzvideo, hook |
| [Boxengassen-Pointe](karten/boxengassen-pointe.md) ⚠ LUFS -11.8 bis -9.8 | Zwei Figuren liefern sich an der Rennstrecke einen kurzen Wortwitz mit großen Untertiteln neben dem Kopf, dann schlägt die Musik ein und ein Kinotrailer-Rennen folgt, dessen Bilder durch schmale Bänder und Fenster ins Bild fallen. | 4 | mittel | trailer, hook, ganzes-kurzvideo |
| [Farbkey mit Zielerfassung](karten/farbkey-zielerfassung.md) | Schwarzweiß-Bilder eines Fahrzeugs, nur sein Lack leuchtet in einer Farbe, dünne Messlinien und ein Zielrahmen erfassen es wie ein Scanner, schräge Kamera und dreifach gestapelte Makros auf einem harten Beat. | 4 | mittel | hook, trailer, produkt, ganzes-kurzvideo |
| [Lichtkante im Studio](karten/lichtkante-studio.md) ⚠ LUFS -9 bis -7 | Ein Fahrzeug in tiefem Lack auf Schwarz, ein einzelner Lichtstreif läuft über seine Kanten, Makros von Rad, Instrument und Leuchte springen im Sechzehntel nach einer langen dunklen Atempause. | 4 | mittel | hook, intro, produkt, trailer |
| [Nachtfahrt Farbkipp](karten/nachtfahrt-farbkipp.md) | Schwarzweiß im harten Blitzlicht, das genau auf dem Bass-Einsatz in Nachtfarbe aus Petrol und Rücklichtrot kippt; Lichter sind das eigentliche Motiv, am Ende frisst ein Weißblitz alles und Schwarz steht mit einem Tiefbass-Schlag. | 4 | mittel | intro, hook, trailer, musikvideo |
| [Rennfieber-Epos](karten/rennfieber-epos.md) | Kinobreite Rennmontage in Glutorange und Petrol, Fahrzeugbilder mit glühenden Lichteffekten wechseln im Puls von 0,7 s mit Gesichtern in Anspannung, Qual und Jubel, bis das Fahrzeug durch eine Feuerwand bricht. | 4 | gross | trailer, hook, ganzes-kurzvideo, musikvideo |
| [Rennstrecken-Slogan](karten/rennstrecken-slogan.md) | Eine Fahrerin als Modefigur an einer leeren Rennstrecke, ein Slogan baut sich Wort für Wort in den Raum hinein, erst langsam im goldenen Abendlicht, nach dem Drop schnell in Teal-Nacht mit Rennwagen, Cockpit und einem bildfüllenden Riesenwort. | 4 | mittel | trailer, hook, ganzes-kurzvideo, produkt |
| [Goldene Passfahrt](karten/goldene-passfahrt.md) | Ein Fahrzeug auf leerer Bergstraße im Abendlicht, Luftbild, Verfolgung und Hand am Bedienelement wechseln ruhig auf jedem Schlag eines satten, langsamen Grooves. | 3 | mittel | ganzes-kurzvideo, produkt, intro |

## musikvideo (9)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Gruppentanz im Kulissenwechsel](karten/gruppentanz-kulissenwechsel.md) ⚠ LUFS -11.3 bis -9.3 | Eine Tanzgruppe in knallbunten, ständig wechselnden Kulissen, vier Schnitte je Sekunde, Formation und Einzelgesicht im Wechsel, verbunden durch verwischte Reißschwenks; kein Text, keine Effekte, nur Tanz, Farbe und Tempo. | 5 | mittel | musikvideo, hook, trailer |
| [Idol-Effektgewitter](karten/idol-effektgewitter.md) | Bunte Bühnen- und Porträtbilder einer Sängerin, im Halbsekundentakt geschnitten und mit wechselnden Effekten überfahren: rote Liedwörter auf dem Gesicht, Zoom-Explosion, 1-Bit-Bild mit Tracking-Rahmen, Strahlenkranz, Rotfilter. | 5 | gross | musikvideo, hook, trailer |
| [Blaulicht-Tracking](karten/blaulicht-tracking.md) ⚠ LUFS -9 bis -7 | Performance-Porträt komplett in einer Blau-Verlaufskarte mit starkem Überstrahlen, über das ein Tracking-Overlay mit Liedwörtern in kleinen Etiketten läuft; dazwischen riesige Wörter aus Wellenlinien und leuchtende Augen als wiederkehrendes Motiv. | 4 | mittel | musikvideo, portrait, hook, ganzes-kurzvideo |
| [Bonbon-Lyric-Bühne](karten/bonbon-lyric-buehne.md) | Eine freigestellte Person tanzt und springt durch knallbunte 3D-Welten aus Glaswürfeln, Neonschläuchen und Sternen, die Liedwörter stehen als glänzende Bonbon-Buchstaben im Raum, zum Schluss blinkt der Hintergrund im Sechzehntel durch alle Farben. | 4 | gross | musikvideo, hook, ganzes-kurzvideo |
| [Rockheld kopfüber](karten/rockheld-kopfueber.md) | Eine einzige Heldenfigur in gedämpftem Kinolook, eröffnet mit schreienden Fisheye-Nahaufnahmen im Zehntelsekundentakt, dann Silhouetten vor Lichtportalen, Stunts, kopfüber gedrehte Bilder und Reißschwenks bis zur Pose mit erhobenen Armen vor dem Sonnenuntergang. | 4 | mittel | musikvideo, trailer, hook, portrait |
| [Untersicht-Hype-Reigen](karten/untersicht-hype-reigen.md) | Viele verschiedene Performer in Weitwinkel-Untersicht, jeder in seiner eigenen Farbwelt, gerahmt wie ein 16-mm-Bild mit runden dunklen Ecken; es beginnt mit einem Sechzehntel-Gewitter erhobener Arme und ruht dann auf einzelnen Gesichtern. | 4 | mittel | musikvideo, hook, trailer, intro |
| [Anime-Lichtwechsel](karten/anime-lichtwechsel.md) ⚠ LUFS -11.6 bis -9.6 | Eine Anime-Sängerin auf dunkler Bühne, jede Einstellung in einer anderen Lichtfarbe (Silber, Rot, Türkis, rote Gegenlicht-Silhouette), nach einem langen ruhigen Einstieg immer schneller geschnitten. | 3 | klein | musikvideo, portrait, hook, intro |
| [Pastell-Ornamentschleife](karten/pastell-ornamentschleife.md) | Weiche Nahaufnahmen einer Sängerin in milchigem Lavendel und Eisblau, umrankt von weißen Linienornamenten (Ranken, Schmetterlinge, Noten, Notenlinien), getrennt von Weißblüten; die zweite Hälfte wiederholt die erste Bildfolge wie eine Schleife. | 3 | mittel | musikvideo, portrait, hook, uebergang |
| [Violett-Lyric im Duoton](karten/violett-lyric-duoton.md) | Kinetisches Lyric-Video in Violett und Fast-Schwarz: eine freigestellte Sängerin im Duoton, riesige fette Versalwörter hinter ihr, kursive Serifenwörter mit Bewegungsunschärfe, Buchstaben als Fenster ins Video und magentafarbene Kreise statt der Os. | 3 | mittel | musikvideo, ganzes-kurzvideo, hook |

## scrapbook (8)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Mixed-Media-Zwölfer](karten/mixed-media-zwoelfer.md) | Sommerliches Footage, über das jede Szene eine andere Handarbeit legt (Kritzel, Konturen, Zeitungscollage, Rotoskop-Tusche, Pixelbild), alles kocht auf Zweiern mit zwölf Bildern je Sekunde. | 4 | gross | musikvideo, trailer, intro, ganzes-kurzvideo |
| [Sticker-Flimmern](karten/sticker-flimmern.md) | Alltagsvideo, übersät mit Ölkreide- und Plastikknopf-Stickern, das alle fünf Bilder zwischen Farbe, Schwarzweiß und wechselnden Musterhintergründen flackert. | 4 | mittel | hook, intro, uebergang, ganzes-kurzvideo |
| [Zine-Raster](karten/zine-raster.md) | Doppelseiten eines bunten Fanzines springen im Viertelnoten-Takt, Fotofelder und satte Farbfelder im Raster, verbunden durch Reißschwenks, Mosaik und Filmstaub. | 4 | mittel | intro, hook, musikvideo, ganzes-kurzvideo |
| [Kiez-Kritzel](karten/kiez-kritzel.md) ⚠ LUFS -12.4 bis -10.4 | Warme, körnige Straßenaufnahmen einer Figur und ihres Viertels, überzeichnet mit weißen Handkritzeln und lila Markerstrichen, dazu Filmstreifen-Raster und Fotos auf zerknittertem Papier. | 3 | mittel | musikvideo, portrait, intro, ganzes-kurzvideo |
| [Marker-Rotoskop](karten/marker-rotoskop.md) ⚠ LUFS -17.5 bis -15.5 | Ruhiges Mode-Footage in Naturfarben, über das ein einziger orangeroter Marker Ringe, Wellen und Konturen um die Figur zeichnet, unterbrochen von kurzen Papier- und Duoton-Einschüben. | 3 | mittel | ganzes-kurzvideo, portrait, produkt, musikvideo |
| [Papierrand-Outfit](karten/papierrand-outfit.md) ⚠ LUFS -12.7 bis -10.7 | Klare Tageslichtfotos einer Person in wechselnden Outfits, jedes Bild mit weißem Papierrand, kippenden Polaroid-Rahmen und blauer Kugelschreiber-Notiz, im Achtel geschnitten. | 3 | klein | hook, ganzes-kurzvideo, produkt, portrait |
| [Fotostapel im Weißraum](karten/fotostapel-weissraum.md) | Analoge Blitzfotos landen im Viertel-Takt auf einer leeren weißen Seite und stapeln sich, darüber steht die ganze Zeit eine kleine gelbe Serifenzeile in der Bildmitte. | 2 | klein | ganzes-kurzvideo, portrait, intro |
| [Vorhang-Bühne](karten/vorhang-buehne.md) ⚠ LUFS -12 bis -10 | Ein Papiertheater auf Cremepapier, rosa Samtvorhänge öffnen und schließen kleine Bühnen mit ausgeschnittenen Figuren, Sprechblasen-Stickern und Goldrahmen. | 2 | mittel | intro, trailer, portrait, ganzes-kurzvideo |

## filmlook (7)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Petrol-Flimmer](karten/petrol-flimmer.md) ⚠ LUFS -12.5 bis -10.5 | Quadratisches Porträt-Footage in kaltem Petrol mit milchigen Lichtern und grobem Korn, fünf Bildwechsel je Sekunde, dazwischen Unschärfe-Blitze, Streifenmasken, invertierte Gesichter in Lachsrosa und schräg gelegte Fotostreifen. | 5 | mittel | hook, trailer, portrait, uebergang |
| [Goldstunden-Hymne](karten/goldstunde-hymne.md) | Sportfilm im Gegenlicht der goldenen Stunde, Petrol in den Schatten und Gold in den Lichtern, Gesichter starren frontal in die Kamera, dazwischen Kraft-Details, Wassertropfen und einzelne Schwarzweiß-Blitzbilder. | 4 | mittel | trailer, produkt, hook, ganzes-kurzvideo |
| [Kapitelwort-Kino](karten/kapitelwort-kino.md) ⚠ LUFS -12.2 bis -10.2 | Eine Figur durchläuft eine Nacht im Regen bis zum Morgen über den Wolken; jede Einstellung trägt genau ein Verb in der Bildmitte, das mit einem kurzen Farbversatz-Glitch erscheint. | 3 | klein | trailer, intro, ganzes-kurzvideo, musikvideo |
| [Nachtband-Streifzug](karten/nachtband-streifzug.md) | Ein 4:3-Filmband mitten im schwarzen Hochformat, darin eine körnige Stadtnacht fast ohne Licht (U-Bahn, Tunnel, Rücklichter), eine Figur mit einer Neonfarbe im Haar und zwei, drei grell gesättigte Tagesbilder als Schock; Wechsel im Halbsekundentakt mit Abblenden ins Schwarz. | 3 | klein | musikvideo, hook, uebergang, ganzes-kurzvideo |
| [Neunziger-Kinomontage](karten/neunziger-kinomontage.md) ⚠ LUFS -10.2 bis -8.2 | Eine überzeichnete Figur wird in eine Kette von Kinoszenen im Look eines 35-Millimeter-Films der Neunziger montiert (Arbeitsplatz, Feier, Freizeit, Stadt, Weite), Schnitt auf den Schlag eines lauten, stampfenden Beats, am Ende ein langer Abgang von hinten. | 3 | klein | ganzes-kurzvideo, trailer, portrait |
| [Grünstich-Melodram](karten/gruenstich-melodram.md) | Kinomaterial mit grünstichigen Wänden, satt schwarzen Schatten und warmen Lampen; eine lange Eröffnung auf eine eigenwillige Figur, dann ein Porträt-Reigen exakt auf jedem Viertel. | 2 | mittel | portrait, trailer, intro, ganzes-kurzvideo |
| [Rotlicht-Camcorder](karten/rotlicht-camcorder.md) | Nächtliche Camcorder-Aufnahmen einer Person, fast einfarbig in Rot bis Magenta getaucht, weich verwischt, darüber tippt sich eine Liedzeile Wort für Wort in kleiner weißer Schrift. | 2 | mittel | musikvideo, hook, portrait |

## 3d-objekt (6)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Monument-Fragmente](karten/monument-fragmente.md) | Ein monumentales Bauwerk aus Steinblöcken, nur in Ausschnitten gezeigt, in Terrakotta und Pflaume vor Creme und Lavendel mit einer leuchtenden blauen Fuge, im gleichmäßigen Sechzehntel-Schnitt; ein Schwarzweiß-Block in der Mitte, Titel am Ende. | 4 | gross | trailer, intro, produkt, ganzes-kurzvideo |
| [Weitwinkel-Umkreisung](karten/weitwinkel-umkreisung.md) | Eine einzige Kamerafahrt im Weitwinkel dicht an einem langen, verchromten, mit Aufklebern beklebten Objekt entlang, umkreist sie zwischen strahlenförmig abstehenden Kabeln und zieht am Ende weit nach unten heraus. | 3 | mittel | uebergang, intro, produkt, hook |
| [Glas zur blauen Stunde](karten/glas-blaue-stunde.md) ✎ `kino3d` | Ein Ding am Fenster, draußen die blaue Stunde mit Stadtlichtern als Bokeh, ein warmes Kantenlicht zeichnet Glas und Rand. | 2 | mittel | ganzes-kurzvideo, intro, produkt |
| [Kante im Studio](karten/kante-im-studio.md) ✎ `kino3d` | Ein Objekt frei auf dunklem Grund, zwei Kantenlichter warm und kühl zeichnen seine Form, ein weiches Licht von oben links gibt ihm Körper. | 2 | mittel | produkt, ganzes-kurzvideo, intro |
| [Lamellen-Goldstunde](karten/lamellen-goldstunde.md) ✎ `kino3d` | Ein Ding auf dem Tisch im warmen Abendlicht, das durch Lamellen fällt; Lichtschächte im Staub, die Kamera gleitet heran. | 2 | mittel | ganzes-kurzvideo, produkt, intro |
| [Lampenkegel bei Nacht](karten/lampenkegel-nacht.md) ✎ `kino3d` | Nachts auf dem Schreibtisch: eine Schirmlampe wirft einen warmen Kegel auf ein einzelnes Ding, ringsum ist es dunkel und kühl. | 2 | mittel | ganzes-kurzvideo, intro, produkt |

## glitch (6)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Figur-Filterkaskade](karten/figur-filterkaskade.md) | Eine einzige markante Figur rast durch dreißig Darstellungsarten, Negativ, Wärmebild, Nachtsicht, Strichzeichnung, Klone, Pixel-Silhouette, Glühkontur, im Bildtakt von drei Bildern, und landet in einer langen Klonszene. | 5 | mittel | trailer, hook, intro, portrait, musikvideo |
| [Projektor-Farbsprung](karten/projektor-farbsprung.md) ⚠ LUFS -8.9 bis -6.9 | Rasante Drei-Frame-Schnitte aus einfarbig getönten Aufnahmen, Lichtlecks, Flares und kinetischen Wörtern, anfangs im Fenster eines Filmprojektors, mit Messkurven über Gesichtern und einem langen, stillen Ausklang. | 5 | mittel | hook, trailer, intro |
| [Zielerfassung Schwarzweiß](karten/zielerfassung-schwarzweiss.md) | Ein Hochkant-Porträt in hartem Schwarzweiß, das wie eine Zielerfassung abläuft: Punktwolke formt das Gesicht, Terminalzeilen tippen, Augen im Kachelraster, Ziffernwände, Silhouetten-Gitter; nur ein Kleidungsstück ist farbig. | 5 | mittel | hook, portrait, produkt, intro |
| [Scan-Bewegungsstudie](karten/scan-bewegungsstudie.md) ⚠ LUFS -12.3 bis -10.3 | Ein Porträt wie eine Laborakte: leuchtende Silhouetten im Bewegungskatalog, eine rote Partikelfigur, ein gescannter Kopf, Produkte auf Weiß und beschriftete Schaubilder, im Wechsel aus Einzelbild-Salven und langen ruhigen Studien. | 4 | gross | portrait, produkt, trailer, intro |
| [Tiefenkarte mit Farbfenstern](karten/tiefenkarte-fenster.md) ⚠ LUFS -9 bis -7 | Das ganze Video läuft als graue Tiefenkarte im Nebel (nah dunkel, fern weiß), nur Augen, Lippen und kleine Pixelflecken zeigen sich in rechteckigen Fenstern in echter Farbe; Schnitt exakt auf jedem Viertel eines langsamen Beats. | 3 | mittel | musikvideo, hook, uebergang, portrait |
| [Nachtstadt-Telemetrie](karten/nachtstadt-telemetrie.md) | Leere Orte einer Stadt bei Nacht in Magenta und Violett, ruhig gefilmt, überlagert von einer feinen Messoberfläche mit Etiketten, Zeigelinien, Zählern und Zeitleiste, als würde eine Maschine die Nacht protokollieren. | 2 | mittel | intro, trailer, ganzes-kurzvideo, uebergang |

## zeichentrick (5)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Manga-Schwellpuls](karten/manga-schwellpuls.md) ⚠ LUFS -10.5 bis -8.5 | Wenige Manga-Zeichnungen einer einzigen Figur in reinem Schwarz und Weiß, immer wieder neu geschwellt, verrauscht und gezoomt, Gründe auch invertiert, im dichten Beat-Schnitt. | 5 | klein | hook, intro, musikvideo, portrait, uebergang |
| [Comic-Freisteller](karten/comic-freisteller.md) | Echte Aufnahmen einer Figur, freigestellt mit verrutschter roter Kontur auf Papier, umgeben von Rasterpunkten, Zickzack, Comic-Etiketten und einem beschrifteten Schaubild; am Ende läuft das unbearbeitete Material kurz und ruhig. | 4 | mittel | hook, intro, portrait, produkt, ganzes-kurzvideo |
| [Kino mit Popblitz](karten/kino-popblitz.md) ⚠ LUFS -10.2 bis -8.2 | Fotorealistische Heldenbilder im Kinolook, in die auf den Schlag einfarbige Pop-Duoton-Blitze in Limette, Magenta und Kobalt schlagen, dazu gekritzelte Sternchen, Konfetti-Punkte und Schreibschrift mit Stickerrand; am Ende kippt alles in eine banale Pointe. | 4 | mittel | ganzes-kurzvideo, hook, trailer, musikvideo |
| [Trickstil-Mixtape](karten/trickstil-mixtape.md) ⚠ LUFS -9.9 bis -7.9 | Eine Heldin und ihre Gegner springen von Schnitt zu Schnitt zwischen 3D-Trickfilm, Bleistift-Zeichentrick, Knete und Comic, verbunden durch Kraft-Effekte, Fenster und große Wörter im Gesangstakt. | 4 | mittel | musikvideo, trailer, hook, ganzes-kurzvideo |
| [Comic-Reißschwenk](karten/comic-reissschwenk.md) ⚠ LUFS -11.1 bis -9.1 | Ein Ensemble aus Pop-Manga-Figuren in Gelb, Orange und Schwarz mit Rasterpunkten und Strahlenkränzen, verbunden durch verwischte Reißschwenks und Durchflüge statt Schnitte. | 3 | mittel | musikvideo, intro, ganzes-kurzvideo, trailer |

## erklaerstimme (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Glasröntgen-Akte](karten/glasroentgen-akte.md) | Ein Wissens-Erklärer als Fallgeschichte im Dunkeln, gläserne Röntgenkörper als Motiv, darüber eine Akten- und Messebene aus Karteikarte, Stempelkästen, Zeigelinien und getippten Mono-Zeilen, unten eine Untertitel-Pille mit dem gesprochenen Wort im Cyan-Kasten. | 3 | mittel | ganzes-kurzvideo, hook, trailer |
| [Strichfigur-Erklärer](karten/strichfigur-erklaerer.md) | Eine gezeichnete Strichfigur mit rundem Kopf steht links auf leerem Weiß und spricht schnell, rechts springt zu jedem Schlüsselwort ein Symbol auf, über dem Kopf laufen Wort-Untertitel mit rotem Aktivwort. | 3 | klein | ganzes-kurzvideo, hook |
| [Neon-Symbolbühne](karten/neon-symbolbuehne.md) | Ein ruhig gesprochener Wissens-Monolog, je Satz eine leuchtende Vektorbühne mit einem einzigen Symbol in der Mitte, darüber jedes betonte Wort einzeln groß in Farbe, die sich aus dem Grund umkehrt, alles unter feinen Röhrenzeilen. | 2 | mittel | ganzes-kurzvideo, intro |
| [Whiteboard mit zeichnender Hand](karten/whiteboard-hand.md) ✎ `handzeichnung` | Eine Hand mit schwarzem Marker schreibt und zeichnet Strich für Strich auf eine große weiße Tafel, die Kamera fährt mit der Erklärung von Gruppe zu Gruppe und zieht am Schluss zurück, bis die ganze Tafel als Landkarte des Gedankens zu sehen ist. | 2 | klein | ganzes-kurzvideo, hook, intro |

## malerei (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Facetten-Saga](karten/facetten-saga.md) | Eine dunkle Sagenwelt aus kantigen Stein- und Papierfacetten in Blaugrau, mit einem einzigen warmen Licht, erzählt in ruhigen Einstellungen von je anderthalb Sekunden genau auf dem Raster, mit einem Akzent im Ton auf jedem Schnitt. | 2 | mittel | intro, trailer, ganzes-kurzvideo, uebergang |
| [Gemälde-Großschrift](karten/gemaelde-grossschrift.md) | Alte Gemälde und Druckgrafiken gleiten langsam durchs Bild, riesige schmale Wörter stehen hinter den gemalten Figuren, jedes Kapitel hat eine eigene Tönung, gerahmt von einer feinen Museums-Beschriftung in den Ecken. | 2 | mittel | ganzes-kurzvideo, intro, trailer |
| [Malerei-Raster](karten/malerei-raster.md) | Eine Farbreise von gemalten Szenen in rotem Rauchlicht über flache Vektorfiguren auf Creme zu kontrastreichem Schwarzweiß, verbunden durch ein Schweizer Typo-Raster aus dünnen Linien und Block-Glitches. | 2 | mittel | intro, trailer, ganzes-kurzvideo, musikvideo |
| [Verwandlungsstrom](karten/verwandlungsstrom.md) | Ein einziger Satz steht von Bild 0 bis zum Ende unbewegt in warmem Gelb in der Bildmitte, darunter fließen handgemalte Motive auf Schwarz ohne Schnitt ineinander, jedes verwandelt sich ins nächste. | 2 | mittel | ganzes-kurzvideo, hook |

## produktspot (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Angebots-Ticker](karten/angebots-ticker.md) | Ein Handels-Spot in Markenfarben, der im Takt nach vorn drückt; große Wörter steigen aus Masken, ein schräges Band in Akzentfarbe wischt von Szene zu Szene, das echte Produktfoto fährt ein und landet, ein Preisschild knallt auf den Schlag, die Dringlichkeit läuft als Band durch, Schlusskarte mit Logo, Handlungsaufforderung und Webadresse. | 4 | mittel | produkt, ganzes-kurzvideo, hook |
| [Produkt-Bühne](karten/produkt-buehne.md) | Social-Media-Anzeige aus einem echten Produktfoto; groß gesetzte Frage auf der Markenfarbe, dann steht das freigestellte Produkt auf einem dunklen oder hellen Studioboden, ein Lichtstreif läuft darüber, Vorteile bauen sich als Liste auf, das Preisschild springt an, Schluss mit Logo und Knopf. | 3 | mittel | produkt, ganzes-kurzvideo, hook |
| [Vorher-Nachher](karten/vorher-nachher.md) | Ein Produktspot als Gegenüberstellung im geteilten Bild; oben das Alte auf gedeckter Fläche (oder als Bild aus den Props), unten das Neue auf dem Grund, zwei bis drei kurze Zeilenpaare, die alte Zeile wird in Akzentfarbe gestrichen, dann schiebt die Teilung das Alte hinaus und das echte Produkt steht allein als Held mit Preis und Schlusskarte. | 3 | mittel | produkt, ganzes-kurzvideo |
| [Detail-Zoom](karten/detail-zoom.md) | Eine ruhige Kamerafahrt über ein echtes Produktfoto; Bild 0 zeigt das ganze Produkt mit dem Hook, dann fährt die Kamera nacheinander in Ausschnitte, ein Ring markiert die Stelle, eine dünne Linie führt zum Merkmal im Infofeld; Rückzug aufs ganze Produkt mit Preis und Schlusskarte. | 2 | mittel | produkt, ganzes-kurzvideo |

## surreal (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Kopf-Farbfeld-Reigen](karten/kopf-farbfeld-reigen.md) | Ausgeschnittene Gesichter ohne Hals mittig auf grellen Vollfarben, jedes mit einem surrealen Anhängsel, wechseln alle vier Bilder in einem festen Farbkreis. | 5 | klein | hook, uebergang, intro, portrait |
| [Pop-Surreal-Revue](karten/pop-surreal-revue.md) ⚠ LUFS -11.9 bis -9.9 | Hochglanz-Modefilm in Siebziger-Popfarben, in dem jede Einstellung einen anderen surrealen Trick zeigt (Papier auf dem Gesicht, Spiegelungen, Kaleidoskop, Raster, Riss, ein Gesicht, das zerspringt). | 4 | gross | trailer, musikvideo, hook, ganzes-kurzvideo |
| [Lichtkegel-Sammlung](karten/lichtkegel-sammlung.md) | Ein Beobachtungsbogen auf Weiß kippt nach Farbblitzen in einen weißen Lichtkegel im Sternenhimmel, darin schwebt die Figur in wechselnden Outfits als nummeriertes Fundstück, bis die Sammlung komplett ist. | 3 | mittel | ganzes-kurzvideo, hook, produkt, portrait |
| [Glieder-Fächer](karten/glieder-faecher.md) | Eine ruhige, realistisch gefilmte Figur, aus der in jeder Szene etwas Unmögliches wächst, zusätzliche Arme, Hände als Fächer, verzweigte Flügel, in wechselnden Bildformaten auf Schwarz. | 2 | gross | hook, portrait, uebergang, trailer |

## kinetik-typo (3)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Nummern-Lyrik](karten/nummern-lyrik.md) ⚠ LUFS -9 bis -7 | Liedzeilen als riesige 3D- und Grotesk-Typo über Fotos, nummerierte Kapitel auf satten Farbfeldern, Schallplatten, Chatblasen und Kalender-Widgets, alles in schnellen Schwenks und Drehungen auf einem sehr lauten Rap-Beat. | 5 | mittel | musikvideo, trailer, hook |
| [Essay-Wortbild](karten/essay-wortbild.md) ⚠ LUFS -12.5 bis -10.5 | Ein gesprochener Kurz-Essay, bei dem jedes Schlüsselwort als Typo ins Kinobild gesetzt wird, schmale rote Versalien hinter der Person, feine weiße Wörter frei im Raum, Schrift im Kreis und Handschrift, die sich zeichnet. | 3 | mittel | ganzes-kurzvideo, intro, trailer, portrait |
| [Umkehrwort-Monolog](karten/umkehrwort-monolog.md) | Eine schnelle Stimme spricht einen Gedanken, und genau das gesprochene Wort steht riesig in Versalien in der Bildmitte, eins nach dem anderen hart getauscht, in der Umkehrfarbe des Bildes darunter, über einer sehr bunten, flachen Trickwelt, die alle drei Sekunden auf einem Wortanfang wechselt. | 3 | mittel | ganzes-kurzvideo, hook, intro |

## kopierer (3)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Kopierer-Blendlicht](karten/kopierer-blendlicht.md) | Körnige Schwarzweiß-Kopien voller ausbrennender Lichter, Blitzlicht-Ketten und Spiegelungen; ein kräftiges Blau taucht erst zur Mitte auf und füllt dann Objekte wie mit dem Marker. | 5 | mittel | trailer, hook, intro, produkt |
| [Kopierer-Pegel](karten/kopierer-pegel.md) | Körnige Schwarzweiß-Kopien mit Messgeräte-Einblendungen und einem knalligen Magenta, eine Zahl im Stempel steigt Bild für Bild, bis die Farbe einmal das ganze Bild flutet. | 5 | mittel | trailer, hook, intro, produkt, musikvideo |
| [Kopierer-Stakkato](karten/kopierer-stakkato.md) | Fotokopie in Zweiton mit genau einem Signalrot, Bilder springen im Sechzehntel auf einem langsamen, schweren Beat. | 5 | mittel | trailer, hook, intro |

## werbespot (3)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Leuchtteil im Dunkelstudio](karten/leuchtteil-dunkelstudio.md) | Ein nachtblaues Dunkelstudio mit je einer harten Lichtquelle, Gesichter, Silhouetten und ein Produkt, dessen eines Teil von selbst mintgrün leuchtet; Licht geht im Takt an und aus, Kantenbilder und Weißblitze trennen die Abschnitte. | 4 | mittel | produkt, trailer, hook, ganzes-kurzvideo |
| [Bernstein-Laufsteg](karten/bernstein-laufsteg.md) | Hochkant-Werbespot im Wechsel aus bernsteinfarbenem Produkt-Makro und Models in dunklen Mänteln bei Nacht, getrennt durch Weißblitze von einem Sechzehntel, das Tempo fällt bis zu einer langen Schlusskarte. | 3 | mittel | produkt, trailer, ganzes-kurzvideo |
| [Flakon-Ruhepuls](karten/flakon-ruhepuls.md) | Ein einzelnes Produkt in fast völliger Dunkelheit, Bühne für Bühne, jedes Bild länger als das vorige und jedes durch genau einen Weißblitz getrennt; fast die Hälfte der Laufzeit gehört der Schlusskarte. | 2 | klein | produkt, ganzes-kurzvideo, intro |

## bewegung (2)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Klon-Spur](karten/klon-spur.md) ⚠ LUFS -9 bis -7 | Eine Figur bewegt sich durch ein endloses weißes Studio und lässt bei jeder Bewegung eingefrorene Kopien zurück, bis eine ganze Spur aus Klonen das Bild füllt; dazwischen Nahaufnahmen und ein rauer roter Slogan. | 4 | mittel | hook, portrait, produkt, ganzes-kurzvideo, musikvideo |
| [Springender Bildausschnitt](karten/springender-bildausschnitt.md) | Ein einziges Handyvideo läuft in einem Bildfenster auf Schwarz; das Fenster selbst tanzt im Takt, wird breit, schmal, kippt in die Tiefe und schließt sich zum Schlitz, um am neuen Ort wieder aufzugehen. | 2 | klein | musikvideo, portrait, uebergang, ganzes-kurzvideo |

## oberflaeche (2)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Vektorweiß Zweitausend](karten/vektorweiss-zweitausend.md) | Weißes Nichts mit schwarzer Vektorgrafik der Nullerjahre und genau einem glänzenden Grün, eine Figur posiert, das Bild ruckelt mit zwölf Bildern je Sekunde, ein Ladekreis trennt die Runden. | 3 | klein | hook, intro, uebergang, musikvideo |
| [Webshop und Blitzlicht](karten/webshop-blitzlicht.md) | Eine pastellige Mode-Webseite klickt sich in weichen Übergängen auf, dann kippt das Stück in überstrahlte Blitzfotos mit kleiner Rosé-Typo. | 2 | mittel | intro, hook, produkt, ganzes-kurzvideo |

## vorspann (1)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Silhouetten-Vorspann](karten/silhouetten-vorspann.md) | Ein Filmvorspann im Stil der Sechziger: schwarze Kopf- und Körpersilhouetten auf grob bedruckten Farbflächen (Tiefblau, Orange, Pink, Creme), ein Titel aus tanzenden Lettern, die sich ordnen, Spiegel- und Kaleidoskopbilder und ein Lichtstreif zum Schluss. | 2 | mittel | intro, trailer, ganzes-kurzvideo, musikvideo |

## Schlag-Angaben im Ton gegen das Tempo

Keine: Jeder Schlagabstand im Feld `ton` passt aufs genannte Tempo.

## Lautheit außerhalb −14 ± 1

35 Karten nennen in `abnahme.lufs` einen Bereich ohne Überschneidung mit −14 ± 1 (Messwert der Vorlage, nicht umgeschrieben). Gebaut wird mit −14 ± 1; der LUFS-Wert der Abnahme ist bei diesen Karten kein Ziel.

| Karte | abnahme.lufs |
|---|---|
| [Anime-Lichtwechsel](karten/anime-lichtwechsel.md) | -11.6 bis -9.6 |
| [Anzug-Monolog](karten/anzug-monolog.md) | -20.7 bis -18.7 |
| [Beton-Fischauge](karten/beton-fischauge.md) | -11.5 bis -9.5 |
| [Blaue Stunde flanieren](karten/blaue-stunde-flanieren.md) | -10.6 bis -8.6 |
| [Blaulicht-Tracking](karten/blaulicht-tracking.md) | -9 bis -7 |
| [Boxengassen-Pointe](karten/boxengassen-pointe.md) | -11.8 bis -9.8 |
| [Burnout-Countdown](karten/burnout-countdown.md) | -11.7 bis -9.7 |
| [Comic-Reißschwenk](karten/comic-reissschwenk.md) | -11.1 bis -9.1 |
| [Drei Farbwelten](karten/drei-farbwelten.md) | -9 bis -7 |
| [Essay-Wortbild](karten/essay-wortbild.md) | -12.5 bis -10.5 |
| [Funken-Aura](karten/funken-aura.md) | -12.3 bis -10.3 |
| [Gruppentanz im Kulissenwechsel](karten/gruppentanz-kulissenwechsel.md) | -11.3 bis -9.3 |
| [Kampagnen-Großschrift](karten/kampagnen-grossschrift.md) | -17.5 bis -15.5 |
| [Kapitelwort-Kino](karten/kapitelwort-kino.md) | -12.2 bis -10.2 |
| [Kiez-Kritzel](karten/kiez-kritzel.md) | -12.4 bis -10.4 |
| [Kino mit Popblitz](karten/kino-popblitz.md) | -10.2 bis -8.2 |
| [Klon-Spur](karten/klon-spur.md) | -9 bis -7 |
| [Laternen-Klone](karten/laternen-klone.md) | -8.5 bis -6.5 |
| [Lichtkante im Studio](karten/lichtkante-studio.md) | -9 bis -7 |
| [Manga-Schwellpuls](karten/manga-schwellpuls.md) | -10.5 bis -8.5 |
| [Marker-Rotoskop](karten/marker-rotoskop.md) | -17.5 bis -15.5 |
| [Negativ und Zeitlupe](karten/negativ-zeitlupe.md) | -20.6 bis -18.6 |
| [Neo-Noir-Steckbrief](karten/neonoir-steckbrief.md) | -18.2 bis -16.2 |
| [Neunziger-Kinomontage](karten/neunziger-kinomontage.md) | -10.2 bis -8.2 |
| [Nummern-Lyrik](karten/nummern-lyrik.md) | -9 bis -7 |
| [Papierrand-Outfit](karten/papierrand-outfit.md) | -12.7 bis -10.7 |
| [Petrol-Flimmer](karten/petrol-flimmer.md) | -12.5 bis -10.5 |
| [Pop-Surreal-Revue](karten/pop-surreal-revue.md) | -11.9 bis -9.9 |
| [Projektor-Farbsprung](karten/projektor-farbsprung.md) | -8.9 bis -6.9 |
| [Rotes Requisit](karten/rotes-requisit.md) | -10.2 bis -8.2 |
| [Scan-Bewegungsstudie](karten/scan-bewegungsstudie.md) | -12.3 bis -10.3 |
| [Tiefenkarte mit Farbfenstern](karten/tiefenkarte-fenster.md) | -9 bis -7 |
| [Trickstil-Mixtape](karten/trickstil-mixtape.md) | -9.9 bis -7.9 |
| [Vorhang-Bühne](karten/vorhang-buehne.md) | -12 bis -10 |
| [Weißblitz-Kampagne](karten/weissblitz-kampagne.md) | -11.9 bis -9.9 |
