# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from resource_data import MENU
from resource_data import resources



profit = 0
# TODO: 2. Check the resources are sufficient or not
def resources_sufficient(order_ingredients):
    """Return True if order can be made and False if ingredient are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# TODO: 3. Process coins
def coin_processing():
    """Returns the Total calculated from the coins inserted"""
    print("Please insert coin.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
# TODO: 4. Check transaction successful?
def transaction(money_received, drink_cost):
    """Return True if payment is accepted, or false if money is insufficient"""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += drink_cost
        return True
    else:
        print("“Sorry thats not enough money, Money refunded.")
        return False
# TODO: 5. Make coffee
def coffee_making(drink_name, order_ingredient):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}, Enjoy!! ")
# TODO: 1. Print report for the available resources in the machine
is_on = True
while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
           payment = coin_processing()
           if transaction(payment, drink["cost"]):
              coffee_making(choice, drink["ingredients"])









