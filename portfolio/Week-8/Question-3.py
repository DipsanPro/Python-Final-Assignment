import sys

def grep_command(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 2:
    pattern = sys.argv[1]
    file_name = sys.argv[2]
    grep_command(pattern, file_name)
else:
    print("Please provide a pattern and a file name as command-line arguments.")