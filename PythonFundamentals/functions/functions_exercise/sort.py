# def bubble_sort(nums: list) -> list:
#     for i in range(len(nums), 0, -1):
#         for j in range(1, i):
#             if nums[j] < nums[j - 1]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#     return nums


# def selection_sort(nums: list) -> list:
#     for i in range(len(nums)):
#         smallest_index = i
#         for j in range(i, len(nums)):
#             if nums[j] < nums[smallest_index]:
#                 smallest_index = j
#         nums[smallest_index], nums[i] = nums[i], nums[smallest_index]
#     return nums


def intersection_sort(nums: list) -> list:
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


numbers = [int(i) for i in input().split()]
sorted_numbers = intersection_sort(numbers)
print(sorted_numbers)
