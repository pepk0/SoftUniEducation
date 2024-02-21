def add_lesson(lesson: str, list_arg: list) -> None:
    if lesson not in list_arg:
        list_arg.append(lesson)


def insert_lesson(lesson: str, idx: int, list_arg: list) -> None:
    if lesson not in list_arg:
        list_arg.insert(idx, lesson)


def remove_lesson(lesson: str, list_arg: list) -> None:
    if lesson in list_arg:
        list_arg.remove(lesson)
        if f"{lesson}-Exercise" in list_arg:
            list_arg.remove(f"{lesson}-Exercise")


def add_exercise(lesson: str, list_arg: list) -> None:
    if f"{lesson}-Exercise" not in list_arg:
        for index in range(len(list_arg)):
            if list_arg[index] == lesson:
                list_arg.insert(index + 1, f"{lesson}-Exercise")
                break
        else:
            list_arg.append(lesson)
            list_arg.append(f"{lesson}-Exercise")


def swap_lessons(lesson_one: str, lesson_two: str, list_arg: list) -> None:
    if lesson_one in list_arg and lesson_two in list_arg:
        index_lesson_one = list_arg.index(lesson_one)
        index_lesson_two = list_arg.index(lesson_two)
        list_arg[index_lesson_one], list_arg[index_lesson_two] \
            = list_arg[index_lesson_two], list_arg[index_lesson_one]
        if f"{lesson_one}-Exercise" in list_arg:
            list_arg.remove(f"{lesson_one}-Exercise")
            add_exercise(lesson_one, list_arg)
        if f"{lesson_two}-Exercise" in list_arg:
            list_arg.remove(f"{lesson_two}-Exercise")
            add_exercise(lesson_two, list_arg)


soft_uni_lessons = [lesson for lesson in input().split(", ")]
while True:

    command, *arguments = input().split(":")
    if command == "Add":
        lesson_title = arguments[0]
        add_lesson(lesson_title, soft_uni_lessons)
    elif command == "Insert":
        lesson_title = arguments[0]
        lesson_index = int(arguments[1])
        insert_lesson(lesson_title, lesson_index, soft_uni_lessons)
    elif command == "Remove":
        lesson_title = arguments[0]
        remove_lesson(lesson_title, soft_uni_lessons)
    elif command == "Swap":
        lesson_title_one = arguments[0]
        lesson_title_two = arguments[1]
        swap_lessons(lesson_title_one, lesson_title_two, soft_uni_lessons)
    elif command == "Exercise":
        lesson_title = arguments[0]
        add_exercise(lesson_title, soft_uni_lessons)
    else:
        break

for number, lesson in enumerate(soft_uni_lessons):
    print(f"{number + 1}.{lesson}")
