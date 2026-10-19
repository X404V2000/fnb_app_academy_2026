'''
The Challenge: “The High-Score Tracker Game”
Build an interactive program that continuously asks an arcade player for their game
score.

1. Start an intentional infinite loop using while True:.

2. Inside the loop, ask the user to enter a game score next to the flashing cursor.

3. If they type the word “stop” (clean it up with .strip().lower()), print “Game session ended!” and use a break statement to shut down the loop.

4. Otherwise, cast their input into an int, check if the score is greater than 100, and print either “Wow! That’s a new high score!” or “Good try, keep playing!” based on the value.
'''
import sys

# Track each player's best single score and the highest score seen this session.
player = {"best": 0, "rounds": 0}
computer = {"best": 0, "rounds": 0}


# Pure logic — kept separate so it is easy to test.
def score_message(score):
	"""Return the game's reaction to a single score."""
	if score > 100:
		return "Wow! That's a new high score!"
	return "Good try, keep playing!"


def add_score(player, computer, computer_score, player_score):
	"""Record one round. Returns False if the input was not a valid integer."""
	try:
		p_score = int(player_score)
		c_score = int(computer_score)
	except ValueError:
		print(f"Error 400 ... '{player_score}', '{computer_score}' are not valid scores (use whole numbers)")
		return False

	if p_score < 0 or c_score < 0:
		print("Scores cannot be negative")
		return False

	player["rounds"] += 1
	computer["rounds"] += 1
	player["best"] = max(player["best"], p_score)
	computer["best"] = max(computer["best"], c_score)

	print(f"\nPlayer asked: {p_score} - {score_message(p_score)}")
	print(f"Computer    : {c_score} - {score_message(c_score)}")
	if player["best"] > computer["best"]:
		print(">> Player is leading the session!")
	elif player["best"] < computer["best"]:
		print(">> Computer is leading the session!")
	else:
		print(">> It's a tie!")

	print(f"\nCurrent Score [Player: {player['best']} | Computer: {computer['best']}]"
	      f" after {player['rounds']} round(s)\n")
	return True


def view_score():
	print("=" * 60, "\nGame Score")
	print("=" * 60)
	print(f"Player  : {player['best']} (best of {player['rounds']} rounds)")
	print(f"Computer: {computer['best']} (best of {computer['rounds']} rounds)")
	print("=" * 60)


def menu():
	print("=" * 60, "\nArcade Score Tracker")
	print("=" * 60)
	print("[1]. Score Tracker")
	print("[2]. View Score")
	print("[3]. End Process")
	print("=" * 60)


def main():
	while True:
		menu()
		try:
			menu_access = int(input("Choose Option: "))
		except ValueError:
			print("Choose option ... 1-3")
			continue

		if menu_access == 1:
			while True:
				player_score = input("What's your score (or 'stop'): ").strip()
				if player_score.lower() == "stop":
					print("\nGame session ended!")
					break
				computer_score = input("Computer score (or 'stop'): ").strip()
				if computer_score.lower() == "stop":
					print("\nGame session ended!")
					break
				add_score(player, computer, computer_score, player_score)

		elif menu_access == 2:
			view_score()
		elif menu_access == 3:
			print("System Tracker process shutting-down")
			break
		else:
			print("Error 400 ... Choose option 1-3")


if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nSystem Tracker process shutting-down")
		sys.exit(0)
