'''
The Challenge: “The High-Score Tracker Game”
Build an interactive program that continuously asks an arcade player for their game
score.

1. Start an intentional infinite loop using while True:.

2. Inside the loop, ask the user to enter a game score next to the flashing cursor.

3. If they type the word “stop” (clean it up with .strip().lower()), print “Game session ended!” and use a break statement to shut down the loop.

4. Otherwise, cast their input into an int, check if the score is greater than 100, and print either “Wow! That’s a new high score!” or “Good try, keep playing!” based on the value.
'''
player = [{"score": 0}]
computer = [{"score": 0}]

def add_score(computer, player, computer_score, player_score):
	if player_score.lower() == "stop" or computer_score.lower() == "stop":
		print("\nGame session ended")
		return False

	try:
		p_score = int(player_score)
		c_score = int(computer_score)
		for dictionary in player:
			dictionary["score"] = dictionary["score"] + p_score

		for dictionary in computer:
			dictionary["score"] = dictionary["score"] + c_score

		if player[0]["score"] > 100 and player[0]["score"] > computer[0]["score"]:
			print("\nWow! That's a new high score!\n")

		if computer[0]["score"] <= player[0]["score"] and player[0]["score"] <= 100:
			print("\nGood try, keep playing!")

		print(f"\nCurrent Score [Player: {player[0]["score"]} | Computer: {computer[0]["score"]}]\n")
		return True
	except ValueError:
		print("Error 400")
		return False

def view_score():
	print("="*60,"\nGame Score")
	print("="*60)
	print(f"PLayer  : {player[0]['score']}\nComputer: {computer[0]['score']}")
	print("="*60)

def menu():
	print("="*60,"\nArcade Score Tracker")
	print("="*60)
	print("[1]. Score Tracker")
	print("[2]. View Score")
	print("[3]. End Process")
	print("="*60)

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
				player_score = input("What's your score: ").strip()
				computer_score = input("Computer score: ").strip()
				
				if player_score.lower() == "stop" or computer_score.lower() == "stop":
					print("\nGame session ended!")
					break
				result = add_score(computer, player, computer_score, player_score)
				if not result:
					break
		elif menu_access == 2:
			view_score()
		elif menu_access == 3:
			print("System Tracker process shutting-down")
			break
		else:
			return False

if __name__ == "__main__":
	main()
