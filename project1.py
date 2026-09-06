# this is first project
import random
choices = ["rock", "paper","scissor"]
player = input("choose rock , paper or scissor :").lower()
computer= random.choices(choices)
if player == computer:
    print("it's a tie ! both chose {player}. ")
elif(player == "rock" and computer == "scissor") or \
    (player == "paper" and computer == "rock") or \
    (player == "scissor" and computer == "paper"):
    print ("you win {player}beats {computer}")
else:
    print ("computer win! {computer} beats {player}")
