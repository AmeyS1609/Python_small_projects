def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')
def main():
    R=input("Enter pascal or camel case to be converted:")
    print(convert_to_snake_case(R))
def error():
    try:
        n=int(input("Enter Choice:"))
        return n
    except Exception:
        print("INVALID!! Enter valid choice")
        return error()
print("Choice 1:Case convert given string")
print("Choice 2:Exit")
while True:
    s=error()
    if s==1:
        main()
    elif s==2:
        break
    else:
        print("Choice not available")