# WAR

import random
import time

# [computer health, user health]
health = [10,10]
play_state = True

print("The game is War. Each player starts with 10 hp. \nIn each round, the computer will generate a random number for each player. If your number is higher, the computer will lose 1 hp. If your number is lower, you will lose 1 hp.\nThe first player to reach 0 hp loses.\n")
input("Press Enter to play the first round.")

while (health[0] != 0 and health[1] != 0) and play_state == True:
  print("-" * 60)
  computer = random.randint(1,10)
  user = random.randint(1,10)
  print("Attack Power:")
  print("Computer: " + str(computer))
  time.sleep(0.5)
  print("User: " + str(user))
  time.sleep(0.5)

  # If draw
  if user == computer:
    yes_no = input("\nDraw. Play again? (y/n)")
    if yes_no != "y":
      play_state = False
  
  # If user wins
  elif user > computer:
    health[0] += -1
    print("\nYou are victorious.")
    print("Computer: " + u"\u25A0 " * health[0])
    print("User:     " + u"\u25A0 " * health[1])
    yes_no = input("Continue? (y/n)")
    if yes_no != "y":
      play_state = False
  
  # If computer wins
  else:
    health[1] += -1
    print("\nYou have lost.")
    print("Computer: " + u"\u25A0 " * health[0])
    print("User:     " + u"\u25A0 " * health[1])
    yes_no = input("Continue? (y/n)")
    if yes_no != "y":
      play_state = False

if health[0] == 0:
  print("\n\nYou have emerged victorious. Your enemy's cities are in ashes, and their treasures are yours for the taking.")
elif play_state == False:
  print("\n\nYou have given up. Forever shall you be remembered as a coward among cowards. Slink back to the hole from whence you came.")
else:
  print("\n\nYou have been vaquinshed. For the rest of time, you shall be remembered as a failure. Your people are dead and your cities are burnt to the ground.")