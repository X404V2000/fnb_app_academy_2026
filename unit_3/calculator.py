'''
Task Overview
Multi-Function Calculator
Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.

Requirements
Use float(input()) to collect two numbers from the user
Calculate and display: addition, subtraction, multiplication, division
Calculate and display: floor division (//) and modulus (%)
Round all results to 2 decimal places using round()
Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
Display all results in a formatted table using f-strings
'''
import sys

OPERATORS = ("+", "-", "*", "/", "//", "%")

num_history = []  # short-term storage of every calculation performed


# Pure calculation helpers — kept separate so they are easy to test.
def calculate(num_1, operator, num_2):
	"""Return the rounded result of num_1 <operator> num_2.

	Raises ZeroDivisionError when the operator needs division and num_2 is 0.
	Raises ValueError for an unknown operator.
	"""
	if operator not in OPERATORS:
		raise ValueError(f"Unsupported operator: {operator}")
	if operator in ("/", "//", "%") and num_2 == 0:
		raise ZeroDivisionError("Division by 0 is invalid")

	if operator == "+":
		result = num_1 + num_2
	elif operator == "-":
		result = num_1 - num_2
	elif operator == "*":
		result = num_1 * num_2
	elif operator == "/":
		result = num_1 / num_2
	elif operator == "//":
		result = num_1 // num_2
	else:  # "%"
		result = num_1 % num_2

	return round(result, 2)


def view_hist(num_history):
	print("=" * 60 + "\nHistory\n" + "=" * 60)
	if not num_history:
		print("(no calculations yet)")
	else:
		for entry in num_history:
			print(entry)
	print("=" * 60)


def menu():
	print("=" * 60 + "\nCalculator\n" + "=" * 60)
	print("[1]. Calculate")
	print("[2]. View history")
	print("[3]. Exit")
	print("\n" + "=" * 60)


def ask_number(prompt):
	"""Keep asking until the user types a valid float. Returns None if cancelled."""
	while True:
		raw = input(prompt).strip()
		if raw.lower() == "c":
			return None
		try:
			return float(raw)
		except ValueError:
			print("Please enter a valid number (or 'c' to cancel).")


def ask_operator():
	"""Keep asking until the user types a supported operator. Returns None if cancelled."""
	while True:
		raw = input("Enter operator (+, -, *, /, //, %): ").strip()
		if raw.lower() == "c":
			return None
		if raw in OPERATORS:
			return raw
		print("Please enter one of: " + " ".join(OPERATORS))


def main():
	print("=" * 60 + "\nCalculator\n" + "=" * 60)
	while True:
		menu()
		try:
			sys_opt = int(input("Choose option: "))
		except ValueError:
			print("Choose option 1-3")
			continue

		if sys_opt == 1:
			num_1 = ask_number("Enter number: ")
			if num_1 is None:
				print("Return to menu ...")
				continue
			add_op = ask_operator()
			if add_op is None:
				print("Return to menu ...")
				continue
			num_2 = ask_number("Enter number: ")
			if num_2 is None:
				print("Return to menu ...")
				continue

			try:
				sys_op = calculate(num_1, add_op, num_2)
			except ZeroDivisionError:
				print("\nDivision by 0 is invalid\n")
				continue

			num_history.append(f"{num_1} {add_op} {num_2} = {sys_op}")
			print("\n+----------------------------------+")
			print(f"| {'Operation':<13} {'Result':>14} |")
			print("+----------------------------------+")
			print(f"| {f'{num_1} {add_op} {num_2}':<13} {sys_op:>14} |")
			print("+----------------------------------+\n")

		elif sys_opt == 2:
			view_hist(num_history)
		elif sys_opt == 3:
			print("System shutting-down")
			break
		else:
			print("Choose option 1-3")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSystem shutting-down")
		sys.exit(0)
