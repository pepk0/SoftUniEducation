import unittest
# from extended_list import IntegerList


class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.integer_list = IntegerList(1, 2, 100)

    def test_init_takes_only_integers(self):
        test_list = IntegerList(1, "str", 1.2, 2)

        self.assertEqual(test_list.get_data(), [1, 2])

    def test_add_method_raises_a_error_for_non_ints_and_adds_ints(self):
        with self.assertRaises(ValueError) as str_exception:
            self.integer_list.add("str")

        with self.assertRaises(ValueError) as float_exception:
            self.integer_list.add(1.2)

        result = self.integer_list.add(2)
        self.assertEqual(result, [1, 2, 100, 2])

        self.assertEqual(str(float_exception.exception),
                         "Element is not Integer")

        self.assertEqual(str(str_exception.exception),
                         "Element is not Integer")

    def test_get_method_error_on_invalid_index_and_works_valid_one(self):
        with self.assertRaises(IndexError) as index_error:
            self.integer_list.get(10)

        result = self.integer_list.get(0)

        self.assertEqual(str(index_error.exception), "Index is out of range")
        self.assertEqual(result, 1)

    def test_remove_index_method_error_on_invalid_index_works_with_valid(self):
        with self.assertRaises(IndexError) as index_error:
            self.integer_list.remove_index(100)

        prev_len = len(self.integer_list.get_data())
        result = self.integer_list.remove_index(0)

        self.assertEqual(str(index_error.exception), "Index is out of range")
        self.assertEqual(result, 1)
        self.assertEqual(prev_len - 1, len(self.integer_list.get_data()),
                         "element still present in list")

    def test_insert_method_error_on_invalid_index_works_with_valid(self):
        with self.assertRaises(IndexError) as index_error:
            self.integer_list.insert(100, 1)

        prev_len = len(self.integer_list.get_data())
        self.integer_list.insert(0, 2)

        self.assertEqual(str(index_error.exception), "Index is out of range")
        self.assertEqual(prev_len + 1, len(self.integer_list.get_data()),
                         "item not inserted in to the list")

    def test_get_biget_method(self):
        test_list = IntegerList(1, 2, 100)
        self.assertEqual(test_list.get_biggest(), 100)

    def test_get_index_method(self):
        self.assertEqual(self.integer_list.get_index(1), 0)


if __name__ == "__main__":
    unittest.main()
