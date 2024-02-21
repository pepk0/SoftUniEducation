junior_bikers = int(input())
senior_bikers = int(input())
type_of_track = input()

junior_entry_fee = 0
senior_entry_fee = 0
percent_for_expense = 0.05
total_participants = junior_bikers + senior_bikers

if type_of_track == "trail":
    junior_entry_fee = 5.5
    senior_entry_fee = 7

elif type_of_track == "cross-country":
    junior_entry_fee = 8
    senior_entry_fee = 9.5
    if total_participants >= 50:
        junior_entry_fee *= 1 - 0.25
        senior_entry_fee *= 1 - 0.25

elif type_of_track == "downhill":
    junior_entry_fee = 12.25
    senior_entry_fee = 13.75

elif type_of_track == "road":
    junior_entry_fee = 20
    senior_entry_fee = 21.5

total_money_saved = (junior_bikers * junior_entry_fee 
                     + senior_bikers * senior_entry_fee)
money_left_for_charity = total_money_saved * (1 - percent_for_expense)

print(f"{money_left_for_charity:.2f}")
