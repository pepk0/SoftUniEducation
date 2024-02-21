from collections import deque


crafting_costs = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_toys = []

boxes_of_materials = deque([int(i) for i in input().split()])
total_magic = deque([int(i) for i in input().split()])

while boxes_of_materials and total_magic:
    materials = boxes_of_materials.pop()
    magic = total_magic.popleft()

    if not materials and not magic:
        continue
    elif not materials:
        total_magic.appendleft(magic)
        continue
    elif not magic:
        boxes_of_materials.append(materials)
        continue

    magic_level = materials * magic

    if magic_level in crafting_costs:
        crafted_toys.append(crafting_costs[magic_level])
    elif magic_level < 0:
        boxes_of_materials.append(materials + magic)
    elif magic_level > 0:
        boxes_of_materials.append(materials + 15)

condition_one = {"Doll", "Wooden train"}.issubset(crafted_toys)
condition_two = {"Teddy bear", "Bicycle"}.issubset(crafted_toys)

if condition_one or condition_two:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_of_materials:
    print("Materials left:", ", ".join([str(x)
          for x in reversed(boxes_of_materials)]))

if total_magic:
    print("Magic left:", ", ".join(str(x) for x in total_magic))

for toy in sorted(set(crafted_toys)):
    print(f"{toy}: {crafted_toys.count(toy)}")
