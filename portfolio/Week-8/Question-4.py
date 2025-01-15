import sys

def wc_command(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)
            print(f"Lines: {num_lines}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    wc_command(file_name)
else:
    print("Please provide a file name as a command-line argument.")