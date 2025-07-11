customers = ["Ali", "Ahmed", "Karim", "Aya", "Omar", "Sara"]
Balance = 10



 

# Ali_password = 0000
# Ahmed_password = 1111
# Karim_password = 2222
# Aya_password = 3333
# Omar_password = 4444
# Sara_password = 5555



while True:   
  Greeting = input("Please enter your name: ")
  if Greeting in customers:
    print(f"Welcome {Greeting}")
    break

  else:
    print("Sorry you are not this Bank costomer!")
    exit()
 
while True:
  print("1. Add Money")
  print("2. Withdraw Money")
  print("3. Exit")
  break
  


Ask = int(input("Enter your Choice (1-3): "))



if Ask == 1:
     print(f"Your current balance is {Balance}")
     Money_add = int(input("How Much you wold like to add: " ))
     print(Balance + Money_add)
     Total_money = Balance + Money_add
     print("Your New Balance is : ", Total_money)
     Ask2 = input(f"Would you like to do another transaction {Greeting} (Y/N): ")
     if Ask2.upper() == "Y":
        print()
     else:
        print("bye_bye")

elif Ask == 2:
   print(f"Your current balance is {Balance}")
   Withdraw_Money = int(input("How Much you wold like to Withdraw: " ))
   Total_money_withdraw = Balance - Withdraw_Money

   if Total_money_withdraw < 0:
    print("You have no Balance !!")

   else:   
    print(Balance - Withdraw_Money)
    print("Your New Balance is : ", Total_money_withdraw)
   

  
elif Ask == 3:
    print("Good Bye")
else:
     print("Invaled Value")



print(f"Thanks {Greeting} For using our bank")


#while True:
 #choices = input ()
  