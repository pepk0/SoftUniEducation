# sequence_sum = sum([ord(input()) for _ in range(int(input()))])

# print(f"The sum equals: {sequence_sum}")

sequence_range = int(input())
sequence_sum = 0

for _ in range(sequence_range):
    sequence_sum += ord(input())

print(f"The sum equals: {sequence_sum}") 
