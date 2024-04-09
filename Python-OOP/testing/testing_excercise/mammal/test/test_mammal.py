import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal(
            "Mira",
            "lion",
            "test_sound",

        )

    def test_simple_init_test(self):
        self.assertEqual(self.mammal.name, "Mira")
        self.assertEqual(self.mammal.type, "lion")
        self.assertEqual(self.mammal.sound, "test_sound")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound_method(self):
        expected = "Mira makes test_sound"
        self.assertEqual(self.mammal.make_sound(), expected)

    def test_info_method(self):
        expected = "Mira is of type lion"
        self.assertEqual(self.mammal.info(), expected)


if __name__ == '__main__':
    unittest.main()
