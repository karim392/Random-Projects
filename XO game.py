print("_____MAIN MENU _____")
print()
#print (input("Choose what would you like to do (1-2): "))
print("1 - Start the game")
print("2 - Quite the game")


while True:
 Ask_for_input = "Choose what would you like to do (1-2): "
 user_choice = input (Ask_for_input)
 
 name = "Write down your name: "

 if user_choice == "1":
    print("Lets start our game !")
    player_name = input(name)
    print(f'Welcome {player_name}')

 elif user_choice == "2":
    print("Good Bye !!")
    break
 else:
    print("Input not valid")
