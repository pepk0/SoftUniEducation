video_card_price = 250
discount_for_more_vga = 0.15

budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())

total_video_card_price = video_card_price * number_video_cards

# the processor costs 35% from the total video card price
processor_price = total_video_card_price *  0.35
total_processor_price = processor_price * number_processors

# the ram costs 10% of the total video card price
ram_price = total_video_card_price *  0.1
total_ram_price = ram_price * number_ram

total_price = total_video_card_price + total_processor_price + total_ram_price

if number_processors < number_video_cards:
    total_price *= 1 - discount_for_more_vga

if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")

else:
    more_money_needed = total_price - budget
    print(f"Not enough money! You need {more_money_needed:.2f} leva more!")
