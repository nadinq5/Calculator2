def validate_numbers(a, b):
    return a.isnumeric() and b.isnumeric()

def print_validity(is_valid:bool):
    if(is_valid == False):
        print("Invalid arguments. Please enter again.")


def validation(a, b):
    is_valid = validate_numbers(a, b)
    print_validity(is_valid)
    return is_valid

def user_input():
    a = 0
    b = 0
    is_valid = False
    num_list = []
    while not is_valid:
        a = input("Please enter the first number: ")
        b = input("Please enter the second number: ")
        is_valid = validation(a, b)
    num_list.append(a)
    num_list.append(b)
    return num_list