import string
import unittest

from helpers import load_module

pwgen = load_module("side_tasks/password_generator.py")


class PasswordGeneratorTests(unittest.TestCase):
	def test_length_is_exact(self):
		# The original produced length + 4 characters.
		for length in (8, 16, 32):
			with self.subTest(length=length):
				password = pwgen.generate_password(length, ["uppercase", "lowercase", "numbers", "special"])
				self.assertEqual(len(password), length)

	def test_one_character_of_each_chosen_type(self):
		for _ in range(50):
			password = pwgen.generate_password(8, ["uppercase", "lowercase", "numbers", "special"])
			self.assertTrue(any(c in string.ascii_uppercase for c in password))
			self.assertTrue(any(c in string.ascii_lowercase for c in password))
			self.assertTrue(any(c in string.digits for c in password))
			self.assertTrue(any(c in pwgen.SPECIAL_CHARS for c in password))

	def test_only_chosen_types_are_used(self):
		allowed = set(string.ascii_lowercase)
		for _ in range(20):
			password = pwgen.generate_password(20, ["lowercase"])
			self.assertTrue(set(password) <= allowed)

	def test_invalid_length_raises(self):
		for length in (7, 33, 0, -1):
			with self.subTest(length=length):
				with self.assertRaises(ValueError):
					pwgen.generate_password(length, ["lowercase"])

	def test_no_types_raises(self):
		with self.assertRaises(ValueError):
			pwgen.generate_password(12, [])

	def test_two_passwords_differ(self):
		self.assertNotEqual(pwgen.generate_password(16, ["lowercase"]),
		                    pwgen.generate_password(16, ["lowercase"]))

	def test_strength(self):
		self.assertEqual(pwgen.strength_label(pwgen.strength_score("abc")), "Weak")
		self.assertEqual(pwgen.strength_label(pwgen.strength_score("Abcdefgh1234")), "Medium")
		self.assertEqual(pwgen.strength_label(pwgen.strength_score("Abcdefgh1234!")), "Strong")


if __name__ == "__main__":
	unittest.main()
