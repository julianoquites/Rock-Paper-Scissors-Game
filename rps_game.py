import random
import sys
from enum import Enum

def play_rps():
  class RPS(Enum):
    ROCK = "1"
    PAPER = "2"
    SCISSORS = "3"

  playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")
  valid_inputs = ["1","2","3"]
  computerchoice = random.choice("123")

  if playerchoice not in valid_inputs:
    print("You must type 1, 2 or 3.\n")
    return play_rps()
        
  print("\nYou chose " + str(RPS(playerchoice)).replace('RPS.','') + ".")
  print("Python chose " + str(RPS(computerchoice)).replace('RPS.','') + ".\n")

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
  
  print("\n Play again?")

  while True:
    playagain = input("\nY for Yes or \nN for No\n")
    if playagain.lower() not in ["y","n"]:
      continue
    else:
      break

  if playagain.lower() == "y":
    return play_rps()
  else:
    print("\n🎉🎉🎉🎉")
    print("Thank you for playing!\n")
    sys.exit("Bye! 👋")

play_rps()