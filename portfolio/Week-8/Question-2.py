import sys

def diff_command(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            if content1 == content2:
                print("The files are the same.")
            else:
                print("The files are different.")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 2:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        diff_command(file1, file2)
else:
        print("Please provide two file names as command-line arguments.")