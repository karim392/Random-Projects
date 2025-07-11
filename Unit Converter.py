Weight = float(input("Enter your weight: "))
Identify = input("Is it in (K) Kilograms or (L) pound: ")

if Identify.upper() == "K":
    KG_to_LP = Weight * 2.205
    unit = "LP"
    print(f"{round(KG_to_LP, 1)} {unit}")

elif Identify.upper() == "L":
    LP_to_KG = Weight / 2.205
    unit = "KG"
    print(f"{round(LP_to_KG, 1)} {unit}")

else:
    print("Please enter a valid number")