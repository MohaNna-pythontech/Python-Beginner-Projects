print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Choose an option (1 or 2):")
if choice == "1":
    celsius =  float(input("Enter temperature in Celsius:"))
    fahrenheit = (celsius * 9 / 5)+32
    print(f"Temperature in Fahrenheit:{fahrenheit}")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit:"))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature in celsius: {celsius}")
else:
    print("Invalid choice!")