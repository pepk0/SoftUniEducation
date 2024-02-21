even_set = set()
odd_set = set()

for line in range(1, int(input()) + 1):
    calculated_name = sum([ord(el) for el in input()]) // line

    if calculated_name % 2 == 0:
        even_set.add(calculated_name)
    else:
        odd_set.add(calculated_name)

result = odd_set.union(even_set)

if sum(even_set) < sum(odd_set):
    result = odd_set.difference(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")
