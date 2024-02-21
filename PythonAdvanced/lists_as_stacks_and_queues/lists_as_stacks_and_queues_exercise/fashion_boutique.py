stack = [int(i) for i in input().split()]

rack_size = int(input())
number_racks = 1
cur_rack_size = rack_size

while stack:
    prev_racks = number_racks
    clothing = stack.pop()

    if clothing <= cur_rack_size:
        cur_rack_size -= clothing
    else:
        number_racks += 1
        cur_rack_size = rack_size - clothing

print(number_racks)
