# Grade Calculator

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

score = int(input("Enter your score (0-100): "))
print("Grade", calculate_grade(score))