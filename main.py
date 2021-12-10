import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissors]
print("Welcome to the Rock Paper Scissors game!")
my_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice >= 3 or my_choice < 0: 
 print("You typed an invalid number, try again!")
else:
 print("You choose:") 
 print(game_images[my_choice])

 computer_choice = random.randint(0, 2)
 print("Computer choose:")
 print(game_images[computer_choice])
 
 if my_choice == 0 and computer_choice == 2:
   print("Yeah, you win!")
 elif computer_choice == 0 and my_choice == 2:
   print("Oh no, you lose.")
 elif computer_choice > my_choice:
   print("Oh no, you lose.")
 elif my_choice > computer_choice:
   print("Yeah, you win!")
 elif computer_choice == my_choice:
   print("Ah, it's a draw.")