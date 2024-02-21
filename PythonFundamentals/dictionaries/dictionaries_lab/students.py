courses = {}

while 1:
    command = input().split(":")
    if len(command) <= 1:
        query_course = command[0].replace("_", " ").lower()
        break
    name, student_id, course = command[0], int(command[1]), command[2].lower()
    if course not in courses:
        courses[course] = {}
    courses[course][name] = student_id

for key, value in courses[query_course].items():
    print(f"{key} - {value}")
