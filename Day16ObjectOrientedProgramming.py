from Day16Menu import Menu, MenuItem
from Day16CoffeeMaker import CoffeeMaker
from Day16MoneyMachine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
#menu_items = MenuItem()
is_on = True

while is_on:
    options = menu.get_items()
    user_input = str(input(f'What would you like? ({options}): ')).lower()
    if user_input == 'off':
        is_on == False
    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
