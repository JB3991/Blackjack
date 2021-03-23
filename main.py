# Blackjack
import random
from replit import clear
from art import logo

# return a random card from the cards array 
def deal_card():
	"""Returns a random card from the deck."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def calculate_score(cards):
	"""Take a list of cards and return the score calculated from the cards"""
	#Check to see if the user or computer has a blackjack 
	if sum(cards) == 21 and len(cards) == 2:
		return 0
#Check to see if the user or Computer has an ace and if they bust, turn the Ace from a 11 to a 1
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)


# Compare the Users and Computer score to see who wins. 
def compare(user_score, computer_score):
	#Bug fix. If you and the computer are both over, you lose.
	if user_score > 21 and computer_score > 21:
		return "You went over. You lose 😤"

	if user_score == computer_score:
		return "Draw 🙃"
	elif computer_score == 0:
		return "Lose, opponent has Blackjack 😱"
	elif user_score == 0:
		return "Win with a Blackjack 😎"
	elif user_score > 21:
		return "You went over. You lose 😭"
	elif computer_score > 21:
		return "Opponent went over. You win 😁"
	elif user_score > computer_score:
		return "You win 😃"
	else:
		return "You lose 😤"


def play_game():

	print(logo)

	user_cards = []
	computer_cards = []
	is_game_over = False

	#Deal the user and computer 2 cards each using deal_card()
	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())


	while not is_game_over:
	# Check to see the users or compouters has a Blackjack or their score is over 21, then end game. 
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"   Your cards: {user_cards}, current score: {user_score}")
		print(f"   Computer's first card: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			# check to see if the user wants another card  
			user_should_deal = input(
			    "Type 'y' to get another card, type 'n' to pass: ")
          #if they do then add another card to the user_cards array 
			if user_should_deal == "y":
				user_cards.append(deal_card())
			else:
        #Otherwise end game
				is_game_over = True

	# Once the user is done we now pull the Computers cards. 
  #if the computers score is below 17 then keep pulling cards. 
	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	print(f"   Your final hand: {user_cards}, final score: {user_score}")
	print(
	    f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
	)
	print(compare(user_score, computer_score))

#ask the user if they want to play another game. if Yes clear the console and start again. 
while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
	clear()
	play_game()
