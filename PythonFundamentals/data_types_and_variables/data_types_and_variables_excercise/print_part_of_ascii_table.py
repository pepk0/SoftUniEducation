range_start = int(input())
range_stop = int(input())
ascii_table = ""

for integer in range(range_start, range_stop + 1):
    ascii_table += chr(integer)

print(*ascii_table, sep=" ")
