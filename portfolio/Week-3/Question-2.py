"""Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error."""

passwd = input('Enter a Passowrd: ')#Asking password for the first time
conformPasswd = input('Conform your Passowrd: ')#Conforming passwod
if passwd  == "" or conformPasswd  == "" :#Condition to verify if there is some text in the password or not
    print('Password Field cant be empty, try again!')
else:
    if passwd == conformPasswd:
        print('Password Set Success!!!!!')
    else:
        print('Error Retry Again.')