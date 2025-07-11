Foods = []
Prices = []
Total = 0

while True:
   Food = input("What would you like o buy? / for quetting press q: ")
   if Food.lower() == "q" :
     break  
   elif Food != str(Food) : 
     print(f"{Food} is not a food please enter a valed value")
   else:
     Price = float(input(f"Please enter the price for, {Food}: "))
     Foods.append(Food)
     Prices.append(Price)

print()
print("_____ YOUR LIST _____")


for Food in Foods:
  print(Food)

for Price in Prices:
  
  Total  += Price
  print(f"Your total price is {Total}")
  