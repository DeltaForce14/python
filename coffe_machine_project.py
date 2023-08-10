
''' COFFEE MACHINE PROJECT  
Create code for coffee machine
3 hot flavours: 
Espresso - 50ml water, 18g coffee - $1.5
Latte - 200ml water, 24g coffee,150ml milk - $2.5
Cappuccino  - 250ml water, 24g coffee, 150ml milk - $3 
Coin operated: 1 cent, 5 cent, 10 cent, 25 cent 

Coffee machine starting resources: 
300ml water
200ml milk
100g coffee

Coffe machine needs to do:
1. Print report of available resources. (add as an option to coffee request) / water, milk, coffee, money 
2. Check if resources are sufficient 
3. Ask to insert coins
4. check if transaction was successful 
'''
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coffee_menu = {
    'Espresso': {
        'Water': '50ml',
        'Coffee': '18g',
        'Price': '$1.5'
    },
    'Latte': {
        'Water': '200ml',
        'Coffee': '24g',
        'Milk': '150ml',
        'Price': '$2.5'
    },
    'Cappuccino': {
        'Water': '250ml',
        'Coffee': '24g',
        'Milk': '150ml',
        'Price': '$3'
    }
}

money_earned = 0

while True:
    choice = input("What would you choose? Latte(L),Cappuccino(C), or Espresso(E)?")  

    if choice == "STOP":
        break

    # Get key for coffe_menu, variable userchoise
    if choice == "L":
        userchoice = "Latte"
    elif choice == "C":
        userchoice = "Cappuccino"   
    elif choice ==  "E":
        userchoice = "Espresso"
    elif choice == 'I':   
        userchoice = 'inventory'

    
    # Check Resources 
    def check_resources_available(coffe_resources):
        # get key (ingredient) and value (quantity) from coffee_menu dictionary
        for ingredient, quantity in coffe_resources.items():
            if quantity <= 0:
                return False  
            return True      


    def deduct_resources(coffee_type):
        for ingredient, quantity in coffee_menu[coffee_type].items():
            if ingredient != 'Price':
                unit = quantity[-1:]  # Get the last two characters to check if it's ml or g
                if unit == 'g':
                    amount = int(quantity[:-1]) # Get the numerical value of the quantity
                else:
                    amount = int(quantity[:-2])   # Get the numerical value of the quantity 
                resources[ingredient.lower()] -= amount

    # Calculate profit from coffee             
    def coffe_profit(coffe_type, money):
        if userchoice == "inventory":
            return money
        else:  
            for ingredient, quantity in coffee_menu[coffe_type].items():
                if ingredient == 'Price':
                    # get everything from Price value except first character and turn to float 
                    money += float(quantity[1:])
            return money

    # Print inventory 
    def return_inventory():
        print(resources)
        print(coffe_profit(userchoice, money_earned))

    print(userchoice)    

    # Check if there are enough resources for the chosen coffee type
    if userchoice in coffee_menu:
        if check_resources_available(resources):
            print(f"There are enough resources to make {userchoice}.")
            deduct_resources(userchoice)
            money_earned = coffe_profit(userchoice, money_earned)  # Update money_earned
            print(f"Enjoy your {userchoice}!")
        else:
            print(f"Sorry, not enough resources to make {userchoice}.")

    return_inventory()     

