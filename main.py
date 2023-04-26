import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe = coffee_maker.CoffeeMaker()
menu = Menu()
money = MoneyMachine()
while True:
    drink =input("What would you like? (espresso/latte/cappuccino/): ")

    if drink == "espresso":
        name = menu.find_drink("espresso")
        if coffe.is_resource_sufficient(name) == True:
            if money.make_payment(name.cost)==True:
                coffe.make_coffee(name)
    elif drink == "cappuccino":
        name = menu.find_drink("cappuccino")
        if coffe.is_resource_sufficient(name) == True:
            if money.make_payment(name.cost)==True:
                coffe.make_coffee(name)
    elif drink == "latte":
        name = menu.find_drink("latte")
        if coffe.is_resource_sufficient(name) == True:
            if money.make_payment(name.cost)==True:
                coffe.make_coffee(name)
    elif drink == "report":
        coffe.report()
        money.report()

    elif drink == "off":
        False
    elif drink == "menu":
        menu.get_items()

    else:
        menu.find_drink(drink)


