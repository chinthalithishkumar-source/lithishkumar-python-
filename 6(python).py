distance_km = 300
fare_per_km = 2.00
reservation_fee = 40
cancellation_penalty_rate = 0.50

passengers = [
    {"name": "Meena", "age": 65, "cancelled": False},
    {"name": "Arun", "age": 30, "cancelled": True},
]

def age_concession(age):
    if age >= 60:
        return 0.40
    return 0.00

for passenger in passengers:
    concession = age_concession(passenger["age"])
    base_fare = distance_km * fare_per_km
    fare_after_concession = base_fare * (1 - concession)
    total_fare = fare_after_concession + reservation_fee

    if passenger["cancelled"]:
        cancellation_charge = total_fare * cancellation_penalty_rate
        refund = total_fare - cancellation_charge
        print(f"{passenger['name']}: Cancelled; refund = ₹{refund:.2f}")
    else:
        print(f"{passenger['name']}: Fare = ₹{total_fare:.2f}")
