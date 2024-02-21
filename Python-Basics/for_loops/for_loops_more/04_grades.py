number_students = int(input())
total_score = 0
students_top_score = 0
students_average_score = 0
students_pass_score = 0
students_fail_score = 0

for _ in range(number_students):

    student_grade = float(input())

    total_score += student_grade
    if student_grade >= 5:
        students_top_score += 1

    elif 4 <= student_grade <= 4.99:
        students_average_score += 1

    elif 3 <= student_grade <= 3.99:
        students_pass_score += 1

    else:
        students_fail_score += 1

average_score = total_score / number_students
percent_top_students = (students_top_score / number_students) * 100
percent_average_students = (students_average_score / number_students) * 100
percent_pass_students = (students_pass_score / number_students) * 100
percent_fail_students = (students_fail_score / number_students) * 100

print(f"Top students: {percent_top_students:.2f}%",
      f"Between 4.00 and 4.99: {percent_average_students:.2f}%",
      f"Between 3.00 and 3.99: {percent_pass_students:.2f}%",
      f"Fail: {percent_fail_students:.2f}%", 
      f"Average: {average_score:.2f}", sep="\n")
