#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

# Pick a random number
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# print (f"pssst the number is {result_number}")
def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
  result_number = random.randint(1,100)
  #Make functionality to set difficulty and lives
  def set_difficulty():
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty_level == 'easy':
      return EASY_LEVEL_TURNS
    elif difficulty_level == 'hard':
      return HARD_LEVEL_TURNS
    else:
      return "You have entered an invalid input"
  
  #Compare
  def compare(user, comp, lives):
    """Function to compare the user passed number to the actual number"""
    # print(lives)
    
    if user < comp:
      print(f"Too low\nGuess again\nYou have {lives-1} attempts remaining to guess the number.")
    elif user > comp:
      print(f"Too high\nGuess again\nYou have {lives-1} attempts remaining to guess the number.")
    else:
      print(f"You got it! The answer was {user}")
    lives -= 1
    return lives

  guess = 0
  turns = set_difficulty()
  print(f"You have {turns} attempts to guess the number:")
  
  while guess!= result_number:
    
    #Let the user guess a number
    guess = int(input("Make a guess: "))
    #Check user guess against actual number
    turns = compare(guess, result_number, turns)
    if turns == 0:
      print(" You've run out of guesses, you lose.")
      print(f" The number was {result_number}.")
      return
game()