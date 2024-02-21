def add_students_score(name: str, grade: float, register: dict) -> None:
    if name not in register:
        register[name] = []
    register[name].append(grade)


number_scores = int(input())
grade_register = {}
average_score = lambda item: sum(item) / len(item)

for _ in range(number_scores):
    student_name = input()
    student_grade = float(input())
    add_students_score(student_name, student_grade, grade_register)

print(*[f"{k} -> {average_score(v):.2f}" for k, v in grade_register.items() 
        if average_score(v) >= 4.5], sep="\n")
