def softuni_students(*students, **courses) -> str:
    invalid_students = []
    result = []

    for student_id, student_username in sorted(students, key=lambda x: x[1]):
        if student_id in courses.keys():
            result.append(f"*** A student with the username {student_username} "
                          f"has successfully finished the "
                          f"course {courses[student_id]}!")
        else:
            invalid_students.append(student_username)

    to_return = "\n".join(result)
    if invalid_students:
        to_return += f"\n!!! Invalid course students: {', '.join(invalid_students)}"

    return to_return
