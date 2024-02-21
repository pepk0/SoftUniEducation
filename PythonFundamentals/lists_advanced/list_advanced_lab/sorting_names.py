def sort_names(list_arg: list) -> list:
    result = sorted(list_arg, key=lambda x: (-len(x), x))
    return result


list_names = [name for name in input().split(", ")]
sorted_list_names = sort_names(list_names)
print(sorted_list_names)
