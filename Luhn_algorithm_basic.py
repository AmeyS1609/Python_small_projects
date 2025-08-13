"""
Luhn Algorithm checks if a number (like a credit card) is valid by doubling every second digit from the right,
summing all digits (splitting doubled digits >9), and verifying the total is divisible by 10.
"""

# Credit card validator using Luhn Algorithm
def credit_card_validator(card_number):
    sum_odd_digits = 0
    sum_even_digits = 0
    reverse_card_number = card_number[::-1]

    odd_digits = reverse_card_number[::2]
    for digit in odd_digits:
        number = int(digit)
        sum_odd_digits += number

    even_digits = reverse_card_number[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = number // 10 + number % 10
        sum_even_digits += number

    total = sum_even_digits + sum_odd_digits
    return total % 10 == 0

def main():
    card_number = input("Enter credit card number with all spaces and punctuations: ")
    card_translation = str.maketrans({'-': '', ' ': ''})
    trans_card_number = card_number.translate(card_translation)
    if credit_card_validator(trans_card_number):
        print("VALID!")
    else:
        print("INVALID!")

def error():
    try:
        n = int(input("Enter a choice: "))
        return n
    except Exception:
        print("INVALID!! Enter valid choice")
        return error()

print("Choice 1: Check credit card validity")
print("Choice 2: Exit")

while True:
    s = error()
    if s == 1:
        main()
    elif s == 2:
        break
    else:
        print("Choice not available")
