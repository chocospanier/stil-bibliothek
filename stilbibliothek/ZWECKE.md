# Zwecke und Branchen

Feste Wörter für drei Felder jeder Karte (Kopfblock, nach `einsatz:`) und für `haus/look.md`. Der Würfel liest sie: `wuerfeln.py mischung` zieht nie eine Karte, deren `branchen_nie` die Branche des Kanals enthält, und bevorzugt Karten, deren `branchen_passt` und `zweck` zum Kanal passen; `wuerfeln.py zug --zweck <wert>` zieht nur Grundstile mit diesem Zweck.

- `zweck`: wofür der Look als Ganzes taugt (eins oder mehrere). Leer heißt: kein Zweck festgelegt.
- `branchen_passt`: Branchen, die mit diesem Look werben würden, ohne dass es fremd wirkt.
- `branchen_nie`: Branchen, für die der Look falsch wäre (ein Parfum-Look ist nie `werkstatt-auto`, ein Kinder-Look nie `finanzen`).
- Was in keiner der beiden Branchenlisten steht, ist neutral: der Würfel darf es ziehen, bevorzugt es aber nicht.

Geurteilt wird nach Kern, Bildtypen, Palette, Ton und Energie der Karte, wie ein Art Director: Würde diese Branche mit genau diesem Look werben? Andere Wörter als die unten stehenden prüft `werkzeuge/bibliothek_index.py` als Fehler.

## Zwecke (13)

| Wert | heißt |
|---|---|
| `produktwerbung` | ein Produkt zeigen und verkaufen: Packshot, Detail, Name, Marke |
| `angebot` | Preis, Aktion, Termin, „jetzt im Shop“: die Ansage steht im Vordergrund |
| `marke-image` | Haltung und Auftritt der Marke ohne ein bestimmtes Produkt |
| `erklaeren` | Ratgeber, Anleitung, Ablauf: Schritt für Schritt verstehen |
| `wissen` | Fakten, Wissenshäppchen, Hintergrund, Nachricht |
| `zitat` | ein Satz, ein Gedanke, ein Leitsatz, der stehen bleibt |
| `musik-lyric` | Musikvideo, Liedzeilen, Auftritt |
| `mode-lookbook` | Kleidung, Look, Outfit, Styling an einer Figur |
| `event-teaser` | Ankündigung, Eröffnung, Trailer, Countdown, Hook für etwas Kommendes |
| `geschichte` | Erzählung, Kurzfilm, Rückblick, Fallgeschichte |
| `kinder` | für Kinder gemacht oder kindgerecht verspielt |
| `person-vorstellen` | Inhaber, Team, Kanalgesicht, Held vorstellen |
| `stimmung` | Atmosphäre, Ort, Alltag, Erinnerung ohne Botschaft |

## Branchen (14)

| Wert | heißt |
|---|---|
| `werkstatt-auto` | Autowerkstatt, Teile, Zubehör, Tuning, Fahrzeughandel, Lackierer |
| `handwerk` | Handwerksbetrieb, Bau, Tischlerei, Elektro, Sanitär, Maler |
| `lebensmittel-feinkost` | Feinkost, Öl, Wein, Delikatessen, Hofladen, Lebensmittelmarke |
| `gastro` | Restaurant, Café, Bar, Lieferdienst |
| `mode-beauty` | Mode, Schmuck, Kosmetik, Friseur, Parfum |
| `technik` | Elektronik, Software, Apps, Geräte, IT |
| `gesundheit` | Praxis, Apotheke, Pflege, Therapie, Fitness mit Gesundheitsbezug |
| `bildung` | Schule, Kurs, Nachhilfe, Wissenskanal, Ratgeber |
| `musik-kultur` | Musik, Band, Club, Theater, Kunst, Festival |
| `immobilien` | Makler, Bauträger, Vermietung, Architektur |
| `finanzen` | Bank, Versicherung, Steuer, Beratung, Kanzlei |
| `sport` | Verein, Studio, Sportartikel, Athlet |
| `kinder-familie` | Spielzeug, Kita, Familienangebote |
| `tourismus` | Hotel, Ferienwohnung, Reiseziel, Ausflug |

## In `haus/look.md`

```
## Branche und Zwecke (aus stilbibliothek/ZWECKE.md)
- branche: werkstatt-auto
- zwecke: produktwerbung, angebot, erklaeren
```

Ein Wert für `branche`, ein bis vier für `zwecke` (die Hauptzwecke des Kanals). Fehlen beide Zeilen, würfelt der Würfel wie vor diesen Feldern.

## Markenfarben

Hat `look.md` Branche oder Zwecke, bekommt die Hausmischung neben `haus` und den zwei Nachbarn die Palette `marke`: Grund, Text, Akzent und Licht sind genau die Hausfarben, keine Farbe wird gedreht. Bei `--zweck produktwerbung` oder `--zweck angebot` ist `marke` Pflicht; der Zug variiert dann nur Schrift, Werte und Grundstil.
