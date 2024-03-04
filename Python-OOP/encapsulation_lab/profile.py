class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str) -> None:
        if not 5 <= len(username) <= 15:
            raise ValueError(
                "The username must be between 5 and 15 characters.")
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        len_check = len(password) >= 8
        uppercase_letter_check = any(s.isupper() for s in password)
        digit_check = any(s.isdigit() for s in password)

        if not len_check or not uppercase_letter_check or not digit_check:
            raise ValueError("The password must be 8 or more characters with "
                             "at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def __str__(self) -> str:
        return (f'You have a profile with username: "{self.username}" '
                f'and password: {"*" * len(self.password)}')


