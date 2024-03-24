import unittest
# from cat import Cat


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Mira")

    def test_correct_init_method(self):
        self.assertEqual(self.cat.name, "Mira")
        self.assertEqual(self.cat.fed, False)
        self.assertEqual(self.cat.sleepy, False)
        self.assertEqual(self.cat.size, 0)

    def test_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_error_if_cat_is_feed_and_we_feed_it(self):
        self.cat.eat()
        with self.assertRaises(Exception) as feed_exception:
            self.cat.eat()

        self.assertEqual(str(feed_exception.exception), "Already fed.")

    def test_error_if_cat_can_sleep_hungry(self):
        with self.assertRaises(Exception) as hungry_exception:
            self.cat.sleep()

        self.assertEqual(str(hungry_exception.exception),
                         "Cannot sleep while hungry")

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
