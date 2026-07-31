'''
Requirements
Core Features:
Ask the user how long they want their password (between 8-32 characters)

Ask what character types to include:

Uppercase letters (A-Z)

Lowercase letters (a-z)

Numbers (0-9)

Special characters (!@#$%^&*)

Generate a random password based on their choices

Display the generated password clearly

Ask if they want to generate another password

Advanced Features (Bonus):
Password strength indicator (Weak/Medium/Strong)

Save passwords to history (like your calculator!)

Copy password to clipboard (research pyperclip library)
'''
import random
import string
import pyperclip
import time
import datetime
import pprint
import json

#simulating external dbase
#stores every passwd generated
passwd_history = []	#simulating external dbase

def passwd_generator(passwd_history, _passwd):
	if _passwd >= 8 and _passwd <= 32:
		passwd_stru = string.ascii_letters + string.digits + string.punctuation
		rand_passwd = random.choice(string.ascii_uppercase)
		rand_passwd += random.choice(string.ascii_lowercase)
		rand_passwd += random.choice(string.digits)
		rand_passwd += random.choice(string.punctuation)

		for i in range(_passwd):
			rand_passwd += random.choice(passwd_stru)
		
		fin_passwd = list(rand_passwd)

		random.SystemRandom().shuffle(fin_passwd)
		rand_passwd = ''.join(fin_passwd)
		
		#creates a new dictionary for every password created
		passwd_history.append({"password": "", "time": ""})
		tm = time.time()
		dt = datetime.datetime.fromtimestamp(tm).strftime("%Y-%m-%d %H-%M-%S")
		passwd_history[-1]["password"] = rand_passwd
		passwd_history[-1]["time"] = dt

		#display password
		print("\n" + "+" + "-"*38 + "+")
		print(f"{'|'} {rand_passwd:<36} {'|'}")
		print("+" + "-"*38 + "+" + "\n")
		
		score = 0
		if len(rand_passwd) >= 12:
			score += 1
		if any(c.isupper() for c in rand_passwd):
			score += 1
		if any(c.islower() for c in rand_passwd):
			score += 1
		if any(c.isdigit() for c in rand_passwd):
			score += 1
		if any(c in string.punctuation for c in rand_passwd):
			score += 1
		
		if score <= 2:
			print("Weak Password")
		elif score <= 4:
			print("Medium Password")
		else:
			print("Strong Password")

		try:
			rsync_copy = input("Copy password:\ny/N\n")
		except ValueError:
			print("Error 400")
		
		if rsync_copy == "y" or rsync_copy == "Y":
			pyperclip.copy(passwd_history[-1]["password"])
		elif rsync_copy == "n" or rsync_copy == "N":
			return True
		else:
			return False

	else:
		print("\nPassword too long or too short\n")
	
def view_psswd_history(passwd_history):
	if not passwd_history:
		print("List Empty")
		return
	print("="*60 + "Password History" + "="*60)
	for entry in passwd_history:
		print(f"{entry['time']} | {entry['password']}")
	print("="*60)

def paste_to():
	clipboard_content = pyperclip.paste()
	if clipboard_content:
		print("\n" + "+" + "-"*38 + "+")
		print(f"| {clipboard_content:<36} |")
		print("+" + "-"*38 + "+")
	else:
		print("Clipboard Empty")

def stor_fil(passwd_history):
	try:
		json_fil = json.dumps(passwd_history, indent = 5)
		with open(input("Save file as: "), "w") as file:
			file.write(json_fil)
	except ValueError:
		return f"{ValueError}"

def menu():
	print("="*60 + "\nPassword Generator\n" + "="*60)
	print("[1]. Create Password")
	print("[2]. View Password History")
	print("[3]. View Copied Password")
	print("[4]. Store Data")
	print("[5]. Exit")
	print("="*60)

def main():
	while True:
		menu()
		try:
			main_opt = int(input("Choose Option: "))
		except ValueError:
			print("Choose Option 1-5")
			continue
		
		if main_opt == 1:
			try:
				_passwd = int(input("How long would you like your password to be: "))
			except ValueError:
				print("Password must be 8-32 longer")
				continue
			passwd_generator(passwd_history, _passwd)
			while True:
				try:
					_passwd_opt = input("Do you want to generate a new password: ").strip().upper()
				except ValueError:
					print("y/N")
					continue
				if _passwd_opt == "Y":
					passwd_generator(passwd_history, _passwd)
				elif _passwd_opt == "N":
					print("\nMake sure to change your password in a while\n")
					break
				
				else:
					print("Error 400")
					continue
						
		elif main_opt == 2:
			view_psswd_history(passwd_history)
		elif main_opt == 3:
			paste_to()
		elif main_opt == 4:
			stor_fil(passwd_history)
		elif main_opt == 5:
			print("System shutting-down")
			break
		else:
			print("Error 400")
			continue

if __name__ == "__main__":
	main()
