def replace_text(text_line: str) -> str:
    replace_characters = {"-", ",", ".", "!", "?"}

    for replace_character in replace_characters:
        if replace_character in text_line:
            text_line = text_line.replace(replace_character, "@")

    return " ".join(text_line.split()[::-1])


def main() -> None:

    with open("even_lines_text.txt", "r") as txt_file:
        for number, line in enumerate(txt_file):
            if number % 2 == 0:
                print(replace_text(line))


if __name__ == "__main__":
    main()
