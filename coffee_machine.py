from data import MENU

profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ask_user_for_order():
    choice = ""
    while not(choice in ["espresso", "latte", "cappuccino", "off", "report"]):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    print("_" * 50)


def check_resources(beverage):
    sufficient = False

    if MENU[beverage]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
    elif beverage != "espresso" and MENU[beverage]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
    elif MENU[beverage]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
    else:
        sufficient = True

    return sufficient


def insert_coins_and_calculate_amount():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    amount = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

    return amount


def process_transaction(beverage, money):
    change = round(money - MENU[beverage]["cost"], 2)

    # TODO 8. Change shall be given back if money is more than cost
    print(f"Here is ${change} dollars in change.")

    resources["water"] -= MENU[beverage]["ingredients"]["water"]

    if beverage != "espresso":
        resources["milk"] -= MENU[beverage]["ingredients"]["milk"]

    resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]
    earnings = MENU[beverage]["cost"]

    return earnings


def is_enough_money(beverage, money):
    if MENU[beverage]["cost"] <= amount:
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


is_machine_on = True

while is_machine_on:
    # TODO 1. Prompt the user "What they want"
    user_choice = ask_user_for_order()

    # TODO 2. If "off" is entered into the prompt, machine shall turn off (secret)
    if user_choice == "off":
        is_machine_on = False
    # TODO 3. Print the report if prompt is "report".
    elif user_choice == "report":
        print_report()
    else:
        # TODO 5. If resources are sufficient
        if check_resources(user_choice):
            # prompt user to enter coins, calculate total value of coins
            amount = insert_coins_and_calculate_amount()
            if is_enough_money(user_choice, amount):
                # TODO 7. If money is sufficient, update profit (reflected in report)
                profit += process_transaction(user_choice, amount)
                # TODO 9. For successful transaction, the resources are updated and success message is printed
                print(f"Here is your {user_choice}☕ Enjoy!")
                print("_"*50)