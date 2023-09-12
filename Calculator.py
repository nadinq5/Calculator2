import re
from add import*
from divide import*
from multiply import*
from power_of import*
from subtract import*
from validate import*
from is_even_odd import*
from is_div_by_5 import*
from is_prime import*
from modulos import*

while True:
    print("Options: ")
    print("a. Add") # + 'a' a. A add Add ADD add
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    print("e. Power of")
    print("f. Modulos")
    print("g.Exit")
    option = input("Enter your choice: ").lower()
    result = 0
    match option:
        case "add":
            numbers = user_input()
            result = add(int(numbers[0]), int(numbers[1]))

        case "subtract":
            numbers = user_input()
            result = subtract(int(numbers[0]), int(numbers[1]))

        case "multiply":
            numbers = user_input()
            result = multiply(int(numbers[0]), int(numbers[1]))

        case "power of":
            numbers = user_input()
            result = power_of(int(numbers[0]), int(numbers[1]))

        case "divide":
            numbers = user_input()
            result = divide(int(numbers[0]), int(numbers[1]))

        case "modulos":
            numbers = user_input()
            result = modulos(int(numbers[0]), int(numbers[1]))

        case "exit":
            quit()

        case _:
            print("Please pick a valid option.")

    print(f'The result is: {result}')
    is_div_by_5(result)
    is_even_odd(result)
    is_prime(result)
    print("###############################################")