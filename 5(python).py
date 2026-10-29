usage = 700
budget = 600

plans = [
    {"name": "Basic", "monthly_fee": 300, "included_units": 500,
     "excess_rate": 1.00, "validity_days": 30},
    {"name": "Plus", "monthly_fee": 450, "included_units": 1000,
     "excess_rate": 0.50, "validity_days": 30},
    {"name": "Short Plan", "monthly_fee": 200, "included_units": 800,
     "excess_rate": 0.75, "validity_days": 15},
]

eligible_plans = []

for plan in plans:
    if plan["validity_days"] < 30:
        continue

    excess_units = max(0, usage - plan["included_units"])
    total_cost = plan["monthly_fee"] + excess_units * plan["excess_rate"]

    if total_cost <= budget:
        eligible_plans.append((total_cost, plan["name"], excess_units))

if eligible_plans:
    best_plan = min(eligible_plans)
    print("Most economical eligible plan:", best_plan[1])
    print(f"Total cost: ₹{best_plan[0]:.2f}")
    print("Excess units:", best_plan[2])
else:
    print("No plan meets the validity and budget requirements.")
