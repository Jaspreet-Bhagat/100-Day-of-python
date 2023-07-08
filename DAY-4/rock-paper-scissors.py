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
option = [rock,paper,scissors]
#Write your code below this line 👇
user_choice = int(input("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
if user_choice<3:
  print(option[user_choice])
else:
  print("index out of range!")
  
comp_choice = random.randint(0,2)
print("computer choice: ")
print(option[comp_choice])

# caparision
if user_choice>=3 or user_choice<0:
  print("invalid!")
elif user_choice ==0 and comp_choice == 2:
  print("you won!")
elif comp_choice == 0 and user_choice == 2:
  print("you lose!")
elif user_choice>comp_choice:
  print("You Win!")
elif comp_choice>user_choice:
  print("you lose!")
elif comp_choice == user_choice:
  print("draw!")
  
