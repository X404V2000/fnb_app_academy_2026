import unittest

from helpers import load_module

directory = load_module("unit_6/phone_dir_search.py")
report = load_module("unit_6/grade_report.py")


class PhoneDirectoryTests(unittest.TestCase):
	def test_lookup_is_case_insensitive(self):
		self.assertEqual(directory.lookup(directory.contacts, "jonathan"), "0870634512")
		self.assertEqual(directory.lookup(directory.contacts, " VICTOR "), "0691341245")

	def test_lookup_missing(self):
		self.assertIsNone(directory.lookup(directory.contacts, "Nobody"))

	def test_phone_numbers_keep_leading_zero(self):
		for number in directory.contacts.values():
			self.assertIsInstance(number, str)
			self.assertTrue(number.startswith("0"))


class GradeReportTests(unittest.TestCase):
	def setUp(self):
		self.results = report.aver_calcu(report.stud_dbase)

	def test_results_shape(self):
		self.assertEqual(len(self.results), len(report.stud_dbase))
		for student in self.results:
			self.assertEqual(set(student), {"name", "average", "grade", "status"})

	def test_known_student_average(self):
		abdul = report.find_student(self.results, "abraham abdul")
		self.assertAlmostEqual(abdul["average"], (98 + 62 + 87) / 3)
		self.assertEqual(abdul["grade"], "A")
		self.assertEqual(abdul["status"], "Pass")

	def test_class_stats(self):
		stats = report.class_stats(self.results)
		self.assertEqual(stats["count"], 5)
		self.assertEqual(stats["highest"]["name"], "Abraham Abdul")
		self.assertEqual(stats["lowest"]["name"], "Senzo Mbatha")

	def test_lowest_report_uses_lowest_student(self):
		# The original printed the highest student's average in the "Lowest" line.
		import io
		from contextlib import redirect_stdout

		out = io.StringIO()
		with redirect_stdout(out):
			report.class_aver(self.results)
		lowest_line = [line for line in out.getvalue().splitlines() if line.startswith("Lowest")][0]
		self.assertIn("Senzo Mbatha", lowest_line)
		self.assertIn("4.3%", lowest_line)

	def test_stud_repor_does_not_raise(self):
		# The original raised NameError (`failures` was undefined).
		import io
		from contextlib import redirect_stdout

		with redirect_stdout(io.StringIO()):
			report.stud_repor(self.results)

	def test_find_student_missing(self):
		self.assertIsNone(report.find_student(self.results, "Nobody"))


if __name__ == "__main__":
	unittest.main()
