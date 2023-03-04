""""
09 Prove: Milestone - Shopping Cart Program
File: cse110_lesson09.py
Author: Evgeny Kozlov
github.com/aforfree/byu

Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Tricky question for price calculation,
            added quit option, used match statement
"""

cart = []

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
            add = input("What item would you like to add? ")
            cart.append(add)
            print(f"{add} has been added to your cart.")
            print(f"There are now {len(cart)} items in your cart.")
        case "2":
            print("Here are the items in your cart:")
            for item in cart:
                print(item)
        case "3":
            remove = input("What item would you like to remove? ")
            if remove in cart:
                cart.remove(remove)
                print(f"{remove} has been removed from your cart.")
                print(f"There are now {len(cart)} items in your cart.")
            else:
                print(f"{remove} is not in your cart.")
        case "4":
            print(f"There are {len(cart)} items in your cart.")
        case "5":
            total = 0
            print(f"The total price of items in your cart is ${total}.")
            print("Yopu haven't added any prices to your items yet. ;-)")
        case "6" | "quit":
            print("Thank you for using the Shopping Cart Program!")
            break
        case _:
            print("That is not a valid option. Please try again.")
    print("")
