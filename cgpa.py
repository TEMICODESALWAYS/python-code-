def calculate_cgpa():
    total_weighted_points = 0
    total_credits = 0

    for i in range(1, 7):
        print(f"Course {i}:")
        grade_point = float(input("Enter grade point (0.0 - 4.0): "))
        credit_hours = int(input("Enter credit hours: "))

        weighted_points = grade_point * credit_hours
        total_weighted_points += weighted_points
        total_credits += credit_hours

    if total_credits == 0:
        print("Total credits cannot be zero.")
        return

    cgpa = total_weighted_points / total_credits
    print(f"\nYour CGPA is: {cgpa:.2f}")


calculate_cgpa()
