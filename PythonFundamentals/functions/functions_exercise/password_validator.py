def validate(psswd: str) -> str:
    errors = []
    if len(psswd) < 6 or len(psswd) > 10:
        errors.append("Password must be between 6 and 10 characters")
    if not psswd.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum([1 for i in psswd if i.isdigit()]) < 2:
        errors.append("Password must have at least 2 digits")
    if not errors:
        return "Password is valid"
    return "\n".join(errors)


password = input()
print(validate(password))
