deposite_summ = float(input())
deposite_period_mounts = int(input())
anual_interest = float(input()) / 100

final_summ = deposite_summ + deposite_period_mounts \
    * ((deposite_summ * anual_interest) / 12)

print(final_summ)