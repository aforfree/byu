""""
10 Prove: Assignment - Shopping Cart Program
File: cse110_lesson10.py
Author: Evgeny Kozlov
github.com/aforfree/byu

Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Added check for item rove out of index range,
            added quit option, used match statement
"""

cart = []
prices = []

print("Welcome to the Shopping Cart Program!")
while True:
    print(
        "Plese select one of the folowing options: \n"
        "1. Add item to cart \n"
        "2. View cart \n"
        "3. Remove item from cart \n"
        "4. Calculate count of items in cart \n"
        "5. Calculate total price of items in cart \n"
        "6. Quit \n"
    )
    user_choice = input("Enter number, or QUIT): ").lower()

    match user_choice:
        case "1":
            item = input("What item would you like to add? ")
            cart.append(item)
            price = int(input("What is its price? "))
            prices.append(price)

            print(f"'{item}' has been added to your cart.")
            print(f"There are now {len(cart)} items in your cart.")

        case "2":
            if sum(cart) == 0:
                print("Your cart is empty.")
            else:
                print("Here are items in your cart:")

            for i, item in enumerate(cart):
                print(f"{i+1}. {item} - ${prices[i]:.2f}")

        case "3":
            if len(cart) == 0:
                print("Your cart is empty.")
            else:
                print("Here are items in your cart:")
                for i, item in enumerate(cart):
                    print(f"{i+1}. {item} - ${prices[i]:.2f}")

                while remove := int(input("What item you want to remove? ")):
                    if remove <= 0:
                        print("Please enter a number greater than 0.")
                    elif remove > len(cart):
                        print(f"{remove} is out of your cart items count.")
                    else:
                        break

                remove -= 1
                item_name = cart.pop(remove)
                prices.pop(remove)
                print(f"The {item_name} has been removed from your cart.")
                print(f"There are now {len(cart)} items in your cart.")

        case "4":
            print(f"There are {len(cart)} items in your cart.")

        case "5":
            total = 0
            print(f"The total price of your cart is ${sum(prices):.2f}.")

        case "6" | "quit":
            print("Thank you for using the Shopping Cart Program!")
            break

        case _:
            print("That is not a valid option. Please try again.")
    print("")
