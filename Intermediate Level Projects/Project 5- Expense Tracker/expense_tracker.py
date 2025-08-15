import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense(amount, category, description):
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added: {amount} in {category} ({description})")

# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("📭 No expenses found.")
        return
    print("\n===== ALL EXPENSES =====")
    for e in expenses:
        print(f"{e['date']} - {e['category']} - ${e['amount']} - {e['description']}")

# View summary by category
def summary_by_category():
    expenses = load_expenses()
    if not expenses:
        print("📭 No expenses to summarize.")
        return
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n===== EXPENSE SUMMARY =====")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

# Main menu
def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()
                add_expense(amount, category, description)
            except ValueError:
                print("❌ Invalid amount.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
