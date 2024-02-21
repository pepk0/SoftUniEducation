student_name = input()

grade = 0
excluded = 0
average_grade = 0

while grade < 12:
    score_for_grade = float(input())
    
    if score_for_grade >= 4:
        grade += 1
        average_grade += score_for_grade
    elif score_for_grade < 4:
        excluded += 1  
    
    if excluded == 2:
        failed_grade = grade + 1
        print(f"{student_name} has been excluded at {failed_grade} grade")
        break   
else:
    average_grade /= 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")