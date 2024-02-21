def grocery_store(**kwargs) -> str:
    result = []

    items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for item, quantity in items:
        result.append(f"{item}: {quantity}")

    return "\n".join(result)
