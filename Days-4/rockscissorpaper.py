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

# Write your code below this line 👇

player = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

player_choice = int(player)
computer_choice = random.randint(0, 2)

list_option = [rock, paper, scissors]

player_play = ''
if player_choice >= 3 or player_choice < 0:
    print("You choose a wrong number, you lose!")
else:
    player_play = list_option[player_choice]
    print(f"You choose:\n{player_play}")

    computer_play = list_option[computer_choice]
    print(f"Computer choose:\n{computer_play}")

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif computer_choice > player_choice:
        print("You lose!")
    elif computer_choice < player_choice:
        print("You win!")
    elif computer_choice == player_choice:
        print("Draw")
