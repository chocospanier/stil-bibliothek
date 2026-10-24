# Glossar

Die Begriffe, die in Karten, Fehlerkatalog und Prüfer-Definition vorkommen. Kurz, in der Bedeutung, die dieses Paket meint.

| Begriff | Bedeutung |
|---|---|
| **Familie** | Eine Gruppe von Stilen mit gleicher Wirkung und gleichen Reglern (zum Beispiel noir, lookbook, musikvideo). 19 Familien, Einstieg über `FAMILIEN.md`. |
| **Karte** | Eine Datei je Stil: Kopfblock (YAML, maschinenlesbar) plus Text mit Erkennung, Bildtypen, Dramaturgie, Schnittmuster, Rezept, Material, Reglern, Abnahme und Fallen. |
| **Kern** | Die drei Merkmale einer Karte, ohne die es nicht der Stil ist. Nicht verhandelbar. |
| **Regler** | Alles an einem Stil, das sich ändern lässt, ohne dass er kippt (Farbe, Tempo, Figurenzahl, Textanteil). |
| **Energie** | Grobmaß der Wucht eines Stils, 1 ruhig bis 5 rasant. |
| **Sechzehntel** | Ein Sechzehntel eines Taktes bei 4/4; die Einheit der Schnittmuster. Bei 120 BPM sind das 0,125 s. Immer vom gemessenen Tempo des fertigen Tons ableiten, nie vom Prompt. |
| **Schnittmuster** | Die Folge der Shot-Längen in Sechzehnteln, gemessen an der Vorlage, als Bauplan für ein eigenes Stück. Inhalt austauschbar, Rhythmus bleibt. |
| **Shot-Median** | Die mittlere Länge einer Einstellung in Sekunden (Median, nicht Durchschnitt). |
| **Schnitte je Sekunde** | Schnittdichte; `schnitte_verlauf` gibt sie je Drittel des Videos an (Anfang, Mitte, Ende). |
| **Schnitt auf Beat** | Wie stark die Schnitte am Taktraster liegen: niedrig, mittel, hoch. |
| **Bildtyp** | Eine Art von Einstellung mit Motivgröße (in % der Bildhöhe), Lage und Grund. |
| **Hook** | Die ersten 0 bis 2 Sekunden; entscheidet, ob jemand bleibt. |
| **Aufbau, Atem, Schlag, Halt** | Die vier Stationen eines Höhepunkts: Spannung aufbauen, kurz Luft holen (Stille oder Leere), der Treffer, dann ein Moment, in dem das Bild stehen darf. |
| **Pointe** | Der Satz oder das Bild, auf das alles zuläuft. Braucht Tonpause davor (mindestens 0,4 s), mindestens 2,3 s Lesezeit und oft ein Etikett im Bild. |
| **Freeze** | Ein Standbild über 1 Sekunde. Verboten; Halt lebt mit Heranfahren, Glanzlicht, Lidschlag. |
| **Bild 0** | Das erste Bild des Videos, zugleich Titelbild der Plattform: Endgröße, nichts angeschnitten, Hauptmotiv mindestens 30 % der Höhe. |
| **Schutzzone** | Flächen, die frei bleiben: unten 15 % (Knöpfe der Plattformen), 40 px Rand für Schrift auch im extremsten Bewegungsbild. |
| **Überschwinger** | Eine Bewegung, die über das Ziel hinausgeht und zurückfedert (Easing). Ihre Extremwerte müssen durchgerechnet werden, sonst wird Schrift am Rand abgeschnitten. |
| **Wackeln** | Verschieben des ganzen Bildes als Effekt. Braucht einen überskalierten Grund (Faktor 1 + 2,2 × Amplitude / Breite), sonst entstehen dunkle Randstreifen. |
| **Blitzregel** | Höchstens 3 harte Hell-Dunkel-Wechsel je Sekunde, gemessen auf linearer Helligkeit; Farbblitze zählen mit. Schutz vor Unruhe und photosensitiven Reaktionen. |
| **Streifen** | Ein Bild aus 12 Einzelbildern je Sekunde eines Zeitfensters. Bewegung lässt sich nur so prüfen, nie am Einzelbild. |
| **Kontaktbogen** | Viele kleine Standbilder (ein Bild je Shot oder je Takt) auf einer Seite. |
| **Storyboard** | Ein Standbild je Beat in voller Größe, vor dem Vollrender. Der Prüfer sieht das Storyboard, nicht den fertigen Film. |
| **Frischer Prüfer** | Ein zweites Modell oder ein zweiter Mensch, der das Stück nicht gebaut hat und nichts zu verteidigen hat. Schreibt `pruefung_r<n>.json`. |
| **Blocker, Polish** | Die zwei Schweregrade eines Befunds. Blocker fällt beim normalen Sehen auf und blockiert den Render; Polish ist nur gezoomt sichtbar oder Geschmack. |
| **Reparaturrunde** | Genau eine je Werk: Blocker beheben, Vorher-Nachher-Ausschnitte ablegen, Prüfer sieht die Reparatur. |
| **Abnahme-Werte** | Zielbereiche im Kopfblock (`abnahme`), gegen die der eigene Render gemessen wird: Shot-Median, Schnitte je Sekunde, Helligkeit, Farbigkeit, LUFS. Messen mit `starter/werkzeuge/abnahme.py` (✓ oder ✗ je Wert). |
| **Helligkeit, Kontrast, Farbigkeit** | Helligkeit = Mittel der Luma (0,299 R + 0,587 G + 0,114 B) auf 0 bis 1, Kontrast = deren Streuung; Farbigkeit = colourfulness nach Hasler und Süsstrunk (Streuung und Mittel der Gegenfarben R−G und (R+G)/2−B), geteilt durch 255. Je Shot aus 3 bis 10 Bildern gemessen, über das Video nach Shot-Länge gewichtet. Nicht die HSV-Sättigung, die `video_schauen.py` in der Kurve zeigt. |
| **LUFS, True Peak** | Lautheit (Ziel −14 LUFS für Plattformen) und Spitzenpegel (höchstens −1 dBTP). Beide Fassungen messen, Master und Handy. |
| **Handy-Fassung** | Die Ausspielung fürs Telefon. Übernimmt den Ton des Masters unverändert (`-c:a copy`). |
| **Freisteller** | Eine Figur oder ein Gegenstand ohne Hintergrund. Auf weiße Inseln (eingeschlossene Reste) und Schattenreste prüfen. |
| **Avatar-Kanon** | Die Regeln für jede gezeichnete oder freigestellte Figur: nur verschieben, gleichmäßig skalieren, leicht drehen; nie strecken, stauchen, scheren, invertieren, filtern. |
| **Material-Abnahme** | Jedes generierte Bild vor dem Einbau in voller Größe ansehen: Schlingen, Seile, Haken, Waffen, Flaggen, Logos, markentypische Formen, Pseudo-Schrift. |
| **Lesart** | Was ein Zuschauer in der Abfolge sehen kann, auch wenn jedes einzelne Bild sauber ist (Abschied, Jenseits, Politik, Marke). Nach dem Storyboard immer einmal als Geschichte lesen. |
| **Effekt-Kennung** | Ein fester Name für eine Technik (`harter-schnitt`, `blitzbild`, `push-in`, `duoton`), Liste in `EFFEKT_VOKABULAR.md`; neue Kennungen als `neu:kennung`. |
| **Motor** | Das Programm, das aus Code Bilder rendert: Remotion, Canvas, SVG, After Effects, Blender. Eine Karte beschreibt, der Motor baut. |
| **Baustein** | Ein wiederverwendbares Element im Motor (Blitzbild, Stottern, Wischer, Bauchbinde, Zahl-Walze). Rund 28 Bausteine tragen fast alle Stile; der Starter liefert sie für Remotion (`starter/src/bausteine/`, Liste in `starter/BAUSTEINE.md`). |
