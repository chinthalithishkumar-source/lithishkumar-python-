def calculate_bill(units):
    slabs = [
        (100, 2.00),   # First 100 units
        (100, 3.00),   # Next 100 units
        (None, 5.00),  # Remaining units
    ]

    remaining = units
    energy_charge = 0

    for slab_units, rate in slabs:
        if remaining <= 0:
            break

        used = remaining if slab_units is None else min(remaining, slab_units)
        energy_charge += used * rate
        remaining -= used

    fixed_charge = 50
    surcharge_rate = 0.05
    rebate = 20

    subtotal = energy_charge + fixed_charge
    total = subtotal + subtotal * surcharge_rate - rebate
    return max(0, total)


monthly_units = {
    "January": 150,
    "February": 180,
    "March": 260,
}

previous_bill = None

for month, units in monthly_units.items():
    bill = calculate_bill(units)
    print(f"{month}: {units} units, bill = ₹{bill:.2f}")

    if previous_bill is not None:
        increase = bill - previous_bill
        print(f"  Change from previous month: ₹{increase:.2f}")
        if increase > 500:
            print("  Unusual increase detected.")

    previous_bill = bill
