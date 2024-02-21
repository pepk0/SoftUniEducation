string_of_integers = [int(s) for s in input().split(", ")]
number_of_beggars = int(input())
acuminated_sums = []
start_from = 0

for _ in range(number_of_beggars):
    acuminated_sum = 0
    for i in range(start_from, len(string_of_integers), number_of_beggars):
        acuminated_sum += string_of_integers[i]
    start_from += 1
    acuminated_sums.append(acuminated_sum)

print(acuminated_sums)
