items = [
    {"name": "Notebook", "category": "stationery", "price": 50, "quantity": 4},
    {"name": "Bag", "category": "accessory", "price": 800, "quantity": 1},
]

category_tax_rates = {
    "stationery": 0.05,
    "accessory": 0.12,
}

discount_threshold = 500
discount_rate = 0.10
maximum_discount = 100

subtotal = 0
total_tax = 0

print("------------- INVOICE -------------")

for item in items:
    amount = item["price"] * item["quantity"]
    tax_rate = category_tax_rates.get(item["category"], 0)
    tax = amount * tax_rate

    subtotal += amount
    total_tax += tax

    print(
        f"{item['name']}: {item['quantity']} x ₹{item['price']:.2f}"
        f" = ₹{amount:.2f}, tax = ₹{tax:.2f}"
    )

if subtotal >= discount_threshold:
    discount = min(subtotal * discount_rate, maximum_discount)
else:
    discount = 0

final_total = subtotal + total_tax - discount

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax: ₹{total_tax:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Amount due: ₹{final_total:.2f}")
