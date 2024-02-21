numbers = int(input())

previous_pairs = 0
max_difference = ""

for number in range(numbers):

    first_pair = int(input())
    second_pair = int(input())
    current_pair = first_pair + second_pair
    if number == 0:
        previous_pairs = current_pair
        continue

    if current_pair != previous_pairs:
        difference = abs(current_pair - previous_pairs)
        if type(difference) != str or difference > max_difference:
            max_difference = difference

    previous_pairs = current_pair

if type(max_difference) != str:
    print(f"No, maxdiff={max_difference}")
else:
    print(f"Yes, value={previous_pairs}")
