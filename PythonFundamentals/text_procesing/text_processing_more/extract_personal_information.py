def find_name(text: str) -> str:
    start_index = text.index("@")
    end_index = text.index("|")
    return text[start_index + 1:end_index]


def find_age(text: str) -> int:
    start_index = text.index("#")
    end_index = text.index("*")
    return int(text[start_index + 1:end_index])


number_of_texts = int(input())
for _ in range(number_of_texts):
    input_text = input()
    print(f"{find_name(input_text)} is {find_age(input_text)} years old.")
