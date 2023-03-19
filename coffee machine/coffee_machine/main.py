from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on :
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options})")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        new_coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        check_resources =new_coffee_maker.is_resource_sufficient(drink)
        if check_resources == True and money_machine.make_payment(drink.cost):
            new_coffee_maker.make_coffee(drink)
