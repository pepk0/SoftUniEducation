def add_student(name: str, course: str, courses: dict) -> None:
    if course not in courses:
        courses[course] = []
    courses[course].append(name)


total_courses = {}
while 1:
    course_information = input().split(" : ")
    if course_information[0] == "end":
        break
    course_name, student_name = course_information
    add_student(student_name, course_name, total_courses)

for course, total_students in total_courses.items():
    print(f"{course}: {len(total_students)}")
    print(*[f" -- {student}" for student in total_students], sep="\n")
