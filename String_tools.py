def ROT13():
    message=input("Enter the message:")
    text=''
    shift=13
    for char in message:
        if not char.isalpha():
            text +=char
        elif char.isupper():
            base=ord('A')
            new_char=chr((ord(char)-base+shift)%26+base)
            text +=new_char
        else:
            base=ord('a')
            new_char=chr((ord(char)-base+shift)%26+base)
            text +=new_char
    return text
def palindrome_check():
    s=input("Enter the string:")
    text=''
    for char in s:
        if not char.isalnum():
            pass
        elif char.isupper():
            new_char=char.lower()
            text +=new_char
        else:
            text +=char
    return text
def string_reverser():
    s=input("Enter a string:")
    text=s[::-1]
    return text
print("Choice 1:ROT13 encryption")
print("Choice 2:Palindrome checker")
print("Choice 3:String reverser")
print("Choice 4:Exit")
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
        Rot13=ROT13()
        print(Rot13)
    elif n==2:
        p=palindrome_check()
        if p[::-1]==p:
            print("The string is a palindrome")
        else:
            print("String is not a palindrome")
    elif n==3:
        reverse=string_reverser()
        print("Reversed string:",reverse)
    elif n==4:
        break
    else:
        print("Choice not available try again")
