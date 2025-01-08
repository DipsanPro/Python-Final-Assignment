"""Write a function that has a single string as its parameter, and returns the number of
    uppercase letters, and the number of lowercase letters in the string. Test the
    function with a short program."""
    
    
def checkLetter():
    word = input('Enter a word: ')
    length = len(word)
    uppercaseLetter = 0 
    lowercaseLetter = 0 
    for char in word:
        if char.isupper():
            uppercaseLetter += 1
        else:
            lowercaseLetter += 1
    print("Total length", length, ", total uppercase letter are ",uppercaseLetter,"and total lowercase letter are", lowercaseLetter)
    
checkLetter()