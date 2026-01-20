# Expense Tracker using Dictionary
expenses = {}
while True:
    print("\nExpence Tracker")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print("Expense added successfully!")

    elif choice == '2':
        print("\nExpenses: ")
        for category, amount in expenses.items():
            print(category, ":", amount)

    elif choice == '3':
        total = sum(expenses.values())
        print("Total Expense: ", total)

    elif choice == '4':
        print("Exiting Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")

