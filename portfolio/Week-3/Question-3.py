"""Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""


#Previous program From Question-2.py

passwd = input('Enter a Password: ')
conformPasswd = input('Confirm your Password: ')

if passwd == "" or conformPasswd == "":
    print('Password field can\'t be empty, try again!')
    
# To check the length of the password

elif 8 <= len(passwd) <= 12:
    if passwd == conformPasswd:
        print('Password Set Success!!!!!')
    else:
        print('Error: Passwords do not match. Retry Again.')
else:
    print('Enter a password that is between 8 and 12 characters long.')
