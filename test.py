# Multiplication Table

def multiplication_table():
    try:
        number = int(input("Enter a number: "))
        for multiplier in range(1, 13):
            result = number * multiplier
            print(number, "x", multiplier, "=", result)
    except ValueError:
        print("Invalid input. Please enter a number, not text.")

while True:
    multiplication_table()
    again = input("Do you want to do another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break