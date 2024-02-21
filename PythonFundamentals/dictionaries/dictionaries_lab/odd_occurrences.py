elements = input().split()
element_count = {}

for element in elements:
    element = element.lower()
    if element not in element_count:
        element_count[element] = 0
    element_count[element] += 1

print(*[el[0] for el in element_count.items() if el[1] % 2 != 0], sep=" ")
