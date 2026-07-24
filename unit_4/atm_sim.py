sys_dbase = {"balance": 500}

def view_balance(sys_dbase):
	print(f"\nBalance: R{sys_dbase["balance"]}\n")

def withdraw_proc(sys_dbase,amount):
	if amount <= sys_dbase["balance"] and amount > 0:
		sys_dbase["balance"] = sys_dbase["balance"] - amount
		print(f"\nCurrent Balance: R{sys_dbase["balance"]}\n")

	elif amount > sys_dbase["balance"]:
		print(f"\nDeclined. Insufficient funds: R{sys_dbase["balance"]}\n")
	
	elif amount <= 0:
		print(f"\nWithdrawal amount must be above R0.00\nCurrent Balance: R{sys_dbase["balance"]}\n")

	else:
		return False

def menu():
	print("="*75,"\nSmart ATM System")
	print("="*75)
	print("[1]. View Balance")
	print("[2]. Withdraw")

def main():
	while True:
		menu()
		sys_opt = int(input("Choose option: "))
		if sys_opt ==1:
			view_balance(sys_dbase)

		elif sys_opt == 2:
			amount = float(input("Enter amount to withdraw: "))
			withdraw_proc(sys_dbase, amount)

		else:
			print("Error 400 ... Choose option 1-2")
if __name__ == "__main__":
	main()
