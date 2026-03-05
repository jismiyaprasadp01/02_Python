#Validate a Password String

password = input("Enter password: ")
if len(password) >= 8 and any(i.isdigit() for i in password):
    print("Valid Password")
else:
    print("Invalid Password")
