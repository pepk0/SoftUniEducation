number_students = int(input())
students = {}

for _ in range(number_students):
    student = input().split()
    name, grade = student[0], float(student[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    formatted_grades = [f"{i:.2f}" for i in grades]
    average = sum(grades) / len(grades)
    print(f"{name} ->", *formatted_grades, f"(avg: {average:.2f})")
