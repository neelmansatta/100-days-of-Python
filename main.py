import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type\n0 for Rock\n1 for Paper\n2 for Scissors "))
if player_choice == 0 or player_choice == 1 or player_choice == 2:
  print(options[player_choice])
  computer_choice_num = random.randint(0,len(options)-1)
  computer_option = options[computer_choice_num]
  print("Computer chose:\n"+computer_option)
if player_choice - computer_choice_num == 0:
  print("Its a tie, Play again")
elif player_choice - computer_choice_num == 1 or player_choice - computer_choice_num == -2:
  print("You win")
elif player_choice - computer_choice_num == -1 or player_choice - computer_choice_num == 2:
  print("You lose")
else:
  print("Incorrect input")