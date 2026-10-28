# Expense Tracker Installment 4, Author: Mark Joshua L. Apor, The Tracker Makes Decisions
print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes...")
print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")
print("-" * 40)

name = input("What is your name? ")
print(f"Welcome, {name}, let's log two expenses.\n")
item = input("First expense? ")
amount = float(input("Amount? "))

if amount > 200:
    print("  are you sure?")
    print("  Huge expense.")
elif amount > 100:
    print("  Big expense.")
elif amount > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if  amount2 > 200:
    print("  are you sure?")
    print("  Huge expense.")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount > 100 and amount2 > 100:
    print("  slow down!")
    print("  Two big expenses in a row")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))


subtotal = amount + amount2
avg = subtotal / 2.0
tax = subtotal * (tax_rate / 100.0)
grand_total = subtotal + tax

print("-" * 40)
print(f"\nSUMMARY for {name}")
print(f"{item + ':':<15}${amount:.1f}")
print(f"{item2 + ':':<15}${amount2:.1f}")
print(f"{'Subtotal:':<15}${subtotal:.1f}")
print(f"{'Average:':<15}${avg:.1f}")
print(f"{f'Tax ({tax_rate:.1f}%):':<15}${tax:.1f}")
print(f"{'Grand total:':<15}${grand_total:.1f}\n")

if grand_total > budget:
    over_amt = grand_total - budget
    print(f"Over budget by ${over_amt}!\n")
elif grand_total > (0.9 * budget):
    left_amt = budget - grand_total
    print(f"Careful: only ${left_amt} left.\n")
else:
    left_amt = budget - grand_total
    print(f"Within budget. ${left_amt} left.\n")

print("Made by: Mark Joshua L. Apor | Installment 4")