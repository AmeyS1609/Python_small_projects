def password_strength():
    password=input("Enter your password:")
    if " " in password:#Dont place this for loop for smooth running and to avoid complications
        print("password can't contain space, try again")
        return password_strength()

    l=len(password)
    count_special=0
    count_number=0
    count_upper=0
    count_lower=0
    for char in password:
        if char.isupper():
            count_upper +=1
        elif char.islower():
            count_lower +=1
        elif char.isnumeric(): 
            count_number +=1
        else:
            count_special +=1
   
    n=0
    p=0
    if l<8:
        print("Password must atleast be 8 charecters")
        p -=1
        
        
    if count_lower>0:
        n +=1
    if count_number>0:
        n +=1
    if count_special>0:
        n +=1
    if count_upper>0:
        n +=1
    if n<2 or p<0:
        print("Password is Weak")
    elif n==2 or n==3:
        print("Password is Moderate")
    elif n==4:
        print("Password is Strong")
    
print("Choice 1:Check passsword strength")
print("Choice 2:Exit")
def error():
    try:
        i=int(input("Enter a choice:"))
        return i
    except Exception:
        print("INVALID!!,Enter valid choice")
        return error()


while True:
    n=error()
    if n==1:
        password_strength()

    elif n==2:
        break
    else:
        print("Choice not available try again")
        




