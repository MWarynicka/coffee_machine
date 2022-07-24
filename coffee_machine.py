MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0
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

# loop for water in coffee machine
old = resources["water"]
while True:
    type_of_coffe = input("What would you like? (espresso/latte/capuccino):")
    new = MENU[type_of_coffe]["ingredients"]["water"]
    current_water = old - new
    old = current_water
    print(current_water)
    if current_water > new:
        continue
    elif current_water < new :
        print("Not enough water")
        break
        
# loop for milk in coffee machine 
old_milk = 200
while True:
    type_of_coffe = input("What would you like? (espresso/latte/cappuccino): ")
    new_milk = MENU[type_of_coffe]["ingredients"]["milk"]
    print(f"Milk to preparation of this coffee {new_milk}")
    current_milk = old_milk - new_milk
    old_milk = current_milk
    if type_of_coffe == "cappuccino" or "latte":
        if current_milk < new_milk and current_milk > 0:
            print(f"Rest milk {current_milk}")
        elif current_milk <= 0:
            print("Not enough milk")
            break
#  loop for coffee in coffee machine          
            
old_coffe= resources["coffee"]
while True:
    type_of_coffe = input("What would you like? (espresso/latte/cappuccino): ")
    new_coffe= MENU[type_of_coffe]["ingredients"]["coffee"]
    current_coffe= old_coffe - new_coffe
    old_coffe = current_coffe
    if current_coffe > new_coffe:
        print(f"Rest coffee {current_coffe}")
        continue
    elif current_coffe < new_coffe:
        print("no coffee")
        break

print(f"water= {current_water}, milk= {current_milk}, coffee= {current_coffe}")
