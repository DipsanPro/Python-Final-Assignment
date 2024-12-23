"""Modify your program again so that the chosen password cannot be one of a list of
    common passwords, defined thus:
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""
    
# Define a list of common passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

passwd = input('Enter a Password: ')
confirmPasswd = input('Confirm your Password: ')

# Check if any of the password fields are empty
if passwd == "" or confirmPasswd == "":
    print('Password field can\'t be empty, try again!')
# Check if the password length is between 8 and 12 characters
elif 8 <= len(passwd) <= 12:
    # Check if the password is one of the common passwords
    if passwd.lower() in BAD_PASSWORDS:
        print('This password is too common, please choose a different one.')
    elif passwd == confirmPasswd:
        print('Password Set Success!!!!!')
    else:
        print('Error: Passwords do not match. Retry Again.')
else:
    print('Enter a password that is between 8 and 12 characters long.')
