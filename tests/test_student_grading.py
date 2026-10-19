import unittest

from helpers import load_module

grading = load_module("unit_4/student_grading_system.py")


class LetterGradeTests(unittest.TestCase):
	def test_grade_boundaries(self):
		cases = {
			100: "A", 80: "A",
			79: "B", 70: "B",
			69: "C", 60: "C",
			59: "D", 50: "D",
			49: "F", 0: "F",
		}
		for mark, expected in cases.items():
			with self.subTest(mark=mark):
				self.assertEqual(grading.letter_grade(mark), expected)


class ClassifierTests(unittest.TestCase):
	def test_average(self):
		self.assertAlmostEqual(grading.average_mark([80, 70, 60]), 70)

	def test_pass_status(self):
		self.assertEqual(grading.pass_status(50), "Pass")
		self.assertEqual(grading.pass_status(49.9), "Fail")

	def test_intervention_flag(self):
		self.assertTrue(grading.needs_intervention(39.9))
		self.assertFalse(grading.needs_intervention(40))


if __name__ == "__main__":
	unittest.main()
