# 🎴 Pokémon Top Trumps (Python)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/lizturay/pokemon-top-trumps?style=social)]()

A command-line card battle game inspired by the classic *Top Trumps*.  
Built using the **PokéAPI**, this project lets players draw random Pokémon and compete based on real in-game stats such as HP, Attack, and Defence.

---

## Live Demo
*(Runs locally via Python — see installation instructions below)*

---

## Overview
This project was created as part of my learning journey in **Python**, **APIs**, and **game logic design**.  
It uses live data from the PokéAPI to generate random Pokémon battles and award points based on stat comparisons.

> *Goal:* Be the first to reach your chosen score limit. Win rounds to earn 100 points, draw to earn 50.

---

## Features
- Fetches **real Pokémon stats** from the PokéAPI  
- Play as the user or let the CPU choose the stat  
- Options to **attack**, **defend**, or compare specific stats (HP, Attack, etc.)  
- Adjustable **score limit** for flexible gameplay  
- Handles **API errors and invalid inputs** gracefully  
- Clear game loop and score tracking  

---

## Project Purpose
I built this to strengthen my understanding of:
- RESTful API interaction using `requests`  
- Input handling and validation in CLI applications  
- Writing modular, readable Python functions  
- Implementing basic game logic and scoring systems  

---

## Tech Stack
| Category | Tools |
|-----------|-------|
| **Language** | Python 3 |
| **Libraries** | `requests`, `random` |
| **Data Source** | [PokéAPI](https://pokeapi.co/) |
| **Environment** | Command-line / Terminal |

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/lizturay/pokemon-top-trumps.git
cd pokemon-top-trumps
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
pip install -r requirements.txt
````

### 🧠 Run the Game

```bash
python pokemon_top_trumps.py
```

### 📦 Requirements File

Create a simple `requirements.txt`:

```
requests>=2.31.0
```

---

## 🕹️ How to Play

1. Enter your target score (e.g. 300).
2. Each round, both you and the CPU draw a random Pokémon.
3. Choose who picks the stat — you or your opponent.
4. If you select **attack**, your Attack vs. their Defence.
5. If you select **defense**, your Defence vs. their Attack.
6. Winning round = **+100 points**, Draw = **+50 points**.
7. First to reach the score limit wins the game!

---

## 🎮 Example Gameplay Preview

```
Game to how many points? 300

You drew: Pikachu  vs  Opponent drew: Bulbasaur
Choose the stat yourself or let opponent choose? me
Pick a stat ['id', 'height', 'weight', 'base_experience', 'hp', 'attack', 'defense'] or type 'attack'/'defense':
attack
Stat choice is: attack
Pikachu attacks Bulbasaur
Your attack: 55  |  Opponent defense: 49
You win this round.
Score — You: 100 | Opponent: 0
```

---

## Challenges & Lessons Learned

* Managing asynchronous API calls in a synchronous CLI environment
* Handling errors gracefully when the PokéAPI times out
* Ensuring clean variable scope (no globals) for long-term maintainability
* Structuring Python scripts for readability and reuse
