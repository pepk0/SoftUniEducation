def next_version(list_arg: list) -> list:
    to_add = 1
    back_of_list = len(list_arg) - 1
    while to_add:
        if list_arg[back_of_list] < 9:
            list_arg[back_of_list] += 1
            to_add -= 1
        else:
            list_arg[back_of_list] = 0
        back_of_list -= 1
    return list_arg
 


current_version = [int(i) for i in input().split(".")]
print(*next_version(current_version), sep=".")