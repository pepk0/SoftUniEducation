diagonal_sum = 0

for index in range(int(input())):
    diagonal_sum += [int(i) for i in input().split()][index]

print(diagonal_sum)
