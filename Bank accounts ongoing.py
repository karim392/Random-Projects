from time import sleep

sleep(1)
print("Welcome to DV Bank")
sleep(1)
print("Processing...")
sleep(1)


customers = {
   'Ali': {'Balance':10},
   'Ahmed': {'Balance':20},
   'Karim': {'Balance':30},
   'Aya': {'Balance':40},
   'Omar': {'Balance':50},
   'Sara': {'Balance':60}
}             



custmer_name = input("Please enter your name: ")
print("Validating ....")
sleep(1)
if custmer_name in customers:
  print(f"Welcome {custmer_name}")
  customer_balance = customers [custmer_name]['Balance']
  
    
else:
  sleep(1)
  print("Sorry you are not DV Bank costomer!")
  sleep(1)
  print("please contact the coustomer service on 19744")
  exit()
  

 

def choose():
 sleep(1)
 while True:
  print("1. Add Money")
  print("2. Withdraw Money")
  print("3. Exit")
  break

def Ask_inp():
  Ask = int(input("Enter your Choice (1-3): "))
  return(Ask)



def handling_choose():
  trial = 0
  while True:
    choose()
    choice = Ask_inp()   

    if choice == 1:
      Add_Money()

    elif choice == 2:
      Withdraw_money()

    elif choice == 3:
      Exit_message()
      

    else:
      trial += 1
      print("Invalid input !")
      if trial >= 3:
       print("Many wrong inputs !")
       Exit_message()
      continue
       
   

    Ask2 = input(f"Would you like to do another transaction {custmer_name} (Y/N): ")
    if Ask2.upper() == "Y":
     return(handling_choose())
    
    else:  
     Ask2.upper                    
     Exit_message()
     



def Add_Money():  
     
 print(f"Your current balance is {customer_balance} EGP")
 Money_add = int(input("How Much you wold like to add: " ))
 Total_money = customer_balance + Money_add
 
 customers[custmer_name]['Balance'] += Money_add
 #print("Your New Balance in EGP is : ", {customers[custmer_name]['Balance']})
 print(f"Your New Balance in EGP is : {customers[custmer_name]['Balance']}")
     

     
def Withdraw_money():    

 print(f"Your current balance is {customer_balance} EGP")
 Withdraw = int(input("How Much you wold like to Withdraw: " ))
 Total_money_withdraw = customer_balance - Withdraw

 if Total_money_withdraw < 0:
  print("You have no Balance !!")
 else:   
  print(customer_balance - Withdraw)
  print("Your New Balance in EGP is : ", Total_money_withdraw)

   

def Exit_message():
 
 print("Good Bye")
 print(f"Thanks {custmer_name} For using DV bank")
 exit()





handling_choose()



