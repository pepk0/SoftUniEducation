money_needed_for_charity = int(input())
is_cash_transaction = True
saved_up_money = 0
card_transaction = 0
cash_transaction = 0
money_from_card = 0
money_from_cash = 0

while money_needed_for_charity > saved_up_money:

    item_price = input()
    if item_price == "End":
        print("Failed to collect required money for charity.")
        break
    
    item_price = int(item_price)
    product_sold = False
    
    if is_cash_transaction:
        is_cash_transaction = False
        if item_price <= 100:
            product_sold = True
            money_from_cash += item_price
            cash_transaction += 1
    
    else:
        is_cash_transaction = True
        if item_price >= 10:
            product_sold = True
            money_from_card += item_price
            card_transaction += 1

    if product_sold:
        print("Product sold!")
        saved_up_money += item_price
    else:
        print("Error in transaction!")

else:
    average_cash_sum = money_from_cash / cash_transaction
    average_card_sum = money_from_card / card_transaction
    print(f"Average CS: {average_cash_sum:.2f}", 
          f"Average CC: {average_card_sum:.2f}", sep="\n")        
