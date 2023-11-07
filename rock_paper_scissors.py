import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game = [rock, paper, scissors]

computer = random.randint(0, 2)

playerChoice = int(
    input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
playerRPS = playerChoice


computerRPS = computer
#
# print(f"Computer chose{computerRPS}")
if playerRPS >= 3 or playerRPS < 0:
    print("You typed an invalid number!")
else:
    print(f"You choose {game[playerRPS]}")
    if playerRPS == 0:
        if computerRPS == 1:
            print(f"You lose computer chose {game[1]}")
        elif computerRPS == 2:
            print(f"You win computer chose {game[computerRPS]}")
        elif computerRPS == 0:
            print(f"Draw computer chose {game[computerRPS]}")
    elif playerChoice == 1:
        if computerRPS == 2:
            print(f"You lose computer chose {game[computerRPS]}")
        elif computerRPS == 0:
            print(f"You win computer chose {game[computerRPS]}")
        elif computerRPS == 1:
            print("Draw computer chose {game[computerRPS]}")
    elif playerChoice == 2:
        if computerRPS == 0:
            print(f"You lose computer chose {game[computerRPS]}")
        elif computerRPS == 1:
            print(f"You win computer chose {game[computerRPS]}")
        elif computerRPS == 2:
            print("Draw computer chose {game[computerRPS]}")
