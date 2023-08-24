from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# OBJECTS 
###############
# MONEY
# Create money machine object 
money_machine = MoneyMachine()

# COFFE
# Create coffe maker object
coffe_maker = CoffeeMaker()

# MENU
# Create a menu object
menu = Menu()

# Machine is on
is_on = True


# RESOURCES 
###############
# There is enough resources 
#coffe_maker.is_resource_sufficient('latte')


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? latte{options}\n")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        # Print report of all resources
        print(coffe_maker.report()) 
        # Print report of profit 
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink)and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
        
        



drink = menu.find_drink(choice)