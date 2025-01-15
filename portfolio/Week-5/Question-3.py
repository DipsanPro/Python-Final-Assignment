#this programme takes command line arguments and prints the shortest argument
import sys

arguments = sys.argv[1:]  # Exclude the script name
if arguments:
    print(f"The shortest argument is: {min(arguments, key=len)}")
else:
    print("No arguments were provided.")