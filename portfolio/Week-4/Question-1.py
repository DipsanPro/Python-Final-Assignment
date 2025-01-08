"""Functions are oen used to validate input. Write a function that accepts a single
    integer as a parameter and returns True if the integer is in the range 0 to 100
    (inclusive), or False otherwise. Write a short program to test the function"""
    
    
def validate():
    num = float(input('Enter a Number: '))
    
    if num <= 100:
        print('Number is in range 0-100')
    else:
        print('Number is larger than 100')

validate()