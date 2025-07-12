# calculator
from art import logo

def add(n1, n2):
    return n1 + n2
    


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    first_number = float(input("what's the first number?\n"))
    is_continue = True
    while is_continue:
        next_number = float(input("what's the next number?\n"))
        choose_function = input("what function do you want?\n +\n -\n *\n /\n my function is: ")
        for function in functions:
            if choose_function == function:
                calculation = functions[function]
                answer = calculation(first_number, next_number)
                print(f"{first_number} {choose_function} {next_number} = {answer}")
                ask_continue = input(f"if you want to continue with {answer} type 'y', if you don't type 'n'\n")
            if ask_continue == "y":
                first_number = answer
            else:
                is_continue = False
                calculator()

calculator()
    




   




    