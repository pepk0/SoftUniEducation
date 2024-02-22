def create_upper_part(length: int) -> str:
    upper_body = ""
    for i in range(1, length + 1):
        upper_body += f"{' ' * (length - i)}{'* ' * i}\n"
    return upper_body


def create_bottom_part(length: int) -> str:
    lower_body = ""
    for i in range(length - 1, 0, -1):
        lower_body += f"{' ' * (length - i)}{'* ' * i}\n"
    return lower_body


def print_whole_figure(length: int) -> str:
    return create_upper_part(length) + create_bottom_part(length)


print(print_whole_figure(int(input())))
