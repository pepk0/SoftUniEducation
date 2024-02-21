number_judges = int(input())
total_grades = 0
total_grade_score = 0

presentation_name = input()

while presentation_name != "Finish":
    total_grades += number_judges
    presentation_grade = 0
    
    for _ in range(number_judges):
        grade_given = float(input())
        presentation_grade += grade_given
        total_grade_score += grade_given    
    
    average_grade = presentation_grade / number_judges
    print(f"{presentation_name} - {average_grade:.2f}.")

    presentation_name = input()

else:
    final_grade = total_grade_score / total_grades
    print(f"Student's final assessment is {final_grade:.2f}.")