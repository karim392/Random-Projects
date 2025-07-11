#crdit_card_number = "1234-5678-9012-7890"

#last = crdit_card_number[-4:]

#print(f"XXXX-XXXX-XXXX-{last}")

#reversed_cd = crdit_card_number[::-1]
#print(reversed_cd)


mail = input("Please enter your e_mail: ")

index = mail.index("@")

#print(index)

name = mail[:index]
Domain = mail[index + 1:]

print(f'Your mail name is {name}')
print(f'Your Domain is {Domain}')
