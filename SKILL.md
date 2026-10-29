---
name: fra-pick-2-limited-draft
description: FRA Fractured Reality Pick 2 Limited Draft assistant and website. Use for FRA draft picks, sealed deck choices, removal, board wipes, sturdy creatures, mana-curve comparisons, pull likelihood, card lookup, or launching and maintaining the bundled Scryfall-powered FRA card finder.
version: "1.1.0"
author: Kurtis and SharpEdge
tags:
  - magic-the-gathering
  - mtg
  - fra
  - fractured-reality
  - pick-2
  - limited
  - draft
  - sealed
  - scryfall
---

# FRA Pick 2 Limited Draft

Use this skill as a practical draft-day assistant for the FRA set. “FRA,”
“Fractured Reality,” and the typo-friendly “Fraxtured Reality” all refer to
this same skill.

## Bundled app

The skill directory contains:

- `index.html` — mobile-friendly FRA card finder and limited scouting app
- `serve.py` — dependency-free local web server for the app
- `README.md` — short human usage guide

To launch the site, run this in the background:

```bash
python ~/.code_puppy/skills/fra-pick-2-limited-draft/serve.py --port 8780
```

Then give the user this exact local URL:

```text
http://127.0.0.1:8780/
```

If port 8780 is occupied, use another unprivileged port and report the URL.
Do not claim the site is running until the command has started successfully
and an HTTP request returns status 200.

## What the website does

The app loads all unique `set:fra` cards from the live Scryfall API and offers:

1. **Board wipes** grouped by rarity.
2. **Removal** with card speed shown as Instant, Sorcery, or ability.
3. **Toughness 4+** creatures and their relevant combat skills.
4. **Best value** rankings by color and mana value.
5. A responsive card-image gallery; each image opens Oracle text, rarity, mana cost, larger artwork, and a Scryfall link.

The bundled HTML is the source of truth for the app’s curated wipe/removal
lists and scoring implementation. Read it before changing classifications or
explaining the precise formula.

## Pick advice protocol

When comparing draft choices:

1. Ask for or inspect every visible candidate, the current pool, colors, mana
   curve, and pick/pack number when available.
2. Prefer reliable removal, efficient threats, card advantage, and flexible
   mana costs. Adjust for synergy only when the pool actually supports it.
3. Treat commons and uncommons as format foundations. Do not let a flashy rare
   automatically outrank a stronger on-color role-player.
4. In Pick 2 formats, account for both cards selected from the pack and explain
   whether the pair improves power, curve, interaction, or synergy.
5. State the recommended pair first, then provide a concise reason and the best
   fallback pair.
6. Separate facts from estimates. Scryfall provides card facts; the website’s
   Power, Pull, and Value grades are heuristics, not win-rate data.
7. Never invent exact booster odds, card collation, ALSA, GIH win rate, or format
   statistics. If verified data is unavailable, say so plainly.

## Maintenance rules

- Keep the app framework-free and usable as a single static HTML file.
- Preserve mobile behavior and accessibility labels.
- Use Scryfall’s paginated API politely; keep the delay between pages.
- Escape any new external data before inserting it with `innerHTML`.
- Validate JavaScript syntax after edits and smoke-test the served page.
- Keep claims narrow: this is a scouting and decision-support tool, not an
  automatic guarantee of draft outcomes. Cardboard remains delightfully rude.
