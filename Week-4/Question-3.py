"""Modify your "greetings" program so that the first letter of the name entered is
    always in uppercase with the rest in lowercase. This should happen even if the user
    entered their name differently. So if the user entered arthur, ARTHUR, or even
    arTHur the name should be displayed as Arthur."""
    
#Greetings Program form week 3
    
    
name = input("Enter Your Name: ")
if name == "":
    print("Hello Stranger!")
else:
    name = name.capitalize()
    print("Hello", name)
    