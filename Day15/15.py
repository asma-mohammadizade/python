# coffe-machine

from data import MENU, resources
total_money = 0 

def measure(drink):
    if drink == "report":
        return (f"Water: {resources['water']}ml\n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: ${total_money}")
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def check_resources(drink):
    if resources["water"] > MENU[drink]["ingredients"]["water"]:
        if resources["milk"] > MENU[drink]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[drink]["ingredients"]["coffee"]:
                return True
            else:
                print("sorry there is not enough coffee")
                return False
        else:
            print("sorry there is not enough milk")
            return False
    else:
        print("sorry there is not enough water")
        return False


def price(drink):
    global total_money
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    cost = quarter * 0.25 + dime * 0.10 + nickles * 0.05 + pennies * 0.01
    total_money += cost
    if cost >= MENU[drink]["cost"]:
        change = round(cost - MENU[drink]["cost"], 2)
        print(f"here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money, money refunded")
        return False
    


def stop_working(drink):
    if MENU[drink]["ingredients"]["water"] < 50 or MENU[drink]["ingredients"]["milk"] < 100:
        print("turn off")
        return False
    else:
        return True



is_continue = True
while is_continue:
    drink = input("what would you like? (espresso/ latte/ cappuccino)\n")

    if drink == "report":
         print(measure(drink))
         continue
    

    get_coffee = check_resources(drink)
    if get_coffee:
        print("Please insert coins.")
        if price(drink):
            print(f"Here is your {drink} Enjoy!")
            measure(drink)
    else:
        print("Sorry, cannot process your order.")
        is_continue = False

    if not stop_working(drink):
        is_continue = False


        

