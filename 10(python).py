venue_cost = 20000
equipment_cost = 5000

catering_per_person = 300
transport_per_person = 100
certificate_per_person = 50

sponsorship = 10000
contribution_per_person = 500
registered_participants = 80

fixed_costs = venue_cost + equipment_cost
variable_cost_per_person = (
    catering_per_person + transport_per_person + certificate_per_person
)

total_cost = fixed_costs + variable_cost_per_person * registered_participants
participant_contributions = contribution_per_person * registered_participants
funds_available = sponsorship + participant_contributions
shortfall = max(0, total_cost - funds_available)

# Find the minimum registrations needed to cover costs.
net_contribution_per_person = contribution_per_person - variable_cost_per_person

if fixed_costs <= sponsorship:
    break_even_count = 0
elif net_contribution_per_person <= 0:
    break_even_count = None
else:
    amount_to_cover = fixed_costs - sponsorship
    break_even_count = (
        amount_to_cover + net_contribution_per_person - 1
    ) // net_contribution_per_person

print(f"Total event cost: ₹{total_cost:.2f}")
print(f"Participant contributions: ₹{participant_contributions:.2f}")
print(f"Sponsorship: ₹{sponsorship:.2f}")
print(f"Funding shortfall: ₹{shortfall:.2f}")

if break_even_count is None:
    print("Break-even is not possible with the current contribution amount.")
else:
    print("Minimum registrations to break even:", break_even_count)
