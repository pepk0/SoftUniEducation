int_sequence = [int(i) for i in input().split()]
ints_to_remove = int(input())

for _ in range(ints_to_remove):
    smallest_index = 0
    for i in range(len(int_sequence)):
        if int_sequence[i] < int_sequence[smallest_index]:
            smallest_index = i
    int_sequence.pop(smallest_index)

print(*int_sequence, sep=", ")

# int_sequence = [int(i) for i in input().split()]
# ints_to_remove = int(input())

# for _ in range(ints_to_remove):
#     smallest_item = min(int_sequence)
#     smallest_item_index = int_sequence.index(smallest_item)
#     int_sequence.pop(smallest_item_index)

# print(*int_sequence, sep=", ")
