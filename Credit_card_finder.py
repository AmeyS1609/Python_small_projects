def credit_card_validator(card_number):
    sum_odd_digits=0#dont declare them globally as if u run the code multiple times errors will occur as global variable keeps updating
    sum_even_digits=0
    reverse_card_number=card_number[::-1]
    odd_digits=reverse_card_number[::2]
    for digit in odd_digits:
        number=int(digit)
        sum_odd_digits +=number
    even_digits=reverse_card_number[1::2]
    for digit in even_digits:
        number=int(digit)*2
        if number>=10:
            number=number//10 + number%10
        sum_even_digits +=number
    total=sum_even_digits+sum_odd_digits
    return total%10==0
def main():
    card_number=input("Enter credid card number with all spaces and hyphens:")
    for char in card_number:
        if char.isalpha():
            return True
        
    card_tranlation=str.maketrans({'-':'',' ':''})#its just a translation map not translated number
    trans_card_number=card_number.translate(card_tranlation)
    if credit_card_validator(trans_card_number):
        print("VALID!")
        if trans_card_number[0]=='4':
            print("The card is a valid VISA card")
        elif trans_card_number[0:5]=='51–55':
            print("The card is a valid MASTERCARD")
        elif trans_card_number[0:2]=='34' or trans_card_number[0:2]=='37':
            print("The card is a valid AMERICAN EXPRESS card")
        elif trans_card_number[0:4]=='6011' or trans_card_number[0:2]=='65':
            print("The card is a valid DISCOVERY card")
        else:
            print("Your card is valid but type unknown")
    else:
        print("INVALID!,Card number not satisfying luhn algorithm")
def error():
    try:
        i=int(input("Enter a choice:"))
        return i
    except Exception:
        print("INVALID!!,Enter valid choice")
        return error()
while True:
    print("Choice 1:Check card number validity and type")
    print("Choice 2:Exit")
    n=error()
    if n==1:
        y=main()
        if y:
            print("INVALID!,Must contain only Numbers,space and hyphen")
    elif n==2:
        break
    else:
        try:
            print("Choice not available")
        except Exception as e:
            print("Enter a valid integer value")
    


