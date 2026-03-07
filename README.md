# Pokémon Top Trumps 🎴

A terminal-based Top Trumps card game using real Pokémon data pulled live from the [PokéAPI](https://pokeapi.co/). Built in Python.

---

## Live Demo
▶️ [Play it on Replit](https://replit.com/@lizturay/PokemonTrump)

---

## How to play

Each round, you and the opponent are dealt a random Gen 1 Pokémon. You pick a stat to battle with (or let the opponent choose). Whoever has the higher stat wins the round.

**Scoring:** Win = 100 pts | Draw = 50 pts each | Loss = 0 pts

First player to reach the target score wins!

---

## Stats available

- Height
- Weight
- Base Experience
- HP
- Attack (competes against opponent's Defend)
- Defend (competes against opponent's Attack)

---

## Getting started

**Requirements:** Python 3.7+ and the `requests` library.

```bash
pip install requests
python pokemon_top_trumps.py
```

**Run the tests:**

```bash
python -m unittest test_pokemon_top_trumps.py -v
```

---

## Project structure

```
pokemon-top-trumps/
├── pokemon_top_trumps.py       # Main game
├── test_pokemon_top_trumps.py  # Unit tests
├── README.md                   # This file
└── .gitignore
```

---

## What it demonstrates

- Calling a real external REST API (PokéAPI) and handling JSON responses
- Error handling for network requests
- Clean function-based structure with no global variables
- Unit testing with Python's built-in `unittest`

---

## Original version

This is a refactored version of a project originally built on [Replit](https://replit.com/@lizturay/PokemonTrump).