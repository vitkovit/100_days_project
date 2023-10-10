MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#“What would you like? (espresso/latte/cappuccino):”
#
#
#

def menu():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice in MENU:
        for key, value in MENU[user_choice]["ingredients"].items():
            if key == "coffee":
                print(f"{key.title()}: {value} g")
            else:
                print(f"{key.title()}: {value} ml")
        print(f"Cost : {MENU[user_choice]['cost']} $")
    else:
        print("That is not an option! Try again")
    fund = coins()
    print(f"you have available ${fund}")

def coins():
    quarters = int(input("how many quarters: ")) * 0.25
    dimes = int(input("how many dimes: ")) * 0.1
    nickles = int(input("how many nickles: ")) * 0.05
    pennies = int(input("how many pennies: ")) * 0.01
    domar_amout = round(quarters+dimes+nickles+pennies, 2)
    return domar_amout

while True:
    menu()

