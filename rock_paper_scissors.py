
# Rock paper scissors game

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

choices = [rock, paper, scissors]


your_choice = input("What is your choice? r/s/p  ")
random_choice = random.randint(0,2)

# printing your choice
if your_choice == "r":
    print(rock)
elif your_choice == "s":
    print(scissors)
else:
    print(paper)    
  
# printing their choice  
if random_choice == 0:
    print(rock)
elif random_choice == 1:
    print(paper)
else:
    print(scissors)        

# choosing outcome
if your_choice == "r" and random_choice == 0:
    print("It's a tie!")
elif your_choice == "r" and random_choice == 1:
    print("You loose!")
elif your_choice == "r" and random_choice == 2:
    print("You win!") 

if your_choice == "s" and random_choice == 2:
    print("It's a tie!")
elif your_choice == "s" and random_choice == 0:
    print("You loose!")
elif your_choice == "s" and random_choice == 1:
    print("You win!")       
        
if your_choice == "p" and random_choice == 1:
    print("It's a tie!")
elif your_choice == "p" and random_choice == 2:
    print("You loose!")
elif your_choice == "p" and random_choice == 0:
    print("You win!")           