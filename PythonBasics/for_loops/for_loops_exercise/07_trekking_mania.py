group_of_climbers = int(input())
total_people = 0
climbers_on_musala = 0
climbers_on_montblanc = 0
climbers_on_kilimanjaro = 0
climbers_on_k2 = 0
climbers_on_everest = 0

for _ in range(group_of_climbers):

    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        climbers_on_musala += people_in_group
    
    elif 6 <= people_in_group <= 12:
        climbers_on_montblanc += people_in_group
    
    elif 13 <= people_in_group <= 25:
        climbers_on_kilimanjaro += people_in_group

    elif 26 <= people_in_group <= 40:
        climbers_on_k2 += people_in_group

    elif people_in_group >= 41:
        climbers_on_everest += people_in_group

percent_musala = (climbers_on_musala / total_people) * 100 
percent_montblanc = (climbers_on_montblanc / total_people) * 100 
percent_kilimanjaro = (climbers_on_kilimanjaro / total_people) * 100 
percent_k2 = (climbers_on_k2 / total_people) * 100 
percent_everest = (climbers_on_everest / total_people) * 100

print(f"{percent_musala:.2f}%", f"{percent_montblanc:.2f}%", 
      f"{percent_kilimanjaro:.2f}%", f"{percent_k2:.2f}%", 
      f"{percent_everest:.2f}%", sep="\n")