#program that takes a list of temperatures as command-line arguments and prints the maximum, minimum, and mean temperatures.
import sys

def process_temperatures(temps):
    temps = [float(temp) for temp in temps]
    max_temp = max(temps)
    min_temp = min(temps)
    mean_temp = sum(temps) / len(temps)
    return max_temp, min_temp, mean_temp

if len(sys.argv) > 1:
    temperatures = sys.argv[1:]
    max_temp, min_temp, mean_temp = process_temperatures(temperatures)
    print(f"Maximum Temperature: {max_temp}")
    print(f"Minimum Temperature: {min_temp}")
    print(f"Mean Temperature: {mean_temp}")
else:
    print("Please provide temperature readings as command-line arguments.")