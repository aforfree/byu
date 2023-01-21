# CSE110 lesson 03
# by Evgeny Kozlov
# github.com/aforfree/byu

# Submission comment:
# Grade: 5. Made it my own
# Creativity: I added tip to calculate total

child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))
chiildren_amount = int(input("How many children are there? "))
adults_amount = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? %"))
tip_amount = float(input("What is the tip amount? %"))

subtotal = child_meal_price * chiildren_amount + \
    adult_meal_price * adults_amount
sales_tax = subtotal * sales_tax_rate / 100
tip = subtotal * tip_amount / 100
total = subtotal + sales_tax + tip

print(f"""
Subtotal: ${subtotal:.2f}
Sales tax: ${sales_tax:.2f}
Tip: ${tip:.2f}
Total: ${total:.2f}""")

payment_amount = float(input("What is the payment amount? $"))
change = payment_amount - total
print(f"Change: ${change:.2f}")
