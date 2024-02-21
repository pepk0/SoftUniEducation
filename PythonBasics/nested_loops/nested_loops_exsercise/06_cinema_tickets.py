movie_name = input()
total_student_tickets = 0
total_standard_tickets = 0
total_kids_tickets = 0
total_tickets = 0

while movie_name != "Finish":
    theater_seats = int(input())
    tickets_sold = 0
    
    for _ in range(theater_seats):
        ticket_type = input()
        
        if ticket_type == "End":
            break
        
        if ticket_type == "student":
            total_student_tickets +=1    
        
        elif ticket_type == "standard":
            total_standard_tickets +=1    
        
        elif ticket_type == "kid":
            total_kids_tickets +=1    
         
        tickets_sold += 1    
    
    total_tickets += tickets_sold
    
    percent_seats_taken = (tickets_sold / theater_seats) * 100
    print(f"{movie_name} - {percent_seats_taken:.2f}% full.")

    movie_name = input()

percent_student_tickets = (total_student_tickets / total_tickets) * 100
percent_standard_tickets = (total_standard_tickets / total_tickets) * 100
percent_kid_tickets = (total_kids_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}", 
     f"{percent_student_tickets:.2f}% student tickets.", 
     f"{percent_standard_tickets:.2f}% standard tickets.",
     f"{percent_kid_tickets:.2f}% kids tickets.", sep="\n")