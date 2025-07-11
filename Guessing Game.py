'''
x = int(input ("Guess number : "))

num = 9

def check_Number():
    if num > x:
        print ("the number is bet smaller")
    elif num < x:
        print ("the nunber is much bigger")
    else:
        print ("Good Job the correct answer is 9")

#Score = (3,2,1,hard luck)

for check_number in range(3):
    print(f"this is the iteration number: {check_number + 1}")

#if check_Number > 3:
#    print




check_Number()

while True:
    print("Bye Bye")
    break
    
'''


import random

secret_number = random.randint(1, 10)


count = 0



while True:
     guess = int(input("Guess number between 1 to 10: "))
    #count += 1
    #guess == secret_number
    #print ("Congratulation ! you chose the correct guess")

     if secret_number < guess:
      print("Too  High !!")
    
     elif secret_number > guess:
      print("Too Low !!!")
     
     else:
      print("Congratulation ! you chose the correct guess")
      break

     count += 1
    
     if count > 3:
      print("Sorry you have reach the limit of trails")
      break

#print(f"This game took you {count} guesses")

