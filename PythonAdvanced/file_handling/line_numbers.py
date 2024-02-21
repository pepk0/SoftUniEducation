from string import punctuation


def parse_content(text: str) -> str:
    letter, punctuation_mark = 0, 0

    for element in text:
        if element.isalpha():
            letter += 1
        elif element in punctuation:
            punctuation_mark += 1

    return f"({letter})({punctuation_mark})"


def main() -> None:

    with open("even_lines_text.txt", "r") as txt_file:

        for number_line, line in enumerate(txt_file, 1):

            with open("output.txt", "a") as output:
                count = parse_content(line)
                output.write(f"Line: {number_line} {line.strip()} {count}\n")


if __name__ == "__main__":
    main()
