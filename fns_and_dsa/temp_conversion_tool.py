
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0  

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius using the global factor."""
    
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit using the global factor."""
    
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        
        temp_input_str = input("Enter the temperature to convert: ")
        temperature = float(temp_input_str)

        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
       
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()