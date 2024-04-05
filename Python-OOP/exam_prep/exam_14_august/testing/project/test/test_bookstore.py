from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.bookstore1 = Bookstore(5)

    def test_simple_init(self):
        self.assertEqual(self.bookstore1.books_limit, 5)
        self.assertEqual(self.bookstore1.availability_in_store_by_book_titles,
                         {})
        self.assertEqual(self.bookstore1.total_sold_books, 0)

    def test_book_limit_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore1.books_limit = 0
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_book_limit_setter_with_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore1.books_limit = -1
        self.assertEqual(str(ve.exception), "Books limit of -1 is not valid")

    def test_dunder_len_method(self):
        self.bookstore1.availability_in_store_by_book_titles["1"] = 20
        self.bookstore1.availability_in_store_by_book_titles["2"] = 20
        self.bookstore1.availability_in_store_by_book_titles["3"] = 20
        self.assertEqual(len(self.bookstore1), 60)

    def test_receive_book_with_more_books_then_limit(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore1.receive_book("test", 10)
        self.assertEqual(str(ex.exception),
                         "Books limit is reached. Cannot receive more books!")

    def test_receive_book_with_correct_book(self):
        result = self.bookstore1.receive_book("test", 5)
        self.assertEqual(result,
                         "5 copies of test are available in the bookstore.")
        self.assertEqual(self.bookstore1.availability_in_store_by_book_titles,
                         {"test": 5})

    def test_receive_book_with_more_of_same_type_of_book(self):
        self.bookstore1.availability_in_store_by_book_titles["1"] = 3
        result = self.bookstore1.receive_book("1", 2)
        self.assertEqual(result,
                         "5 copies of 1 are available in the bookstore.")
        self.assertEqual(self.bookstore1.availability_in_store_by_book_titles,
                         {"1": 5})

    def test_sell_book_with_non_existing_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore1.sell_book("1", 100)
        self.assertEqual(str(ex.exception), "Book 1 doesn't exist!")

    def test_sell_book_with_more_books_than_in_inventory(self):
        self.bookstore1.receive_book("1", 5)
        with self.assertRaises(Exception) as ex:
            self.bookstore1.sell_book("1", 20)
        self.assertEqual(str(ex.exception),
                         "1 has not enough copies to sell. Left: 5")

    def test_sell_book_with_correct_number_of_books(self):
        self.bookstore1.receive_book("1", 3)
        self.bookstore1.receive_book("2", 2)
        result = self.bookstore1.sell_book("1", 3)
        self.assertEqual(result, "Sold 3 copies of 1")
        self.assertEqual(self.bookstore1.availability_in_store_by_book_titles,
                         {"1": 0, "2": 2})
        self.assertEqual(self.bookstore1.total_sold_books, 3)

    def test_dunder_str_method(self):
        self.bookstore1.receive_book("1", 2)
        self.bookstore1.receive_book("2", 3)
        self.assertEqual(str(self.bookstore1),
                         "Total sold books: 0"
                         "\nCurrent availability: 5"
                         "\n - 1: 2 copies\n - 2: 3 copies")


if __name__ == '__main__':
    unittest.main()
