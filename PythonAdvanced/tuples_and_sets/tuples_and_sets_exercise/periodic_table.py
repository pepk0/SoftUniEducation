number_of_lines = int(input())

unique_elements = set()

for _ in range(number_of_lines):
    for element in input().split():
        unique_elements.add(element)

print(*unique_elements, sep="\n")
