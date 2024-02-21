longest_intersection_length = 0
loges_interception = None

for _ in range(int(input())):
    ranges = [[int(i) for i in j.split(",")] for j in input().split("-")]

    range_one = {i for i in range(ranges[0][0], ranges[0][1] + 1)}
    range_two = {i for i in range(ranges[1][0], ranges[1][1] + 1)}

    interception = range_one.intersection(range_two)

    if len(interception) > longest_intersection_length:
        longest_intersection_length = len(interception)
        loges_interception = list(interception)

print(f"Longest intersection is {loges_interception} "
      f"with length {longest_intersection_length}")
