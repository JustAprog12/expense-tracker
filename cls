[1mdiff --git a/tracker.py b/tracker.py[m
[1mindex 6028f3b..cf0614b 100644[m
[1m--- a/tracker.py[m
[1m+++ b/tracker.py[m
[36m@@ -1,15 +1,34 @@[m
[31m-# Project: Expense Tracker Installment 1, Author: Mark Joshua L. Apor, A simple landing page for expense tracking[m
[32m+[m[32m# Expense Tracker Installment 2, Author: Mark Joshua L. Apor, Tracker takes input and shows summary[m
 print("=" * 40)[m
 print("\tEXPENSE TRACKER")[m
 print("\tKnow where your money goes...")[m
[31m-print("\nWelcome! This is your personal expense tracker.\n")[m
 print("MAIN MENU")[m
[31m-[m
 print("[1] Add an expense\t(coming soon)")[m
 print("[2] View all expenses\t(coming soon)")[m
 print("[3] Show total spent\t(coming soon)")[m
 print("[4] Exit\t\t(coming soon)")[m
 print("-" * 40)[m
[31m-print("Made by: Mark Joshua L. Apor | Installment 1")[m
[31m-print("=" * 40)[m
 [m
[32m+[m
[32m+[m[32mname = input("What's your name? ")[m
[32m+[m[32mprint(f"Welcome, {name}! Let's log two expenses.")[m
[32m+[m
[32m+[m[32mitem1 = input("First expense? ")[m
[32m+[m[32mamount1 = float(input("Amount? "))[m
[32m+[m[32mitem2 = input("Second expense? ")[m
[32m+[m[32mamount2 = float(input("Amount? "))[m
[32m+[m
[32m+[m
[32m+[m[32mtotal = amount1 + amount2[m
[32m+[m[32maverage = total / 2[m
[32m+[m
[32m+[m
[32m+[m[32mprint("SUMMARY")[m
[32m+[m[32mprint("-" * 40)[m
[32m+[m[32mprint(f"{item1}:\t\t${amount1}")[m
[32m+[m[32mprint(f"{item2}:\t\t${amount2}")[m
[32m+[m[32mprint(f"Total spent:\t${total}")[m
[32m+[m[32mprint(f"Average:\t${average}")[m
[32m+[m[32mprint("-" * 40)[m
[32m+[m[32mprint("Made by: Mark Joshua L. Apor | Installment 2")[m
[32m+[m[32mprint("=" * 40)[m
\ No newline at end of file[m
