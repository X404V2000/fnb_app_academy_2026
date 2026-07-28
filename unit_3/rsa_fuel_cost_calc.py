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

fuel_dbase = [{"kilometers": 0, "fuel_price": 0, "total_price": 0}]

def kl_func(fuel_dbase):
	main_1 = float(input(f"[1]. Enter your kilometers: \n"))
	fuel_dbase[0]["kilometers"] = round(main_1, 2)
	return True

def petrol_pr(fuel_dbase):
	main_2 = float(input(f"[2]. Enter current petrol price per liter: \n"))
	fuel_dbase[0]["fuel_price"] = round(main_2, 2)
	return True

def fuel_calc(fuel_dbase):
	print("="*60 + "=\nRSA Fuel Cost\n" + "="*60)
	print(f"{'Kilometers':<15} {'Fuel Price':<15} {'Cost Price'}")
	kl = fuel_dbase[0]['kilometers']
	fp = fuel_dbase[0]['fuel_price']
	index_3 = kl * fp
	print(f"{kl:<15} R{fp:<14} R{index_3}")
	print("="*60)

def menu():
	print("="*60 + "\nRSA Fuel Cost Calculator\n" + "="*60)
	print("[1]. Enter your kilometers")
	print("[2]. Enter current petrol price per liter")
	print("[3]. Show total cost")
	print("[4]. Exit")
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
			kl_func(fuel_dbase)
		elif main_opt == 2:
			petrol_pr(fuel_dbase)
		elif main_opt == 3:
			fuel_calc(fuel_dbase)
		elif main_opt == 4:
			break
		else:
			print("Choose Option 1-3")
			continue

if __name__ == "__main__":
	main()
