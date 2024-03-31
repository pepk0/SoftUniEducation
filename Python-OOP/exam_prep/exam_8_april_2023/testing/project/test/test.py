from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):

    def setUp(self):
        self.player_one = TennisPlayer("peter", 20, 10.5)
        self.player_two = TennisPlayer("mira", 21, 15)
        self.player_three = TennisPlayer("ivan", 30, 5)

    def test_simple_init(self):
        self.assertEqual(self.player_one.name, "peter")
        self.assertEqual(self.player_one.age, 20)
        self.assertEqual(self.player_one.points, 10.5)
        self.assertEqual(self.player_one.wins, [])

    def test_name_setter(self):
        with self.assertRaises(ValueError) as er:
            self.player_one.name = "11"
        self.assertEqual(str(er.exception),
                         "Name should be more than 2 symbols!")

    def test_age_setter(self):
        with self.assertRaises(ValueError) as er:
            self.player_one.age = 1
        self.assertEqual(str(er.exception),
                         "Players must be at least 18 years of age!")

    def test_add_new_win_with_non_existing_tournament(self):
        result = self.player_one.add_new_win("test")
        self.assertEqual(self.player_one.wins, ["test"])
        self.assertIsNone(result)

    def test_ad_new_win_with_existing_tournament(self):
        self.player_one.wins.append("test")
        result = self.player_one.add_new_win("test")
        self.assertEqual(result,
                         "test has been already added to the list of wins!")
        self.assertEqual(self.player_one.wins, ["test"])

    def test_dunder_lt_method_with_someone_that_has_more_points(self):
        self.assertEqual(self.player_one < self.player_two,
                         'mira is a top seeded player '
                         'and he/she is better than peter')

    def test_dunder_lt_with_someone_that_has_less_points(self):
        self.assertEqual(self.player_one < self.player_three,
                         'peter is a better'
                         ' player than ivan')

    def test_dunder_str_method(self):
        self.assertEqual(str(self.player_one), f"Tennis Player: peter\n"
                                               f"Age: 20\n"
                                               f"Points: 10.5\n"
                                               f"Tournaments won: ")

    def test_dunder_str_method_with_wins(self):
        self.player_one.add_new_win("1")
        self.player_one.add_new_win("2")
        self.player_one.add_new_win("3")
        self.assertEqual(str(self.player_one), f"Tennis Player: peter\n"
                                               f"Age: 20\n"
                                               f"Points: 10.5\n"
                                               f"Tournaments won: 1, 2, 3")


if __name__ == '__main__':
    unittest.main()
