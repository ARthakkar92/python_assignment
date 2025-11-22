####### Python script to check the strength of the password ###########
import string

def check_password_strength(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True
            break
        
    has_lower = False
    for ch in password:
        if ch.islower():
            has_lower = True
            break
        
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break
        
    special_characters = "!@#$%^&*()_+-={}[]|:;'<>,.?/"
    has_special = False
    for ch in password:
        if ch in special_characters:
            has_special = True
            break
    
    if has_upper and  has_lower and has_digit and has_special:
        return True
    else:
        return False
    

password = input("Enter your password:")

if check_password_strength(password):
    print("your password is strong.")
else:
    print("your password doesn't meet the password criteria.")