nylon_sqr_m = int(input())
paint_liter = int(input())
thinner_liter = int(input())
working_hours = int(input())
nylon_sqr_m_prize = (nylon_sqr_m + 2) * 1.50
paint_liter_prize = (paint_liter + (paint_liter * 0.10)) * 14.50
thinner_liter_prize = thinner_liter * 5
prize_plastic_bags = 0.40
materials_prize = nylon_sqr_m_prize + prize_plastic_bags + thinner_liter_prize + paint_liter_prize
personel_expenses_pre = materials_prize * 0.30
personal_expenses = personel_expenses_pre * working_hours
total_prize = materials_prize + personal_expenses
print (total_prize)