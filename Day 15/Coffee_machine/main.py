resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from menu import MENU
import os

money_in_coffie_machine = 0

def check_can_make(item):
    if(resources["water"] < MENU[item]["ingredients"]["water"]):
        print('Sorry there is not enough water.')
    elif resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
        print('Sorry there is not enough coffee.')
    elif (not item == 'espresso') and resources["milk"] < MENU[item]["ingredients"]["milk"]:
        print('Sorry there is not enough milk.')
    else:
        return True
    return False

def make_coffee(item):
    resources["water"] -= MENU[item]["ingredients"]["water"]
    if (not item == 'espresso'):
        resources["milk"] -= MENU[item]["ingredients"]["milk"]
    resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
    print(f'Here is your {item} ☕. Enjoy!')

def get_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennines = int(input("How many pennines?: "))
    return quarters * .25 + dimes * .1 + nickles * .05 + pennines * .01

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == 'off':
        break
    if user_choice == 'report':
        print(f'''Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money_in_coffie_machine}''')
        continue
    if check_can_make(user_choice):
        money_got = get_money()
        if money_got >= MENU[user_choice]["cost"]:
            money_in_coffie_machine += money_got
            print(f"Here is ${round(money_got - MENU[user_choice]['cost'], 2)} in change.")
            make_coffee(user_choice)
        else:
            print("Sorry that's not enough money. Money refunded.")
