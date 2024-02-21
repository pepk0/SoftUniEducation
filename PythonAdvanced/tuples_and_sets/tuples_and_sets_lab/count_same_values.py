numbers = [float(i) for i in input().split()]
count = {}
for element in numbers:
    if element not in count:
        count[element] = 0
    count[element] += 1

for element, count in count.items():
    print(f"{element:.1f} - {count} times")
