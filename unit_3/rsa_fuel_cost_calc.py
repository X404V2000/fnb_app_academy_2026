'''
The Challenge: “The South African Fuel Cost Calculator”
With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:

1. Ask the user how many kilometers they want to drive.

2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).

3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
(Formula: liters_needed = kilometers / 10).

4. Calculate the total cost (liters_needed * petrol_price).

5. Use type casting to ensure your numbers work, and use round() to format the
final cost to 2 decimal places.
'''
import sys

KM_PER_LITER = 10

# None means "not entered yet", so we never show a misleading R0 total.
fuel_dbase = {"kilometers": None, "fuel_price": None}


# Pure calculation helpers — kept separate so they are easy to test.
def liters_needed(kilometers):
	"""A car uses 1 liter of fuel for every 10 km driven."""
	return kilometers / KM_PER_LITER


def total_cost(kilometers, fuel_price):
	"""Total fuel cost, rounded to 2 decimal places."""
	return round(liters_needed(kilometers) * fuel_price, 2)


def ask_positive_float(prompt):
	"""Keep asking until the user types a number greater than zero."""
	while True:
		raw = input(prompt).strip()
		try:
			value = float(raw)
		except ValueError:
			print("Please enter a valid decimal number (e.g. 22.45).")
			continue
		if value <= 0:
			print("Value must be greater than 0.")
			continue
		return value


def kl_func(fuel_dbase):
	fuel_dbase["kilometers"] = round(ask_positive_float("[1]. Enter your kilometers: "), 2)
	return True


def petrol_pr(fuel_dbase):
	fuel_dbase["fuel_price"] = round(ask_positive_float("[2]. Enter current petrol price per liter: "), 2)
	return True


def fuel_calc(fuel_dbase):
	print("=" * 60 + "\nRSA Fuel Cost\n" + "=" * 60)
	kl = fuel_dbase["kilometers"]
	fp = fuel_dbase["fuel_price"]

	if kl is None or fp is None:
		print("Please enter the kilometers and the petrol price first.")
		print("=" * 60)
		return

	liters = liters_needed(kl)
	index_3 = total_cost(kl, fp)

	print(f"{'Kilometers':<15} {'Fuel Price':<15} {'Litres':<10} {'Cost'}")
	print("-" * 60)
	print(f"{kl:<15} R{fp:<14.2f} {liters:<10.2f} R{index_3:.2f}")
	print("=" * 60)


def menu():
	print("=" * 60 + "\nRSA Fuel Cost Calculator\n" + "=" * 60)
	print("[1]. Enter your kilometers" + (" (done)" if fuel_dbase["kilometers"] is not None else ""))
	print("[2]. Enter current petrol price per liter" + (" (done)" if fuel_dbase["fuel_price"] is not None else ""))
	print("[3]. Show total cost")
	print("[4]. Exit")
	print("=" * 60)


def main():
	while True:
		menu()
		try:
			main_opt = int(input("Choose Option: "))
		except ValueError:
			print("Choose Option 1-4")
			continue

		if main_opt == 1:
			kl_func(fuel_dbase)
		elif main_opt == 2:
			petrol_pr(fuel_dbase)
		elif main_opt == 3:
			fuel_calc(fuel_dbase)
		elif main_opt == 4:
			print("System shutting-down")
			break
		else:
			print("Choose Option 1-4")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSystem shutting-down")
		sys.exit(0)
