def gather_materials(items: list, resources_dict: dict, 
                     legendaries: dict) -> str | None:
    for index in range(0, len(items), 2):
        material = items[index + 1].lower()
        if material not in resources_dict:
            resources_dict[material] = 0
        resources_dict[material] += int(items[index])
        for material in legendaries:
            if resources_dict[material] >= 250:
                resources_dict[material] -= 250
                return f"{legendary_items[material]} obtained!"


resources = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_items = {
    "motes": "Dragonwrath",
    "fragments": "Valanyr",
    "shards": "Shadowmourne"
}

while 1:
    materials = input().split()
    obtained = gather_materials(materials, resources, legendary_items)
    if obtained:
        print(obtained)
        break

print(*[f"{k}: {v}" for k, v in resources.items()], sep="\n")
