# Stil-Bibliothek: Index

106 Stil-Karten in 19 Familien. Maschinenlesbar: `index.json`.

So liest man die Felder: `braucht` heißt „eins davon reicht“; ob das eigene Material trägt, entscheidet der Kern der Karte (Beispiel: ein Kern ohne Fotos lässt sich mit Illustrationen oder nur Typo bauen). `abnahme` gilt im Format der Quelle (`format_quelle`). Formatfest sind Schnitte je Sekunde, Shot-Median und LUFS; Helligkeit und Farbigkeit dürfen im Hochformat um 0,03 höher liegen, außer die Karte hat einen eigenen Block `abnahme_9x16`. Gemessen wird mit `starter/werkzeuge/abnahme.py`.

Lautheit: −14 LUFS ist der Standard. Nennt die Karte einen Bereich, gilt die Karte, solange er innerhalb −14 ± 1 bleibt (Ziel dann im gemeinsamen Teil, etwa −13,5). ⚠ LUFS hinter einer Karte heißt: Ihr Bereich liegt ganz außerhalb von −14 ± 1; die Messwerte der Vorlage bleiben stehen, gebaut wird trotzdem mit −14 ± 1, und dieser eine Wert fällt in der Abnahme durch.

Filtern: `python -I werkzeuge/bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook` gibt die passenden Karten als Tabelle aus. Nur mit Code baubar (braucht nur `nur-typo` oder `illustrationen`): `--filter nur_code=ja` oder `--filter braucht<=nur-typo,illustrationen`.

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

## malerei (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Facetten-Saga](karten/facetten-saga.md) | Eine dunkle Sagenwelt aus kantigen Stein- und Papierfacetten in Blaugrau, mit einem einzigen warmen Licht, erzählt in ruhigen Einstellungen von je anderthalb Sekunden genau auf dem Raster, mit einem Akzent im Ton auf jedem Schnitt. | 2 | mittel | intro, trailer, ganzes-kurzvideo, uebergang |
| [Gemälde-Großschrift](karten/gemaelde-grossschrift.md) | Alte Gemälde und Druckgrafiken gleiten langsam durchs Bild, riesige schmale Wörter stehen hinter den gemalten Figuren, jedes Kapitel hat eine eigene Tönung, gerahmt von einer feinen Museums-Beschriftung in den Ecken. | 2 | mittel | ganzes-kurzvideo, intro, trailer |
| [Malerei-Raster](karten/malerei-raster.md) | Eine Farbreise von gemalten Szenen in rotem Rauchlicht über flache Vektorfiguren auf Creme zu kontrastreichem Schwarzweiß, verbunden durch ein Schweizer Typo-Raster aus dünnen Linien und Block-Glitches. | 2 | mittel | intro, trailer, ganzes-kurzvideo, musikvideo |
| [Verwandlungsstrom](karten/verwandlungsstrom.md) | Ein einziger Satz steht von Bild 0 bis zum Ende unbewegt in warmem Gelb in der Bildmitte, darunter fließen handgemalte Motive auf Schwarz ohne Schnitt ineinander, jedes verwandelt sich ins nächste. | 2 | mittel | ganzes-kurzvideo, hook |

## surreal (4)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Kopf-Farbfeld-Reigen](karten/kopf-farbfeld-reigen.md) | Ausgeschnittene Gesichter ohne Hals mittig auf grellen Vollfarben, jedes mit einem surrealen Anhängsel, wechseln alle vier Bilder in einem festen Farbkreis. | 5 | klein | hook, uebergang, intro, portrait |
| [Pop-Surreal-Revue](karten/pop-surreal-revue.md) ⚠ LUFS -11.9 bis -9.9 | Hochglanz-Modefilm in Siebziger-Popfarben, in dem jede Einstellung einen anderen surrealen Trick zeigt (Papier auf dem Gesicht, Spiegelungen, Kaleidoskop, Raster, Riss, ein Gesicht, das zerspringt). | 4 | gross | trailer, musikvideo, hook, ganzes-kurzvideo |
| [Lichtkegel-Sammlung](karten/lichtkegel-sammlung.md) | Ein Beobachtungsbogen auf Weiß kippt nach Farbblitzen in einen weißen Lichtkegel im Sternenhimmel, darin schwebt die Figur in wechselnden Outfits als nummeriertes Fundstück, bis die Sammlung komplett ist. | 3 | mittel | ganzes-kurzvideo, hook, produkt, portrait |
| [Glieder-Fächer](karten/glieder-faecher.md) | Eine ruhige, realistisch gefilmte Figur, aus der in jeder Szene etwas Unmögliches wächst, zusätzliche Arme, Hände als Fächer, verzweigte Flügel, in wechselnden Bildformaten auf Schwarz. | 2 | gross | hook, portrait, uebergang, trailer |

## erklaerstimme (3)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Glasröntgen-Akte](karten/glasroentgen-akte.md) | Ein Wissens-Erklärer als Fallgeschichte im Dunkeln, gläserne Röntgenkörper als Motiv, darüber eine Akten- und Messebene aus Karteikarte, Stempelkästen, Zeigelinien und getippten Mono-Zeilen, unten eine Untertitel-Pille mit dem gesprochenen Wort im Cyan-Kasten. | 3 | mittel | ganzes-kurzvideo, hook, trailer |
| [Strichfigur-Erklärer](karten/strichfigur-erklaerer.md) | Eine gezeichnete Strichfigur mit rundem Kopf steht links auf leerem Weiß und spricht schnell, rechts springt zu jedem Schlüsselwort ein Symbol auf, über dem Kopf laufen Wort-Untertitel mit rotem Aktivwort. | 3 | klein | ganzes-kurzvideo, hook |
| [Neon-Symbolbühne](karten/neon-symbolbuehne.md) | Ein ruhig gesprochener Wissens-Monolog, je Satz eine leuchtende Vektorbühne mit einem einzigen Symbol in der Mitte, darüber jedes betonte Wort einzeln groß in Farbe, die sich aus dem Grund umkehrt, alles unter feinen Röhrenzeilen. | 2 | mittel | ganzes-kurzvideo, intro |

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

## 3d-objekt (2)

| Karte | kurz | Energie | Aufwand | Einsatz |
|---|---|---:|---|---|
| [Monument-Fragmente](karten/monument-fragmente.md) | Ein monumentales Bauwerk aus Steinblöcken, nur in Ausschnitten gezeigt, in Terrakotta und Pflaume vor Creme und Lavendel mit einer leuchtenden blauen Fuge, im gleichmäßigen Sechzehntel-Schnitt; ein Schwarzweiß-Block in der Mitte, Titel am Ende. | 4 | gross | trailer, intro, produkt, ganzes-kurzvideo |
| [Weitwinkel-Umkreisung](karten/weitwinkel-umkreisung.md) | Eine einzige Kamerafahrt im Weitwinkel dicht an einem langen, verchromten, mit Aufklebern beklebten Objekt entlang, umkreist sie zwischen strahlenförmig abstehenden Kabeln und zieht am Ende weit nach unten heraus. | 3 | mittel | uebergang, intro, produkt, hook |

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
