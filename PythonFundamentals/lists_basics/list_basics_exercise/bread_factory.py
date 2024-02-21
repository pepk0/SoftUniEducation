events = [el.split("-") for el in input().split("|")]
coins = 100
energy = 100

for event, amount in events:
    amount = int(amount)
    if event == "rest":
        if energy + amount > 100:
            gained_energy = abs(100 - energy)
            energy = 100
        else:
            gained_energy = amount
            energy += amount
        print(f"You gained {gained_energy} energy.",
              f"Current energy: {energy}.", sep="\n")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += amount
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:  # everything else is a ingredient
        if coins >= amount:
            coins -= amount
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            break
else:
    print("Day completed!", f"Coins: {coins}", f"Energy: {energy}", sep="\n")
