def distribute_wealth(min_wealth: int, list_arg: list) -> list | str:
    if sum(list_arg) // len(list_arg) < min_wealth:
        return "No equal distribution possible"
    for index in range(len(list_arg)):
        if list_arg[index] < min_wealth:
            take_from_index = list_arg.index(max(list_arg))
            to_take = min_wealth - list_arg[index]
            list_arg[index] += to_take
            list_arg[take_from_index] -= to_take
    return list_arg


population_list = [int(i) for i in input().split(", ")]
minimum_wealth = int(input())
print(distribute_wealth(minimum_wealth, population_list))
