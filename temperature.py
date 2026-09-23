# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

try:
    celsius = float(input("Enter temperature in Celsius: "))
    print(celsius, "°C =", celsius_to_fahrenheit(celsius), "°F")
except ValueError:
    print("Invalid input. Please enter a number, not text.")