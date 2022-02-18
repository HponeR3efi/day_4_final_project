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

import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

options = [rock,paper,scissors]

user_choose = options[choose]

print("You chose: ")

print(user_choose)

computer_choose = random.randint(0,2)

computer_choice = options[computer_choose]

print("Computer chose:")

print(computer_choice)

if choose == computer_choose:
  print("You are Draw")
elif choose == 0 and computer_choose == 2:
  print("You Win")
elif choose == 1 and computer_choose == 0:
  print("You Win")
elif choose == 2 and computer_choose == 1:
  print("You Win")
else:
  print("You Lose")