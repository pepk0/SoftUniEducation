def gen_ascii_dict(char_list: list) -> dict:
    return {el: ord(el) for el in char_list}


print(gen_ascii_dict(input().split(", ")))
