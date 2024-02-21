number_of_males = int(input())
number_of_females = int(input())
number_of_tables = int(input())
out_of_tables = False


for male in range(1, number_of_males + 1):
    for female in range(1, number_of_females + 1):
        
        if number_of_tables == 0:
            out_of_tables = True
            break

        number_of_tables -= 1
        print(f"({male} <-> {female})", end=" ")    

    if out_of_tables:
        break