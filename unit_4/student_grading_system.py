'''
Practical Task
Task Overview

Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must correctly use conditionals for all grade and status logic.

Requirements

Collect learner name and marks for three subjects (as floats) using input()
Calculate the average mark across the three subjects
Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
Assign Pass status if the average is 50 or above, Fail otherwise
Flag any individual subject mark below 40 as ‘needs intervention’
Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags
'''
import sys

INTERVENTION_THRESHOLD = 40

stud_dbase = {
	"stud_name": "",
	"stud_surn": "",
	"Subject": ["", "", ""],
	"Final %": [0.0, 0.0, 0.0],
	"Grade": ["", "", ""],
	"Average": 0.0,
}  # stores all students report


# Pure calculation helpers — kept separate so they are easy to test.
def letter_grade(mark):
	"""Return the letter grade for a single mark."""
	if mark >= 80:
		return "A"
	if mark >= 70:
		return "B"
	if mark >= 60:
		return "C"
	if mark >= 50:
		return "D"
	return "F"


def average_mark(marks):
	return sum(marks) / len(marks)


def pass_status(average):
	return "Pass" if average >= 50 else "Fail"


def needs_intervention(mark):
	return mark < INTERVENTION_THRESHOLD


# --- input helpers -------------------------------------------------------
def ask_text(prompt):
	while True:
		value = input(prompt).strip().upper()
		if value:
			return value
		print("This field cannot be empty.")


def ask_mark(prompt):
	while True:
		raw = input(prompt).strip()
		try:
			mark = float(raw)
		except ValueError:
			print("Please enter a valid mark between 0 and 100.")
			continue
		if 0 <= mark <= 100:
			return mark
		print("Mark must be between 0 and 100.")


def ask_name(stud_dbase):
	stud_dbase["stud_name"] = ask_text("Enter student name: ")
	stud_dbase["stud_surn"] = ask_text("Enter student surname: ")


def sub_modify(stud_dbase):
	for i in range(len(stud_dbase["Subject"])):
		stud_dbase["Subject"][i] = ask_text(f"Enter student's subject {i + 1}: ")


def grad_modify(stud_dbase):
	for i in range(len(stud_dbase["Subject"])):
		stud_dbase["Final %"][i] = ask_mark(f"Enter student's mark for {stud_dbase['Subject'][i] or f'subject {i + 1}'}: ")


def grad_avar(stud_dbase):
	stud_dbase["Average"] = average_mark(stud_dbase["Final %"])


def third_layer_grad(stud_dbase):
	for i, mark in enumerate(stud_dbase["Final %"]):
		stud_dbase["Grade"][i] = letter_grade(mark)


# --- reporting -----------------------------------------------------------
def report(stud_dbase):
	print("=" * 77, "\nReport Card")
	print("=" * 77)
	print(f"Name   : {stud_dbase['stud_name'] or '-'} {stud_dbase['stud_surn']}")
	print("-" * 77)
	print(f"{'Subject':<20} {'Mark':>8} {'Grade':>8} {'Flag':<22}")
	print("-" * 77)
	for subj, mark, grade in zip(stud_dbase["Subject"], stud_dbase["Final %"], stud_dbase["Grade"]):
		flag = "needs intervention" if needs_intervention(mark) else ""
		print(f"{subj or '-':<20} {mark:>8.1f} {grade:>8} {flag:<22}")
	print("-" * 77)

	avg_grd = stud_dbase["Average"]
	print(f"Average: {avg_grd:.2f}%  ->  Overall grade {letter_grade(avg_grd)}  ({pass_status(avg_grd)})")
	print("=" * 77)


# menu
def grad_menu():
	print("Main Menu")
	print("=" * 100)
	print("[1]. Insert Student Name and Surname")
	print("[2]. Insert Student Subject")
	print("[3]. Insert Student Marks")
	print("[4]. Calculate Average Marks")
	print("[5]. Show report")
	print("[6]. Exit")


def main_loop(stud_dbase):
	print("=" * 100)
	while True:
		grad_menu()  # show main menu
		try:
			menu_opt = int(input("Choose option: "))
		except ValueError:
			print("Error 400\nChoose option 1-6")
			continue

		if menu_opt == 1:
			ask_name(stud_dbase)
		elif menu_opt == 2:
			sub_modify(stud_dbase)
		elif menu_opt == 3:
			grad_modify(stud_dbase)
		elif menu_opt == 4:
			grad_avar(stud_dbase)
			print(f"\nAverage: {stud_dbase['Average']:.2f}%")
		elif menu_opt == 5:
			# Always work from the latest marks so edits are reflected.
			grad_avar(stud_dbase)
			third_layer_grad(stud_dbase)
			report(stud_dbase)
		elif menu_opt == 6:
			print("System shutting-down")
			break
		else:
			print("Error 400\nChoose option 1-6")


if __name__ == "__main__":
	try:
		main_loop(stud_dbase)
	except (KeyboardInterrupt, EOFError):
		print("\nSystem shutting-down")
		sys.exit(0)
