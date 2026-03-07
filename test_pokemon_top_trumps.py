import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokemon_top_trumps import compare_stats, resolve_fight, STAT_OPTIONS


class TestCompareStats(unittest.TestCase):

    def test_player_wins(self):
        result = compare_stats(80, 50)
        self.assertEqual(result["my_points"], 100)
        self.assertEqual(result["opponent_points"], 0)

    def test_opponent_wins(self):
        result = compare_stats(30, 90)
        self.assertEqual(result["my_points"], 0)
        self.assertEqual(result["opponent_points"], 100)

    def test_draw(self):
        result = compare_stats(60, 60)
        self.assertEqual(result["my_points"], 50)
        self.assertEqual(result["opponent_points"], 50)


class TestResolveFight(unittest.TestCase):

    def setUp(self):
        self.my_pokemon = {
            "name": "Charmander",
            "height": 6, "weight": 85,
            "base experience": 62,
            "hp": 39, "attack": 52, "defend": 43
        }
        self.opponent_pokemon = {
            "name": "Squirtle",
            "height": 5, "weight": 90,
            "base experience": 63,
            "hp": 44, "attack": 48, "defend": 65
        }

    def test_attack_vs_defend(self):
        # my attack (52) vs opponent defend (65) — opponent should win
        result = resolve_fight("attack", self.my_pokemon, self.opponent_pokemon)
        self.assertEqual(result["my_points"], 0)
        self.assertEqual(result["opponent_points"], 100)

    def test_defend_vs_attack(self):
        # my defend (43) vs opponent attack (48) — opponent should win
        result = resolve_fight("defend", self.my_pokemon, self.opponent_pokemon)
        self.assertEqual(result["my_points"], 0)
        self.assertEqual(result["opponent_points"], 100)

    def test_hp_direct_compare(self):
        # my hp (39) vs opponent hp (44) — opponent should win
        result = resolve_fight("hp", self.my_pokemon, self.opponent_pokemon)
        self.assertEqual(result["my_points"], 0)
        self.assertEqual(result["opponent_points"], 100)

    def test_weight_direct_compare(self):
        # my weight (85) vs opponent weight (90) — opponent should win
        result = resolve_fight("weight", self.my_pokemon, self.opponent_pokemon)
        self.assertEqual(result["my_points"], 0)
        self.assertEqual(result["opponent_points"], 100)


class TestStatOptions(unittest.TestCase):

    def test_all_expected_stats_present(self):
        for stat in ["height", "weight", "base experience", "hp", "attack", "defend"]:
            self.assertIn(stat, STAT_OPTIONS)


if __name__ == "__main__":
    unittest.main()