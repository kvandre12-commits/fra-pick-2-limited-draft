# FRA Pick 2 Limited Draft

A mobile-friendly FRA Limited scouting website and portable Code Puppy skill.
It loads the current `set:fra` card gallery from Scryfall and organizes useful
information for Pick 2 draft and sealed-deck decisions.

**Use the live site:** <https://kvandre12-commits.github.io/fra-pick-2-limited-draft/>

## Features

- Board wipes and targeted removal grouped by rarity
- Removal speed identified as Instant, Sorcery, or ability
- Creatures with toughness 4+ and relevant combat abilities
- Heuristic Best Value rankings by color and mana value
- Responsive card-image tiles that open the full detail view
- Search, Oracle text, larger artwork, mana costs, and Scryfall links
- Framework-free static HTML that works on mobile

Power, Pull, and Value grades are transparent scouting heuristics—not game
win-rate data or exact booster probabilities.

## Use the website locally

```bash
git clone https://github.com/kvandre12-commits/fra-pick-2-limited-draft.git
cd fra-pick-2-limited-draft
python serve.py --port 8780
```

Open <http://127.0.0.1:8780/> and stop the server with `Ctrl+C`.

## Install as a Code Puppy skill

```bash
mkdir -p ~/.code_puppy/skills
git clone https://github.com/kvandre12-commits/fra-pick-2-limited-draft.git \
  ~/.code_puppy/skills/fra-pick-2-limited-draft
```

Then ask Code Puppy to activate `fra-pick-2-limited-draft`, or ask about FRA
draft picks, removal, board wipes, sealed pools, mana curves, or the website.

## Data and methodology

Scryfall supplies live card facts, images, and links. Curated classifications
and the scoring implementation live in `index.html`. The app deliberately does
not invent exact pack collation, pull odds, ALSA, or win-rate statistics.

An internet connection is required to load the card gallery and images.

## License and acknowledgements

The source code is available under the [MIT License](LICENSE).

Card data and images are provided through [Scryfall](https://scryfall.com/).
This project is unofficial Fan Content and is not approved or endorsed by
Wizards of the Coast. Portions of the materials used are property of Wizards
of the Coast. © Wizards of the Coast LLC.
