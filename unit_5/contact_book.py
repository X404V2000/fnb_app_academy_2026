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
import pprint

sys_storage = [
		{"name": "Nelson Nkosi", "contact": "0821234567", "email": "nelnkosi82@gmail.com"},
		{"name": "Kate Mohammad", "contact": "0739876543", "email": "kathee73@gmial.com"},
		{"name": "Devis Brown", "contact": "0715551234", "email": "Davisbrown71@gmial.com"},
		{"name": "Jackson Thwala", "contact": "0844445678", "email": "jackthwal84@gmial.com"}
]

def add_contact(sys_storage):
	first_name = str(input("Enter contact's firstname: ")).strip().title()
	last_name = str(input("Enter contact's lastname: ")).strip().title()
	con_number = input("Enter phone number: ").strip()
	email = str(input("Enter email: ")).strip()
	if first_name and last_name and con_number:
		ful_name = first_name+" "+last_name
		sys_storage.append({"name": ful_name, "contact": con_number, "email": email})
		print("Contact added")
		return True
	else:
		print("Couldn't add contact")
		return False

def search_contact(sys_storage, search_dta):
	for dictionary in sys_storage:
		if dictionary.get("name") == search_dta:	
			print("Contact for found")
			print(f"Name   : {dictionary['name']}")
			print(f"Contact: {dictionary['contact']}")
			print(f"Email  : {dictionary['email']}")
			return dictionary
	else:
		print("Data not found")
		return None

def view_contacts(sys_storage):
	pprint.pprint(sys_storage)

def del_contact(sys_storage, del_input):
	for i, d in enumerate(sys_storage):
		if d["name"] == del_input:
			del sys_storage[i]
			print("Contact deleted")
			return True
	print("Contact not found")

def menu():
	print("="*75,"\nMenu")
	print("="*75)
	print("[1]. Add contact")
	print("[2]. Search contact")
	print("[3]. View contacts")
	print("[4]. Delete contact")
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
			add_contact(sys_storage)
		elif menu_opt == 2:
			search_dta = str(input("Enter user name: ")).strip().title()
			search_contact(sys_storage, search_dta)
		elif menu_opt == 3:
			view_contacts(sys_storage)
		elif menu_opt == 4:
			del_input = str(input("Enter contact name you want to delete: ")).strip().title()
			del_contact(sys_storage, del_input)
		elif menu_opt == 5:
			print("System terminating process")
			break
		else:
			print("Error 400 ... Choose option 1-4")
if __name__ == "__main__":
	main()
