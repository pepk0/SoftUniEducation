def calculate_stats(dragons: dict) -> tuple:
    total_damage = 0
    total_health = 0
    total_armor = 0
    average = 0
    for damage, health, armor in dragons.values():
        total_damage += damage
        total_health += health
        total_armor += armor
        average += 1
    total_damage /= average
    total_health /= average
    total_armor /= average
    return total_damage, total_health, total_armor


all_dragons = {}
total_dragons = int(input())
for _ in range(total_dragons):
    dragon_stats = input().split()
    dragon_type, dragon_name, damage, health, armor = dragon_stats
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    if dragon_type not in all_dragons:
        all_dragons[dragon_type] = {}
    all_dragons[dragon_type][dragon_name] = (damage, health, armor)

for type, dragons in all_dragons.items():
    average_damage, average_health, average_armor = calculate_stats(dragons)
    print(f"{type}::({average_damage:.2f}"
          f"/{average_health:.2f}/{average_armor:.2f})")
    for name, (damage, health, armor) in sorted(dragons.items(),
                                                key=lambda x: x[0]):
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")
