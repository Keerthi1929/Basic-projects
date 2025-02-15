# ROCK PAPER SCISSOR GAME
# Here rock 0 paper 1 scissor 2

class rps:
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

def Rock_Paper_Scissor_Game(user_choice):
    game = [rps.rock, rps.paper, rps.scissor]
    if user_choice >= 3 or user_choice < 0:
        print("YOUR CHOICE IS INVALID. YOU SHOULD GIVE ROCK(0) PAPER(1) SCISSOR(2)")
    else:
        comp_choice = random.randint(0, 2)
        print(f"USER CHOICE:\n{game[user_choice]}")
        print(f"COMPUTER CHOICE:\n{game[comp_choice]}")
        if comp_choice == user_choice:
            print("DRAW")
        elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
            print("YOU WIN")
        else:
            print("YOU LOSE")

user_choice = int(input("Enter the value number that you choose: rock(0), paper(1), or scissor(2): "))
Rock_Paper_Scissor_Game(user_choice)
