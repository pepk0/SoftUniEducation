number_integers = int(input())

positives = []
negatives = []

for _ in range(number_integers):

    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives, negatives, f"Count of positives: {len(positives)}",
      f"Sum of negatives: {sum(negatives)}", sep="\n")
