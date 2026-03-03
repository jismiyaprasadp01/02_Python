#Validate a Password String

import string

def is_valid_password(password):
    
    if len(password) < 8:
        return False
    
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    
    return upper and lower and digit and special

password = "MyPass123@"
if is_valid_password(password):
    print("Valid password: Yes")
else:
    print("Valid password: No")
