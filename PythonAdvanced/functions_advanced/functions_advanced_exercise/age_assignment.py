def age_assignment(*names, **ages) -> str:
    results = []

    for name in (sorted(names)):
        results.append(f"{name} is {ages[name[0]]} years old.")

    return "\n".join(results)
