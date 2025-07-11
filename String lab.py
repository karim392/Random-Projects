username = str(input("Enter the user name: "))

length = len(username)
#print(length)
print("Please enter only 12 letters" if length > 12 else "Welcome")
no_spaces = username.replace(" ", "")
print(no_spaces)
name_only = no_spaces.isalpha()
print(name_only)
if name_only == False:
    print("The name must be only Alohabetic")
else:
    print("Welcome again")