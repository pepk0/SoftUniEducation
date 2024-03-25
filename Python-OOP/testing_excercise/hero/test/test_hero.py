import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero_one = Hero("hero_one", 10, 15.5, 6.5)
        self.hero_two = Hero("hero_two", 6, 20.5, 5.5)ч

    def test_correct_init(self):
        self.assertEqual(self.hero_one.username, "hero_one")
        self.assertEqual(self.hero_one.level, 10)
        self.assertEqual(self.hero_one.health, 15.5)
        self.assertEqual(self.hero_one.damage, 6.5)

    def test_battle_with_yourself(self):
        with self.assertRaises(Exception) as same_name:
            self.hero_one.battle(self.hero_one)

        self.assertEqual(str(same_name.exception), "You cannot fight yourself")

    def test_battle_with_zero_or_less_health(self):
        self.hero_one.health = 0
        with self.assertRaises(ValueError) as zero_health:
            self.hero_one.battle(self.hero_two)

        self.hero_one.health = -1
        with self.assertRaises(ValueError) as negative_health:
            self.hero_one.battle(self.hero_two)

        self.assertEqual(str(zero_health.exception),
                         "Your health is lower than or "
                         "equal to 0. You need to rest")
        self.assertEqual(str(negative_health.exception),
                         "Your health is lower than or "
                         "equal to 0. You need to rest")

    def test_battle_enemy_with_zero_or_less_health(self):
        self.hero_two.health = 0
        with self.assertRaises(ValueError) as zero_health:
            self.hero_one.battle(self.hero_two)

        self.hero_two.health = -1
        with self.assertRaises(ValueError) as negative_health:
            self.hero_one.battle(self.hero_two)

        self.assertEqual(str(zero_health.exception),
                         f"You cannot fight hero_two. He needs to rest")
        self.assertEqual(str(negative_health.exception),
                         f"You cannot fight hero_two. He needs to rest")

    def test_battle_method_draw(self):
        self.hero_one.health, self.hero_two.health = 1, 1

        expected = "Draw"
        result = self.hero_one.battle(self.hero_two)
        self.assertEqual(expected, result)

    def test_battle_method_win(self):
        self.hero_one.health, self.hero_two.health = 1000, 1
        expected = "You win"

        enemy_hero_damage = self.hero_two.damage * self.hero_two.level

        expected_level = self.hero_one.level + 1
        expected_health = self.hero_one.health - enemy_hero_damage + 5
        expected_damage = self.hero_one.damage + 5
        result = self.hero_one.battle(self.hero_two)

        self.assertEqual(expected, result)
        self.assertEqual(expected_level, self.hero_one.level)
        self.assertEqual(expected_health, self.hero_one.health)
        self.assertEqual(expected_damage, self.hero_one.damage)

    def test_battle_method_lose(self):
        self.hero_one.health, self.hero_two.health = 1, 1000
        expected = "You lose"

        enemy_hero_damage = self.hero_one.damage * self.hero_one.level

        expected_level = self.hero_two.level + 1
        expected_health = self.hero_two.health - enemy_hero_damage + 5
        expected_damage = self.hero_two.damage + 5
        result = self.hero_one.battle(self.hero_two)

        self.assertEqual(expected, result)
        self.assertEqual(expected_level, self.hero_two.level)
        self.assertEqual(expected_health, self.hero_two.health)
        self.assertEqual(expected_damage, self.hero_two.damage)

    def test_hero_class_string_method(self):
        expected = (f"Hero hero_one: 10 lvl"
                    f"\nHealth: 15.5\n"
                    f"Damage: 6.5\n")

        self.assertEqual(expected, str(self.hero_one))


if __name__ == '__main__':
    unittest.main()
