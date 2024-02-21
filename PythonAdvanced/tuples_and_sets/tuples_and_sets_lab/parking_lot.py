actions = {
    "IN": lambda x, y: x.add(y),
    "OUT": lambda x, y: x.remove(y)
}

car_park = set()
number_plates = int(input())
for _ in range(number_plates):
    command, license_plate = input().split(", ")
    actions[command](car_park, license_plate)

print("Parking Lot is Empty" if not car_park else "\n".join(car_park), sep=" ")
