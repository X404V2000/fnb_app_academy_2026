import unittest

from helpers import load_module

atm = load_module("unit_4/atm_sim.py")


class WithdrawTests(unittest.TestCase):
	def test_valid_withdrawal(self):
		message, balance = atm.withdraw(500, 150)
		self.assertEqual(message, "Withdrawal successful!")
		self.assertEqual(balance, 350)

	def test_withdraw_exact_balance(self):
		_, balance = atm.withdraw(500, 500)
		self.assertEqual(balance, 0)

	def test_insufficient_funds(self):
		message, balance = atm.withdraw(500, 600)
		self.assertEqual(message, "Declined. Insufficient funds")
		self.assertEqual(balance, 500)

	def test_zero_and_negative_amounts_are_invalid(self):
		for amount in (0, -20):
			with self.subTest(amount=amount):
				message, balance = atm.withdraw(500, amount)
				self.assertIn("Invalid amount", message)
				self.assertEqual(balance, 500)

	def test_decimals_round_to_cents(self):
		_, balance = atm.withdraw(500, 0.1)
		self.assertEqual(balance, 499.9)


if __name__ == "__main__":
	unittest.main()
