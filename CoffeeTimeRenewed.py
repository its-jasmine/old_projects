# Jasmine Gad El Hak
# This is a self-serve coffee ordering machine.

# global variable declarations
global ordertext
global cost

# this variable will contain the cost sum for entire order with tax
billcost = 0.00

# this variable will contain the accumulated total bill value
totalcost = 0.00

# this variable will contain the accumulated list of items in the order.
totalordertext = ""


def order():  # defining a function
    # assigning value to variables
    cost = 0.00
    ordertext = ""
    drink = input("Select a beverage.\n A. Coffee \n B. Latte \n C. Cappuccino ") # assigns user input to variable
    if drink == "A":
        # assigns value to variables
        ordertext += "Coffee " # assigns existing value + new value
        temp = input("Select a drink type.\n A. Hot \n B. Iced ")
        if temp == "A":
            # assigns value to variable
            cost = coffee
        elif temp == "B":
            ordertext = "Iced " + ordertext  # assigns existing value + new value
            cost = coffee * ice  # calculates and assigns value to variable
        else:
            # prints message
            print("That is not a valid response. Try again.")
    elif drink == "B":
        # assigns value to variables
        ordertext = "Latte "
        temp = input("Select a drink type.\n A. Hot \n B. Iced ")
        if temp == "A":
            cost = latte  # assigns value to variable
        elif temp == "B":
            ordertext = "Iced " + ordertext  # assigns existing value + new value
            cost = latte * ice  # calculates and assigns value to variable
    elif drink == "C":
        # assigns values to variables (cappuccinos cannot be iced in my program)
        ordertext = "Cappuccino "
        cost = cappuccino
    else:
        print("That is not a valid response. Try again.")  # prints message
    return cost, ordertext


def bill():  # defining a function
    billcost = "$" + str("%.2f" % (totalcost * 1.13))  # assigns value to variable in currency format w/ tax
    print("Your order: \n%sYour total is %s" % (totalordertext, billcost))  # prints order and total cost


# these are the drinks with their designated price (hot)
coffee = 1.25
latte = 2.00
cappuccino = 2.75

# this is the % increase to the beverage if the option is chosen
ice = 1.05 # * 1.05
decaf = 1.05 # * 1.05

# these are additional costs for added flavours
vanilflav = 0.25 # + $0.25
chocoflav = 0.15 # + $0.25

print("Welcome to the self serve coffee vending machine.")  # welcomes the customer by printing message

ordervalues = order() # runs the order function and assigns return value to variable
cost = ordervalues[0] # accessing list value to retrieve both
ordertext = ordervalues[1]


caffeine = input("Would you like your drink to be...\n A. Caffeinated \n B. Decaf ")  # assigns user input to variable
if caffeine == "B":
    ordertext = "Decaf " + ordertext # assigns existing value + new value
    cost *= decaf # assigns existing value * new value

# assigns user input to variable
option = input("Would you like any added flavours? \n A. Vanilla \n B.Chocolate \n C. No Thanks ")
if option == "A":
    # assigns existing value + new value
    cost += vanilflav
    ordertext = "Vanilla " + ordertext
elif option == "B":
    # assigns existing value + new value
    cost += chocoflav
    ordertext = "Chocolate " + ordertext
elif option != "C":
    print("That is not a valid response. Try again. ")  # displays string

done = input("Would you like to add another item to your order? \n Y. yes \n N. no ")  # assigns user input to variable
totalcost += cost  # adds to the value of the variable
totalordertext += ordertext + "\n" # adds to the value of the variable and creates a new line

while done == "Y":
    cost = 0.00
    ordertext = ""
    ordervalues = order()  # runs the order function and assigns return value to variable
    cost = ordervalues[0]
    ordertext = ordervalues[1]

    # assigns user input to variable
    caffeine = input("Would you like your drink to be...\n A. Caffeinated \n B. Decaf ")
    if caffeine == "B":
        ordertext = "Decaf " + ordertext
        cost *= decaf  # assigns existing value * new value

    # assigns user input to variable
    option = input("Would you like any added flavours? \n A. Vanilla \n B.Chocolate \n C. No Thanks ")
    if option == "A":
        # assigns existing value + new value
        cost += vanilflav
        ordertext = "Vanilla " + ordertext
    elif option == "B":
        # assigns existing value + new value
        cost += chocoflav
        ordertext = "Chocolate " + ordertext
    elif option != "C":
        print("That is not a valid response. Try again. ")  # displays string

    done = input("Would you like to add another item to your order? \n Y. yes \n N. no ")  # assigns input to variable
    totalcost += cost  # adds to the value of the variable
    totalordertext += ordertext + "\n"  # adds to the value of the variable and creates a new line

if done == "N":
    bill()  # runs function
else:
    print("That is not a valid response. Try again.")  # displays string
