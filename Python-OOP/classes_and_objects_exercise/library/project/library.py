from project.user import User


class Library:
    def __init__(self) -> None:
        self.user_records: list = []
        self.books_available: dict = {}
        self.rented_books: dict = {}

    def get_book(self, author: str, book_name: str, days_to_return: int,
                 user: User) -> str:
        if book_name in self.books_available[author] and book_name:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: days_to_return}
            self.rented_books[user.username][book_name] = days_to_return

            return (f"{book_name} successfully rented for the "
                    f"next {days_to_return} days!")

        for _, info in self.rented_books.items():
            if book_name in info:
                days_left = info[book_name]

        return (f'The book "{book_name}" is already rented '
                f'and will be available in {days_left} days!')

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"
