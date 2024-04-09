from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return (f"User with id = {user.user_id} "
                    f"already registered in the library!")

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str,
                        library: Library):
        if user_id in library.user_records:
            user = library.user_records[library.user_records.index(user_id)]
            if user.username == new_username:
                return ("Please check again the provided username - "
                        "it should be different than the username used so far!")

            if user.username in library.rented_books:
                info = library.rented_books[user.username]
                library.rented_books[new_username] = info
            user.username = new_username
            return (f"Username successfully changed to: {new_username} "
                    f"for user id: {user.user_id}")

        return f"There is no user with id = {user_id}!"


