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
print(resources)
type_of_coffe = input("What would you like? (espresso/latte/capuccino):")
print(f'the cost of your coffee is  {MENU[type_of_coffe]["cost"]}')



#the sum of your money

print("Pleas insert coins ")
penny = float(input("how many pennies? "))
nickel = float(input("how many nickles? "))
dime = float(input("how many dimes? "))
quarter = float(input("how many quarters? "))

total= penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 25
print(total)

print("your rest after purchase:")
print(total - MENU[type_of_coffe]["cost"])

# resources after making coffee

for water in resources:
    old= resources["water"]
    new= MENU[type_of_coffe]["ingredients"]["water"]
    current_water= old - new

for milk in resources:
    old_milk= resources["milk"]
    new_milk= MENU[type_of_coffe]["ingredients"]["milk"]
    current_milk= old_milk - new_milk

for coffe in resources:
    old_coffe= resources["coffee"]
    new_coffe= MENU[type_of_coffe]["ingredients"]["coffee"]
    current_coffe= old_coffe - new_coffe

print(f"water= {current_water}, milk= {current_milk}, coffee= {current_coffe}")
