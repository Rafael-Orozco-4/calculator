def add(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def mult(a,b):
    result = a*b
    return result

def div(a,b):
    if b == 0:
        print("That is an invalid entry, you must enter a non-zero number")
        return None
    result = a/b
    return result

def rem(a,b):
    if b ==0:
        print("That is a an invalid entry, you must enter a non-sero number")
        return None
    result = a%b
    return result

def operations(user_selection,a,b):
    if user_selection == 1:
       return add(a,b)
    elif user_selection == 2:
       return sub(a,b)
    elif user_selection == 3:
        return mult(a,b)
    elif user_selection == 4:
        return div(a,b)
    elif user_selection == 5:
       return  rem(a,b)
    else:
        print("You entered an invalid selection, the available operations are: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division,\n and 5 for remainder")
        return None

user_selection = int(input("Welcome to the calculator program. Please select an available operation. They are: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division,\n and 5 for remainder: "))
a = int(input("Enter  your first value: "))
b = int(input("Enter your second value: "))

result  = operations(user_selection,a,b)
if result is not None:
    print(f"The result value is: {result}")