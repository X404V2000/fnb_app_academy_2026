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
import json

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

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
		print(f"\n{RED}" + "+" + "-"*38 + f"{RED}+{RESET}")
		print(f"{RED}{'|'} {rand_passwd:<36} {'|'}{RESET}")
		print(f"{RED}+" + "-"*38 + f"{RED}+{RESET}" + "\n")
		
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
			print(f"{RED}Weak Password{RESET}")
		elif score <= 4:
			print(f"{RED}Medium Password{RESET}")
		else:
			print(f"{RED}Strong Password{RESET}")

		try:
			rsync_copy = input(f"{GREEN}Copy password:\ny/N{RESET}\n")
		except ValueError:
			print(f"{RED}Error 400{RESET}")
		
		if rsync_copy == "y" or rsync_copy == "Y":
			pyperclip.copy(passwd_history[-1]["password"])
		elif rsync_copy == "n" or rsync_copy == "N":
			return True
		else:
			return False

	else:
		print(f"\n{RED}Password too long or too short{RESET}\n")
	
def view_psswd_history(passwd_history):
	if not passwd_history:
		print(f"{RED}List Empty{RESET}")
		return
	print(f"{RED}="*60 + "\nPassword History\n" + f"{RED}={RESET}"*60)
	for entry in passwd_history:
		print(f"{RED}{entry['time']} | {entry['password']}{RESET}")
	print(f"{RED}={RESET}"*60)

def paste_to():
	clipboard_content = pyperclip.paste()
	if clipboard_content:
		print(f"\n{RED}" + "+" + "-"*38 + f"{RED}+{RESET}")
		print(f"{RED}| {clipboard_content:<36} |{RESET}")
		print(f"{RED}+" + "-"*38 + f"{RED}+{RESET}")
	else:
		print(f"{RED}Clipboard Empty{RESET}")

def stor_fil(passwd_history):
	try:
		json_fil = json.dumps(passwd_history, indent = 5)
		with open(input(f"{GREEN}Save file as: {RESET}"), "w") as file:
			file.write(json_fil)
	except ValueError:
		print(f"{RED}Error 400{RESET}")

def menu():
	print(f"{RED}="*60 + f"\nPassword Generator\n" + f"{RED}={RESET}"*60)
	print(f"{RED}[1]{RESET}. {GREEN}Generate Password{RESET}")
	print(f"{RED}[2]{RESET}. {GREEN}View Password History{RESET}")
	print(f"{RED}[3]{RESET}. {GREEN}View Copied Password{RESET}")
	print(f"{RED}[4]{RESET}. {GREEN}Store Data{RESET}")
	print(f"{RED}[5]{RESET}. {GREEN}Exit{RESET}")
	print(f"{RED}={RESET}"*60)

def main():
	while True:
		menu()
		try:
			main_opt = int(input(f"{GREEN}Choose Option: {RESET}"))
		except ValueError:
			print(f"{RED}Choose Option 1-5{RESET}")
			continue
		
		if main_opt == 1:
			try:
				_passwd = int(input(f"{GREEN}How long would you like your password to be: {RESET}"))
			except ValueError:
				print("{RED}Password must be 8-32 longer{RESET}")
				continue
			passwd_generator(passwd_history, _passwd)
			while True:
				try:
					_passwd_opt = input(f"{GREEN}Do you want to generate a new password: {RESET}").strip().upper()
				except ValueError:
					print(f"{RED}y/N{RESET}")
					continue
				if _passwd_opt == "Y":
					try:
						_passwd = int(input(f"{GREEN}How long would you like your password to be: {RESET}"))
					except ValueError:
						print("{RED}Password must be 8-32 longer{RESET}")
						continue
					passwd_generator(passwd_history, _passwd)
				elif _passwd_opt == "N":
					print(f"\n{RED}Make sure to change your password in a while{RESET}\n")
					break
				
				else:
					print(f"{RED}Error 400{RESET}")
					continue
						
		elif main_opt == 2:
			view_psswd_history(passwd_history)
		elif main_opt == 3:
			paste_to()
		elif main_opt == 4:
			stor_fil(passwd_history)
		elif main_opt == 5:
			print(f"{RED}System shutting-down{RESET}")
			break
		else:
			print(f"{RED}Error 400{RESET}")
			continue

if __name__ == "__main__":
	main()

