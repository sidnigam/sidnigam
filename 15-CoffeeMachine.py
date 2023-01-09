MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_money(drink, quarters, dimes, nickels, pennies):
    total = float(quarters) * 0.25 + float(dimes) * 0.10 + float(nickels) * 0.05 + float(pennies) * 0.01
    change = round(total - MENU[drink]["cost"], 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded!")
        return False
    else:
        print(f'Here is ${change} in change.')
        profit = MENU[drink]["cost"]
        return profit


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water!")
        return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee!")
        return False
    elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk!")
        stop_machine = True
        return False
    else:
        resources_used = {
            "water": MENU[drink]["ingredients"]["water"],
            "coffee": MENU[drink]["ingredients"]["coffee"],
            "milk": MENU[drink]["ingredients"]["milk"],
        }
        return resources_used


def run_coffee_machine():
    stop_machine = False
    while not stop_machine:
        request = input("What would you like? (type 'espresso', 'latte', or 'cappuccino'):\n")
        if request == 'off':
            stop_machine = True
        elif request == 'report':
            print(
                f'Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
        else:
            resources_used = check_resources(drink=request)
            if not resources_used:
                run_coffee_machine()
            else:
                q, d, n, p = input(
                    "Please enter how much money you put in (quarters, dimes, nickels, pennies): ").split()
                profit = check_money(drink=request, quarters=q, dimes=d, nickels=n, pennies=p)
                resources["money"] += profit
                resources["milk"] -= resources_used["milk"]
                resources["water"] -= resources_used["water"]
                resources["coffee"] -= resources_used["coffee"]
                print(f"Here is your {request}. Enjoy!")


run_coffee_machine()
