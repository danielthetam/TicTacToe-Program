import random
import time
from numpy.random import choice

# Welcome Player
# Ask if they want to play
# If they do, begin the while loop and reset scores
# Ask player if they want to hit, if yes, generate random number and add to score
# As long as player score isn't over or equal to 21
# Continue

player_score = 0
ai_score = 0

running = False

play = input("Would you like to start playing? (Y/N)  ")


# Checking Functions

def check_winner():
    if ai_score > player_score:
        return "AI won, you lost."
    elif ai_score < player_score:
        return "You won! Hurray for humanity"


def check_explode():
    if ai_score == 21 or player_score == 21:
        if ai_score == 21:
            return "AI won, you lost."
        elif player_score == 21:
            return "You won!! AI lost hahaha, hurray for humanity"
    elif ai_score > 21 or player_score > 21:
        if ai_score > 21:
            return "You won!! AI lost hahaha, hurray for humanity!!"
        elif player_score > 21:
            return "You lost, rip!"


# Starting Game
if play.lower() == "y":
    running = True
    counter = 3
    for i in range(3):
        print("Starting in ", counter)
        counter -= 1
        time.sleep(1)

elif play.lower() == "n":
    print("Have a great day.")

# Game loop
while running:
    if ai_score < 21 and player_score < 21:
        ai_hit = choice([True, False], 1, p=[0.5, 0.5])
        if ai_hit:
            ai_score += random.randint(1, 10)
        hit = input("Would you like to hit or stand? (H/S)  ")
        if hit.lower() == "h":
            player_score += random.randint(1, 10)
            print(f"Current Score: {player_score}")
        elif hit.lower() == "s":
            print(check_winner())
            print(f"Current Score: {player_score}\nAI Score: {ai_score}")
            running = False

    if check_explode() is not None:
        print(check_explode())
        running = False
