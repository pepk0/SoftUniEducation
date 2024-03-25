from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("test_name")

    def test_init_with_no_courses(self):
        self.assertEqual(self.student.name, "test_name")
        self.assertEqual(self.student.courses, {})

    def test_init_with_courses(self):
        student = Student("Mira", {"math": [1]})
        self.assertEqual(student.name, "Mira")
        self.assertEqual(student.courses, {"math": [1]})

    def test_enroll_to_existing_course(self):
        self.student.courses["math"] = [1, 2]
        result = self.student.enroll("math", [3, 4])
        self.assertEqual(result,
                         "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["math"], [1, 2, 3, 4])

    def test_enroll_course_with_notes_as_empty_string(self):
        result = self.student.enroll("math", [1, 2, 3])

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"math": [1, 2, 3]})

    def test_enroll_course_with_notes_as_y(self):
        result = self.student.enroll("math", [1, 2, 3], "Y")

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["math"], [1, 2, 3])

    def test_enroll_without_notes_and_some_string_for_notes(self):
        course = "math"
        result = self.student.enroll(course, [1, 2], "some_string")

        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["math"], [])

    def test_add_notes_to_existing_course(self):
        self.student.courses["math"] = [1, 2]
        result = self.student.add_notes("math", 3)

        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["math"], [1, 2, 3])

    def test_add_notes_exception_when_course_not_present(self):
        with self.assertRaises(Exception) as no_course:
            self.student.add_notes("math", [])

        self.assertEqual(str(no_course.exception),
                         "Cannot add notes. Course not found.")

    def test_leave_valid_course(self):
        self.student.courses["math"] = []
        result = self.student.leave_course("math")

        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student.courses, {})

    def test_leave_invalid_course(self):
        with self.assertRaises(Exception) as no_course:
            self.student.leave_course("math")

        self.assertEqual(str(no_course.exception),
                         "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
