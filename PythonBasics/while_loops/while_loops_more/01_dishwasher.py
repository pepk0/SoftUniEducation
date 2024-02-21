bottles_of_detergent = int(input())
milliliters_of_detergent = bottles_of_detergent * 750
detergent_used = 0
washing_machine_loadings = 0
dishes_washed = 0
pans_washed = 0

while milliliters_of_detergent >= detergent_used:

    items_for_washing = input()
    if items_for_washing == "End":
        left_over_detergent = milliliters_of_detergent - detergent_used
        print("Detergent was enough!", f"{dishes_washed} dishes and"
              f" {pans_washed} pots were washed.", f"Leftover detergent "
              f"{left_over_detergent} ml.", sep="\n")
        break

    items_for_washing = int(items_for_washing)
    washing_machine_loadings += 1
    
    if washing_machine_loadings % 3 == 0:
        milliliters_per_item = 15
        pans_washed += items_for_washing
    else:
        milliliters_per_item = 5
        dishes_washed += items_for_washing

    detergent_used += items_for_washing * milliliters_per_item

else:
    detergent_needed = detergent_used - milliliters_of_detergent
    print(f"Not enough detergent, {detergent_needed} ml. more necessary!")