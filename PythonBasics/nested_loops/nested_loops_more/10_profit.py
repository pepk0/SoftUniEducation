total_one_dollar_bills = int(input())
total_two_dollar_bills = int(input())
total_five_dollar_bills = int(input())
target_sum = int(input())
current_sum = 0

for one_dollar_bills in range(total_one_dollar_bills + 1):
    for two_dollar_bills in range(total_two_dollar_bills + 1):
        for five_dollar_bills in range(total_five_dollar_bills + 1):

            combined_sum = ((1 * one_dollar_bills) + (2 * two_dollar_bills) 
                            + (5 * five_dollar_bills))  
            
            if combined_sum == target_sum:
                print(f"{one_dollar_bills} * 1 lv. + {two_dollar_bills} * 2 lv."
                      f" + {five_dollar_bills} * 5 lv. = {target_sum} lv.")

