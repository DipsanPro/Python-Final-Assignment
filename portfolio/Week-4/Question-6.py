"""Write a program that takes a centigrade temperature and displays the equivalent in
    fahrenheit. The input should be a number followed by a letter C. The output should
    be in the same format."""
    
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
input_temp = input("Enter temperature in Celsius (e.g., 25C): ")

if input_temp[-1].upper() == 'C':
    celsius = float(input_temp[:-1]) 
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print (fahrenheit)
else:
    print("Invalid input. Please enter a temperature followed by 'C'.")
