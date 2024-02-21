annual_training_cost = int(input())

basketball_shoes = annual_training_cost * 0.6
basketball_kit = basketball_shoes * 0.8
basketball = basketball_kit / 4
basketball_accessories = basketball / 5

total_price = annual_training_cost + basketball_shoes + basketball_kit \
            + basketball + basketball_accessories

print(total_price)