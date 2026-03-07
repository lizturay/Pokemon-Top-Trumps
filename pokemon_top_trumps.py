import random
import requests


# =============== CONSTANTS ===============

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/{}/"
WIN_POINTS = 100
DRAW_POINTS = 50
FIRST_GEN_LIMIT = 151

STAT_OPTIONS = ["height", "weight", "base experience", "hp", "attack", "defend"]


# =============== DATA FETCHING ===============

def fetch_random_pokemon() -> dict:
    """Fetches a random Gen 1 pokemon from the PokéAPI and returns its key stats."""
    pokemon_number = random.randint(1, FIRST_GEN_LIMIT)
    url = POKEAPI_URL.format(pokemon_number)

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Could not reach PokéAPI: {e}")
        raise

    pokemon = response.json()

    return {
        "name": pokemon["name"].capitalize(),
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "base experience": pokemon["base_experience"],
        "hp": pokemon["stats"][0]["base_stat"],
        "attack": pokemon["stats"][1]["base_stat"],
        "defend": pokemon["stats"][2]["base_stat"],
    }


# =============== DISPLAY ===============

def print_header(title: str):
    print("\n" + "=" * 50)
    print(f"  POKEMON TOP TRUMPS — {title}")
    print("=" * 50)


def show_pokemon_card(pokemon: dict):
    """Prints a pokemon's stats like a Top Trumps card."""
    print(f"\n  {pokemon['name'].upper()}")
    print(f"  {'—' * 30}")
    for stat in STAT_OPTIONS:
        print(f"  {stat.title():<20} {pokemon[stat]}")


def show_scores(my_score: int, opponent_score: int, limit: int):
    print(f"\n  Your score:     {my_score} / {limit}")
    print(f"  Opponent score: {opponent_score} / {limit}")


# =============== PLAYER INPUT ===============

def player_choose_stat() -> str:
    """Prompts the player to pick a stat."""
    print("\nChoose a stat:")
    for i, stat in enumerate(STAT_OPTIONS, start=1):
        print(f"  {i}. {stat.title()}")

    while True:
        raw = input("Enter number (1-6): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(STAT_OPTIONS):
            return STAT_OPTIONS[int(raw) - 1]
        print("Please enter a number between 1 and 6.")


def opponent_choose_stat() -> str:
    """Opponent picks a stat at random."""
    stat = random.choice(STAT_OPTIONS)
    print(f"\n  Opponent chose: {stat.title()}")
    return stat


# =============== GAME LOGIC ===============

def compare_stats(my_val: int, opponent_val: int) -> dict:
    """
    Compares two stat values and returns points for each player.
    Win = 100 pts, Draw = 50 pts each, Loss = 0 pts.
    """
    print(f"\n  Your stat:     {my_val}")
    print(f"  Opponent stat: {opponent_val}")

    if my_val > opponent_val:
        print("\n  You win this round!")
        return {"my_points": WIN_POINTS, "opponent_points": 0}
    elif my_val < opponent_val:
        print("\n  Opponent wins this round!")
        return {"my_points": 0, "opponent_points": WIN_POINTS}
    else:
        print("\n  It's a draw!")
        return {"my_points": DRAW_POINTS, "opponent_points": DRAW_POINTS}


def resolve_fight(stat: str, my_pokemon: dict, opponent_pokemon: dict) -> dict:
    """
    Handles attack vs defend logic.
    If attack is chosen, it competes against the opponent's defend stat (and vice versa).
    All other stats compare directly.
    """
    if stat == "attack":
        print(f"\n  {my_pokemon['name']} attacks {opponent_pokemon['name']}!")
        return compare_stats(my_pokemon["attack"], opponent_pokemon["defend"])
    elif stat == "defend":
        print(f"\n  {opponent_pokemon['name']} attacks {my_pokemon['name']}!")
        return compare_stats(my_pokemon["defend"], opponent_pokemon["attack"])
    else:
        return compare_stats(my_pokemon[stat], opponent_pokemon[stat])


def play_round(my_score: int, opponent_score: int) -> dict:
    """Plays one full round and returns updated scores."""
    print("\nFetching your Pokémon...")
    my_pokemon = fetch_random_pokemon()
    opponent_pokemon = fetch_random_pokemon()

    show_pokemon_card(my_pokemon)

    # Player or opponent picks the stat
    chooser = input("\nWho picks the stat? (me/opponent): ").strip().lower()
    if chooser == "me":
        stat = player_choose_stat()
    else:
        stat = opponent_choose_stat()

    print(f"\n  Opponent's Pokémon: {opponent_pokemon['name']}")

    result = resolve_fight(stat, my_pokemon, opponent_pokemon)

    my_score += result["my_points"]
    opponent_score += result["opponent_points"]

    return {"my_score": my_score, "opponent_score": opponent_score}


# =============== MAIN ===============

def main():
    print_header("WELCOME")
    print("""
  Rules:
  - Each round you get a random Gen 1 Pokemon
  - Pick a stat to battle with (or let the opponent choose)
  - Win a round = 100 pts | Draw = 50 pts | Loss = 0 pts
  - First to the target score wins!
    """)

    while True:
        raw = input("How many points to win? (e.g. 300): ").strip()
        if raw.isdigit() and int(raw) > 0:
            limit = int(raw)
            break
        print("Please enter a positive number.")

    my_score = 0
    opponent_score = 0

    while True:
        print_header("NEW ROUND")
        show_scores(my_score, opponent_score, limit)

        scores = play_round(my_score, opponent_score)
        my_score = scores["my_score"]
        opponent_score = scores["opponent_score"]

        show_scores(my_score, opponent_score, limit)

        if my_score >= limit or opponent_score >= limit:
            break

        input("\nPress Enter for next round...")

    # Final result
    print_header("GAME OVER")
    show_scores(my_score, opponent_score, limit)

    if my_score > opponent_score:
        print("\n  YOU WIN! Congratulations!")
    elif opponent_score > my_score:
        print("\n  OPPONENT WINS! Better luck next time.")
    else:
        print("\n  IT'S A TIE!")


if __name__ == "__main__":
    main()