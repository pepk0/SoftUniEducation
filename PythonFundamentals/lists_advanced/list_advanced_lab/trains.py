def add_people(num: int, list_arg: list) -> None:
    list_arg[-1] += num


def insert_people(index: int, people: int, list_arg: list) -> None:
    list_arg[index] += people


def leave(index: int, people: int, list_arg: list) -> None:
    list_arg[index] -= people


number_wagons = int(input())
train = [0] * number_wagons

while True:
    
    command = input()

    command, *arguments = command.split()
    if command == "add":
        people = int(arguments[0])
        add_people(people, train)
    elif command == "insert":
        train_index = int(arguments[0])
        number_people = int(arguments[1])
        insert_people(train_index, number_people, train)
    elif command == "leave":
        train_index = int(arguments[0])
        number_people = int(arguments[1])
        leave(train_index, number_people, train)
    else:
        break

print(train)