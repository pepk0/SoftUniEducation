import re


class InvalidNameError(Exception):

    @classmethod
    def check(cls, email_: str) -> None:
        messages = []

        name, _, = email_.split("@")

        if len(name) < 4:
            messages.append("4 characters in length")

        if not re.findall(r"^([A-Za-z0-9]+[._]*[A-Za-z0-9]+)$", name):
            messages.append("using only allowed characters")

        if messages:
            message = "Email must be: " + ", ".join(messages)
            raise cls(message)


class MustContainAtSymbolError(Exception):

    @classmethod
    def check(cls, email_: str) -> None:
        if "@" not in email_:
            raise cls("Email must contain at -> '@' symbol")


class InvalidDomainError(Exception):

    @classmethod
    def check(cls, email_: str) -> None:
        valid_domains = {"com", "bg", "org", "net"}

        if email_.split(".")[-1] not in valid_domains:
            raise cls(f"Email domain must be one of the "
                      f"following {', '.join(valid_domains)}")


def main() -> str:
    while True:

        email = input("Enter a email to validate,\nor enter 'q' to quit: ")

        if email.lower() == "q":
            break

        # check for "@" symbol
        MustContainAtSymbolError.check(email)

        # check email name validity
        InvalidNameError.check(email)

        # check the domain of the email must be one of .com, .bg, .org, .net
        InvalidDomainError.check(email)

        return "Email is valid!"

    return "Exited!"


if __name__ == "__main__":
    print(main())
