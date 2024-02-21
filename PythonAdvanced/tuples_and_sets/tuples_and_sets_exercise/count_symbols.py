sentence = input()

count = {}

for element in sentence:
    if element not in count:
        count[element] = 0
    count[element] += 1

for element, count in sorted(count.items(), key=lambda x: x[0]):
    print(f"{element}: {count} time/s")


# solution with no if statements,
# (code runs faster, because CPU can
# optimize runtime when there are no logical splits)

# for element in sentence:
    # count[element] = count.get(element, 0) + 1

# for element, count in sorted(count.items(), key=lambda x: x[0]):
#     print(f"{element}: {count} time/s")
