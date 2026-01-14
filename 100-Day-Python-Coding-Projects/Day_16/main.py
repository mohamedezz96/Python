from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_power = True
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
while 1 :
    print(menu.get_items())
    user_input = input("What Would You Like To Drink From Our Menu: ").lower()

    if user_input == "off":
        coffee_machine_power = False
        break
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_input)
        if menu_item != None:
            if coffee_machine.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_machine.make_coffee(menu_item)
