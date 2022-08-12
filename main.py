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
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
result_number = random.randint(1,100)
# print (f"pssst the number is {result_number}")

difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
lives = 5
if difficulty_level == 'easy':
  lives = 10
elif difficulty_level == 'hard':
  lives = 5
else:
  print ("You have entered an invalid input")


#Compare
def compare(user, comp, lives):
  lives -= 1
  print(lives)
  if user < comp:
    print(f"Too low\nGuess again\nYou have {lives} attempts remaining to guess the number.")
  if user > comp:
    print(f"Too high\nGuess again\nYou have {lives} attempts remaining to guess the number.")
  if user == comp:
    print(f"You got it! The answer was {user_number}")
    lives = 0
  return lives

while lives > 0:
  user_number = int(input("Make a guess: "))
  lives = compare(user_number, result_number, lives)