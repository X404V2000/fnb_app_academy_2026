import unittest

from helpers import load_module

fuel = load_module("unit_3/rsa_fuel_cost_calc.py")


class FuelCostTests(unittest.TestCase):
	def test_liters_needed_is_km_divided_by_ten(self):
		self.assertEqual(fuel.liters_needed(100), 10)
		self.assertEqual(fuel.liters_needed(55), 5.5)

	def test_total_cost_for_100km_at_22_45(self):
		# 100 km -> 10 L -> 10 * 22.45 = 224.50 (the original code returned 2245.0)
		self.assertEqual(fuel.total_cost(100, 22.45), 224.5)

	def test_total_cost_is_rounded_to_two_decimals(self):
		# 15 km -> 1.5 L -> 1.5 * 22.45 = 33.675 -> 33.67
		self.assertEqual(fuel.total_cost(15, 22.45), 33.67)

	def test_zero_distance_costs_nothing(self):
		self.assertEqual(fuel.total_cost(0, 22.45), 0)


if __name__ == "__main__":
	unittest.main()
