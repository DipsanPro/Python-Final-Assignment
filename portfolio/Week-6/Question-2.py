#function that takes an integer as its parameter and returns the factors of that integer
def find_factors(n):
    if n <= 0:
        raise ValueError("The number must be a positive integer.")
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

try:
    number = int(input("Enter a positive integer: "))
    print(f"Factors of {number}: {find_factors(number)}")
except ValueError as e:
    print(e)