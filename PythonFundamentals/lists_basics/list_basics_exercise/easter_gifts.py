def out_of_stock(gift: str, items: list) -> list:
    for index in range(len(items)):
        if items[index] == gift:
            items[index] = None
    return items


def just_in_case(gift: str, items: list) -> list:
    items[-1] = gift
    return items


def required(index: int, gift: str, items: list) -> list:
    if 0 <= index < len(items):
        items[index] = gift
        return items
    return items


gift_list = input().split()

while True:

    command_input = input()
    if command_input == "No Money":
        break
    
    command, *items = command_input.split()
    if command == "OutOfStock":
        gift = items[0]
        gift_list = out_of_stock(gift, gift_list)
    elif command == "Required":
        gift, index = items
        index = int(index)
        gift_list = required(index, gift, gift_list)
    elif command == "JustInCase":
        gift = items[0]
        gift_list = just_in_case(gift, gift_list)

result_list = [el for el in gift_list if el != None] 
print(*result_list)
