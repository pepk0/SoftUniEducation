def accommodate_new_pets(capacity: int, max_weight: float, *pets) -> str:
    accommodated_pets = {}
    message = []
    total_pets = len(pets)

    for pet_type, weight in pets:
        if not capacity:
            break

        total_pets -= 1

        if weight <= max_weight:
            accommodated_pets[pet_type] = accommodated_pets.get(pet_type, 0) + 1
        else:
            continue

        capacity -= 1

    if total_pets == 0 and capacity >= 0:
        message.append(
            f"All pets are accommodated! Available capacity: {capacity}.")
    elif total_pets > 0 and capacity == 0:
        message.append("You did not manage to accommodate all pets!")

    message.append("Accommodated pets:")
    [message.append(f"{t}: {n}") for t, n in sorted(accommodated_pets.items())]

    return "\n".join(message)
