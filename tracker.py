# Expense Tracker Installment 2, Author: Mark Joshua L. Apor, Tracker takes input and shows summary
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes...")
print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")
print("-" * 40)


name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
Tax_Rate = float(input("Tax Rate %? "))
budget = float(input("What's your budget? "))


average = (amount1 + amount2) / 2
total = amount1 + amount2
tax = total * (Tax_Rate / 100)
grandtotal = total + tax
overbudget = bool(budget < grandtotal)
remaining_budget = budget - grandtotal

print("-" * 40)
print("SUMMARY")
print(f"- {item1}:\t\t${amount1}")
print(f"- {item2}:\t\t${amount2}")
print(f"Subtotal:\t\t${total}")
print(f"Average:\t\t${average}")
print(f"Tax {Tax_Rate}%:\t\t${tax}")
print(f"Grand Total:\t\t${grandtotal}")
print(f"Over Budget?:\t\t{overbudget}")
print(f"Left in budget:\t\t${remaining_budget}")
print("-" * 40)
print("Made by: Mark Joshua L. Apor | Installment 3")
print("=" * 40)

