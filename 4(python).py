basic_pay = 30000
allowances = 5000
overtime_hours = 4
overtime_rate = 250
incentive = 2000

overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_pay + allowances + overtime_pay + incentive

# Progressive deductions
deduction = 0
remaining_salary = gross_salary

slabs = [
    (20000, 0.05),
    (20000, 0.10),
    (None, 0.15),
]

for slab_amount, rate in slabs:
    if remaining_salary <= 0:
        break

    taxable_amount = (
        remaining_salary if slab_amount is None
        else min(remaining_salary, slab_amount)
    )
    deduction += taxable_amount * rate
    remaining_salary -= taxable_amount

net_salary = gross_salary - deduction

print("--------- SALARY STATEMENT ---------")
print(f"Basic pay:       ₹{basic_pay:.2f}")
print(f"Allowances:      ₹{allowances:.2f}")
print(f"Overtime pay:    ₹{overtime_pay:.2f}")
print(f"Incentive:       ₹{incentive:.2f}")
print(f"Gross salary:    ₹{gross_salary:.2f}")
print(f"Deductions:      ₹{deduction:.2f}")
print(f"Net salary:      ₹{net_salary:.2f}")
