# Python Utility Menu

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

def grade_calculator():
    try:
        score = int(input("Enter your score (0-100): "))
        print("Grade", calculate_grade(score))
    except ValueError:
        print("Invalid input. Please enter a number, not text.")

def multiplication_table():
    while True:
        try:
            number = int(input("Enter a number: "))
            for multiplier in range(1, 13):
                print(number, "x", multiplier, "=", number * multiplier)
        except ValueError:
            print("Invalid input. Please enter a number, not text.")
        again = input("Do you want to do another calculation? (yes/no): ")
        if again.lower() != "yes":
            break

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def temperature_converter():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        print(celsius, "°C =", celsius_to_fahrenheit(celsius), "°F")
    except ValueError:
        print("Invalid input. Please enter a number, not text.")

while True:
    print("\n--- Python Utility Menu ---")
    print("1. Grade Calculator")
    print("2. Multiplication Table")
    print("3. Temperature Converter")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        grade_calculator()
    elif choice == "2":
        multiplication_table()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please pick 1-4.")