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
import pprint

num_history = []	#short-term storage to remember digit if usable

# addition function
def add_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "+":
		sys_op = round((float(num_1) + float(num_2)), 2)
		num_history.append(f"{float(num_1)} + {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# subtraction function
def sub_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "-":
		sys_op = round((float(num_1) - float(num_2)), 2)
		num_history.append(f"{float(num_1)} - {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# multiplication function
def mul_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "*":
		sys_op = round((float(num_1) * float(num_2)), 2)
		num_history.append(f"{float(num_1)} * {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# division function
def div_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "/":
		if num_2 != "0":
			sys_op = round((float(num_1) / float(num_2)), 2)
			num_history.append(f"{float(num_1)} / {float(num_2)} = {sys_op}")
			print(f"= {sys_op}\n")
		else:
			print("Division by 0 is invalid")

# floor division
def fl_divfunc(num_1, add_op, num_2):
	if num_1 and num_2 or add_op == "//":
		if num_2 != "0":
			sys_op = round((float(num_1) // float(num_2)), 2)
			num_history.append(f"{float(num_1)} // {float(num_2)} = {sys_op}")
			print(f"= {sys_op}\n")
		else:
			print("Division by 0 is invalid")

# modules
def mod_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "%":
		sys_op = round((float(num_1) % float(num_2)), 2)
		num_history.append(f"{float(num_1)} % {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

def view_hist(num_history):
	print("="*60 + "\nHistory"+ " "*52 + "=\n" + "="*60)
	pprint.pprint(num_history)
	print("="*60)

def menu():
	print("="*60 + "\nCalculator"+ " "*49 + "=\n" + "="*60)
	print("[1]. Calculate")
	print("[2]. View history")
	print("[3]. Exit")
	print("\n" + "="*60)

def main():
	while True:
		menu()
		try:
			sys_opt = int(input("Choose option: "))
		except ValueError:
			print("Choose option 1-2")
			continue
		if sys_opt == 1:
			print("="*60 + "\nCalculator\n" + "="*60)
			try:
				num_1 = input("Enter number: ").strip()
				add_op = input("")
				num_2 = input("Enter number: ").strip()

			except ValueError:
				print("Error 400")
				continue

			if add_op == "+":
				add_func(num_1, add_op, num_2)
			elif add_op == "-":
				sub_func(num_1, add_op, num_2)
			elif add_op == "*":
				mul_func(num_1, add_op, num_2)
			elif add_op == "/":
				div_func(num_1, add_op, num_2)
			elif num_1.lower() == "c" or add_op.lower() == "c" or num_2.lower() == "c":
				print("Return to menu ...")
			else:
				continue
		elif sys_opt == 2:
			view_hist(num_history)
		elif sys_opt == 3:
			print("System shutting-down")
			break
		else:
			continue

if __name__ == "__main__":
	main()

	main()
