def even_numbers(nums: list) -> list:
    even = lambda x: x % 2 == 0
    return list(filter(even, nums))


numbers = [int(i) for i in input().split()]
print(even_numbers(numbers))
