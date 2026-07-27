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
num_history = []	#short-term storage to remember digit if usable

# addition function
def add_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "+":
		sys_op = float(num_1) + float(num_2)
		num_history.append(f"{float(num_1)} + {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# subtraction function
def sub_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "-":
		sys_op = float(num_1) - float(num_2)
		num_history.append(f"{float(num_1)} - {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# multiplication function
def mul_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "*":
		sys_op = float(num_1) * float(num_2)
		num_history.append(f"{float(num_1)} * {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

# division function
def div_func(num_1, add_op, num_2):
	if num_1 and num_2 and add_op == "/":
		sys_op = float(num_1) / float(num_2)
		num_history.append(f"{float(num_1)} / {float(num_2)} = {sys_op}")
		print(f"= {sys_op}\n")

def menu():
	print("="*60 + "\nCalculator\n" + "="*60)
	print("[1]. Calculate")
	print("[2]. Exit")
	print("\n" + "="*60)


def main():
	while True:
		print("="*60 + "\nCalculator\n" + "="*60)
		try:
			num_1 = input("Enter number: ").strip()
			add_op = input("")
			num_2 = input("Enter number: ").strip()

		except ValueError:
			print("Error 400")
			continue
		print("="*60)
		if add_op == "+":
			add_func(num_1, add_op, num_2)
		elif add_op == "-":
			sub_func(num_1, add_op, num_2)
		elif add_op == "*":
			mul_func(num_1, add_op, num_2)
		elif add_op == "/":
			div_func(num_1, add_op, num_2)
		elif num_1 == "c" or "C":
			break
		elif add_op == "c" or "C":
			break
		elif num_2 == "c" or "C":
			break
		else:
			continue
if __name__ == "__main__":
	main()
