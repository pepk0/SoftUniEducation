def modify_input(command: str, value: str) -> str:
    actions = {
        "int": lambda x: (int(x) * 2),
        "real": lambda x: f"{float(x) * 1.5:.2f}",
        "string": lambda x: f"${x}$",
    }
    return actions[command](value)


user_command = input()
user_value = input()
print(modify_input(user_command, user_value))
