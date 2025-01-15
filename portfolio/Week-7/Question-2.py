def letters_in_at_least_one(word1, word2):
    unique_letters = set(word1) | set(word2)
    return sorted(unique_letters)

def letters_in_both(word1, word2):
    common_letters = set(word1) & set(word2)
    return sorted(common_letters)

def letters_in_either_but_not_both(word1, word2):
    unique_letters = set(word1) ^ set(word2)
    return sorted(unique_letters)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(f"Letters in at least one of the words: {letters_in_at_least_one(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either word, but not in both: {letters_in_either_but_not_both(word1, word2)}")