#a function that accepts a positive integer as a parameter and then returns a representation of that number in binary
def int_to_binary(n):
    if n < 0:
        raise ValueError("The number must be a positive integer.")
    return bin(n)[2:]

try:
    number = int(input("Enter a positive integer: "))
    print(f"Binary representation: {int_to_binary(number)}")
except ValueError as e:
    print(e)