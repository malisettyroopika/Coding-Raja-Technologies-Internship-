expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount ($): "))
    print("Select a category:")
    print("1. Food\n2. Home\n3. Work\n4. Fun\n5. Misc")
    category_number = int(input("Enter a category number: "))
    categories = ["Food", "Home", "Work", "Fun", "Misc"]
    category = categories[category_number - 1]
    expenses.append({"name": name, "amount": amount, "category": category})
    print(f"You've added {name} (${amount:.2f}) to your expenses.")

def calculate_total_expenses():
    total_expenses = sum(expense["amount"] for expense in expenses)
    return total_expenses

def expenses_by_category():
    categories = set(expense["category"] for expense in expenses)
    category_totals = {category: sum(expense["amount"] for expense in expenses if expense["category"] == category)
                       for category in categories}
    return category_totals
def calculate_budget(income):
    total_expenses = calculate_total_expenses()
    remaining_budget = income - total_expenses
    return remaining_budget

def daily_budget(remaining_budget, days_in_month):
    daily_limit = remaining_budget / days_in_month
    return daily_limit

# Example Usage:
print("Welcome to the expense tracker!")

# Add expenses
add_expense()
add_expense()

# Display expense summary
total_expenses = calculate_total_expenses()
print(f"You have {len(expenses)} expenses totaling ${total_expenses:.2f}.")

# Display expenses by category
category_totals = expenses_by_category()
print("Expenses by category:")
for category, amount in category_totals.items():
    print(f"{category}: ${amount:.2f}")
# Budget calculation
income = float(input("Enter your monthly income ($): "))
remaining_budget = calculate_budget(income)
print(f"Budget:")
print(f"You have ${remaining_budget:.2f} left to spend this month.")
days_in_month = int(input("Enter the number of days in the month: "))
daily_limit = daily_budget(remaining_budget, days_in_month)
print(f"That's roughly ${daily_limit:.2f} per day.")