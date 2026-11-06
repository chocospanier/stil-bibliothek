# Der Bauweg: von der Stilwahl bis zur Abnahme

> **Hinweis zur freien Fassung:** Dieser Ablauf nennt Werkzeuge (`vorpruefung.py`, `abnahme.py`, `takt.py`, den Prüfer, den Remotion-Starter). Sie liegen im Werkzeugkasten, nicht in dieser freien Hälfte. Der Ablauf gilt trotzdem: Jeder Schritt lässt sich auch von Hand oder mit eigenen Werkzeugen gehen.

So entsteht ein Kurzvideo mit dieser Bibliothek. Der Weg ist aus 26 gebauten Stücken und 24 Prüfberichten entstanden; jede Station gibt es, weil ihr Fehlen einmal etwas gekostet hat. Wer mit einer KI baut, gibt ihr diesen Ablauf und [SKILL.md](stilbibliothek/SKILL.md).

## 0. Absicht in einem Satz
Was soll das Video tun (Hook, Trailer, ganzes Kurzvideo, Lyric-Clip, Produkt), für wen, auf welcher Plattform, in welcher Länge und welchem Format (9:16, 16:9, beide)? Welche Energie, 1 ruhig bis 5 rasant? Welches Material gibt es schon (Fotos einer Figur, Illustrationen, Ortsaufnahmen, Produkt, nur Typo, 3D)?

## 0a. Erzählform wählen
In [GRAMMATIK.md](stilbibliothek/GRAMMATIK.md) eine der acht Kurzformen wählen (Chronologie mit Verwandlung, Auftrag mit Beat-Schnitten, fester Held, Katalog, Gegenüberstellung, Frage und Antwort, Vorher und nachher, Ablauf). Die Form entscheidet, ob das Stück schneidet, verwandelt oder fährt; erst danach die Karte. Den einen Satz aufschreiben, der das Stück trägt.

## 1. Stil würfeln (seit 31.10.2026)
- Normalweg: `python -I starter/werkzeuge/wuerfeln.py zug --haus haus --projekt <projektordner> --probe`. Der Zug wählt den Grundstil aus der Hausmischung des Kanals (`haus/mischung.json`), nie den des letzten Videos, dazu Palette, Schriftpaar und Werte im Spielraum der Karte. `stil.json` sagt, ob die Karte einen Motor für eigenen Inhalt hat (sofort rendern, immer mit `--props <inhalt.json>`) oder von Hand gebaut wird, bei `vorlage` als Kopie dieser Komposition mit ganz ersetztem Beispielinhalt (dann weiter mit Schritt 2; danach `wuerfeln.py motor` und `wuerfeln.py probe`, siehe [starter/LIESMICH.md](starter/LIESMICH.md), Abschnitt „Würfelstile“).
- Die Bestellung hat einen Zweck ([ZWECKE.md](stilbibliothek/ZWECKE.md)). Er geht als `--zweck` in den Zug; Produktwerbung und Angebote laufen immer in den Markenfarben. Passt kein Grundstil der Hausmischung zum Zweck, zieht der Zug aus allen Karten des Zwecks und der Branche und schreibt das ins Protokoll; zeige dem Menschen dann drei Standbilder, bevor du baust.
- Wünscht der Mensch einen bestimmten Stil, gilt sein Wunsch; der Zug liefert trotzdem Palette und Werte.
- Die Wahl von Hand (unten) bleibt für neue Kanäle ohne Mischung und für Stile außerhalb der Mischung:
- In [FAMILIEN.md](stilbibliothek/FAMILIEN.md) die Familie nach Wirkung und Einsatz wählen.
- Nach `einsatz`, `energie`, `braucht` und `motor_aufwand` filtern: `python -I werkzeuge/bibliothek_index.py --filter braucht=nur-typo motor_aufwand=klein einsatz=hook` gibt die passenden Karten als Tabelle aus (mehrere Werte mit Komma, Zahlen auch mit `>=`, etwa `energie>=4`). Wer nur Code hat (keine Fotos, kein Footage, kein Produkt, kein 3D): `--filter nur_code=ja` oder `braucht<=nur-typo,illustrationen` („nur diese“); die Tabelle zeigt die Spalte „nur Code“. `braucht=nur-typo` allein reicht nicht, weil bei Listen ein Treffer genügt.
- Höchstens drei Karten in die engere Wahl, eine empfehlen. Entscheidung festhalten.

## 2. Karte lesen, Kern zuerst
- Die drei `kern`-Merkmale sind Pflicht. Wer nur diese drei trifft, ist zu 80 % da.
- `Bildtypen` sagen, welche Einstellungen es gibt und wie groß das Motiv ist. `Schnittmuster` ist der Bauplan. `Regler` sagt, was sich ändern darf, ohne dass der Stil kippt.
- Strecken-Regel: Ist das eigene Stück länger als der Bauplan, wachsen Hook, Atem und Schluss; kurze Slots bleiben kurz, sonst kippen Median und Schnittdichte. Kürzen genauso. Im Starter erledigt das `stretch()` für alle Slots mit `grows`.
- Schleifen-Regel: Karten mit Runden wachsen um Runden, nicht durch Strecken; nur der Schluss wächst für die Pflichtzeile. Gestreckt würden Hook und Übergänge (etwa ein Ladekreis) so lang, dass sie wie Standbild oder Fehler wirken.
- Die `Fallen` am Ende der Karte vor dem Bau lesen, nicht danach.

## 3. Skript und Storyboard locken
- Text, Pointe, Hook und Schluss stehen fest, bevor etwas gerendert wird.
- Die ganze Abfolge einmal als Zuschauer lesen: Kann jemand in einer schlechten Phase darin einen Abschied sehen? Lässt es sich als Politik, Gewalt oder Marke lesen? Ergibt die Fakten-Kette Sinn? Gestreute Buchstaben dürfen keine Abkürzungen bilden.
- Bild 0 ist das Titelbild: Endgröße, nichts angeschnitten, Hauptmotiv mindestens 30 % der Höhe. Bild 0 hat Vorrang vor Slot 1 der Karte: Beginnt die Karte mit einem leeren oder kleinen Motiv, wird Slot 1 so umgebaut, dass schon das erste Bild Titel und Hauptmotiv zeigt.

## 3a. Look-Check (vor dem Storyboard)
- Zwei bis vier der verschiedensten Beats als Standbild in Endgröße bauen und nebeneinander zeigen: `npm run storyboard -- <komposition> <look.json> <ordner>` mit nur diesen Beats.
- Der Mensch sagt je Bild Ja oder Nein. Erst nach den Ja entsteht das ganze Storyboard. Ein falscher Look kostet so Minuten, nicht ein Storyboard.
- Jedes Bild gegen die Bild-Checkliste in [GRAMMATIK.md](stilbibliothek/GRAMMATIK.md) und die `kern`-Merkmale der Karte halten. Der Code der Standbilder wird der Code des Videos.

## 4. Material erzeugen und abnehmen
- Bilder und Musik mit den Prompts aus `Material` erzeugen oder eigenes Material nehmen. Nie Motive, Marken oder Texte einer Vorlage nachbauen.
- Prompts nennen keine Gerätearten oder Produktformen, die Marken herbeirufen (Blickwinkel beschreiben statt „smartphone photo“, „plain smooth leather sneaker“ statt „canvas sneaker“), kein „hook“, keine hängenden Seile.
- **Jedes generierte Bild in voller Größe ansehen, bevor es ins Stück kommt.** Suchen nach: Schlingen, Seilen, Haken, Waffen, Blut, Flaggen, Zeichen, Logos, markentypischen Formen, lesbarer oder Pseudo-Schrift, Gesichtern im Hintergrund.
- Ein Produkt = ein Master-Packshot; alle Bühnen daraus freistellen, nicht je Bühne neu generieren.
- Kundenmaterial (Produktfoto, Logo) über `starter/werkzeuge/freistellen.py`; das Prüfbild gehört zum Look-Check. Die Stimme bekommt je Zeile `text` (gesprochen) und `anzeige` (Untertitel), Zahlen und Kürzel schreibst du im `text` so aus, wie sie gesprochen werden.
- Figuren (Avatare, Freisteller): nur verschieben, gleichmäßig skalieren, leicht drehen. Nie strecken, stauchen, scheren, invertieren, filtern. Neue Posen gegen das Original abgleichen.

## 5. Raster vom echten Ton
**Musik und Stimme (Hausregel seit 18.10.2026):** Musik ist immer echte Musik: ElevenLabs Music über `starter/werkzeuge/musik.py` (Prompt aus dem Abschnitt `Material` der Karte, Länge aus der Bestellung, rund 900 Credits je Minute) oder eigene, lizenzierte Musik. Der Taktbauer ist keine Musikquelle; er setzt nur einzelne Schläge und Klicks über die Musik (`taktbauer.py --nur-schlaege`). Ohne Schlüssel: Stille mit Hinweis, nie ein Ersatzbett. Jedes Stück mit Text bekommt eine Vorlesestimme (`starter/werkzeuge/stimme.py`, ElevenLabs v4, Wortzeiten für `WortSpur`, Untertitel); „ohne Stimme“ nur auf ausdrückliche Bestellung. Schlüssel nur in der Umgebung (`ELEVENLABS_API_KEY` oder `ELEVENLABS_KEY_DATEI`), nie in einer Datei des Pakets. **Seit 1.5 (Zeichen-Motoren):** Musik und Geräusche aus den Partitur-Motoren der Zeichen-Motoren (`animskill.py`, Weg `code`: modellierte Instrumente, Taktraster, Geräusche auf der Bildaktion) sind zugelassen. Sie werden immer nach dem Ton-Standard gemischt (`starter/werkzeuge/ton_standard.py`): Bett allein um −24 LUFS und unter der Stimme 3 dB tiefer, Stimme −16, Geräusche −20, Gesamt −14 LUFS, True Peak höchstens −1 dBTP. Geräusche und Stimme tragen den Pegel, die Musik liegt darunter. Kein dumpfer Schlag, Boom oder Impact am Ende; den Payoff hell setzen (Glocke, Akkord, Glanz), die Endprüfung des Mischers meldet einen tiefen Einschlag in den letzten 2,5 s.
- Musik zuerst fertig machen, dann Tempo und ersten Schlag am fertigen Ton messen: `python -I starter/werkzeuge/takt.py <ton> --out takt.json` (Tempo mit einer Nachkommastelle, Phase, erster Schlag, Sechzehntel in Bildern). Die Sechzehntel des Schnittmusters auf dieses gemessene Raster umrechnen, nie auf die Zahl im Prompt. Musik: `python -I starter/werkzeuge/musik.py --karte <karte.md> --sekunden <länge> --aus <ordner>/musik.wav --takt <ordner>/takt.json` (ElevenLabs Music, Prompt aus der Karte, misst das Raster gleich mit) oder eigene, lizenzierte Musik. Den Schlag auf der Pointe legt `taktbauer.py --nur-schlaege --schlag <sechzehntel>` als eigene Spur darüber; die Musik ist davor stumm (Atem).
- Bei eigener Fläche unter einem Bett (Bordun, Pad, Atmo): am Bett messen, nicht am fertigen Ton; die Fläche verschiebt sonst das gemessene Tempo. Meldet `takt.py` einen Rastertreffer unter 30 %, ist das Tempo unsicher: am Bett messen oder `--band hoch`. Bei langsamen Stücken (unter 80 BPM) meldet `takt.py` oft das Doppeltempo mit Halbtempo-Hinweis; dann mit `--min` und `--max` um das erwartete Tempo messen.
- Sprechstimme: Wortzeiten aus einer Transkription mit Wortstempeln; Schnitte und Wörter auf die Silben. Höchstens 3,5 Wörter je Sekunde; jeder Beat beginnt rund 0,3 s nach dem Satzende.
- **Treffer in die Sprechpause:** Der Treffer der Pointe liegt in der Pause vor dem Satz, der sie nennt, nie unter Sprache (unter der Stimme wird er verschluckt).
- Pointe: Musik hart stoppen, echte Stille davor (mindestens 0,4 s), Satz zusätzlich als Etikett im Bild. Bett endet am Schnitt.
- Verlangt die Karte am Schluss einen Nachklang (ausklingender Akkord, letzter Ton), gilt die Karte: Stille vor dem Schlag bleibt Pflicht, nach dem Schlag darf der Ton ausklingen. Die allgemeine Regel „hart stoppen“ gilt, wenn die Karte nichts anderes sagt.

## 6. Bauen
- Nach `Rezept für einen Code-Motor`: erst Grund und Bildbehandlung als Standbild prüfen, dann Bausteine, dann Bewegung. Teure Filter einmal vorrechnen und cachen.
- Extremwerte aller Bewegungen durchrechnen (Überschwinger, Zoom, Ruckzoom, Wackeln): Schrift bleibt auch im extremsten Bild 40 px vom Rand; Wackeln braucht überskalierten Grund (1 + 2,2 × Amplitude / Breite).
- In 9:16 die unteren 15 % freihalten (Knöpfe der Plattformen). Wörter in Nahaufnahmen auf Nasen- oder Kinnhöhe, nie über den Augen; Text nie über Text.
- Höchstens 3 harte Hell-Dunkel-Wechsel je Sekunde. Kein Standbild über 1 s. Pointen und Pflichtzeilen mindestens 2,3 s lesbar, einzelne Wörter mindestens 0,5 s.
- Storyboard in voller Größe exportieren (ein Bild je Beat) und selbst ansehen, auch bei 390 px Breite. Im Starter: `npm run storyboard -- <komposition> <beats.json> <ordner>`.

## 7. Prüfen, bevor gerendert wird
1. Selbstprüfung mit der Checkliste im [Fehlerkatalog](pruefen/FEHLERKATALOG.md), Haken in die Projektnotiz.
2. Automatische Vorprüfung am Probe-Render: `python -I werkzeuge/vorpruefung.py <video.mp4> --handy <video_handy.mp4> --out <ordner>`. Rot = sehr wahrscheinlich Blocker, Gelb = ansehen. Mit Stimme dazu `--woerter <wortzeiten.json>` (Sprechtempo, Treffer in der Sprechpause), mit geplantem Treffer `--treffer <sekunde>` (Höhepunkt nach der Stille), mit festem Helden `--anker <name>` (Hauptmotiv bleibt an seinem Platz). Die Textprüfung (abgeschnitten, überlappend, zu klein) läuft von selbst, wenn neben dem Video das Text-Protokoll aus `npm run render` liegt.
3. **Frischer Prüfer** ([PRUEFER.md](pruefen/PRUEFER.md)): ein zweites Modell oder ein zweiter Mensch, der das Stück nicht gebaut hat, sieht Storyboard-Standbilder und 12-fps-Streifen an jeder Bewegungsstelle und schreibt `pruefung_r1.json` mit `blocker` und `polish`.
4. Bestanden = kein Blocker. Erst dann Vollrender.

Probe-Render und Vollrender sind derselbe Befehl (`npm run render -- <komposition>`, Endgröße, in Sekunden fertig). „Vollrender“ heißt: nach bestandener Prüfung (und nach der Reparatur) noch einmal rendern, damit Prüfung, Abnahme und Auslieferung dieselbe Datei meinen. Die Messdateien tragen Größe und Änderungszeit des gemessenen Videos; nach jedem Render neu messen.

## 8. Rendern, reparieren, abnehmen
- Vollrender in Endgröße (derselbe Befehl wie der Probe-Render, nach bestandener Prüfung noch einmal). Lautheit: −14 LUFS ist der Standard; nennt die Karte einen Bereich, gilt die Karte, solange sie innerhalb −14 ± 1 bleibt (Ziel dann im gemeinsamen Teil, mit `handy.py --lufs`). Liegt der Bereich einer Karte ganz außerhalb, ist er kein Ziel (in `INDEX.md` markiert). Handy-Fassung mit dem Ton des Masters (`-c:a copy`), beide auf demselben Ziel, True Peak höchstens −1 dBTP: `python -I starter/werkzeuge/handy.py <master.mp4>` (H.264 High, CRF 23, höchstens 6 Mbit/s, faststart, TV-Bereich bt709) misst beide Fassungen gleich mit; liegt der Master nicht bei −14 LUFS oder sein True Peak über −1 dBTP, setzt es die Lautheit vorher linear nach, gemessen nach der AAC-Kodierung (AAC hebt den True Peak um bis zu 0,5 dB). `abnahme.py` zeigt den True Peak der fertigen Datei mit.
- Lautheit linear setzen (Verstärkung plus Begrenzer), nicht mit `loudnorm` im dynamischen Modus: der drückt die Lautheitsspanne stark zusammen (im Fremdtest von 9,9 auf 1,7 LU).
- Abnahme-Werte messen: `python -I starter/werkzeuge/abnahme.py <video> <karte.md>` gibt je Wert ✓ oder ✗ mit Soll und Ist, mit denselben Formeln wie bei der Kartenerstellung.
- Genau **eine** Reparaturrunde: Prüfer kurz auf den Render, Blocker beheben, Vorher-Nachher-Ausschnitte ablegen, Prüfer sieht die Reparatur. Keine Endlosschleife: Was danach noch stört, entscheidet ein Mensch.
- Abnahme mit Auge und Ohr am Handy. Ton hört nur ein Mensch; keine Messung ersetzt das.
- Jede neue Falle in die Karte unter `Fallen` eintragen. So wird die Bibliothek mit jedem Stück besser.

## 8a. Register-Abgleich (seit 31.10.2026)
- `handy.py` gleicht das fertige Video als Schritt 4 mit dem Register ab (`haus/register.db`, mit Register-Schlüssel auch zentral). Grün: liefern. Gelb: liefern, der nächste Zug meidet diesen Grundstil. Rot: nicht hochladen.
- Ist das rote Gegenstück die eigene, nie gelieferte Vorfassung desselben Videos (Reparatur nach der Prüfrunde), ist es kein Rot: im selben `render/`-Ordner ersetzt `handy.py` den alten Eintrag selbst, sonst `--fassung-von`. Neu würfeln nur bei Rot gegen ein anderes Video.
- Bei Rot gegen ein anderes Video: neu würfeln und mit **anderem Inhalt** neu bauen. Farbe und Schrift allein reichen nicht, das Register misst Helligkeit und Lage. Nach zwei roten Runden entscheidet der Mensch (`register.py freigeben <id> --grund "…"`).
- Beim Liefern die Material-IDs mitgeben (`handy.py … --material id1,id2`), damit die Material-Suche weiß, was dieser Kanal schon genutzt hat.
- Neuer Kanal: einmal `overlays.py --seed kanal` und `texturen.py ../haus/material --seed kanal`, damit Korn, Lichtlecks und Kacheln nur diesem Kanal gehören (`starter/LIESMICH.md`, Abschnitt „Eigene Grafik je Kanal“).

## Faustregeln, die alles überleben
- Messung ist kein Urteil.
- Ein Stück, das niemand in einem Klick ansehen kann, ist nicht geliefert.
- Je Werk eine Prüfrunde und eine Reparatur, dann der Mensch.
- Erst sehen, dann einbauen. Erst Storyboard, dann Render. Erst Prüfer, dann Vollrender.
- Eigener Inhalt je Video. Den Beispieltext einer Komposition liefert nie jemand aus.

## Bildrate: zwei feste Werte, nie mischen (Hausregel)

**30 fps für alles aus Code** (Remotion-Motoren: Typo, Erklärer, Motion Graphics; liegt auf Handy-Displays mit 60 und 120 Hz sauber) und **24 fps für alles mit KI-Bewegtbild** (Seedance, Kling, Kino; native Rate der Modelle, Filmlook). Keine 60, keine 25.
- **Mischstück (Code-Typo über KI-Clip):** die Komposition übernimmt die Rate des Bewegtbilds, also 24; nie den Clip auf 30 hochrechnen (jedes fünfte Bild doppelt = Mikro-Ruckler).
- **Lokale Clips (Wan 16 fps, LTX nach Karte):** vor dem Einbau auf 24 bringen (Bewegungsinterpolation `minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1`, danach die schnellste Stelle als Streifen ansehen; schmiert sie, schneiden statt interpolieren).
- **Web-Clip-Stile mit 12-fps-Look** dürfen wie bisher mit 12 fps rendern, wenn die Karte es so trägt.
- **Prüfung:** `ffprobe -show_entries stream=r_frame_rate` zeigt in Master und Handy-Fassung den Wert, den die Karte oder der Bauplan nennt (30, 24 oder 12); ein anderer Wert ist ein Blocker.

## Zitat in einem Rutsch (`starter/werkzeuge/zitat.py`)

Für die zwei Zitat-Karten gibt es den ganzen Weg oben als ein Werkzeug: aus einem Satz mit Zuschreibung entsteht ein fertiges Hochkant-Stück von rund 20 s, mit allen Prüfungen dieses Ablaufs. Gedacht für Serien (ein Zitat am Tag), für jede Nische: Leitsatz, Spruch, Zitat, Frage, Satz einer Marke.

| Karte | Was entsteht | Ton |
|---|---|---|
| `verwandlungsstrom` | Satz steht ab Bild 0 (Komposition `ZitatStrom`), vier bis sechs gemalte Motive verwandeln sich ineinander, das letzte zurück ins erste | Musikbett |
| `umkehrwort-monolog` | Stimme spricht das Zitat, jedes Wort steht groß in der Gegenfarbe des Bildes (`UmkehrwortMonolog`), Szenen wechseln auf Wortanfängen, am Schluss Name und Herkunft in fester Farbe | Stimme, Bett rund 10 dB darunter |

**Drei Wege zum Material** (Feld `material` der Bestellung, oder Schalter `--nur-code`):
- `dienste`: Standbilder und Clips aus Bild- und Videodiensten über den Adapter oder von Hand (unten), 24 fps.
- `code`: nur Code, kein Dienst. Jede Szene ist ein gemaltes Motiv der Code-Bühne (`starter/src/beispiele/codebuehne.tsx`): `{"id": "k1", "form": "stein", "farbe": "#C0763A", "horizont": "#1B2240"}`, Formen `sonne`, `sichel`, `blatt`, `tropfen`, `flamme`, `wolke`, `stern`, `blume`, `stein`, `berg`; jede verwandelt sich in die nächste, die letzte zurück in die erste. Die Schritte `bilder` und `clips` entfallen, die Lesbarkeit misst an einem Render des Grunds ohne Schrift, Render mit 30 fps. Die Prüfung blockt einen hellen Kern im Satzband (36 bis 56 % der Höhe) und ein Motiv unter 30 % der Höhe in Bild 0, sie meldet blasse Farben (Sättigung unter 0,5 drückt die Farbigkeit unter das Soll). Bei `verwandlungsstrom` höchstens 19,9 s, die letzten zwei Szenen länger (Atem und Ruhebild).
- `ordner`: eigene Bilder (`"material": {"weg": "ordner", "ordner": "eigene_bilder/"}`), Szenenplan aus den Dateinamen, Randbeschnitt und Bogen wie bei den Diensten, je Bild eine langsame Eigenbewegung (Zoom 1 auf 1,04) und eine lange Überblendung, 30 fps.
`--vorlage <ordner> --nur-code` legt eine Bestellung für den Weg `code` an. Ohne Stimme bekommt `umkehrwort-monolog` die Wortzeiten aus dem Lesetakt (`lesetakt` in der Bestellung, Standard 2,5 Wörter je Sekunde; dieselbe Formel wie `lesezeiten()` im Starter). Stimme und Musik ohne eigenen Adapter: ElevenLabs eingebaut, sobald ein Schlüssel da ist; die Stimme liest bei beiden Karten das Zitat vor, die Musik wird unter ihr leiser und danach wieder offener. Ohne Schlüssel: Stimme von Hand ablegen (Handweg), Musik Stille mit Hinweis.

**Bestellung:** `python -I starter/werkzeuge/zitat.py --vorlage <projektordner>` legt `bestellung.json` an. Pflicht sind `zitat`, `zuschreibung` und `karte`; dazu `herkunft` (Werk, Stelle, Übersetzung; erscheint bei `umkehrwort-monolog` am Schluss), `dauer` (Ziel, Standard 20), `stimme` (`{"an": true, "kennung": "<Stimme>", "tags": "[calm]", "stabil": 0.5, "sprache": "de", "vor": "<Kontextsatz, wird nicht gesprochen>"}`), `musik` (`{"weg": "motor" | "datei" | "taktbauer", "datei": "…", "prompt": "…"}`), `zeilen` (eigener Umbruch für `verwandlungsstrom`), `schrift` und `farbe` (sonst aus `haus/look.md`, sonst aus der Karte), `motoren` (Adapter, siehe unten), `haus` (anderer Ordner als `haus/`). Die Quelle des Zitats gehört in eine eigene `FAKTEN.md` im Projektordner: gemeinfreier Wortlaut, Ausgabe, Seite, Beleg.

**Szenenplan:** Fehlt `szenen.json`, legt der erste Lauf eine Vorlage an und hält an. Je Szene ein englischer Bild-Prompt (`bild`, ein konkreter Ort mit zwei eigenen Requisiten, Licht aus einem Pool, kein Mensch, der handelt), ein `detail` (ein unerwartetes Element) und je Karte `bewegung` mit `kamera` und `ab_wort` (bei `umkehrwort-monolog`: das Wort, mit dem die Szene beginnt; die letzte Szene `"schluss"`) oder `verwandlung` (bei `verwandlungsstrom`: wie das Motiv ins nächste übergeht). Den Look-Satz der Karte hängt das Werkzeug selbst an. Die Prüfung blockt: Platzhalter, nicht Englisch, mehr als zwei Standard-Floskeln, Wörter, die Hände, Seile, Zeichen oder Schrift ins Bild holen, und bei `umkehrwort-monolog` eine Bildmitte, die nicht als ruhige, sehr dunkle oder sehr helle Fläche bestellt ist.

**Schritte** (jeder einzeln mit `--nur`, ab einer Stelle mit `--ab`, einzelne Teile neu mit `--neu s3,stimme,musik`; Fertiges wird sonst übersprungen, eine Reparatur macht also nicht alles neu):
1. `szenen`: Plan prüfen (`pruefung/szenen_pruefung.json`).
2. `stimme`: Stimme erzeugen, mit Whisper gegenhören (Treffer mindestens 0,86, Anfang in der bestellten Sprache mit mindestens 0,9, sonst neuer Versuch, höchstens drei). Geschnitten wird am gemessenen Einsatz der Aufnahme (erste Stelle über −40 dBFS), nie an der Zeichenzeit des Dienstes, die bei manchen Stimmen hinter dem Anlaut liegt; 5 ms Einblendung. Erstes Wort auf Bild 0, Szenenanfänge auf Wortanfänge, das letzte Wort (die Pointe) steht mindestens 2,5 s, danach Name und Herkunft 2,8 s; die `dauer` der Bestellung ist eine Obergrenze, kein leerer Nachlauf. Musik besorgen. Ohne Stimme nur die Musik.
3. `bilder`: zwei Varianten je Szene, weißen Papierrand finden und beschneiden, die Variante mit dem besten Kontrast im Schriftband wählen (überstimmen mit `"wahl": 2` in der Szene), Bogen aller Varianten nach `pruefung/bilder_bogen.jpg`. **Den Bogen in voller Größe ansehen, bevor die Clips entstehen** (Schrift, Zeichen, Heikles, markentypische Formen).
4. `clips`: je Szene ein Clip in der Länge, die die Szene braucht (Bewegung aus dem Startbild, Kamera im Videomotor stehend; die langsame Fahrt von 5 % macht der Schnitt) oder eine Verwandlung mit Start- und Endbild; der Prompt bekommt die fließende Echtzeit-Bewegung angehängt (Falle Zeichentrick-Takt). Jede Datei wird auf Ruckeln gemessen, nicht grün heißt neuer Seed, höchstens zweimal; der beste Versuch bleibt, ein roter steht in `STAND.md`. Clips mit anderer Bildrate werden auf 24 interpoliert und gemeldet.
5. `lesbarkeit` (vor dem Render): misst an jeder Stelle, an der Schrift steht, das Bild darunter (aus dem Clip, der dort liegt, im geschätzten Schriftkasten). Maß ist die relative Luminanz nach WCAG 2.1 und das Kontrastverhältnis je Pixel: bei Differenzschrift zwischen dem Grund und seiner Umkehrung, bei fester Farbe zwischen Schriftfarbe und Grund mit dem dunklen Band. Gezählt wird der Anteil schwacher Pixel (Differenz unter 2:1, feste Farbe unter 3:1, das WCAG-Minimum für große Schrift) und bei Differenzschrift der Anteil im Mittelton-Fenster 0,35 bis 0,65 (Helligkeit nach Rec. 601), wo die Gegenfarbe fast dieselbe Farbe wird. Rot: mehr als 30 % schwach oder mehr als die Hälfte Mittelton. Gelb: mehr als 15 % schwach oder mehr als 25 % Mittelton. Geeicht an zwei Stücken, je Wort mit dem Auge am Handy verglichen: lesbare Wörter lagen bei höchstens 13 % schwachen Pixeln, schwache bei 20 bis 33 %; der Median-Kontrast trennte nicht, weil Komplementärfarben (Blau auf Brotbraun) über den Farbton tragen. Ergebnis je Wort oder je halbe Sekunde in `pruefung/lesbarkeit.json`.
6. `render`: Name und Herkunft auf die ruhigste Höhe des Schlussbilds (30 bis 50 %), Herkunftszeile in 0,45 der Wortgröße (darunter am Handy nicht lesbar), Props nach `render/props.json`, Material nach `bau/`, Mischung auf die echte Länge, Render mit 24 fps (KI-Bewegtbild) oder 30 fps (Code, eigene Bilder), Master über `handy.py --master`: Lautheit linear auf −14 LUFS mit Begrenzer, gemessen nach der AAC-Kodierung (True Peak höchstens −1, Ziel −1,5), Handy-Fassung mit dem Ton des Masters, Untertitel `.srt` bei Stimme und Lesetakt.
7. `pruefen`: Vorprüfung mit Handy-Fassung, Wortzeiten und Text-Protokoll, Abnahme gegen die Karte, Kontaktbogen, Storyboard (Bild 0, Mitte jeder Szene, Ende), 12-fps-Streifen an jedem Wechsel, `STAND.md` mit Messwerten und Checkliste. Danach der frische Prüfer auf Storyboard und Streifen, eine Reparatur (`--neu <szene>` und `--ab render`), dann der Mensch.
8. `liefern`: nur mit Adapter; lädt Handy-Fassung, Master und Kontaktbogen auf den eigenen Lieferweg und trägt die Links in `STAND.md` ein.

**Motoren (Adapter):** Welche Dienste Bilder, Clips, Stimme und Musik machen, steht nicht im Werkzeug. Eine Python-Datei, deren Pfad im Feld `motoren` steht (oder in der Umgebungsvariable `ZITAT_MOTOREN`), liefert diese Funktionen, alle optional:
- `bild(a) -> [pfade]`: `a` hat `id`, `prompt`, `breite`, `hoehe`, `anzahl`, `seed`, `ziel_ordner`; Dateien als `<szene>_v1.png`, `<szene>_v2.png` in den Zielordner.
- `clip(a) -> pfad`: `id`, `prompt`, `start` (Bild), `ende` (Bild oder leer), `dauer_s`, `breite`, `hoehe`, `seed`, `ziel_ordner`.
- `stimme(a) -> {"audio": pfad, "woerter": [{"w", "von", "bis"}], "pruefung"?}`: `id`, `text`, `sprache`, `kennung`, `tags`, `stabil`, `seed`, `vor`, `ziel_ordner`. Wortzeiten in Sekunden der Datei.
- `musik(a) -> pfad`: `id`, `prompt`, `sekunden`, `ziel`.
- `liefern(a) -> url`: `datei`.

Ohne Adapter gilt der **Handweg**: das Werkzeug schreibt jeden Auftrag mit Prompt, Seed und Zieldatei nach `auftraege_hand.md` und hält an; wer die Dateien unter diesen Namen ablegt (aus einem beliebigen Bild-, Video- oder Stimmen-Dienst), startet es erneut. Stimme und Musik übernimmt ohne Adapter ElevenLabs eingebaut (Schlüssel in der Umgebung); ohne Schlüssel ist die Musik Stille. Kosten entstehen nur in den Diensten, die der Adapter ruft; das Werkzeug selbst ruft keinen.

**Was kein Werkzeug entscheidet:** ob ein Bild etwas Heikles zeigt, ob die Abfolge als Abschied gelesen werden kann, ob die Stimme trägt. Die Checkliste in `STAND.md` lässt diese Punkte offen, bis ein Mensch oder der frische Prüfer sie gesehen hat.

## Zeichen-Motoren in einem Rutsch (`starter/werkzeuge/animskill.py`, seit 1.5)

Für die Familien `strichzeichnung`, `malstil`, `erklaergrammatik`, `selbstzeichnend` und die Karte `whiteboard-hand` zeichnet ein Motor jedes Bild in Code (kein Bild- oder Videodienst, gleiches Ergebnis bei jedem Render). Einrichten einmal je Rechner: `python -I starter/werkzeuge/animskills/einrichten.py --pruefen` (holt die Motoren auf festem Stand, Windows-Fixes inklusive; Einzelheiten `starter/werkzeuge/animskills/LIESMICH.md`).

| Motor | Was er kann | Rechenzeit je Filmsekunde | Ton aus Code |
|---|---|---|---|
| `huashu` | 53 Malstil-Rezepte (Höhlenwand bis Vaporwave) als Szenen-Code, 8 Erklär-Grammatiken als Clip aus JSON | Szenen 15 s, Grammatik 1,5 s | Musik und Geräusche |
| `anidoodle` | 32 Strich-Stile, zeichnet in Handreihenfolge, Federschrift mit Umlauten | 3,5 s | Musik und Geräusche |
| `handzeichnung` | Whiteboard, eine Hand zeichnet vor (Remotion `WhiteboardHand`, würfelbar) | siehe Karte | Geräusche |
| `manim` | Formeln, Geometrie, Graphen | 1,4 s | nein |
| `zeichnen` | 77 Malstile, ein Bild malt sich selbst | 11 s | nein |
| `pinsel` | Aquarell-Figur mit Stimmungen (Startfigur Klecks) | 25 s | nein |
| `jsanim` | Canvas-Szene mit Web-Audio in einer HTML-Datei | 2,7 s | Musik und Geräusche |
| `bilddienst` | Papiercollage aus Bild- und Videodienst (Credits, Handweg) | Dienst | nein |
| `kino3d` | 3D-Kino seit 1.6: Held im Kinolicht, vier Licht-Rezepte, Wörter im Raum (Karten der Familie 3d-objekt, Skill `kino3d`) | 5 bis 6 s auf starker Grafikkarte, Standbild 15 bis 20 s | Musik und Geräusche |

**Weg:**
1. Stil würfeln wie immer (`wuerfeln.py zug … --zweck erklaeren`). Beim ersten Mal braucht der Kanal seine Mischung (`wuerfeln.py mischung --haus haus`). Eine bestimmte Karte (auch eine Familie, die nicht in der Mischung liegt) bestellst du mit `--nur-karte <id>`; Palette und Werte würfelt der Zug trotzdem. Prüfe vor dem Bau, ob `haus/tabus.md` dem Kern der Karte widerspricht (etwa „keine Personen“ gegen eine Profilfigur), und frag dann den Menschen. Zieht der Zug eine Zeichen-Karte, steht in `stil.json` `bauweg: animskill`, der Motor, die Stil-Kennung und ein `motor_spec_entwurf` mit Palette und Schrift des Zugs.
2. `python -I starter/werkzeuge/animskill.py --vorlage <projektordner> --motor <motor>` legt `bestellung.json` und `stimme_zeilen.json` an. `motor_spec` aus dem Entwurf übernehmen, Sprechtext in `stimme_zeilen.json`.
3. `animskill.py <bestellung.json> --nur stimme`: Stimme mit Wortzeiten zuerst, die Länge ergibt sich aus der Stimme (`"dauer": "stimme"`).
4. Die Datei schreiben, die der Motor erwartet (Film, Szene, Skript oder Szenen-JSON; Beispiel im Docstring des Motor-Moduls). Szenenwechsel auf Wortanfänge legen (`ton/stimme_woerter.json`). Ein Film, ein Stil, eine Palette.
5. `animskill.py <bestellung.json> --nur look --zeiten 0,<mitte>,<ende>`: zwei bis vier Standbilder in Endgröße ansehen, Ja oder Nein (Look-Check). Bei `handzeichnung` gibt der Schritt die Warnungen des Zeitplans aus (Hand hinkt der Stimme nach, Zeichnen endet nach der Dauer); erst beheben, dann `--nur render`.
6. `animskill.py <bestellung.json> --ab ton`: Musik und Geräusche (Weg `code` aus dem Motor, sonst `elevenlabs` mit Prompt), Mischung nach Ton-Standard, Film mit Untertiteln (Komposition `SkillClip`), Master und Handy-Fassung über `handy.py` (Reinigung, Register), Vorprüfung, Kontaktbogen, `STAND.md`.
7. Frischer Prüfer auf Kontaktbogen und Streifen, eine Reparatur (`--neu render` oder `--neu ton`), dann der Mensch mit Auge und Ohr. Nach der Reparatur Bilder für Runde 2 in einen neuen Ordner legen (`storyboard_r2/`), im Projektordner wird nichts gelöscht. Nur Pausen oder Zeilenlagen ändern: `stimme.py --zeilen … --pruefen` ohne `--neu` nutzt die vorhandenen Aufnahmen (keine Kosten), `animskill.py --neu stimme` bestellt alle Zeilen neu.

**Akzent und Kontrast:** Zieht der Würfel einen hellen Akzent auf hellem Grund (unter 3:1), Zahlen und Schlagwörter in Tinte setzen und den Akzent nur für Flächen und Linien nehmen; Abweichung in `STAND.md` notieren.

**Fallen, die schon passiert sind:** Malstil-Szenen bewegen sich zu wenig (das Bewegungs-Tor von `huashu` meldet rot; je Szene eine schnelle Bewegung einplanen). Titel, die Buchstabe für Buchstabe erscheinen, zeigen halbe Wörter (bei `anidoodle` Option `wortweise`). Dünne Linien verschwinden am Handy (Mindeststrich setzen). Ein dumpfer Schlag am Ende stört (Endprüfung des Mischers). Bild 0 darf kein leeres Papier sein: bei `zeichnen` und `anidoodle` das Titelbild vorzeichnen oder die erste Szene mit stehendem Titel beginnen.
