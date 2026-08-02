# ============================================
# Arshiya's Pizza Palace
# Shopping Cart Project
# ============================================

print("=" * 50)
print("      Welcome to Arshiya's Pizza Palace!")
print("=" * 50)
print()

# My restaurant Menu
menu = [
    "Cheese Pizza",
    "Pepperoni Pizza",
    "Garlic Bread",
    "Soft Drink",
    "Chocolate Cake",
    "Pasta"
]

# The prices are in order so it matches
price = [12.99, 14.99, 5.99, 2.99, 6.99, 11.99]

# I printed the menu so it looks pretty
print("--------------- MENU ---------------")
print(f'{"ITEM":<30}{"PRICE ($)":>10}')
print("-" * 40)

# This will help to display each item and its price. I wanted it to be aligned so it looks neat.
for i in range(len(menu)):
    print(f'{str(i+1)+". "+menu[i]:<30}${price[i]:>8.2f}')

#Option 7 is to proceed to checkout, so like whenever u r done ordering
print("7.\tCheckout")
print()
#There is a fun special to attract the customers.
print("Today's Special!")
print("Buy any Pizza and receive 10% OFF that pizza!")
print()

# These lists help to store everything that the customer buys
shopping_cart = []
shopping_quant = []

# Keep the restaurant open until the customer decides to checkout
shopping_complete = False

while shopping_complete == False:

    # Ask the customer what they want to order
    order = int(input("Choose an item (1-7): "))

    # Make sure they picked one of the menu items
    if order >= 1 and order <= 6:

        print("You selected:", menu[order-1])

        # Ask how many they would like
        quantity = int(input("How many would you like? "))

        # I don't want anyone ordering 0 or negative pizzas :)
        while quantity <= 0:
            print("Quantity must be greater than 0.")
            quantity = int(input("Enter quantity again: "))

        # If they've already ordered this before, just increase the quantity
        if menu[order-1] in shopping_cart:

            index = shopping_cart.index(menu[order-1])
            shopping_quant[index] += quantity

        # Otherwise, add it to the shopping cart for the first time
        else:

            shopping_cart.append(menu[order-1])
            shopping_quant.append(quantity)

        print(quantity, menu[order-1], "added to your cart!")

        # Every pizza deserves a drink, so let's recommend one!
        if menu[order-1] == "Cheese Pizza" or menu[order-1] == "Pepperoni Pizza":

            recommend = input("Soft drinks with pizza are so yummy! Would you like to add a Soft Drink for $2.99? (yes/no): ")

            # If they say yes, add a drink to their cart
            if recommend.lower() == "yes":

                # If there's already a drink in the cart, just add another one
                if "Soft Drink" in shopping_cart:

                    drink_index = shopping_cart.index("Soft Drink")
                    shopping_quant[drink_index] += 1

                # Otherwise, add the first Soft Drink
                else:

                    shopping_cart.append("Soft Drink")
                    shopping_quant.append(1)

                print("Soft Drink added to your cart!")

        print()

    # Customer is finished shopping
    elif order == 7:

        shopping_complete = True

    # Handle any numbers that aren't on the menu
    else:

        print("Invalid choice. Please enter a number from 1 to 7.")
        print()


print()
print("="*60)
print("                 RECEIPT")
print("="*60)


print(f'{"Item":<25}{"Qty":>6}{"Unit":>12}{"Total":>12}')
print("-" * 60)

grand_total = 0

# This loop will help me calculate the price. 
for i in range(len(shopping_cart)):
    menu_index = menu.index(shopping_cart[i])

    unit_price = price[menu_index]
    total = unit_price * shopping_quant[i]

    # Pizza discount...this helps with the discount special. 
    if shopping_cart[i] == "Cheese Pizza" or shopping_cart[i] == "Pepperoni Pizza":
        total *= 0.9

    total = round(total, 2)
    grand_total += total

    print(f'{shopping_cart[i]:<25}{shopping_quant[i]:>6}${unit_price:>11.2f}${total:>11.2f}')

print("-" * 60)
print(f'{"Grand Total:":<43}${grand_total:>11.2f}')
print("=" * 60)

# Thank you customer for visiting my restaurant!
print("Thanks for visiting Arshiya's Pizza Palace! 🍕")
print("Hope to see you again soon!")
#I thought of pizza restaurant because I love pizza and cheese and pepperoni are the most common ones in America. 
#If we have pizza, we have to include pasta. and in a restaurant you always need dessert. 
