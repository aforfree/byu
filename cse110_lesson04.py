""""
File: cse110_lesson04.py
Author: Evgeny Kozlov
github.com/aforfree/byu

Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Tip added to calculations, pep8 formatted
"""

child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))
chiildren_number = int(input("How many children are there? "))
adults_number = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? %"))
tip_amount = float(input("What is the tip? %"))

subtotal = child_meal_price * chiildren_number + \
    adult_meal_price * adults_number
sales_tax = subtotal * sales_tax_rate / 100
# Creativity: Tip added to calculations
tip = subtotal * tip_amount / 100
total = subtotal + sales_tax + tip

print(f"""
Subtotal: ${subtotal:.2f}
Sales tax: ${sales_tax:.2f}
Tip: ${tip:.2f}
====================
Total: ${total:.2f}
""")

payment_amount = float(input("What is the payment amount? $"))
change = payment_amount - total
print(f"Change: ${change:.2f}")
