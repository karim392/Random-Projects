import random

def roll():
  die_low = 1
  die_high = 6
  roll = random.randint(die_low, die_high)
  return roll


while True:
  players = input("Enter the number of players (2-4): ")
  if players.isdigit():
    players = int(players) 
    if 2 <= players <= 4:
      print(f'Nice we have {players} players')
      break
    else:
      print("max 4 players only !!")
      continue

  print("In Valid  Please enter numbers between 2 and 4 !!")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) <= max_score:
     
  for player_idx in range (players):
    current_score = 0
    while True:
     question = input("Lets start by rolling the dies? (y/n) ")
     if question.lower() != "y":
        break
 
     value = roll()
     if value == 1:
         print(value)
         print("OOPS sorry you got Number 1 !!")
         break
 
     else:
         current_score += value
         print("you rolled: ",value)
     
     print("your score is: ",current_score)
  
     