"""Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive."""

num1=int(input('Enter a number: '))

for i in range(13):
    result = num1 * i
    print(num1, '*' ,i ,"=", result)