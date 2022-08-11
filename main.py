############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
from art import logo
from replit import clear
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit(cards_passed, n):
    for i in range(n):
      cards_passed.append(random.choice(cards))
    return cards_passed

def calculate_score(cards):
  # print(cards)
  if sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_final_score, dealer_final_score):
    if user_final_score == dealer_final_score:
      return "It's a draw"
    elif dealer_final_score == 0:
      return "The dealer has a blackjack. You lose!"
    elif user_final_score == 0:
      return "you have a blackjack. You win!"
    elif user_final_score > 21:
      return "You went over. You lose!"
    elif dealer_final_score > 21:
      return "The dealer went over. You win!" 
    elif user_final_score > dealer_final_score:
      return "You win!"
    else:
      return "You lose!"

      

def play():
  clear()
  print(logo)
  
  user_cards = []
  dealer_cards = []
  user_score = 0
  dealer_score = 0
  game_end = False
  
  hit(user_cards, 2)
  hit(dealer_cards, 2)
  
  while not game_end:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
  
    print(f" Your cards : {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {dealer_cards[0]}")
  
    if user_score == 0 or dealer_score ==0 or user_score>21:
      game_end = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass ").lower()
      if user_should_deal == "y":
        hit(user_cards, 1)
      else:
        game_end = True
        
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.     
  while dealer_score !=0 and dealer_score < 17:
    hit(dealer_cards, 1)
    dealer_score = calculate_score(dealer_cards)
        
  print (f"Your final hand: {user_cards}, final_score: {user_score}")
  print (f"Dealer's final hand: {dealer_cards}, final_score: {dealer_score}")
  print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play()
  
  # def score(cards_passed):
  #   sum = 0
  #   for card in cards_passed:
  #     sum += int(score)
  #   return sum
  
    
  
  # def dealer_hit():
  #   dealer_cards += random.choice(cards)
  #   for n in dealer_cards:
  #     dealer_score += int(n)
  #   while dealer_score < 17:
  #     dealer_hit()

  # def final():
  #   dealer_hit()
  #   print(f"Your final hand: {user_cards}, final score: {user_score}")
  #   print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
      
  # should_continue = input("Type 'y' to get another card, type 'n' to pass ").lower()
  # while should_continue =="y" and user_score <= 21:
  #   card_count = 1
  #   hit()  
  # final()
    
      
  ## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.



#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

