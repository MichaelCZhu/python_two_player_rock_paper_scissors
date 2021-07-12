# title and introduction
print("\n")
print("Welcome to Michael's python two player version of rock paper scissors (v2)")
print("\n")
print("Please select one of these three options:")
print("\n")
print("...rock...")
print("...paper...")
print("...scissors...")
print("\n")

#player1 input
print("enter Player 1's choice:")
print("\n")
player1 = input()
print("\n")

# Below is the no cheating screen
print("*** NO CHEATING ***\n\n" * 200)

#player2 input
print("enter Player 2's choice:")
print("\n")
player2 = input()

# beginning of game logic
if player1 and player2:
# These 6 lines below gives the variables string values 
	rock = str("rock")
	big_rock = str("Rock")
	paper = str("paper")
	big_paper = str("Paper")
	scissors = str("scissors")
	big_scissors = str("Scissors")

	print("\n")
	print("Rock...Paper...Scissors...SHOOT!")
	print("\n")

#The lines below is the primary logic behind the rock paper scissors game
	if player1 == rock or player1 == big_rock:
		if player2 == rock or player2 == big_rock:
			print("It's a TIE. Try again!")
			print("\n")
		elif player2 == paper or player2 == big_paper:
			print("Player2 wins!")
			print("\n")
		elif player2 == scissors or player2 == big_scissors:
			print("Player1 wins!")
			print("\n")
	elif player1 == paper or player1 == big_paper:
		if player2 == paper or player2 == big_paper:
			print("It's a TIE. Try again!")
			print("\n")
		elif player2 == rock or player2 == big_rock:
			print("Player1 wins!")
			print("\n")
		elif player2 == scissors or player2 == big_scissors:
			print("Player2 wins!")
			print("\n")
	elif player1 == scissors or player1 == big_scissors:
		if player2 == scissors or player2 == big_scissors:
			print("It's a TIE. Try again!")
			print("\n")
		elif player2 == rock or player2 == big_rock:
			print("Player2 wins!")
			print("\n")
		elif player2 == paper or player2 == big_paper:
			print("Player1 wins!")
			print("\n")
	else:
		print("Something went wrong. Please try again!")
else:
	print("Please input a choice next time!")
	print("\n")
