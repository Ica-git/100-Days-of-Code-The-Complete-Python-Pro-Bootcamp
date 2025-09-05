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

def report(resource_dictionary):
    water = resource_dictionary["water"]
    milk = resource_dictionary["milk"]
    coffee = resource_dictionary["coffee"]
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: $0")

def sufficient_resources(resource_dictionary, menu_dictionary, coffee_choice):
    resource_water = resource_dictionary["water"]
    resource_milk = resource_dictionary["milk"]
    resource_coffee = resource_dictionary["coffee"]

    needed_water = menu_dictionary[coffee_choice]["ingredients"]["water"]
    needed_coffee = menu_dictionary[coffee_choice]["ingredients"]["coffee"]

    if "milk" in menu_dictionary[coffee_choice]["ingredients"]:
        needed_milk = menu_dictionary[coffee_choice]["ingredients"]["milk"]
    else:
        needed_milk = 0

    if resource_water <= 0 or resource_milk <= 0 or resource_coffee <= 0:
        return  False


    # debugg 1
    # print(f"{resource_water}, {needed_water}\n"
    #       f"{resource_coffee}, {needed_coffee}\n"
    #       f"{resource_milk}, {needed_milk}\n")

    missing_resource = ""

    if resource_water < needed_water:
        missing_resource = "water"
        print(f"Sorry there is not enough {missing_resource}.")
        return False
    elif resource_milk < needed_milk:
        missing_resource = "milk"
        print(f"Sorry there is not enough {missing_resource}.")
        return False
    elif resource_coffee < needed_coffee:
        missing_resource = "coffee"
        print(f"Sorry there is not enough {missing_resource}.")
        return False
    else:
        return True

def insert_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"You have inserted: ${money}")
    return money


def make_cofee(resource_dictionary, menu_dictionary, coffee_choice, current_money):

    needed_water = menu_dictionary[coffee_choice]["ingredients"]["water"]
    needed_coffee = menu_dictionary[coffee_choice]["ingredients"]["coffee"]
    if "milk" in menu_dictionary[coffee_choice]["ingredients"]:
        needed_milk = menu_dictionary[coffee_choice]["ingredients"]["milk"]
    else:
        needed_milk = 0

    needed_money = menu_dictionary[coffee_choice]["cost"]

    needed_money = round(needed_money, 2)
    current_money = round(current_money, 2)

    resource_dictionary["water"] -= menu_dictionary[coffee_choice]["ingredients"]["water"]
    resource_dictionary["coffee"] -= menu_dictionary[coffee_choice]["ingredients"]["coffee"]

    if needed_milk != 0:
        resource_dictionary["milk"] -= menu_dictionary[coffee_choice]["ingredients"]["milk"]

    change = current_money - needed_money

    print(f"Here is ${change:.2f} in change.")
    current_money -= needed_money

    print(f"Here is your {coffee_choice} ☕ Enjoy!")

def process(current_drink_cost,resource_dictionary,menu_dictionary, coffee_choice):
    current_money = insert_coins()
    if current_money < current_drink_cost:
        while current_money < current_drink_cost:
            print(f"Sorry that's not enough money. ${current_money} refunded.")
            current_money = insert_coins()
        make_cofee(resource_dictionary, menu_dictionary, coffee_choice, current_money)
    else:
        make_cofee(resource_dictionary, menu_dictionary, coffee_choice, current_money)



#before we start
is_running = True


#print a resource report



while is_running:
    choice = input("What would you like? ☕ (espresso/latte/cappuccino) ☕: ")
    if choice == "report":
        report(resources)
    elif choice == "off":
        is_running = False
        break
    elif choice == "espresso":
        drink_cost = MENU["espresso"]["cost"]

        possible = sufficient_resources(resources, MENU, choice)
        if possible:
            process(drink_cost,resources, MENU,choice)
        else:
            continue

    elif choice == "latte":
        drink_cost = MENU["latte"]["cost"]

        possible = sufficient_resources(resources, MENU, choice)
        if possible:
            process(drink_cost,resources, MENU,choice)
        else:
            continue

    elif choice == "cappuccino":
        drink_cost = MENU["cappuccino"]["cost"]

        possible = sufficient_resources(resources, MENU, choice)
        if possible:
            process(drink_cost,resources, MENU,choice)
        else:
            continue

#check input

#check resources

#sufficient resources (check)

#process coins
#calculate the value

#check transaction success if not refund

#make a coffee, and deduct the resources










