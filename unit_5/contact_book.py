'''
Practical Task
Task Overview

Build a command-line contact book called contact_book.py that stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. This is a foundational data structure pattern used in virtually every real app.

Requirements

Store contacts as a list of dictionaries, each with keys: name, phone, email
Implement an add_contact() function that appends a new dictionary to the list
Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
Implement a delete_contact(name) function that removes a contact by name
Implement a view_all() function that displays all contacts in a formatted layout
Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)

'''
import sys

sys_storage = [
	{"name": "Nelson Nkosi", "phone": "0821234567", "email": "nelnkosi82@gmail.com"},
	{"name": "Kate Mohammad", "phone": "0739876543", "email": "kathee73@gmail.com"},
	{"name": "Devis Brown", "phone": "0715551234", "email": "davisbrown71@gmail.com"},
	{"name": "Jackson Thwala", "phone": "0844445678", "email": "jackthwal84@gmail.com"},
]


# Pure data helpers — kept separate so they are easy to test.
def find_contact(contacts, name):
	"""Return the matching contact dictionary, or None if not found (case-insensitive)."""
	search = name.strip().lower()
	for contact in contacts:
		if contact["name"].lower() == search:
			return contact
	return None


def add_contact(contacts, first_name, last_name, phone, email):
	"""Add a contact to the list. Returns the new contact, or None if required fields are missing."""
	first_name = first_name.strip().title()
	last_name = last_name.strip().title()
	phone = phone.strip()
	email = email.strip()

	if not (first_name and last_name and phone):
		return None

	contact = {"name": f"{first_name} {last_name}", "phone": phone, "email": email}
	contacts.append(contact)
	return contact


def delete_contact(contacts, name):
	"""Remove a contact by name. Returns True if a contact was deleted."""
	contact = find_contact(contacts, name)
	if contact is None:
		return False
	contacts.remove(contact)
	return True


def search_contact(contacts, name):
	for contact in contacts:
		if contact["name"].lower() == name.strip().lower():
			print("\nContact found")
			print(f"Name   : {contact['name']}")
			print(f"Phone  : {contact['phone']}")
			print(f"Email  : {contact['email'] or '-'}")
			return contact
	print(f"\nData not found ... '{name.strip().title()}' is not in your contact book")
	return None


def view_contacts(contacts):
	print("=" * 75, "\nAll Contacts")
	print("=" * 75)
	print(f"{'Name':<22} {'Phone':<14} {'Email'}")
	print("-" * 75)
	if not contacts:
		print("(contact book is empty)")
	for contact in contacts:
		print(f"{contact['name']:<22} {contact['phone']:<14} {contact['email'] or '-'}")
	print("=" * 75)
	print(f"Total contacts: {len(contacts)}")


def menu():
	print("=" * 75, "\nMenu")
	print("=" * 75)
	print("[1]. Add contact")
	print("[2]. Search contact")
	print("[3]. Delete contact")
	print("[4]. View contacts")
	print("[5]. Cancel")


def main():
	while True:
		menu()
		try:
			menu_opt = int(input("Choose option: "))
		except ValueError:
			print("Choose option ... 1-5")
			continue

		if menu_opt == 1:
			first_name = input("Enter contact's firstname: ")
			last_name = input("Enter contact's lastname: ")
			phone = input("Enter phone number: ")
			email = input("Enter email (optional): ")
			if add_contact(sys_storage, first_name, last_name, phone, email):
				print("Contact added")
			else:
				print("Couldn't add contact ... firstname, lastname and phone number are required")
		elif menu_opt == 2:
			search_dta = input("Enter contact name: ")
			search_contact(sys_storage, search_dta)
		elif menu_opt == 3:
			del_input = input("Enter contact name you want to delete: ")
			if delete_contact(sys_storage, del_input):
				print("Contact deleted")
			else:
				print("Contact not found")
		elif menu_opt == 4:
			view_contacts(sys_storage)
		elif menu_opt == 5:
			print("System terminating process")
			break
		else:
			print("Error 400 ... Choose option 1-5")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSystem terminating process")
		sys.exit(0)
