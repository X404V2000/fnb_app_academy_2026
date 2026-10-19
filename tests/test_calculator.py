import unittest

from helpers import load_module

calculator = load_module("unit_3/calculator.py")


class CalculateTests(unittest.TestCase):
	def test_basic_operations(self):
		self.assertEqual(calculator.calculate(7, "+", 3), 10)
		self.assertEqual(calculator.calculate(7, "-", 3), 4)
		self.assertEqual(calculator.calculate(7, "*", 3), 21)
		self.assertEqual(calculator.calculate(7, "/", 2), 3.5)

	def test_advanced_operations(self):
		self.assertEqual(calculator.calculate(7, "//", 2), 3.0)
		self.assertEqual(calculator.calculate(7, "%", 3), 1.0)

	def test_results_are_rounded_to_two_decimals(self):
		self.assertEqual(calculator.calculate(1, "/", 3), 0.33)
		self.assertEqual(calculator.calculate(10, "/", 3), 3.33)

	def test_zero_as_first_number_is_valid(self):
		# The old code skipped every calculation that contained 0.
		self.assertEqual(calculator.calculate(0, "+", 5), 5)
		self.assertEqual(calculator.calculate(0, "*", 5), 0)
		self.assertEqual(calculator.calculate(0, "-", 5), -5)

	def test_division_by_zero_raises(self):
		for operator in ("/", "//", "%"):
			with self.subTest(operator=operator):
				with self.assertRaises(ZeroDivisionError):
					calculator.calculate(5, operator, 0)

	def test_unknown_operator_raises(self):
		with self.assertRaises(ValueError):
			calculator.calculate(5, "^", 2)


if __name__ == "__main__":
	unittest.main()
