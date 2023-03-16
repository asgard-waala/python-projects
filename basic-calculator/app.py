def add(x, y):
    answer = x + y
    print(str(x) + " + " + str(y) + " = " + str(answer) + "\n")

def subtract(x, y):
    answer = x - y
    print(str(x) + " - " + str(y) + " = " + str(answer) + "\n")

def multiply(x, y):
    answer = x * y
    print(str(x) + " * " + str(y) + " = " + str(answer) + "\n")

def divide(x, y):
    answer = x / y
    print(str(x) + " / " + str(y) + " = " + str(answer) + "\n")

while True:

    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter what do you want to do?: ")

    if choice == "A" or choice == "a":
        print("So you want to do the addition today, please enter the numbers you want to add.")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add(x, y)

    elif choice == "B" or choice == "b":
        print("So you want to do the subtraction today, please enter the numbers you want to subtract.")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        subtract(x, y)

    elif choice == "C" or choice == "c":
        print("So you want to do the multiplication today, please enter the numbers you want to multiply.")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        multiply(x, y)

    elif choice == "D" or choice == "d":
        print("So you want to do the division today, please enter the numbers you want to divide.")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        divide(x, y)

    elif choice == "E" or choice == "e":
        print("Thank you for using the calculator!")
        quit()

    else:
        print("Please choose the option from the above mentioned points, do not try to be oversmart! ")
