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
import creds
import smtplib
import ssl
from getpass import getpass
from fastapi import FastAPI
import random

app = FastAPI()

class creds:
	@app.get("/str/{sys_usrId}/{sys_usrPasswd}/{sys_usrEmail}")
	def _creds(sys_usrId: str, sys_usrPasswd: str, sys_usrEmail: str):
		#stores data from external file
		sys_email= creds.sys_email
		sys_usrId = creds.usr_id
		sys_usrPasswd = creds.usr_passwd
		sys_usrEmail = creds.email

class loginPage:	#if login pass
	@staticmethod
	def validateResponse(sys_usrId, sys_usrPasswd, main_usrName, main_usrPasswd):
		if main_usrName in sys_usrId and main_usrPasswd in sys_usrPasswd:
			# failResponse_menu
			print("="*60 + "\nOpenx\n" + "="*60)
			print("[1]. ")	#correct argument for main page
			print("[2]. ")	#correct argument for main page
			print("="*60)
		return False

class fail_loginPage:	#if login fail
	def failResponse_returnOutput(main_usrName, sys_usrId, main_usrPasswd, sys_usrPasswd):
		for entry in main_usrName and sys_usrId:
			if main_usrName not in sys_usrId and main_usrPasswd not in sys_usrPasswd:
				return 

class usr_AccReset:
	def usrnameValidating(sys_usrEmail: str) -> str:
		if '@' not in sys_usrEmail:
			return sys_usrEmail
		local_part, domain = sys_usrEmail.split('@')
		if len(local_part) <= 1:
			return sys_usrEmail
		masked_local = local_part[0] + '*' * (len(local_part) - 1)
		return f"{masked_local}@{domain}"

	@app.get("/value/{randomOTP}")	
	def genOTP(randomOTP: str = None):
		num = 6
		otpStructure = string.digits
		randomOPT = random.choice(string.digits)
		finalOutput = list(randomOTP)
		random.SystemRandom().shuffle(randomOTP)
		randomOTP = ''.join(finalOutput)

	@app.put("/value/{randomOTP}")
	def reset_loginPage(sys_email: str, sys_usrId: str, sys_usrEmail: str, rec_usrId: str):
		if rec_usrId in sys_id:
			try:
				port = 465
				smtp_server = smtp.gmail.com
				sender_email = sys_email
				sender_passwd = getpass("Enter password to continue: ")

				context = ssl.create_default_context()
				with smtplib.SMTP_SSL(
					smtp_server,
					port,
					context = context,
					) as server:
					server.login(sender_email, password)
					message = f"OTP [{randomOTP}]"
					server.sendmail(sender_email, sys_usrEmail, message)
				return {"OTP sent to you"}
			except Exception as e:
				return {"error": str(e)}

		else:
			print("Username not found")
			return False

	def reset_loginValidate(sys_usrPasswd, newPasswd):
		if newPasswd not in sys_usrPasswd:
			sys_usrPasswd = newPasswd
			if newPasswd in sys_usrPasswd:
				print("Successfully updated your password")
				return True
			else:
				print("Unsuccessful process")
				return False
		else:
			print("Password cannot be the same as old password")
			return True

	def menu():
		print("="*60 + "OpenX" + "="*60)
		print("[1]. Login")
		print("[2]. Forgot password")
		print("[3]. Exit")
		print("="*60)

	def main():
		sys_email = creds.sys_email if hasattr(creds, 'sys_email') else None
		sys_email = creds.usr_id if hasattr(creds, 'usr_id') else None
		sys_ursPasswd = creds.usr_passwd if hasattr(creds, 'usr_passwd') else None
		sys_usrEmail = creds.email if hasattr(creds, 'email') else None
		while True:
			print("Log in to OpenX")
			try:
				main_usrName = input("Enter username: ").strip()
				main_usrPasswd = input("Enter password: ").strip()
			except ValueError:
				print("Invalid details")
				continue
			
			if main_usrName and main_usrPasswd:
				menu()

				try:
					menuArg = int(input("Choose Option ... 1-4: "))
				except ValueError:
					print("Invalid details")
					continue

				if menuArg == 1:
					loginPage.validateResponse(sys_usrId, sys_usrPasswd, main_usrName, main_usrPasswd)
				elif menuArg == 2:
					usrnamValidate = input("Enter username to continue: ").strip()
					if usrnamValidate in sys_usrId:
						usrnameValidating(sys_usrEmail)
						print(f"OTP sent to\n{maske_email(maske_email)}")
						print("\n")

						otp_data = self.genOTP(None)
						generated_otp = otp_data["generated"]
						
						result = self.reset_loginPage(sys_email, sys_usrId, sys_usrEmail, rec_usrId)
						try:
							otpInput = int(input("Enter OTP: "))
						except ValueError:
							print("Invalid option")
							continue
						if str(otpInput) == generated_otp
							newPasswd = input("Create new password: ").strip()
							self.reset_loginValidate(sys_usrPasswd)
				elif menuArg == 3:
					print("System Shutting-down")
					break
				else:
					continue
			else:
				continue

__name__ == "__main__":
	app = usrAccReset()
	app.main()
