'''
The Challenge: “The Smart ATM Withdrawal Simulator”
Simulate a bank transaction checking if a user has enough money.

1. Set a fixed variable representing a bank balance, for example: balance = 500.

2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).

3. If the request is less than or equal to the balance, deduct the amount and print:
“Withdrawal successful! Remaining balance: RX”.

4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.

5. Otherwise (else), print: “Declined. Insufficient funds”
'''
import sys

STARTING_BALANCE = 500

sys_dbase = {"balance": STARTING_BALANCE}


# Pure business logic — kept separate so it is easy to test.
def withdraw(balance, amount):
	"""Return (message, new_balance) for a withdrawal request.

	The balance only changes when the withdrawal is successful.
	"""
	if amount <= 0:
		return "Invalid amount. You must withdraw more than R0.00", balance
	if amount > balance:
		return "Declined. Insufficient funds", balance
	return "Withdrawal successful!", round(balance - amount, 2)


def view_balance(sys_dbase):
	print(f"\nBalance: R{sys_dbase['balance']:.2f}\n")


def withdraw_proc(sys_dbase, amount):
	message, new_balance = withdraw(sys_dbase["balance"], amount)
	print(f"\n{message}")
	if message == "Withdrawal successful!":
		sys_dbase["balance"] = new_balance
		print(f"Remaining balance: R{new_balance:.2f}")
	else:
		print(f"Balance unchanged: R{new_balance:.2f}")
	print()


def menu():
	print("=" * 75, "\nSmart ATM System")
	print("=" * 75)
	print("[1]. View Balance")
	print("[2]. Withdraw")
	print("[3]. Exit")


def ask_amount():
	"""Keep asking until the user types a valid number."""
	while True:
		raw = input("Enter amount to withdraw: ").strip()
		try:
			return float(raw)
		except ValueError:
			print("Please enter a valid amount (e.g. 150 or 99.50).")


def main():
	while True:
		menu()
		try:
			sys_opt = int(input("Choose option: "))
		except ValueError:
			print("Error 400 ... Choose option 1-3")
			continue

		if sys_opt == 1:
			view_balance(sys_dbase)
		elif sys_opt == 2:
			withdraw_proc(sys_dbase, ask_amount())
		elif sys_opt == 3:
			print("Thank you for banking with us. Goodbye!")
			break
		else:
			print("Error 400 ... Choose option 1-3")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSession closed. Goodbye!")
		sys.exit(0)
