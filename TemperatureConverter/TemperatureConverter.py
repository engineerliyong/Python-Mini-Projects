def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Get temperature with error handling
try:
    print("Enter temperature to convert: ")
    temp = float(input())
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Get units with validation
print("Enter units (C for Celsius, F for Fahrenheit): ")
units = input().strip().upper()

if units == 'C':
    if temp < -273.15:
        print("Error: Temperature below absolute zero in Celsius.")
    else:  
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.1f}°F")

elif units == 'F':
    if temp < -459.67:
        print("Error: Temperature below absolute zero in Fahrenheit.")
    else:  
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted:.1f}°C")

else:  
    print("Error: Please enter 'C' or 'F'.")