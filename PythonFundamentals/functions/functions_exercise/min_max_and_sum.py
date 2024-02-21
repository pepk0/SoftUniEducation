def find_min(list_nums: list) -> int:
    min_number = 0
    for index in range(len(list_nums)):
        if list_nums[min_number] > list_nums[index]:
            min_number = index
    return list_nums[min_number]


def find_max(list_nums: list) -> int:
    min_number = 0
    for index in range(len(list_nums)):
        if list_nums[min_number] < list_nums[index]:
            min_number = index
    return list_nums[min_number]


def sum_all_elements(nums_list: list) -> int:
    result = 0
    for i in range(len(nums_list)):
        result += nums_list[i]
    return result


numbers = [int(i) for i in input().split()]
max_number = find_max(numbers)
min_number = find_min(numbers)
sum_numbers = sum_all_elements(numbers)
print(f"The minimum number is {min_number}", 
      f"The maximum number is {max_number}",
      f"The sum number is: {sum_numbers}", sep="\n")
