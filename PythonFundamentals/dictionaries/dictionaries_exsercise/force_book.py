def add_side(user: str, side: str, register: dict) -> None:
    found_user = False
    if side not in register:
        register[side] = []
    for users in register.values():
        if user in users:
            found_user = True
    if not found_user:
        register[side].append(user)


def switch_sides(user: str, side: str, register: dict) -> str:
    for _, side_users in register.items():
        if user in side_users:
            side_users.remove(user)
    add_side(user, side, register)
    return f"{user} joins the {side} side!"


sides = {}
while 1:
    command = input()
    if "|" in command:
        command_side, command_user = command.split(" | ")
        add_side(command_user, command_side, sides)
    elif "->" in command:
        command_user, command_side = command.split(" -> ")
        print(switch_sides(command_user, command_side, sides))
    else:
        break

for side, side_users in sides.items():
    if side_users:
        print(f"Side: {side}, Members: {len(side_users)}")
        print(*[f"! {user}" for user in side_users], sep="\n")
