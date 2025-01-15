#function that takes a string as a parameter and returns a sorted list
def unique_sorted_letters(s):
    unique_letters = set(s)
    sorted_letters = sorted(unique_letters)
    return sorted_letters

test_string = input("Enter a string: ")
result = unique_sorted_letters(test_string)
print(f"Sorted list of unique letters: {result}")