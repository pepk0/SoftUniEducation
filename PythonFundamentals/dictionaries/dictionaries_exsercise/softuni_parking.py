def register_user(user: str, plate: list, parking_lot: dict) -> str:
    if plate:
        plate = plate[0]
    if user in parking_lot:
        return f"ERROR: already registered with plate number {parking_lot[user]}"
    parking_lot[user] = plate
    return f"{user} registered {plate} successfully"


def unregister(user: str, parking_lot: dict) -> str:
    if user not in parking_lot:
        return f"ERROR: user {user} not found"
    parking_lot.pop(user)
    return f"{user} unregistered successfully"


softuni_parking_lot = {}
number_commands = int(input())
for _ in range(number_commands):
    command, username, *license_plate = input().split()
    if command == "register":
        print(register_user(username, license_plate, softuni_parking_lot))
    else:
        print(unregister(username, softuni_parking_lot))

print(*[f"{k} => {v}" for k, v in softuni_parking_lot.items()], sep="\n")
