material_costs = [10000, 5000]
labour_cost = 3000
wastage_rate = 0.05
machine_cost = 2000

units_produced = 100
selling_price_per_unit = 250
target_profit = 3000

materials_total = sum(material_costs)
wastage_cost = materials_total * wastage_rate
total_production_cost = materials_total + wastage_cost + labour_cost + machine_cost

total_revenue = units_produced * selling_price_per_unit
profit = total_revenue - total_production_cost

print(f"Material cost: ₹{materials_total:.2f}")
print(f"Wastage cost: ₹{wastage_cost:.2f}")
print(f"Labour cost: ₹{labour_cost:.2f}")
print(f"Machine cost: ₹{machine_cost:.2f}")
print(f"Total production cost: ₹{total_production_cost:.2f}")
print(f"Total revenue: ₹{total_revenue:.2f}")
print(f"Profit: ₹{profit:.2f}")

if profit >= target_profit:
    print("The production meets the profit target.")
else:
    print("The production does not meet the profit target.")
