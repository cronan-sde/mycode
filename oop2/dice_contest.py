from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapperV2 = Cheat_Swapper_V2()

swapper_score = 0
loaded_dice_score = 0
swapperV2_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  swapperV2.roll()

  swapper.cheat()
  loaded_dice.cheat()
  swapperV2.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) or sum(loaded_dice.get_dice()) == sum(swapperV2.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(swapperV2.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1

  elif sum(swapperV2.get_dice()) > sum(swapper.get_dice()) and sum(swapperV2.get_dice()) > sum(loaded_dice.get_dice()):
   swapperV2_score += 1
  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Swapper V2 won: " + str(swapperV2_score))
if swapper_score == loaded_dice_score or loaded_dice_score == swapperV2_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score and swapper_score > swapperV2_score:
  print("Swapper won most games")
elif swapperV2_score > swapper_score and swapperV2_score > loaded_dice_score:
  print("Swapper V2 won most games")
else:
  print("Loaded dice won most games")

