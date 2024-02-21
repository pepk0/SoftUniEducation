cards = input().split()
number_shuffles = int(input())
middle = len(cards) // 2

for _ in range(number_shuffles):
    left_half_pointer = 0
    right_half_pointer = middle
    shuffled = []

    for _ in range(middle):
        shuffled.append(cards[left_half_pointer])
        shuffled.append(cards[right_half_pointer])
        left_half_pointer += 1
        right_half_pointer += 1
    cards = shuffled

print(cards)
