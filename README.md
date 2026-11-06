# Style Library: 289 short-video styles for code engines

**289 video styles in 24 families, written down precisely enough that a person or an AI agent can rebuild them in code.** Remotion, Canvas, SVG, After Effects, Blender: the cards do not care which engine you use. Version 1.6.3.

Every card tells you what makes a look work, in numbers:

- **cut rhythm** in sixteenth notes, shot length, cuts per second
- **palette** with roles (ground, paper, accent) as hex values
- **typography**, camera, image treatment, sound
- **a build recipe** for a code engine, material prompts for your own images
- **acceptance values** you can measure against your render
- **pitfalls** that actually happened while building, and the fix for each

This repository is the **free half** of the library. It is licensed under [CC BY 4.0](LICENSE): use it, translate it, build on it, also commercially, as long as you give credit.

## Two kinds of cards

- **115 measured cards** in 20 families (noir, lookbook, music video, glitch, photocopier, kinetic type, product spot and more). Each one comes from measuring a publicly available preview video.
- **174 drawing-engine cards** in four families (`strichzeichnung`, `malstil`, `erklaergrammatik`, `selbstzeichnend`): line drawing, painting styles, explainer grammars and pictures that draw themselves. They are written from the style files of open drawing engines that paint every frame in code, so they carry target values instead of measurements.

## What is in here

| Folder / file | What it is |
|---|---|
| [`stilbibliothek/`](stilbibliothek/LIESMICH.md) | 289 style cards (one Markdown file per style, machine-readable front matter), 24 families, an effect vocabulary, `index.json` for filtering, and `SKILL.md`, the instructions for an AI agent |
| [`stilbibliothek/katalog/KATALOG.html`](stilbibliothek/katalog/KATALOG.html) | A visual catalogue with three stills per card (hook, middle, punch), at the moment for 106 measured cards; stills for the newer cards follow with the next version. Open it in a browser |
| [`pruefen/FEHLERKATALOG.md`](pruefen/FEHLERKATALOG.md) | The error catalogue: the root causes behind the mistakes of the pieces built so far, with a checklist to run before every render |
| [`ABLAUF.md`](ABLAUF.md) | The build process from choosing a style to acceptance |
| [`GLOSSAR.md`](GLOSSAR.md) | The terms used on the cards (sixteenths, flash rule, safe zone, frame 0, hold, punchline) |
| [`vorlagen/`](vorlagen/HAUSSTIL_VORLAGE.md), [`haus/`](haus/LIESMICH.md) | Templates for your own house style and channel, with a filled-in example |
| [`werkzeuge/bibliothek_index.py`](werkzeuge/LIESMICH.md) | Card filter: validates the cards, rebuilds the index, filters by any field |
| [`CLAUDE.md`](CLAUDE.md) | Working instructions for an AI agent (Claude Code or similar) that builds with the library |

## Start here

1. Open `stilbibliothek/katalog/KATALOG.html` and pick a look you like, or browse `stilbibliothek/FAMILIEN.md` by effect and use.
2. Read that card in `stilbibliothek/karten/`. The three `kern` traits are not negotiable; everything else is a dial.
3. Follow the section "Rezept für einen Code-Motor": ground, image treatment, building blocks, typography, motion, formats.
4. Filter cards from the command line (needs PyYAML):
   ```bash
   python -I werkzeuge/bibliothek_index.py --bib stilbibliothek --filter braucht=nur-typo motor_aufwand=klein
   ```
5. Before you render, run the checklist in `pruefen/FEHLERKATALOG.md`. The whole process is in `ABLAUF.md`.

Working with an AI agent? Hand it `stilbibliothek/SKILL.md` and `CLAUDE.md` as instructions.

**Language:** the cards and guides are written in German. They are structured and numeric enough that an AI agent reads them fine in any language.

## The toolkit (paid add-on)

A card describes a look; it does not build one. The first build of a style is the slow one, because you invent the flash frame, the stutter and the wipe from scratch. The **toolkit** removes that step:

- a **Remotion starter** with 28 building blocks plus a sound-track block, 24 helpers (beat grid from audio, storyboard, acceptance check, phone version, music and voice, house sound standard) and 114 worked examples in 9:16 and 16:9
- **ten engines** behind one entry point: eight draw every frame in code (painting styles, pen strokes, a whiteboard with a drawing hand, formulas, a watercolour character, canvas scenes, a picture that paints itself, 3D cinema), plus a recipe for image and video services and a set of motion rules
- the **checker system**: a fresh-reviewer role for a second model, an automatic pre-check of every frame, acceptance measurement against the card
- **measurement tools** for cuts, contact sheets, loudness and tempo

The paths in `ABLAUF.md` and `CLAUDE.md` (`starter/`, `werkzeuge/vorpruefung.py`, `pruefen/PRUEFER.md` and so on) point into the toolkit. Without it, every step still works by hand or with your own tools. With it, one command drops the toolkit into this folder and every card becomes a build you can run.

**Get the toolkit: https://content-autopilot.de**

## Where the styles come from

The measured cards are based on measuring a publicly available preview video (cut detection, optical flow, dominant colours, loudness, tempo) and on reading contact sheets. Only the look is described: rhythm, image treatment, composition, typography, sound. The cards contain no motifs, characters, brands, texts or images from those sources. The drawing-engine cards describe styles of open engines released under MIT or Apache 2.0. The catalogue stills were rendered with the starter; the people in them are AI-generated from each card's own material prompt.

## Licence and credit

Text, cards, catalogue images and the card filter: [Creative Commons Attribution 4.0 International](LICENSE).
Credit line: **"Style Library by David Jiménez Pérez, content-autopilot.de, CC BY 4.0"**. The toolkit is not part of this repository and not covered by this licence.

---

## Deutsch, kurz

Die **freie Hälfte** der Stil-Bibliothek, Fassung 1.6.3: 289 Stil-Karten in 24 Familien (115 gemessene Karten und 174 Karten der Zeichen-Motoren), Stil-Katalog, Effekt-Vokabular, Kartenfilter, Bauablauf, Glossar, Fehlerkatalog und Vorlagen. Lizenz: Creative Commons Namensnennung 4.0 ([LICENSE](LICENSE), Namensnennung in [NOTICE.md](NOTICE.md), deutsche Fassung in [LIZENZ.md](LIZENZ.md)). Einstieg: `stilbibliothek/katalog/KATALOG.html` oder `stilbibliothek/FAMILIEN.md`, dann eine Karte, dann `ABLAUF.md`. Für KI-Agenten: `stilbibliothek/SKILL.md`. Gesamtübersicht beider Hälften: `UEBERSICHT_GESAMTPAKET.md`.

Der **Werkzeugkasten** (Remotion-Starter mit 28 Bausteinen, zehn Motoren, Prüf-System, Messwerkzeuge) ist ein bezahlter Zusatz und wird mit einem Befehl in diesen Ordner gelegt: https://content-autopilot.de
