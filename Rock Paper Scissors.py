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
#Inputs are always strings**
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



# Exclude invalid entries before checking and calling lists:
if player_choice >= 3 or player_choice < 0:
  print("You lose (invalid number")
else:
  #Put images into a list:
  game_images = [rock, paper, scissors]
  print(game_images[player_choice])
  
  computer_choice = random.randint(0,2) 
  print("Computer chose: ")
  print(game_images[computer_choice])
  
  #Logic of the game
  if player_choice == 0 and computer_choice == 2:
    print("You win")
  
  elif computer_choice == 0 and player_choice == 2:
    print("You lose")
  elif computer_choice > player_choice:
    print("You lose")
  elif player_choice > computer_choice:
    print("You win")
  elif computer_choice == player_choice:
    print("Draw")


  

