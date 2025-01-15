from collections import Counter

def frequency_analysis(message):
    # Convert the message to lowercase and filter out non-letter characters
    filtered_message = ''.join(filter(str.isalpha, message.lower()))
    
    # Count the frequency of each letter
    letter_counts = Counter(filtered_message)
    
    # Get the six most common letters
    most_common_letters = letter_counts.most_common(6)
    
    return most_common_letters

# Test the function
message = input("Enter the encrypted message: ")
most_common_letters = frequency_analysis(message)
print("The six most common letters are:")
for letter, count in most_common_letters:
    print(f"{letter}: {count}")