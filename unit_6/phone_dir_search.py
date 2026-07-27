'''
The Challenge: “The Phone Directory Search”
Create a mini data directory using a List and a Dictionary combined.

1. Create a dictionary called contacts where the Keys are friend names and the Values are their phone numbers (keep phone numbers as strings so the leading 0 doesn’t drop off, e.g., “0821112222”). Fill it with 3 people.

2. Ask the user to input the name of the friend they want to look up.

3. Use a conditional check to see if the name matches a key. If it exists, pull out and print their number: “Found! [Name]’s number is [Number]”.

4. Otherwise, print “Contact not found.”
'''
contacts = {
	"Jonathan": "0870634512",
	"Victor": "0691341245",
	"Mandla": "0780695478",
	"Abdul": "0730012839"
}

def call_operator(contacts, cell_search):
	print("processing request ...\n")
	if cell_search in contacts:
		print(f"Contact found ... number ({contacts[cell_search]})")
		return True
	else:
		print(f"Contact not found ... {cell_search} does not exist")
		return False

def view_all(contacts):
	print("="*60,"\nContacts","\n","="*60)
	for nam, num in contacts.items():
		print(f"{nam}: {num}")
		print("="*60)

def menu():
	print("="*60,f"\nMobileX")
	print("="*60)
	print("[1]. Search phone number")
	print("[2]. View contacts")
	print("[3]. Cancel")
	print("\n")
	print("="*60)

def main():
	while True:
		menu()
		try:
			call_opt = int(input("Choose option: "))
		except ValueError:
			print("Choose option ... 1-3")
			continue
		if call_opt == 1:
			cell_search = input("Enter contact's name: ").strip().title()
			call_operator(contacts, cell_search)
		elif call_opt == 2:
			view_all(contacts)
		elif call_opt == 3:
			print("System shutting-down")
			break
		else:
			print("Error 400 ... Choose option 1-3")
if __name__ == "__main__":
	main()
