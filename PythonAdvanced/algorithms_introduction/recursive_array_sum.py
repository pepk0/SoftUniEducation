def array_sum(array: list, idx: int = 0) -> int:
    if idx == len(array) - 1:
        return array[idx]

    return array[idx] + array_sum(array, idx + 1)


input_array = [int(i) for i in input().split()]
print(array_sum(input_array))
