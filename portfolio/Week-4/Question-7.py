"""Write a program that reads 6 temperatures (in the same format as before), and
    displays the maximum, minimum, and mean of the values."""
    
    
    
temp = []
choice = 6  # Number of valid inputs to collect
valid_inputs = 0  # Counter for valid inputs

while valid_inputs < choice:
    input_temp = input("Enter temperature in Celsius (e.g., 25C): ")
    
    if input_temp[-1].upper() == 'C':  # Check if input ends with 'C'
        temp.append(input_temp)
        valid_inputs += 1  # Increment the counter for valid inputs
    else:
        print("Temperature must end with 'C'. Please try again.")
        
numeric_temps = [float(t[:-1]) for t in temp]  #removes the C
print ("The maximum Temperature is ",max(numeric_temps) )
print ("The minimum Temperature is ",min(numeric_temps) )
print ("The mean Temperature is ",sum(numeric_temps) / len(numeric_temps) )
