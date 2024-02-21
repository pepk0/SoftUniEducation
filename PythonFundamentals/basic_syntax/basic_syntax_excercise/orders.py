iterations = int(input())
total_price = 0

for _ in range(iterations):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    condition_one = 0.01 <= price_per_capsule <= 100
    condition_two = 1 <= days <= 31
    condition_three = 1 <= capsules_per_day <= 2000

    if condition_one and condition_two and condition_three:
    
        total = price_per_capsule * capsules_per_day * days
        total_price += total
        print(f"The price for the coffee is: ${total:.2f}")

print(f"Total: ${total_price:.2f}")