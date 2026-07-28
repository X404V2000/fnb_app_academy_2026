import random
import string
import pyperclip

passwd_dbase = []	#simulating external dbase

passwd_cache = []		#clipboard ///data removed when system shut-down

def passwd_generator(passwd_dbase, _passwd):
	if _passwd:
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
		passwd_dbase.append({"password": ""})
		passwd_dbase[-1]["password"] = rand_passwd
		
		#display password
		print("\n" + "+" + "-"*38 + "+")
		print(f"{'|'} {rand_passwd:<36} {'|'}")
		print("+" + "-"*38 + "+" + "\n")
		
		while True:
			_passwd_opt = input("Do you want to generate a new passwd: ")
			if _passwd_opt == "y" or _passwd_opt == "Y":
				passwd_dbase.append({"password": ""})
				passwd_dbase[-1]["password"] = rand_passwd
				
				#display password
				print("\n" + "+" + "-"*38 + "+")
				print(f"{'|'} {rand_passwd:<36} {'|'}")
				print("+" + "-"*38 + "+" + "\n")
			
			elif _passwd_opt == "n" or _passwd_opt == "N":
				print("Make sure to change your password in a while")
				break
			
			else:
				print("Error 400")
				continue
			
def copy_to(passwd_cache):
	if rand_passwd in passwd_dbase:
		while True:
			copy_opt = input("Would you like to copy this. y/N: ")
			if copy_opt == "y" or copy_opt == "Y":
				pyperclip.clear()
				pyperclip.copy(rand_passwd)
				break
			elif copy_opt == "n" or copy_opt == "N":
				break
			else:
				continue
		
#def passwd_varification():

def menu():
	print("="*60 + "\nPassword Genarator\n" + "="*60)
	print("[1]. Create Password")
	print("[2]. Copy Password to Clipboard")
	print("[3]. Exit")
	print("="*60)

def main():
	while True:
		menu()
		try:
			main_opt = int(input("Choose Option: "))
		except ValueError:
			print("Error 400")
			continue
		
		if main_opt == 1:
			_passwd = int(input("How long would you like your rand_passwd to be: "))
			passwd_generator(passwd_dbase, _passwd)
		elif main_opt == 2:
			copy_to(passwd_cache)
		else:
			print("Error 400")
			continue

if __name__ == "__main__":
	main()
