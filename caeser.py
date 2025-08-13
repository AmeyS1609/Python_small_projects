def caeser(message,shift,direction):
    text=''
    for char in message:#Preserving Non-alphabets
        if not char.isalpha():
            text +=char
        elif char.isupper():#Preserving uppercase letters
            base=ord('A')
            new_char=chr((ord(char)-base-shift*direction)%26+base)
            #ord(char)-base :gets position in english alphabet [0-->A,25-->Z]
            #-shift: decodes the cypher
            #%26: modulo method, wraps around the alphabet so thet the new_char stays an alphabet,[A to Z , then after Z again A starts]
            #+base: converts the expression back to ASCII
            text +=new_char
        else:#preserving lowercase alphabets
            base=ord('a')
            new_char=chr((ord(char)-base-shift*direction)%26+base)
            #ord(char)-base :gets position in english alphabet [0-->a,25-->z]
            #-shift: decodes the cypher
            #%26: modulo method, wraps around the alphabet so thet the new_char stays an alphabet,[A to Z , then after Z again A start
            #+base: converts the expression back to ASCII
            text +=new_char
    return text #remember to return or else output  is none
def encryption():
    message=input("Enter message:")#here if u r giving message and shift no need to give inside caeser function and vice versa
    def user1():
        try:
            shift=int(input("Enter shift:"))
            return shift #remember to return or else output is none
        except Exception:
            print("Invalid shift,enter again")
            return user1()#remember to return or else output is none
    
    shift=user1()
    n=caeser(message,shift,1)#remember what function is being called and what is returned
    return n #remember to return or else output  is none
def decryption():
    message=input("Enter message:")#here if u r giving message and shift no need to give inside caeser function and vice versa
    def user2():
        try:
            shift=int(input("Enter shift:"))
            return shift#remember to return or else output is none
        except Exception:
            print("Invalid shift,enter again")
            return user2()#remember to return or else output is none
    shift=user2()

    n=caeser(message,shift,-1)#remember what function is being called what is returned
    return n #remember to return or else output is none
while True:
    need=input("Do you want to do encryption or decryption or exit:").lower()#so that is does not give error even if requirement is typed in uppercase
    if need.lower()=="encryption":
        encrypt=encryption()#remember what function is being called what is returned
        print("Needed message:",encrypt)
    elif need.lower()=="decryption":
        decrypt=decryption()#remember what function is being called what is returned
        print("Needed message:",decrypt)
    elif need.lower()=='exit':
        break
    else:
        print("INVALID!!,Enter either encryption or decryption")