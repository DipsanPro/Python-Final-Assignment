import random
import os

def clearScreen():
    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Linux/Mac
        _ = os.system('clear')

def checkExit(userInput):
    if userInput.lower() in ['exit', 'e']:
        print(f"\nThank you for chatting with {botName}! Goodbye!")
        exit()
    if userInput == "back":
        welcomeScreen()
# Open the file and read the names
with open("names.txt", "r") as file:
    botName = (random.choice([line.strip() for line in file if line.strip()]))

def welcomeScreen():
    clearScreen()
    global selectedCourse #added this to make it accessable in FAQ section
    global userName
    print("Welcome to TBC chatbot!, I am", botName, "how can i help you today?")
    print("Type Exit or E to end chat")
    # Get user name and mobile number details

    userName = input("Enter your name: ")
    if userName.lower() == "admin":
        adminName = input("Enter Username: ")
        adminPassword = input("Enter Password: ")
        if adminName == "admin" and adminPassword == "admin":
            adminScreen()
            return
        else:
            print("Invalid Username or Password")

            welcomeScreen()
            return
    while True:
        checkExit(userName)
        if userName:
            break
        print("Name cannot be empty!")

    while True:
        mobileNumber = input("Enter your mobile number: ")
        checkExit(mobileNumber)
        if mobileNumber.isdigit() and len(mobileNumber) == 10:
            break
        print("Please enter a valid number with at least 10 digits!")
        if ValueError:
            print("Please enter numbers only!")
    
    # Course Selection
    print("\nHello, " +userName+ " select a course you are intrested in:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    while True:
        selectedCourse = input("Enter the course you are intrested in: ")
        checkExit(selectedCourse)
        if selectedCourse in ["1", "2", "3"]:
            break
        print("Please enter a valid course number!")

    if selectedCourse == "1":
        selectedCourse = "Computing"
        computing()
    elif selectedCourse == "2":
        selectedCourse = "CyberSecurity"
        cyberSecurity()
    else:
        selectedCourse = "DataScience"
        dataScience()
    # Save user details to a file
    with open("user.txt", "a") as file:
        file.write(f"Name: {userName}\n")
        file.write(f"Number: {mobileNumber}\n")
        file.write(f"Course: {selectedCourse}\n")
        file.write("-" * 30 + "\n")

#Computing
def computing():
    clearScreen()
    global computing_qa
    computing_qa = {
        "coffee": "The coffee shop opens at 7am.",
        "subject": "We teach various programming and data science related subjects in this course.",
        "time": "College hour starts form morning 6 AM"
    }

    print("Welcome to Computing")
    print("Press 1 to view FAQs or type 'back' to restart chat")
    while True:
        question = input(f"\n{userName}: ").lower()
        checkExit(question)
        
        if question == "back":
            computing()
            break
        
        if question == "1":
            faq()
            break
        
        # Split input into words and check for keywords
        words = question.split()
        found = False
        for key in computing_qa:
            if key in words:
                print(f"\n{botName}: {computing_qa[key]}")
                found = True
                break
        
        if not found:
            print(f"\n{botName}: Sorry, I can't answer that at this moment. Please call us for more enquiries.")

#Cyber Security
def cyberSecurity():
    print("Welcome to Cyber Security")
    choice2 = input("Press 1 to view FAQs or enter question to chat with " + botName + " : ")    
    if choice2 == "1":
        faq()
    if choice2 == "back":
        cyberSecurity()

#Data Science
def dataScience():
    print("Welcome to Data Science")
    choice3 = input("Press 1 to view FAQs or enter question to chat with " + botName + " : ")    
    if choice3 == "1":
        faq()

#Functon to display Faq
def faq():
    print("Welcome to FAQs")
    print("Here you can find the frequently asked questions for " + selectedCourse)
    with open("faq.txt", "r") as file:
        print(file.read())


def adminScreen():  
    print("Welcome Admin")
    print("1. View Users Setting")
    print("2. View Faq Settings")
    print("3. Manage Keywords")
    print("4. Exit")
    adminChoice = input("Enter your choice: ")
    if adminChoice == "1":
        viewUsers()
    elif adminChoice == "2":
        viewFaq()
    elif adminChoice == "3":
        manageKeywords()
    else:
        exit()

def viewUsers():
    print("1. View Users")
    print("2. Delete User")
    print("3. Exit")
    adminChoiceU = input("Enter your choice: ")
    if adminChoiceU == "1":
        with open("user.txt", "r") as file:
            print(file.read())
    elif adminChoiceU == "2":
        with open("user.txt", "r") as file:
            lines = file.readlines()
            print("".join(lines))
        
        userToDelete = input("Enter the name of the user you want to delete: ")
        
        # Find and delete user block (4 lines - name, number, course, separator)
        i = 0
        while i < len(lines):
            if f"Name: {userToDelete}" in lines[i]:
                del lines[i:i+4]  # Delete 4 lines (name, number, course, separator)
                break
            i += 1
        
        # Write remaining lines back
        with open("user.txt", "w") as file:
            file.writelines(lines)
        print("User and related information deleted!")
    
    input("Press Enter to go back")
    adminScreen()

def viewFaq():
   pass

def viewChats():
    print("View Chats")

def manageKeywords():
    clearScreen()
    global computing_qa
    while True:
        print("\nKeyword Management")
        print("1. View Keywords")
        print("2. Add Keyword")
        print("3. Delete Keyword")
        print("4. Back")
        
        choice = input("Enter choice: ")
        if choice == "1":
            print("\nCurrent Keywords and Answers:")
            for key, value in computing_qa.items():
                print(f"\nKeyword: {key}")
                print(f"Answer: {value}")
        elif choice == "2":
            keyword = input("Enter new keyword: ").lower()
            answer = input("Enter answer for this keyword: ")
            computing_qa[keyword] = answer
            print("Keyword added successfully!")
        elif choice == "3":
            keyword = input("Enter keyword to delete: ").lower()
            if keyword in computing_qa:
                del computing_qa[keyword]
                print("Keyword deleted successfully!")
            else:
                print("Keyword not found!")
        elif choice == "4":
            break
        input("\nPress Enter to continue...")

welcomeScreen()