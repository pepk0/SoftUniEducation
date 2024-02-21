aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
used_space_percent = float(input()) / 100

aquarium_volume_liters = (aquarium_length * aquarium_width * aquarium_height) \
                        / 1000

free_aquarium_space = aquarium_volume_liters * (1 - used_space_percent)

print(free_aquarium_space)