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
import datetime
import json
import secrets
import string
import sys

# pyperclip is optional: without it everything else still works.
try:
	import pyperclip
	CLIPBOARD_AVAILABLE = True
except ImportError:
	pyperclip = None
	CLIPBOARD_AVAILABLE = False

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

MIN_LENGTH = 8
MAX_LENGTH = 32

SPECIAL_CHARS = "!@#$%^&*"
CHARACTER_SETS = {
	"uppercase": string.ascii_uppercase,
	"lowercase": string.ascii_lowercase,
	"numbers": string.digits,
	"special": SPECIAL_CHARS,
}

# simulating external dbase
# stores every passwd generated
passwd_history = []  # simulating external dbase


# Pure helper functions — kept separate so they are easy to test.
def build_character_pool(types):
	"""Combine the chosen character sets into one pool."""
	pool = ""
	for name in types:
		pool += CHARACTER_SETS[name]
	return pool


def generate_password(length, types):
	"""Generate a password of `length` using at least one character from each chosen type.

	Raises ValueError for an invalid length or no chosen character types.
	"""
	if not MIN_LENGTH <= length <= MAX_LENGTH:
		raise ValueError(f"Password must be {MIN_LENGTH}-{MAX_LENGTH} characters long")
	if not types:
		raise ValueError("Choose at least one character type")

	# Guarantee one character of every chosen type (the requirement), then fill the rest.
	password = [secrets.choice(CHARACTER_SETS[name]) for name in types]
	pool = build_character_pool(types)
	while len(password) < length:
		password.append(secrets.choice(pool))

	# Shuffle with a SystemRandom so the guaranteed characters aren't always first.
	secrets.SystemRandom().shuffle(password)
	return "".join(password)


def strength_score(password):
	"""Score 0-5: length >= 12, upper, lower, digit and special character each add 1."""
	score = 0
	if len(password) >= 12:
		score += 1
	if any(c.isupper() for c in password):
		score += 1
	if any(c.islower() for c in password):
		score += 1
	if any(c.isdigit() for c in password):
		score += 1
	if any(c in SPECIAL_CHARS for c in password):
		score += 1
	return score


def strength_label(score):
	if score <= 2:
		return "Weak"
	if score <= 4:
		return "Medium"
	return "Strong"


def strength_color(label):
	return {"Weak": RED, "Medium": YELLOW, "Strong": GREEN}[label]


# --- interactive helpers -------------------------------------------------
def ask_yes_no(prompt):
	"""Ask a y/N question. Returns True for yes, False for no."""
	while True:
		answer = input(prompt).strip().lower()
		if answer in ("y", "yes"):
			return True
		if answer in ("n", "no", ""):
			return False
		print(f"{RED}Please answer y or n{RESET}")


def ask_length():
	while True:
		raw = input(f"{GREEN}How long would you like your password to be ({MIN_LENGTH}-{MAX_LENGTH}): {RESET}").strip()
		try:
			length = int(raw)
		except ValueError:
			print(f"{RED}Password must be a number between {MIN_LENGTH} and {MAX_LENGTH}{RESET}")
			continue
		if MIN_LENGTH <= length <= MAX_LENGTH:
			return length
		print(f"{RED}Password must be {MIN_LENGTH}-{MAX_LENGTH} characters long{RESET}")


def ask_character_types():
	"""Ask which character types to include (all four are on by default)."""
	print(f"{GREEN}Include character types? (Enter = yes){RESET}")
	types = []
	for name, chars in CHARACTER_SETS.items():
		example = "A-Z" if name == "uppercase" else "a-z" if name == "lowercase" else "0-9" if name == "numbers" else SPECIAL_CHARS
		if ask_yes_no(f"  {name.title()} ({example})? [Y/n] "):
			types.append(name)
	if not types:
		print(f"{YELLOW}No types chosen, using all of them{RESET}")
		types = list(CHARACTER_SETS)
	if "special" not in types:
		print(f"{YELLOW}Note: without special characters some sites reject the password{RESET}")
	return types


def passwd_generator(passwd_history, _passwd, types=None):
	if types is None:
		types = list(CHARACTER_SETS)
	try:
		rand_passwd = generate_password(_passwd, types)
	except ValueError as error:
		print(f"\n{RED}{error}{RESET}\n")
		return False

	# creates a new dictionary for every password created
	passwd_history.append({
		"password": rand_passwd,
		"time": datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
	})

	score = strength_score(rand_passwd)
	label = strength_label(score)
	color = strength_color(label)

	# display password
	print(f"\n{RED}+" + "-" * 38 + f"+{RESET}")
	print(f"{RED}| {rand_passwd:<36} |{RESET}")
	print(f"{RED}+" + "-" * 38 + f"+{RESET}")
	print(f"{color}{label} Password{RESET} ({score}/5: length, upper, lower, digit, special)\n")

	if CLIPBOARD_AVAILABLE:
		if ask_yes_no(f"{GREEN}Copy password to clipboard? (y/N) {RESET}"):
			try:
				pyperclip.copy(rand_passwd)
				print(f"{GREEN}Copied to clipboard{RESET}")
			except pyperclip.PyperclipException:
				print(f"{RED}Clipboard not available in this environment{RESET}")
	else:
		print(f"{YELLOW}Clipboard support disabled (install pyperclip to enable){RESET}")
	return True


def view_psswd_history(passwd_history):
	if not passwd_history:
		print(f"{RED}List Empty{RESET}")
		return
	print(f"{RED}=" * 60 + f"\nPassword History\n" + f"{RED}={RESET}" * 60)
	for entry in passwd_history:
		print(f"{RED}{entry['time']} | {entry['password']}{RESET}")
	print(f"{RED}={RESET}" * 60)


def paste_to():
	if not CLIPBOARD_AVAILABLE:
		print(f"{YELLOW}Clipboard support disabled (install pyperclip to enable){RESET}")
		return
	try:
		clipboard_content = pyperclip.paste()
	except pyperclip.PyperclipException:
		print(f"{RED}Clipboard not available in this environment{RESET}")
		return
	if clipboard_content:
		print(f"\n{RED}+" + "-" * 38 + f"+{RESET}")
		print(f"{RED}| {clipboard_content:<36} |{RESET}")
		print(f"{RED}+" + "-" * 38 + f"+{RESET}")
	else:
		print(f"{RED}Clipboard Empty{RESET}")


def stor_fil(passwd_history):
	if not passwd_history:
		print(f"{RED}List Empty ... nothing to save{RESET}")
		return
	file_name = input(f"{GREEN}Save file as: {RESET}").strip() or "passwords.json"
	try:
		with open(file_name, "w", encoding="utf-8") as file:
			json.dump(passwd_history, file, indent=5)
		print(f"{GREEN}Saved {len(passwd_history)} password(s) to {file_name}{RESET}")
	except OSError as error:
		print(f"{RED}Could not save file: {error}{RESET}")


def menu():
	print(f"{RED}=" * 60 + f"\nPassword Generator\n" + f"{RED}={RESET}" * 60)
	print(f"{RED}[1]{RESET}. {GREEN}Generate Password{RESET}")
	print(f"{RED}[2]{RESET}. {GREEN}View Password History{RESET}")
	print(f"{RED}[3]{RESET}. {GREEN}View Copied Password{RESET}")
	print(f"{RED}[4]{RESET}. {GREEN}Store Data{RESET}")
	print(f"{RED}[5]{RESET}. {GREEN}Exit{RESET}")
	print(f"{RED}={RESET}" * 60)


def main():
	while True:
		menu()
		try:
			main_opt = int(input(f"{GREEN}Choose Option: {RESET}"))
		except ValueError:
			print(f"{RED}Choose Option 1-5{RESET}")
			continue

		if main_opt == 1:
			types = ask_character_types()
			while True:
				passwd_generator(passwd_history, ask_length(), types)
				if not ask_yes_no(f"{GREEN}Do you want to generate a new password? (y/N) {RESET}"):
					print(f"\n{RED}Make sure to change your password in a while{RESET}\n")
					break
				if ask_yes_no(f"{GREEN}Change character types? (y/N) {RESET}"):
					types = ask_character_types()

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
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print(f"\n{RED}System shutting-down{RESET}")
		sys.exit(0)
