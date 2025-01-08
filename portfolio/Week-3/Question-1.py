"""Question-1.Modify your greeting program so that if the user does not enter a name (i.e. they
            just press enter), the program responds "Hello, Stranger!". Otherwise it should print
            a greeting with their name as before"""
            
name = input("Enter Your Name: ")
if name == "":
    print("Hello Stranger!")
else:
    print("Hello", name)
    