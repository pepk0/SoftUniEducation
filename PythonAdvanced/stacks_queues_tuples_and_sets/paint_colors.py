from collections import deque
from itertools import permutations


mixes = {
    "red": None, # not smooth
    "blue": None,
    "yellow": None,
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
    "orange": {"red", "yellow"},
}

mixed_colors = deque(input().split())
resulting_colors = []

while mixed_colors:
    left_color = mixed_colors.popleft()
    if mixed_colors:
        right_color = mixed_colors.pop()
    else:
        right_color = ""

    combinations = {''.join(combination)
                    for combination in permutations((right_color, left_color))}

    for combination in combinations:
        if combination in mixes:
            resulting_colors.append(combination)
            break
    else:
        insertion_index = len(mixed_colors) // 2

        left_color, right_color = left_color[:-1], right_color[:-1]

        if right_color:
            mixed_colors.insert(insertion_index, right_color)
        if left_color:
            mixed_colors.insert(insertion_index, left_color)

for color in resulting_colors[:]: # copy()
    if mixes[color]:
        if not mixes[color].issubset(resulting_colors):
            resulting_colors.remove(color)

print(resulting_colors)
