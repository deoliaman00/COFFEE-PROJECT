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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_integrients):
    # RETURNS TRIE IF ORDER CAN BE MADE OTHERWISE SAYS NO
    for item in order_integrients:
        if order_integrients[item] >= resources[item]:
            print(f"Sorry we are out of order.{item} ")
            return False
    return True

def process_coins():
    #RETURNS THE TOTAL CALCULATED
    print("Please insert the coins: ")
    total= int(input("How many quarters: "))* 0.25
    total +=int(input("How many quarters: ")) * 0.1
    total += int(input("How many quarters: ")) * 0.05
    total +=int(input("How many quarters: ")) * 0.01
    return total


def id_transaction_successful(money_rec,drink_cost):
    #'''THIS FUNC CHECKS IF THE USER HAS ENTERED ENOUGH MONEY TO GET THE PRODUCT OR LESS'''
    if money_rec>= drink_cost:
        change=round(money_rec-drink_cost,2)
        print(f"Change is {change}")
        global profit
        profit +=drink_cost
        return True
    else:
        print("Sorry the money is not enough")
        return False


def makecoffee(drink_name,order_indegredients):
    ## DEDUCTING THE RESOURCES WILL
    for item in order_indegredients:
        resources[item] -= order_indegredients[item]
    print(f"Here is your coffee {drink_name} ")







is_on = True

# TODO: luckyou
while is_on:
    choice = input("what would you like? Espresso, latte or cappuccino.")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee:{resources['coffee']}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payement=process_coins()
            id_transaction_successful(payement,drink['cost'])
            makecoffee(choice,drink["ingredients"])

