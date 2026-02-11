import random
import sys
import os

# Add parent directory to path so we can import constants
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from constants.RPS_ASCII_ART import HAND

# hand  = ['rock', 'paper', 'scissors']

times = int(input("How many times do you want to play?(best of how many)"))
score = 0
while times > 0:
    user = input("Enter your choice: ").lower()
    if user not in HAND:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(list(HAND.keys()))
    print("You chose: ", HAND[user])
    
    print("Computer chose: ", HAND[computer])

    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
        score += 1
    elif user == "paper" and computer == "rock":
        print("You win!")
        score += 1
    elif user == "scissors" and computer == "paper":
        print("You win!")
        score += 1
    else:
        print("You lose!")
        score -= 1
    times -= 1
    print(f"Current Score: {score}")
if score > 0:
    print("You win!")
elif score < 0:
    print("You lose!")
else:
    print("It's a tie!")
