---
id: kante-im-studio
name: "Kante im Studio"
familie: 3d-objekt
kurz: "Ein Objekt frei vor einem weichen Lichtfleck auf dunklem Grund, ein Hauptlicht von vorn links gibt ihm Körper, zwei Kanten warm und kühl zeichnen den Umriss."
kern: [Objekt frei auf dunklem Grund ohne Zimmer, "weicher Lichtfleck auf der Hohlkehle hinter dem Objekt", "Hauptlicht von vorn links führt, zwei Kanten warm und kühl zeichnen nur den Umriss"]
energie: 2
format_quelle: "9:16"
laenge_s: [8, 20]
bauweg: animskill
animskill:
  motor: kino3d
  stil: "studio_kante"
  quelle: "src/kino/motor/licht.ts"
  schrift: [schmal, grotesk]
lizenz: "Eigener Code des Pakets (Paketlizenz); three.js, React Three Fiber MIT, postprocessing Zlib, Remotion nach LIZENZ.md Abschnitt 9; Schriften OFL"
sollwerte:        # keine Messung einer Vorlage: Zielwerte für den eigenen Render (Vorlage KARTE_VORLAGE_MOTOR.md)
  shot_median_s: 12
  schnitte_pro_s: 0.05
  ereignisse_pro_s: 0.7
  lufs: -14
  helligkeit: 0.36
  farbigkeit: 0.11
palette:
  grund: "#0A0A0B"
  text: "#F4F4F4"
  akzent: "#FFD0A0"
  licht: "#FFF1E2"
  blau: "#A8C4FF"
  wand: "#202124"
effekte: [3d-render, 3d-schrift, geringe-schaerfentiefe, orbit, push-in, glow, vignette, filmkorn, makro-material, untertitel, sprechstimme, geraeusche]
kamera: "Ein langsamer Bogen um das Objekt, Nahschuss über Material und Kante, zum Schluss ein Push-in auf die Pointe; fließend, nie über 6 Bilder Stillstand."
ton: "Helles, leises Bett aus Code (allein um −24 LUFS), Atmo Studio, wenige klare Geräusche (Schimmer, Klick, Whoosh), die Stimme trägt; gesamt −14 LUFS, Schluss mit hellem Akkord."
braucht: [nur-typo]
motor_aufwand: mittel
einsatz: [produkt, ganzes-kurzvideo, intro]
zweck: [produktwerbung, angebot, marke-image]
branchen_passt: [technik, mode-beauty, lebensmittel-feinkost, werkstatt-auto, handwerk]
branchen_nie: []
abnahme:
  shot_median_s: [5, 60]
  schnitte_pro_s: [0.0, 0.3]
  helligkeit: [0.2, 0.55]
  farbigkeit: [0.04, 0.22]
  lufs: [-15, -13]
# Würfel-Felder (Etappe 0 Bauplan Würfelstile, 31.10.2026; karten_wuerfelfelder.py, Familien-Standard)
creator: ja
spielraum:
  palette: nachbarn
  schrift: klasse
  blitzbild_bilder: [2, 4]
  stottern_wiederholungen: [2, 3]
  push_in_prozent: [2, 5]
  wackeln_faktor: [0.3, 0.7]
  korn: [0.0, 0.025]
  vignette: [0.3, 0.5]
  beat_versatz_16tel: [0, 1]
  textgroesse_prozent: [-10, 10]
  textlage: regel
  musik: bausteine
palettenrolle:
  grund: grund
  text: text
  akzent: akzent
  dunkel: grund
  hell: text
  licht: licht
quelle: Eigene Beschreibung des 3D-Kino-Motors des Pakets (Lizenz im Feld lizenz); keine Bilder, Figuren, Texte oder Marken Dritter übernommen.
---
# Kante im Studio

Ein Objekt steht frei auf dunklem Grund, kein Zimmer, kein Fenster. Hinter ihm liegt ein weicher Lichtfleck auf der Hohlkehle, so steht es als Kontur vor Helligkeit statt vor Leere. Ein weiches Hauptlicht von vorn links gibt ihm Körper, zwei Kanten, eine warm, eine kühl, ziehen die Umrisse nach. Ruhig und wertig wie ein Produktfoto, das sich bewegt; die Spannung liegt im Material und in der Fahrt um die Form.

## Kern
- Objekt frei auf dunklem Grund (`set.typ: studio`), gern auf einem Podest.
- Ein weicher Lichtfleck auf der Hohlkehle hinter dem Objekt (`hinten`: Strahler hinter dem Helden, 45 cd, Kegel 24°, Halbschatten 1); der Grund oben und an den Rändern bleibt dunkel.
- Rangfolge der Lichter: Hauptlicht 95 cd von vorn links (Halbschatten 0,9) führt, die Kanten (warm 48 cd hinten links, kühl 36 cd hinten rechts) liegen am Helden bei rund 40 % davon. Die Schattenseite hellt keine zweite Lampe auf, sondern eine helle Fläche rechts vorn in der Umgebung; sie bleibt deutlich dunkler als die Lichtseite.

Wer diese drei trifft, ist zu 80 % da; alles andere sind Regler.

## Erkennung
- **Bild:** 3D aus Code, dunkler Grund ohne Nebel mit hellem Fleck hinter dem Objekt, Volumen nur aus dem Hauptlicht (0,25). Farben: grund `#0A0A0B`, text `#F4F4F4`, akzent `#FFD0A0`, licht `#FFF1E2`, blau `#A8C4FF`, wand `#202124`.
- **Bewegung:** Bogen um das Objekt, Lichtkanten wandern über die Form; was sich am Objekt bewegt (Deckel, Flamme, Zeiger), bewegt sich auf den Wörtern der Stimme.
- **Ton:** Helles, leises Bett, Atmo Studio, wenige klare Geräusche, Stimme vorn.
- **Text:** Ein bis drei 3D-Wörter (Stil `messing` oder `glut`), Name oder Preis als Wort im Raum nur, wenn die Bestellung es will; dazu Untertitel.

## Bildtypen

| Bildtyp | Anteil | Komposition (Motivgröße in % der Bildhöhe, Lage, Grund) | Dauer typisch |
|---|---:|---|---|
| Bogen um das Objekt | 40 % | Objekt 40 bis 60 %, Mitte, Kanten sichtbar, Grund dunkel | 4 bis 7 s |
| Nahschuss über Material | 30 % | Oberfläche 70 bis 100 %, Kratzer, Rillen, Glanz | 3 bis 5 s |
| Push-in auf die Pointe | 20 % | Objekt 50 bis 70 %, Wort im Raum darüber | 2 bis 4 s |
| Wort im Raum | 10 % | ein 3D-Wort vor dem Objekt, mindestens 1,2 s sichtbar | 1,2 bis 3 s |

## Regler
Objekt und Podest, Grundfarbe (`set.farbe`, dunkel halten), Fleck hinten (`"licht": {"rezept": "studio_kante", "hinten": {"staerke": 30, "winkel": 20}}`, `"staerke": 0` schaltet ihn ab), Stärke und Farbe der Kanten über `licht.kanten` (unter dem Hauptlicht bleiben), Belichtung (`"post": {"belichtung": 0.85}`), Korn bis 0,025 (`"post": {"korn": 0.02}`), Kamerarezepte, Wörter. Glas als Held: Gegenlicht einschalten (`"gegenlicht": {"farbe": "#fff4e8", "staerke": 5, "pos": [0, 0.02, -0.8], "ziel": [0, 0.04, 0], "winkel": 7, "halbschatten": 0.8}`, Lage relativ zum Helden). Fest bleiben der dunkle Grund mit dem Fleck dahinter, die Rangfolge Hauptlicht vor Kanten und die zwei farbigen Kanten. Bei `produktwerbung` und `angebot` nimmt die Grundfarbe den Hausgrund und die 3D-Wörter den Hausakzent; das Licht bleibt das des Rezepts.

## Fallen
- Muster ist `beispiel/studio` (Vase auf Podest, Fleck hinten auf 65 cd, Kamera hoch und quer). Ein eigenes Objekt tauscht nur die zweite Requisite und `held`; Zimmer-Beiwerk (Pflanze, Bücher, Fenster) gehört nicht ins Studio.
- Ohne Fleck hinten steht das Objekt vor schwarzer Leere und verliert seine Kontur auf der Schattenseite. Fleck nicht abschalten, nur dämpfen; er braucht einen dunklen Grund, auf hellem Grund wirkt er flau.
- Kanten stärker als das Hauptlicht machen aus dem Objekt einen Scherenschnitt mit leuchtendem Rand. Erst eine graue Probe (`"motor_spec": {"aus": ["grau"]}`, jede Fläche einheitlich grau), dann mit Material: Lichtseite, Schattenseite und Fleck müssen im Grau klar zu trennen sein.
- Glas verschwindet vor dunklem Grund: Gegenlicht einschalten und mit `"aus": ["hauptlicht"]` prüfen, ob es ohne Hauptlicht lesbar bleibt. Schräg von oben und breit gesetzt (in der Probe 11° Kegel, von 13 cm über dem Helden) macht es einen grellen Fleck auf dem Podest vor dem Glas; flach in Höhe der Glasmitte und eng (7°) bleibt vorn nur ein weicher Schein. Teilwerte wie `{"staerke": 3}` reichen, die übrigen Felder kommen aus einer Vorgabe.
- Helle Metallflächen fressen aus: in der Probe war eine Alu-Kanne vorn fast weiß, die Kanten glühten im Bloom. Belichtung 0,8 bis 0,9 über `licht.post.belichtung`, Rauheit um 0,35 bis 0,4, und am Standbild prüfen.
- Glattes Metall braucht Metall: `metall: 1`, Rauheit um 0,3, sonst sieht es aus wie Gips.
- Ohne Fenster gibt es keine Lichtschächte; das Volumen kommt nur aus dem Schlüssellicht und bleibt schwach. Wer Schächte will, nimmt die Karte `lamellen-goldstunde`.
- Echte Produkte des Kunden sind hier nachgebaute 3D-Formen, keine Fotos: Form und Farbe gegen ein Foto des Produkts prüfen, Logos nur, wenn der Mensch es will.
- Harte Kanten an Eigenbauten fangen kein Licht: Kanten runden oder fasen (`RoundedBoxGeometry`, `kantenDrehkoerper` in `requisiten.tsx`), so dass in der Nahfahrt zwei bis vier Pixel Glanzlinie entstehen.
- Querformat: eigener Kamerablock `kamera_quer` in der Szene (fehlt er, gilt `kamera`) und je Wort `platz_quer`; Wortzone, Untertitelband und Vignette richten sich nach dem Seitenverhältnis. Layout-Check mit dem Format (`layout.mjs <szene.json> 1.777778`) und ein Standbild je Format.

## Ton
Code-Musik ist erlaubt, das Bett liegt leise (allein um −24 LUFS), Geräusche und Stimme tragen; gesamt −14 LUFS, True Peak −1 dBTP; kein dumpfer Schlag am Ende, der Schluss klingt hell. Gemischt wird mit `ton_standard.py`, der Motor liefert nur getrennte Stems. In der Szene: `"ton": {"bett": {"stimmung": "hell"}, "atmo": "studio", "schluss": "akkord_hell", "ereignisse": [{"t": "w2", "typ": "schimmer", "staerke": 0.5, "dauer": 1.4}]}`.

## Bauweg
3D-Kino-Motor `kino3d`, Licht-Rezept `studio_kante`, Quelle `src/kino/motor/licht.ts`. Kein Remotion-Bau im Starter: `wuerfeln.py zug` schreibt `bauweg: animskill` in `stil.json`, dazu `motor_spec_entwurf`.

```
python -I starter/werkzeuge/animskill.py --vorlage <projekt> --motor kino3d --format 9:16
python -I starter/werkzeuge/animskill.py <projekt>/bestellung.json
```

`motor_spec` (Felder im Kopf von `starter/werkzeuge/animskills/motoren/kino3d.py`):

```json
{"szene": "kino3d/szene.json", "licht": "studio_kante"}
```

## Abnahme
Sollwerte, keine Messung einer Vorlage: Shot-Median 5 bis 60 s, Schnitte je Sekunde 0,0 bis 0,3, Helligkeit 0,2 bis 0,55, Farbigkeit 0,04 bis 0,22, LUFS −15 bis −13 (`python -I starter/werkzeuge/abnahme.py <video> <karte.md>`). Helligkeit und Farbigkeit stammen aus einem Probe-Standbild. Vor dem Vollrender: graue Probe und Standbild mit Material an derselben Stelle, Layout-Check ohne blocker, drei Standbilder zeigen alle drei Kern-Merkmale (Fleck hinter dem Objekt sichtbar, Schattenseite dunkler als die Lichtseite, Kanten schmaler und schwächer als das Hauptlicht), keine Fläche des Objekts ist weiß ausgefressen. Der Layout-Check meldet außerdem (Stufe polish) zu kurze Lesezeit eines 3D-Worts (Grundzeit 0,5 s plus 0,3 s je Wort, ab Ende des Einflugs) und einen Helden unter 12 % oder über 85 % der Bildhöhe, als blocker Körper, die ineinander stecken, und eine Kamera, die durch einen Körper oder unter die Tischplatte fährt.
