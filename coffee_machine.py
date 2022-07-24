MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
print(resources)
#type_of_coffe = input("What would you like? (espresso/latte/capuccino):")
#print(f'the cost of your coffee is  {MENU[type_of_coffe]["cost"]}')



#the sum of your money

#print("Pleas insert coins ")

#print("your rest after purchase:")
#print(total - MENU[type_of_coffe]["cost"])

# resources after making coffee

# loop for water in coffee machine

def coins():
    total = float(input("how many pennies? ")) * 0.01
    total += float(input("how many nickles? ")) * 0.05
    total += float(input("how many dimes? ")) * 0.1
    total += float(input("how many quarters? ")) * 25
    return total



type_of_coffe = input("What would you like? (espresso/latte/cappuccino):")

def all_resources(ingredients):
    for res in ingredients:
        if ingredients < resources[res]:
            print(f"Not enough {res} in machine")
            return False
    return True


def transaction(your_money, drink_cost):
    if your_money >= drink_cost:
        rest=
