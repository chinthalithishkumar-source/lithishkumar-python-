consultation_charge = 500
diagnostic_charge = 1200
treatment_charge = 3000
payment_made = 1000

concession_rate = 0.10
eligible_for_concession = True
maximum_allowed_bill = 100000

gross_bill = consultation_charge + diagnostic_charge + treatment_charge

if eligible_for_concession:
    concession = gross_bill * concession_rate
else:
    concession = 0

final_bill = gross_bill - concession

if final_bill < 0 or final_bill > maximum_allowed_bill or payment_made < 0:
    print("Invalid billing information.")
else:
    balance = max(0, final_bill - payment_made)

    if balance == 0:
        payment_status = "Paid"
    elif payment_made > 0:
        payment_status = "Partially paid"
    else:
        payment_status = "Unpaid"

    print(f"Gross bill: ₹{gross_bill:.2f}")
    print(f"Concession: ₹{concession:.2f}")
    print(f"Final bill: ₹{final_bill:.2f}")
    print(f"Payment made: ₹{payment_made:.2f}")
    print(f"Balance due: ₹{balance:.2f}")
    print("Patient classification:", payment_status)
