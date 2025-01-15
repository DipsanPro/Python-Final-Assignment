import sys

def nl_command(file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:>6}\t{line}", end='')
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    nl_command(file_name)
else:
    print("Please provide the name of the file as a command-line argument.")