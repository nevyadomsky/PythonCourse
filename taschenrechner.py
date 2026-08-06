import math
while True:
    number_1 = int(input("Please enter a number: "))
    operation = input("Please choose operation or exit: +, -, *, /, √n, n², n³: ")

    if operation in ["+", "-", "*", "/"]:
        number_2 = int(input("Please enter another number: "))
        if operation == "+":
            print(number_1 + number_2)
        elif operation == "-":
            print(number_1 - number_2)
        elif operation == "*":
            print(number_1 * number_2)
        elif number_2 == 0 and operation == "/":
            print("Division by zero is impossible")
        elif operation == "/":
            print(number_1 / number_2)

    elif operation in ["√n", "n²", "n³"]:
        if operation == "√n":
            print("The result comes from the first digit:", math.sqrt(number_1))
        elif operation == "n²":
            print("The result comes from the first digit:", number_1 ** 2)
        elif operation == "n³":
            print("The result comes from the first digit:", number_1 ** 3)
    elif operation == exit:
        break






