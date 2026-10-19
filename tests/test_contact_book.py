import unittest

from helpers import load_module

book = load_module("unit_5/contact_book.py")


def sample():
	return [
		{"name": "Nelson Nkosi", "phone": "0821234567", "email": "n@example.com"},
		{"name": "Kate Mohammad", "phone": "0739876543", "email": ""},
	]


class ContactBookTests(unittest.TestCase):
	def test_find_is_case_insensitive(self):
		contacts = sample()
		self.assertEqual(book.find_contact(contacts, "nelson nkosi")["phone"], "0821234567")
		self.assertEqual(book.find_contact(contacts, "  KATE MOHAMMAD ")["name"], "Kate Mohammad")
		self.assertIsNone(book.find_contact(contacts, "Nobody"))

	def test_add_contact(self):
		contacts = []
		contact = book.add_contact(contacts, "sipho", "dlamini", "0812345678", "s@example.com")
		self.assertEqual(contact["name"], "Sipho Dlamini")
		self.assertEqual(contacts, [contact])

	def test_add_contact_requires_name_and_phone(self):
		contacts = []
		self.assertIsNone(book.add_contact(contacts, "", "Dlamini", "081", ""))
		self.assertIsNone(book.add_contact(contacts, "Sipho", "Dlamini", "", ""))
		self.assertEqual(contacts, [])

	def test_delete_contact(self):
		contacts = sample()
		self.assertTrue(book.delete_contact(contacts, "nelson nkosi"))
		self.assertEqual(len(contacts), 1)
		self.assertEqual(contacts[0]["name"], "Kate Mohammad")
		self.assertFalse(book.delete_contact(contacts, "Nelson Nkosi"))

	def test_search_prints_not_found_for_missing_name(self):
		# The original loop-else printed "Data not found" even after a successful match.
		contacts = sample()
		import io
		from contextlib import redirect_stdout

		out = io.StringIO()
		with redirect_stdout(out):
			self.assertIsNotNone(book.search_contact(contacts, "Kate Mohammad"))
		self.assertNotIn("Data not found", out.getvalue())

		out = io.StringIO()
		with redirect_stdout(out):
			self.assertIsNone(book.search_contact(contacts, "Nobody"))
		self.assertIn("Data not found", out.getvalue())


if __name__ == "__main__":
	unittest.main()
