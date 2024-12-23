"""Write and test a function that converts a temperature measured in degrees
    centigrade into the equivalent in fahrenheit, and another that does the reverse
    conversion. Test both functions."""


def celciusToFahrenheit():
    number = float(input('Enter Temp : '))
    fahrenheit = (number * 9/5) + 32
    print(fahrenheit)
    
    
def fahrenheitToCelcius():
    number = float(input('Enter Temp : '))
    celcius = (number - 32) * 5/9
    print(celcius)
    
    
print("Press 1 to Convert Celcius to Fahrenheit \n")
print("Press 2 to Convert Fahrenheit to Celcius \n")
choice = input("Enter your choice: ")

if choice == '1':
    celciusToFahrenheit()
else:
    fahrenheitToCelcius()

