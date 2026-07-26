'''
Task Overview
Extend the Unit 5 grade classifier into a full grade report generator called grade_report.py. The program must process a list of student dictionaries (each with name and marks for three subjects), generate a grade and status for each student, and produce a full class summary report.

Requirements
• Store at least 5 students as a list of dictionaries: [{name, maths, english, science}, …]

• Use a for loop to iterate over all students and calculate each student’s average

• Apply the grade/status logic from Unit 5 inside the loop

• Build a results list of dictionaries containing: name, average, grade, status

• After the main loop, calculate: class average, highest mark, lowest mark

• Display a formatted class report showing individual results and class statistics

• Use a while loop to let the user search for a student by name after the report is shown
'''
stud_dbase = [
	{"name": "Mike Davis", "maths": 45, "english": 46, "science": 13},
	{"name": "Abraham Abdul", "maths": 98, "english": 62, "science": 87},
	{"name": "Ling Long", "maths": 13, "english": 50, "science": 50},
	{"name": "Senzo Mbatha", "maths": 1, "english": 9, "science": 3},
	{"name": "Victor Croch", "maths": 75, "english": 82, "science": 53}
]

def aver_calcu(stud_dbase):
	stud_result = []
	for dictionary in stud_dbase:
		stud_total = dictionary["maths"] + dictionary["english"] + dictionary["science"]
		aver = stud_total/3
		if aver >= 80:
			grade = "A"
		elif aver >= 70 and aver <= 79:
			grade = "B"
		elif aver >= 60 and aver <= 69:
			grade = "C"
		elif aver >= 50 and aver <= 59:
			grade = "D"
		else:
			grade = "F"
		status = "Pass" if grade != "F" else "Fail"
		stud_result.append({
			"name": dictionary["name"],
			"average": aver,
			"grade": grade,
			"status": status
		})
	return stud_result

def view_resul(stud_result):
	if not stud_result:
		print("\nResults not found")
		return
	print("="*65,"\nStudents Result")
	print("="*65)
	print(f"{'Name':<10} {'Average':<10} {'Grade':<10} {'Status':<10}")
	print("="*65)
	for dictionary in stud_result:
		print(f"{dictionary['name']:<10} {dictionary['average']:<10.1f} {dictionary['grade']:<10} {dictionary['status']}")
	print("="*65)
	
def class_aver(stud_result):
	if not stud_result:
		print("\nResults not found")
		return
	total_aver = sum(stud["average"] for stud in stud_result)/len(stud_result)
	highest = max(stud_result, key=lambda x: x["average"])
	lowest = min(stud_result, key=lambda x: x["average"])
	_pass = sum(1 for stud in stud_result if stud["status"] == "Pass")
	failure = len(stud_result) - _pass
	print("\n","="*65)
	print("Class Stats")
	print(f"Class average: {total_aver:.1f}%")
	print(f"Highest: {highest['name']} - {highest['average']:.1f}% ({highest['grade']})")
	print(f"Lowest: {lowest['name']} - {highest['average']:.1f}% ({lowest['grade']})")
	print(f"Passes: {_pass} ({_pass/len(stud_result)*100:.0f}%)")
	print(f"Failures: {failure} ({failure/len(stud_result)*100:.0f}%)")
	print("="*65)
	
def stud_repor(stud_result):
	if not stud_result:
		print("\nResult not found")
		return
	print("Individual Result")
	print("="*65)
	print(f"{'Name':<10} {'Maths':<10} {'English':<10} {'Science':<10} {'Avarage':<8} {'Grade':<10} {'Status'}")
	print("="*65)
	for student in stud_dbase:
		resul = next((stud for stud in stud_result if stud["name"] == student["name"]), None)
		if resul:
			print(f"{student['name']:<10} {student['maths']:<10} {student['english']:<10} {student['science']:<10} {resul['average']:<8.1f} {resul['grade']:<6} {resul['status']}")
			print("="*65)
			total_aver = sum(stud["average"] for stud in stud_result)/len(stud_result)
			highest = max(stud_result, key=lambda x: x["average"])
			lowest = min(stud_result, key=lambda x: x["average"])
			_pass = sum(1 for stud in stud_result if stud["status"] == "Pass")
			failure = len(stud_result) - _pass
			print("\nClass Summary")
			print(f"Total Students: {len(stud_result)}")
			print(f"Class Average: {total_aver:.1f}%")
			print(f"Highest: {highest['name']} - {highest['average']:.1f}% ({highest['grade']})")
			print(f"Lowest: {lowest['name']} - {lowest['average']:.1f}% ({lowest['grade']})")
			print(f"Pass Rate: {_pass/len(stud_result)*100:.0f}% ({_pass} student)")
			print(f"Fail Rate: {failures/len(stud_result)*100:.0f}% ({failures} students)")
			print("="*65)

def searc_stud(stud_result):
	if not stud_result:
		print("\nResult not found")
		return
	search_nam = input("\nEnter student name: ").strip().title()
	stud_tbl_schema = None
	for student in stud_dbase:
		if student["name"].lower() == search_nam.lower():
			stud_tbl_schema = student
			break
	result = None
	for student in stud_result:
		if student["name"].lower() == search_nam.lower():
			result = student
			break
	if result and stud_tbl_schema:
		print("\nStudent found")
		print("="*65)
		print(f"Maths: {stud_tbl_schema['maths']}")
		print(f"English: {stud_tbl_schema['english']}")
		print(f"Science: {stud_tbl_schema['science']}")
		print(f"Average: {result['average']:.1f}%")
		print(f"Grade: {result['grade']}")
		print(f"Status: {result['status']}")
		print("="*65)
	else:
		print(f"\nStudent '{search_nam}' not found")

def menu():
	print("="*60,"Student System")
	print("="*60)
	print("[1]. Calculate student's average marks")
	print("[2]. Show Results")
	print("[3]. Average System Calculations")
	print("[4]. Students' Report")
	print("[5]. Search Student")
	print("[6]. Exit")
	print("="*60)

def main():
	stud_result = []
	while True:
		menu()
		try:
			men_opt = int(input("Choose Option ... 1-6: "))
		except ValueError:
			print("Choose Option ... 1-6")
			continue
		if men_opt == 1:
			stud_result = aver_calcu(stud_dbase)
			print("\nAverage Score")
		elif men_opt == 2:
			view_resul(stud_result)
		elif men_opt == 3:
			  class_aver(stud_result)
		elif men_opt == 4:
			stud_repor(stud_result)
		elif men_opt == 5:
			searc_stud(stud_result)
		elif men_opt == 6:
			print("\nSystem shutting-down")
			break
		else:
			print("Error 400 ... Choose 1-6.")
		
		input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
