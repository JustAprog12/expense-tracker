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


total = amount1 + amount2
average = total / 2


print("SUMMARY")
print("-" * 40)
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Mark Joshua L. Apor | Installment 2")
print("=" * 40)