#Rock, Paper, Scissors game

import random

print ("Which number you do wanna choose?")
person = input("Type 0 for Rock, 1 for Paper and 2 for Scissors.\n\nPlayer chooses: ")

player = int(person)
computer = random.randint(0,2)

print("Computer chooses:",computer)
print()

if player == computer:
    print("Its a Draw.")
elif player < computer and computer != 0 and computer !=2:
    print("Computer wins.")
elif player < computer and computer != 0 and computer !=1 and player ==0:
    print("Player wins.")
elif player > computer and computer != 1 and computer !=2 and player ==1:
    print("Player wins.")
elif player < computer and computer != 0 and computer !=1 and player ==1:
    print("Computer wins.")
elif player > computer and computer != 1 and computer !=2 and player ==2:
    print("Computer wins.")
elif player > computer and computer != 0 and computer !=2 and player ==2:
    print("player wins.")
else:
    print("You have typed an incorrect number")