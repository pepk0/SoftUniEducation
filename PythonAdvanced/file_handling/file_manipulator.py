from os import remove


def create_file(name: str) -> None:
    with open(name, "w") as txt_file:
        txt_file.write("")


def add_to_file(file_name: str, content: tuple) -> None:
    with open(file_name, "a") as txt_file:
        txt_file.write(content[0] + "\n")


def replace_in_file(file_name: str, content: tuple) -> None:
    try:
        with open(file_name, "r+") as txt_file:
            new_content = txt_file.read().replace(content[0], content[1])

        with open(file_name, "w") as write_file:
            write_file.write(new_content)

    except FileNotFoundError:
        print("An error occurred!")


def delete_file(file_name: str) -> None:
    try:
        remove(file_name)
    except FileNotFoundError:
        print("An error occurred!")


def main() -> None:
    actions = {
        "Create": create_file,
        "Add": add_to_file,
        "Replace": replace_in_file,
        "Delete": delete_file,
    }

    while True:

        command = input().split("-")
        if command[0] == "End":
            break

        action, file_name, *args = command

        if args:
            actions[action](file_name, args)
        else:
            actions[action](file_name)

if __name__ == "__main__":
    main()
