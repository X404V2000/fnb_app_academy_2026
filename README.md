# fnb_app_academy_2026

Practical Python projects built during the **FNB App Academy 2026**, organised by unit. Every program is a small command-line app that demonstrates core Python concepts: functions, dictionaries and lists, loops, conditionals, user input validation and f-strings.

## Projects

| Unit | File | What it does |
| --- | --- | --- |
| 3 | [`unit_3/calculator.py`](unit_3/calculator.py) | Multi-function calculator: `+ - * / // %`, rounds to 2 dp, handles division by zero, keeps a calculation history |
| 3 | [`unit_3/rsa_fuel_cost_calc.py`](unit_3/rsa_fuel_cost_calc.py) | South African fuel cost calculator (1 L per 10 km) |
| 4 | [`unit_4/atm_sim.py`](unit_4/atm_sim.py) | Smart ATM withdrawal simulator with balance checks |
| 4 | [`unit_4/student_grading_system.py`](unit_4/student_grading_system.py) | Collects a learner's marks, grades each subject and prints a full report card with intervention flags |
| 5 | [`unit_5/contact_book.py`](unit_5/contact_book.py) | Contact book stored as a list of dictionaries: add, search, delete, view |
| 5 | [`unit_5/score_tracker.py`](unit_5/score_tracker.py) | Arcade high-score tracker with an intentional `while True` loop and `stop` keyword |
| 6 | [`unit_6/grade_report.py`](unit_6/grade_report.py) | Full class grade report: individual results, class statistics and student search |
| 6 | [`unit_6/phone_dir_search.py`](unit_6/phone_dir_search.py) | Mini phone directory using a dictionary lookup |
| — | [`side_tasks/password_generator.py`](side_tasks/password_generator.py) | Password generator with selectable character types, strength indicator, history, JSON export and optional clipboard copy |

## Requirements

- Python 3.10 or newer
- No external packages are required. `pyperclip` (see `requirements.txt`) is **optional** and only enables clipboard support in the password generator.

## Getting started

```bash
git clone https://github.com/X404V2000/fnb_app_academy_2026.git
cd fnb_app_academy_2026

# optional: clipboard support for the password generator
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Run any project from the repository root:

```bash
python3 unit_3/calculator.py
python3 unit_3/rsa_fuel_cost_calc.py
python3 unit_4/atm_sim.py
python3 unit_4/student_grading_system.py
python3 unit_5/contact_book.py
python3 unit_5/score_tracker.py
python3 unit_6/grade_report.py
python3 unit_6/phone_dir_search.py
python3 side_tasks/password_generator.py
```

In the calculator, type `c` at any prompt to cancel a calculation and return to the menu. `Ctrl+C` exits any program cleanly.

## Running the tests

The logic in every project (calculations, grading rules, lookups, validation) is written as pure functions that do not touch the terminal, so it can be tested directly:

```bash
python3 -m unittest discover -s tests -t tests -v
```

All 43 tests should pass.

## Project layout

```
.
├── side_tasks/          # bonus projects
├── tests/               # unittest suite (one file per project)
├── unit_3/              # calculator, fuel cost
├── unit_4/              # ATM simulator, student grading
├── unit_5/              # contact book, score tracker
├── unit_6/              # class grade report, phone directory
├── requirements.txt     # optional dependency (pyperclip)
└── README.md
```

## What was improved

- **Fuel cost bug** – the total was calculated as `kilometers × price` instead of `(kilometers / 10) × price` (a 10× overcharge, e.g. R2245.00 instead of R224.50).
- **Calculator** – removes a stray duplicate `main()` call, accepts `0` as an input (the old truthiness checks skipped it), adds the missing `//` and `%` handling to the menu, validates numbers before casting and keeps a working history table.
- **ATM** – no longer crashes on a non-numeric menu choice, has an exit option, validates the amount and formats balances to 2 decimal places.
- **Student grading** – empty names are rejected, the average is calculated and shown on the report card, the overall grade now uses the average, and marks below 40 are flagged as *needs intervention*.
- **Contact book** – "Data not found" no longer prints after a successful search, the menu matches the required order, and contacts use the `phone` key from the task spec.
- **Score tracker** – invalid scores no longer end the session, scores must be non-negative whole numbers, and the high-score messages depend only on the current score as required.
- **Grade report** – fixes the `NameError` in the individual report, the "Lowest" line now shows the lowest student (not the highest), and the table columns line up.
- **Password generator** – the requested password length is now exact (the old code produced length + 4 characters), the four character types are chosen by the user as required, `secrets` is used instead of `random`, and clipboard support is optional.

## Motivation

I built this from scratch to solidify my understanding of core Python concepts and to create something I am proud of.
