import re
import secrets
import string
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),#\d is used to represent class of numbers 0-9 i.e '[0-9]'
            (special_chars, fr'[{symbols}]'),#interpolating symbols in combined f and r(raw) string
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]
        #raw string (rstring) treats '\' as a commen charecter rather than a exiting charecter
        # Check constraints        
        if all( #all() replaces need of for loop and counting
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            #re module helps identifying specific charecters in a given text, better to use than if/else.
            #The '^' inside brackets ([^...]) means negation (not A to Z); outside brackets it means start of string
            #The '$' symbol is used to mark end of line/string
            #'.*' matches any characters in between; '^[aeiou].*[aeiou]$' checks if string starts and ends with a vowel

            break

    return password
print("Choice 1:Use Password generator")
print("Choice 2:Exit")
def get_user_input_and_generate():
    l=input("Enter length of needed pasword(press Enter for default = 16):") 
    l=int(l) if l else 16
    n=input("Enter number of numbers needed(press Enter for default =1):") 
    n=int(n) if n else 1
    s=input("Enter number of special charecters needed(press Enter for default =1:") 
    s=int(s) if s else 1
    lc=input("Enter number of lowercase letters needed(press Enter for default =1:")
    lc=int(lc) if lc else 1 
    uc=input("Enter number of uppercase letters needed(press Enter for default =1:")
    uc=int(uc) if uc else 1 
    try:
        return generate_password(length=l, nums=n, special_chars=s, uppercase=uc, lowercase=lc)
    except ValueError:
        print("Error: constraints exceed password length, please try again.")
        return get_user_input_and_generate()
def error():
    try:
        n=int(input("Enter a choice:"))
        return n
    except Exception:
        print("INVALID!!,Enter a valid choice")
        return error()
while True:
    s=error()
    if s==1:
        if __name__ == "__main__":
            print("Needed password:",get_user_input_and_generate())
    elif s==2:
        break
    else:
        print("Choice not available,Try again")
