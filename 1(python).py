applicants = [
    {"name": "Asha", "aggregate": 88, "subjects": [80, 75, 91],
     "attendance": 92, "income": 180000},
    {"name": "Ravi", "aggregate": 84, "subjects": [79, 82, 76],
     "attendance": 95, "income": 150000},
]

seats = 1
min_aggregate = 75
min_subject_score = 70
min_attendance = 80
max_income = 300000

eligible = []

for student in applicants:
    if (
        student["aggregate"] >= min_aggregate
        and min(student["subjects"]) >= min_subject_score
        and student["attendance"] >= min_attendance
        and student["income"] <= max_income
    ):
        eligible.append(student)

# Tie-breakers: aggregate, lowest subject score, then attendance
eligible.sort(
    key=lambda s: (s["aggregate"], min(s["subjects"]), s["attendance"]),
    reverse=True
)

print("Scholarship recipients:")
for student in eligible[:seats]:
    print(student["name"], "Aggregate:", student["aggregate"])
