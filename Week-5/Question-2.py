"""Write a program that, when run from the command line, reports how many
    arguments were provided. (Remember that the program name itself is not an
    argument)."""
    
    
import sys

# The arguments passed to the script (excluding the script name)
arguments = sys.argv[1:]

# Count the number of arguments
num_arguments = len(arguments)

# Print the result
print(f"Number of arguments provided: {num_arguments}")


#Example Command
#python Question-2.py.py arg1 arg2 arg3