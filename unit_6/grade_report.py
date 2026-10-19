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
import sys

SUBJECTS = ("maths", "english", "science")
WIDTH = 80

stud_dbase = [
	{"name": "Mike Davis", "maths": 45, "english": 46, "science": 13},
	{"name": "Abraham Abdul", "maths": 98, "english": 62, "science": 87},
	{"name": "Ling Long", "maths": 13, "english": 50, "science": 50},
	{"name": "Senzo Mbatha", "maths": 1, "english": 9, "science": 3},
	{"name": "Victor Croch", "maths": 75, "english": 82, "science": 53},
]


# Pure calculation helpers — kept separate so they are easy to test.
def letter_grade(average):
	if average >= 80:
		return "A"
	if average >= 70:
		return "B"
	if average >= 60:
		return "C"
	if average >= 50:
		return "D"
	return "F"


def aver_calcu(stud_dbase):
	"""Build the results list: [{name, average, grade, status}, ...]"""
	stud_result = []
	for student in stud_dbase:
		average = sum(student[s] for s in SUBJECTS) / len(SUBJECTS)
		grade = letter_grade(average)
		stud_result.append({
			"name": student["name"],
			"average": average,
			"grade": grade,
			"status": "Pass" if grade != "F" else "Fail",
		})
	return stud_result


def class_stats(stud_result):
	"""Return a dictionary of class-wide statistics."""
	averages = [stud["average"] for stud in stud_result]
	passed = sum(1 for stud in stud_result if stud["status"] == "Pass")
	total = len(stud_result)
	return {
		"count": total,
		"class_average": sum(averages) / total,
		"highest": max(stud_result, key=lambda x: x["average"]),
		"lowest": min(stud_result, key=lambda x: x["average"]),
		"passed": passed,
		"failed": total - passed,
	}


def find_student(stud_result, name):
	search = name.strip().lower()
	for student in stud_result:
		if student["name"].lower() == search:
			return student
	return None


# --- reporting -----------------------------------------------------------
def view_resul(stud_result):
	if not stud_result:
		print("\nResults not found ... run option 1 first")
		return
	print("=" * WIDTH, "\nStudents Result")
	print("=" * WIDTH)
	print(f"{'Name':<20} {'Average':>8} {'Grade':>7} {'Status'}")
	print("=" * WIDTH)
	for student in stud_result:
		print(f"{student['name']:<20} {student['average']:>8.1f} {student['grade']:>7} {student['status']}")
	print("=" * WIDTH)


def class_aver(stud_result):
	if not stud_result:
		print("\nResults not found ... run option 1 first")
		return
	stats = class_stats(stud_result)
	print("\n", "=" * WIDTH)
	print("Class Stats")
	print(f"Class average : {stats['class_average']:.1f}%")
	print(f"Highest       : {stats['highest']['name']} - {stats['highest']['average']:.1f}% ({stats['highest']['grade']})")
	print(f"Lowest        : {stats['lowest']['name']} - {stats['lowest']['average']:.1f}% ({stats['lowest']['grade']})")
	print(f"Passes        : {stats['passed']} ({stats['passed'] / stats['count'] * 100:.0f}%)")
	print(f"Failures      : {stats['failed']} ({stats['failed'] / stats['count'] * 100:.0f}%)")
	print("=" * WIDTH)


def stud_repor(stud_result):
	if not stud_result:
		print("\nResult not found ... run option 1 first")
		return
	results = {stud["name"]: stud for stud in stud_result}
	print("Individual Result")
	print("=" * WIDTH)
	print(f"{'Name':<13} {'Maths':<7} {'English':<9} {'Science':<9} {'Average':<9} {'Grade':<7} {'Status'}")
	print("=" * WIDTH)
	for student in stud_dbase:
		resul = results.get(student["name"])
		if resul:
			print(f"{student['name']:<13} {student['maths']:<7} {student['english']:<9} "
			      f"{student['science']:<9} {resul['average']:<9.1f} {resul['grade']:<7} {resul['status']}")
	print("=" * WIDTH)
	class_aver(stud_result)


def searc_stud(stud_result):
	if not stud_result:
		print("\nResult not found ... run option 1 first")
		return
	search_nam = input("\nEnter student name (or press Enter to stop): ").strip()
	if not search_nam:
		return
	ress = find_student(stud_result, search_nam)
	if not ress:
		print(f"\nStudent '{search_nam.title()}' not found")
		return

	raw = next(stud for stud in stud_dbase if stud["name"].lower() == search_nam.lower())
	print("\nStudent found")
	print("=" * WIDTH)
	for subject in SUBJECTS:
		print(f"{subject.capitalize():<10}: {raw[subject]}")
	print(f"{'Average':<10}: {ress['average']:.1f}%")
	print(f"{'Grade':<10}: {ress['grade']}")
	print(f"{'Status':<10}: {ress['status']}")
	print("=" * WIDTH)


def menu():
	print("=" * 60, "Student System")
	print("=" * 60)
	print("[1]. Calculate student's average marks")
	print("[2]. Show Results")
	print("[3]. Average System Calculations (class stats)")
	print("[4]. Students' Report")
	print("[5]. Search Student")
	print("[6]. Exit")
	print("=" * 60)


def main():
	stud_result = aver_calcu(stud_dbase)  # pre-load so the report is ready immediately
	while True:
		menu()
		try:
			men_opt = int(input("Choose Option ... 1-6: "))
		except ValueError:
			print("Choose Option ... 1-6")
			continue

		if men_opt == 1:
			stud_result = aver_calcu(stud_dbase)
			print(f"\nAverage Score calculated for {len(stud_result)} students")
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

		if men_opt != 6:
			input("\nPress Enter to continue...")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSystem shutting-down")
		sys.exit(0)
