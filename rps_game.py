import random
from enum import Enum

class RPS(Enum):
  ROCK = "1"
  PAPER = "2"
  SCISSORS = "3"

playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")
valid_inputs = ["1","2","3"]

while playerchoice not in valid_inputs:
  print("You must type 1, 2 or 3.\n")
  playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")
      
computerchoice = random.choice("123")

print("")
print("You chose " + str(RPS(playerchoice)).replace('RPS.','') + ".")
print("Python chose " + str(RPS(computerchoice)).replace('RPS.','') + ".")
print("")

if playerchoice == "1" and computerchoice == "3":
  print("🎉 You win!")
elif playerchoice == "2" and computerchoice == "1":
  print("🎉 You win!")
elif playerchoice == "3" and computerchoice == "2":
  print("🎉 You win!")
elif playerchoice == computerchoice:
  print("😲 Its a tie!")
else:
  print("🐍 Python wins!")


