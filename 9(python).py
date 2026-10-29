expenses = {
    "Hotel": (500, "USD"),
    "Food": (200, "EUR"),
    "Transport": (10000, "INR"),
}

exchange_rates = {
    "USD": 83.00,
    "EUR": 90.00,
    "INR": 1.00,
}

conversion_fee_rate = 0.02
budget_inr = 70000

converted_expenses = {}

for category, (amount, currency) in expenses.items():
    rate = exchange_rates[currency]
    converted_amount = amount * rate
    converted_amount += converted_amount * conversion_fee_rate
    converted_expenses[category] = converted_amount

total_spending = sum(converted_expenses.values())
largest_category = max(converted_expenses, key=converted_expenses.get)

for category, amount in converted_expenses.items():
    print(f"{category}: ₹{amount:.2f}")

print(f"Total spending: ₹{total_spending:.2f}")
print(f"Budget: ₹{budget_inr:.2f}")
print(f"Remaining budget: ₹{budget_inr - total_spending:.2f}")
print("Largest expense category:", largest_category)
print("Within budget:", total_spending <= budget_inr)
