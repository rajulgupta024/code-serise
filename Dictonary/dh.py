price = float(input("Enter the price:\n"))
quantity = float(input("Enter the quantity:\n"))
amount = price * quantity

if amount >= 100:
    discount = amount*0.10
    amount = amount - discount

print(f"Total amount to be paid: {amount}")