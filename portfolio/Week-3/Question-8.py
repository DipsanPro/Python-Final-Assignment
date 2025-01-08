"""Modify the "Times Table" again so that the user still enters the number of the table,
    but if this number is negative the table is printed backwards. So entering "-7"
    would produce the Seven Times Table starting at "12 times" down to "0 times"."""
    
num1=int(input('Enter a number: '))
if num1<0:
    i=12
    for i in range(12, -1, -1):
        result = num1 * i
        print(num1, '*' ,i ,"=", result)
else:
    for i in range(13):
        result = num1 * i
        print(num1, '*' ,i ,"=", result)