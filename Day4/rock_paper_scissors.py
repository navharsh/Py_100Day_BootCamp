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
game_img = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice <0 or user_choice >=3:
    print("You chose an Invalid Number!!!")
    exit()

print(game_img[user_choice])

print("Computer chose:")
computer_choice = random.randint(0,2)
print(game_img[computer_choice])


if user_choice == computer_choice:
    print("It's Draw :|")
if user_choice == 0:
    if computer_choice == 1:
        print("You Lose :(")
    if computer_choice == 2:
        print("You Win :)")
if user_choice == 1:
    if computer_choice == 0:
        print("You Win :)")
    if computer_choice == 2:
        print("You Lose :(")
if user_choice == 2:
    if computer_choice == 0:
        print("You Lose :(")
    if computer_choice == 1:
        print("You Win :)")      











