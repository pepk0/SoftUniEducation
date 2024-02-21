budget = float(input())
price_flour = float(input())

price_pack_eggs = price_flour * 0.75
price_liter_milk = price_flour * 1.25
cost_milk_for_loaf = price_liter_milk / 4  # 250ml needed
total_cost_loaf = price_flour + price_pack_eggs + cost_milk_for_loaf
loafs = 0
colored_eggs = 0

while budget > total_cost_loaf:
    loafs += 1
    colored_eggs += 3

    if loafs % 3 == 0:
        colored_eggs -= loafs - 2

    budget -= total_cost_loaf

print(f"You made {loafs} loaves of Easter bread! Now you have "
      f"{colored_eggs} eggs and {budget:.2f}BGN left.")
