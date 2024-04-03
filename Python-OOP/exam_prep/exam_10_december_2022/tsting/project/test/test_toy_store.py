from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.shelf1 = ToyStore()

    def test_simple_init(self):
        self.assertEqual(self.shelf1.toy_shelf,
                         {"A": None, "B": None, "C": None, "D": None, "E": None,
                          "F": None, "G": None, }
                         )

    def test_add_toy_invalid_shelf_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("random_test", "test")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_with_same_toy_already_in_shelf_raises_error(self):
        self.shelf1.add_toy("A", "test")
        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("A", "test")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_when_shelf_is_taken_raises_error(self):
        self.shelf1.add_toy("A", "test")
        with self.assertRaises(Exception) as ex:
            self.shelf1.add_toy("A", "test-second")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_adds_toy_correctly(self):
        result = self.shelf1.add_toy("A", "this must work!")
        self.assertEqual(self.shelf1.toy_shelf["A"], "this must work!")
        self.assertEqual(result, "Toy:this must work! placed successfully!")

    def test_remove_toy_invalid_shelf_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.shelf1.remove_toy("random_test", "test")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_with_incorrect_toy_raises_error(self):
        self.shelf1.add_toy("A", "test")
        with self.assertRaises(Exception) as ex:
            self.shelf1.remove_toy("A", "not supposed to work!")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_with_correct_toy_works(self):
        self.shelf1.add_toy("A", "test")
        result = self.shelf1.remove_toy("A", "test")
        self.assertEqual(self.shelf1.toy_shelf["A"], None)
        self.assertEqual(result, "Remove toy:test successfully!")


if __name__ == '__main__':
    unittest.main()
