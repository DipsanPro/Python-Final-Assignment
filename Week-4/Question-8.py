
"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""



temp = []

while True:
    input_temp = input("Enter temperature in Celsius (e.g., 25C), or press Enter to finish: ")
    
    # If the input is an empty string, terminate the loop
    if input_temp == "":
        break
    
    # Check if the input ends with 'C'
    if input_temp[-1].upper() == 'C':
        temp.append(input_temp)
    else:
        print("Temperature must end with 'C'. Please try again.")

# Convert the temperatures to numeric values
numeric_temps = [float(t[:-1]) for t in temp]  # Removes 'C' and converts to float

# Calculate and print the max, min, and mean temperatures
if numeric_temps:  # Check if the list is not empty
    print("The maximum temperature is", max(numeric_temps), "°C")
    print("The minimum temperature is", min(numeric_temps), "°C")
    print("The mean temperature is", sum(numeric_temps) / len(numeric_temps), "°C")
else:
    print("No valid temperatures were entered.")
