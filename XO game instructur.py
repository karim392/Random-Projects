class player:
  def __inte__(self):
    self.name = ""
    self.symbol = ""

  def choose_name(self):
    while True:
     name = input("Enter your name: ")
     if name.isalpha():
       self.name = name
       print(f'Welcome {name}')
       break
    print("Please enter only Alphabtic")

  def choose_symplo(self):
    while True:
     symbol = input(" Enter your prefered symbol X - O: ")
     if symbol.isalpha() and len(symbol) == 1:
       self.symbol = symbol.upper()
       print(f"Lets play with {symbol}")
       break
     print("Please enter Valid symbol !")

class Menu:
  def display_main_menu(self):
    print("_____MAIN MENU _____")
    print()
    print("1 - Start the game")
    print("2 - Quite the game")
    while True:
      choice = input("Enter your Choise (1 or 2)")
      if choice != "1" or "2":
        break

  def end_game_menu(self):
    end_menu = """
    Game over!!
    1. Restart Game
    2. Quite Game
    Enter your choise (1 or 2): """
    choice = input(end_menu)
    return choice

class Board:
  def __init__(self):
    self.Board =  [str(i) for i in range(1,10)]
    for i in range(0, 10, 3):
     print("|".join(self.Board[i:i+3]))
     if i<6:
      print("-"*5)
    
#







#choose_name = input("Enter your name: ")
#choose_symbol = input(" Enter your prefered symbol X - O: ")
#if choose_symbol != "X" or "O":
#  print("Please enter value X or O !")

