# Expense Tracker Installment 5, Author: Mark Joshua L. Apor, The Menu Comes Alive
 

print("=" * 40)
print("          EXPENSE TRACKER")
print("      Installment 5: The Menu Comes Alive")
print("=" * 40)
 
AUTHOR = "Mark Joshua L. Apor"
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))    
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")
 
count = 0          
subtotal = 0.0     
choice = ""       
 

while choice != "4":
    print()
    print("MAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")
 
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount          
        count += 1
 
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
 
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
 
    elif choice == "3":
        tax = round(subtotal * tax_percent / 100, 2)
        total = round(subtotal + tax, 2)
        over_budget = total > budget
        left = round(budget - total, 2)
 
        print(f"  {'Expenses:':<14}{count}")
        print(f"  {'Subtotal:':<14}${round(subtotal, 2)}")
        print(f"  {f'Tax ({tax_percent}%):':<14}${tax}")
        print(f"  {'Grand total:':<14}${total}")
 
        if over_budget:
            print(f"  Over budget by ${round(total - budget, 2)}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")
 
    elif choice == "4":
        print(f"Goodbye, {name}!")
 
    else:
        print("  Please choose 1, 2, 3 or 4.")
 
print("-" * 40)
print(f"Made by: {AUTHOR}  |  Installment 5")
print("=" * 40)
