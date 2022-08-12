from game_data import data
from art import logo
import random
from replit import clear
SCORE = 0
print(logo)
# print name1, description1, country1
#print vs
#select object from the dictionary
def select():
  object = random.choice(data)
  return object

def compare(object1, object2):
  if int(object1['follower_count']) >= int(object2['follower_count']):
    return "a"
  else:
    return "b"

def print_match(object1, object2):
  from art import vs
  print(f"\n{object1['name']}, a {object1['description']}, from {object1['country']}")
  print(vs)
  print(f"\n{object2['name']}, a {object2['description']}, from {object2['country']}")

  # print name2, description2, country2


object_a = select()
object_b = select()
print_match(object_a, object_b)
choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

while choice == compare(object_a, object_b):
  SCORE += 1
  object_a = object_b
  object_b = select()
  clear()
  print(f"\nYou're right! Current Score: {SCORE}.")
  print_match(object_a, object_b)
  choice = input("\nWho has more followers? Type 'A' or 'B'").lower()
clear()
print(f"\nSorry, that's wrong. Final score: {SCORE}")
# print art 