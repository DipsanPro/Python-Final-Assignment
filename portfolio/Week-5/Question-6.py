import sys
import shutil

def create_backup(file_name):
    backup_name = file_name + ".bak"
    shutil.copy(file_name, backup_name)
    print(f"Backup created: {backup_name}")

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    create_backup(file_name)
else:
    print("Please provide the name of the file as a command-line argument.")