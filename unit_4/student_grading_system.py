stud_dbase = {
	"stud_name": "",
	"stud_surn": "",
	"Subject": ["","",""],
	"Final %": [0,0,0],
	"Grade": ["","",""],
	"Average": [0]
}		#stores all students report

# main function
def std_nam_surnam(stud_dbase, input_for_studNam, input_for_studSurn):
	if input_for_studNam and input_for_studSurn:
		stud_dbase["stud_name"] = input_for_studNam
		stud_dbase["stud_surn"] = input_for_studSurn
	else:
		print("Error 400")

# second layer function
def sub_modify(stud_dbase):		
	# store subject in stud_dbase["Subject"]
	stud_dbase["Subject"][0] = str(input(f"Enter student's subject: ")).strip().upper()
	stud_dbase["Subject"][1] = str(input(f"Enter student's subject: ")).strip().upper()
	stud_dbase["Subject"][2] = str(input(f"Enter student's subject: ")).strip().upper()

def grad_modify(stud_dbase):
	# store grades in stud_dbase["Final %"]
	stud_dbase["Final %"][0] = int(input(f"Enter student's grade for {stud_dbase["Subject"][0]}: "))
	stud_dbase["Final %"][1] = int(input(f"Enter student's grade for {stud_dbase["Subject"][1]}: "))
	stud_dbase["Final %"][2] = int(input(f"Enter student's grade for {stud_dbase["Subject"][2]}: "))
	
def grad_avar(stud_dbase):
	avg_grd = ((stud_dbase["Final %"][0] + stud_dbase["Final %"][1] + stud_dbase["Final %"][2])/3)*(100/100)
	stud_dbase["Average"] = avg_grd
	
# third layer function to auto calculate grading
def third_layer_grad(stud_dbase):
	# determine pass grading
	if stud_dbase["Final %"][0] >= 80 and stud_dbase["Final %"][0] <= 100:
	    stud_dbase["Grade"][0] = "A"
	elif stud_dbase["Final %"][0] >= 70 and stud_dbase["Final %"][0] <= 79:
	    stud_dbase["Grade"][0] = "B"
	elif stud_dbase["Final %"][0] >= 60 and stud_dbase["Final %"][0] <= 69:
	    stud_dbase["Grade"][0] = "C"
	elif stud_dbase["Final %"][0] >= 50 and stud_dbase["Final %"][0] <= 59:
	    stud_dbase["Grade"][0] = "D"
	elif stud_dbase["Final %"][0] >= 0 and stud_dbase["Final %"][0] <= 49:
	    stud_dbase["Grade"][0] = "F"
	else:
	    return False

	if stud_dbase["Final %"][1] >= 80 and stud_dbase["Final %"][1] <= 100:
	    stud_dbase["Grade"][1] = "A"
	elif stud_dbase["Final %"][1] >= 70 and stud_dbase["Final %"][1] <= 79:
	    stud_dbase["Grade"][1] = "B"
	elif stud_dbase["Final %"][1] >= 60 and stud_dbase["Final %"][1] <= 69:
	    stud_dbase["Grade"][1] = "C"
	elif stud_dbase["Final %"][1] >= 50 and stud_dbase["Final %"][1] <= 59:
	    stud_dbase["Grade"][1] = "D"
	elif stud_dbase["Final %"][1] >= 0 and stud_dbase["Final %"][1] <= 49:
	    stud_dbase["Grade"][1] = "F"
	else:
	    return False

	if stud_dbase["Final %"][2] >= 80 and stud_dbase["Final %"][2] <= 100:
	    stud_dbase["Grade"][2] = "A"
	elif stud_dbase["Final %"][2] >= 70 and stud_dbase["Final %"][2] <= 79:
	    stud_dbase["Grade"][2] = "B"
	elif stud_dbase["Final %"][2] >= 60 and stud_dbase["Final %"][2] <= 69:
	    stud_dbase["Grade"][2] = "C"
	elif stud_dbase["Final %"][2] >= 50 and stud_dbase["Final %"][2] <= 59:
	    stud_dbase["Grade"][2] = "D"
	elif stud_dbase["Final %"][2] >= 0 and stud_dbase["Final %"][2] <= 49:
	    stud_dbase["Grade"][2] = "F"
	else:
	    return False	

third_layer_grad(stud_dbase)

def report(stud_dbase):
	print(f"Name: {stud_dbase["stud_name"]}\nSurname: {stud_dbase["stud_surn"]}")
	print(f"Subject: {stud_dbase["Subject"][0]} | {stud_dbase["Subject"][1]} | {stud_dbase["Subject"][2]} |")
	print(f"Final %: {stud_dbase["Final %"][0]} | {stud_dbase["Final %"][1]} | {stud_dbase["Final %"][2]} |")
	spacing = " "*20
	print(f"{spacing} [Average Grade: {stud_dbase["Average"]}]") 

# menu
def grad_menu():
	print("Main Menu")
	print("="*100)
	print("[1]. Insert Student Name and Surname")
	print("[2]. Insert Student Subject")
	print("[3]. Insert Student Marks")
	print("[4]. Calculate Average Marks")
	print("[5]. Show report")

def main_loop(stud_dbase):
	print("="*100)
	while True:
		grad_menu()	#show main menu
		menu_opt = int(input("Choose option: "))
		
		if menu_opt == 1:
			input_for_studNam = str(input("Enter student name: ")).strip().upper()
			input_for_studSurn = str(input("Enter student surname: ")).strip().upper()
			std_nam_surnam(stud_dbase, input_for_studNam, input_for_studSurn)
		elif menu_opt == 2:
			sub_modify(stud_dbase)
		elif menu_opt == 3:
			grad_modify(stud_dbase)
		elif menu_opt == 4:
			grad_avar(stud_dbase)
		elif menu_opt == 5:
			report(stud_dbase)
		else:
			print("Error 400\nChoose option 1-5")
		input("Press enter to return to menu")
if __name__ == "__main__":
	main_loop(stud_dbase)
