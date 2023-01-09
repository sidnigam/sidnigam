from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    request = input(f"What would you like? {menu.get_items()}:\n")
    if request == 'off':
        is_on = False
    elif request == 'report':
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(request)
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(menu.find_drink(request))