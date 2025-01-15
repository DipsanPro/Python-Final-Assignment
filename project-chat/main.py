import random
import os
import json
import time

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
with open("./files-chat/names.json", "r") as file:
    names = json.load(file)
    botName = random.choice(names).capitalize()

def saveUserInfo(userName, mobileNumber, selectedCourse):
    try:
        # Ensure directory exists
        os.makedirs('./files-chat', exist_ok=True)
        
        # Save to users file
        with open("./files-chat/users.txt", "a") as file:
            file.write(f"Name: {userName}\n")
            file.write(f"Number: {mobileNumber}\n")
            file.write(f"Course: {selectedCourse}\n")
            file.write("-" * 30 + "\n")
            
        # Create chat log file for user
        chat_filename = f"./files-chat/chat_{userName.lower()}.txt"
        with open(chat_filename, "a") as file:
            file.write(f"Chat log for {userName} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("-" * 50 + "\n")
            
        return True
        
    except Exception as e:
        print(f"Error saving user information: {e}")
        return False

def logChat(userName, message, isBot=False):
    try:
        chat_filename = f"./files-chat/chat_{userName.lower()}.txt"
        with open(chat_filename, "a") as file:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            sender = botName if isBot else userName
            file.write(f"[{timestamp}] {sender}: {message}\n")
    except Exception as e:
        print(f"Error logging chat: {e}")

def saveChat(userName, question, answer):
    try:
        # Ensure directory exists
        os.makedirs('./files-chat', exist_ok=True)
        
        # Save chat to file
        chat_filename = f"./files-chat/chat_{userName.lower()}.txt"
        with open(chat_filename, "a") as file:
            file.write(f"User: {question}\n")
            file.write(f"Bot: {answer}\n\n")
            
    except Exception as e:
        print(f"Error saving chat: {e}")

def welcomeScreen():
    clearScreen()
    global selectedCourse #added this to make it accessable in FAQ section
    global userName
    print(f"Welcome to  University of Poppleton chatbot!, I am {botName}, how can I help you today?")
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
    print(f"\nHello, {userName} select a course you are interested in:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    while True:
        selectedCourse = input("Enter the course you are interested in: ")
        checkExit(selectedCourse)
        if selectedCourse in ["1", "2", "3"]:
            break
        print("Please enter a valid course number!")

    if saveUserInfo(userName, mobileNumber, selectedCourse):
        if selectedCourse == "1":
            selectedCourse = "Computing"
            computing()
        elif selectedCourse == "2":
            selectedCourse = "CyberSecurity"
            cyberSecurity()
        else:
            selectedCourse = "DataScience"
            dataScience()
    else:
        print("Failed to save user information. Please try again.")
        welcomeScreen()

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
        
        # Check keywords and save chat
        words = question.split()
        found = False
        for key in computing_qa:
            if key in words:
                response = computing_qa[key]
                print(f"\n{botName}: {response}")
                saveChat(userName, question, response)
                found = True
                break
        
        if not found:
            response = "Sorry, I can't answer that at this moment. Please call us for more enquiries."
            print(f"\n{botName}: {response}")
            saveChat(userName, question, response)

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
    clearScreen()
    print(f"Welcome to {selectedCourse} FAQs")
    try:
        with open("./files-chat/faq.txt", "r") as file:
            faqs = file.readlines()
            if not faqs:
                print("No FAQs available!")
                return
            
            i = 1
            for line in faqs:
                if line.strip():
                    if line.startswith("Q:"):
                        print(f"\n{i}) {line.strip()[2:]}")
                    elif line.startswith("A:"):
                        print(f">> {line.strip()[2:]}")
                        i += 1
    except FileNotFoundError:
        print("FAQ file not found!")
    
    input("\nPress Enter to continue...")


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
        try:
            with open("./files-chat/users.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No users found.")
    elif adminChoiceU == "2":
        try:
            with open("./files-chat/users.txt", "r") as file:
                lines = file.readlines()
                print("".join(lines))
            
            userToDelete = input("Enter the name of the user you want to delete: ")
            
            i = 0
            while i < len(lines):
                if f"Name: {userToDelete}" in lines[i]:
                    del lines[i:i+4]
                    break
                i += 1
            
            with open("./files-chat/users.txt", "w") as file:
                file.writelines(lines)
            print("User deleted successfully!")
        except FileNotFoundError:
            print("No users found.")
    
    input("Press Enter to go back")
    adminScreen()

def viewFaq():
    clearScreen()
    print("\nFAQ Settings")
    print("1. View FAQs")
    print("2. Add FAQ")
    print("3. Delete FAQ")
    print("4. Edit FAQ")
    print("5. Back")
    print("\nType 'exit' to quit or 'back' to return to admin menu")
    
    choice = input("Enter choice: ").lower()
    
    if choice == 'exit':
        print(f"\nThank you for chatting with {botName}! Goodbye!")
        exit()
    elif choice == 'back':
        adminScreen()
        return
    
    if choice == "1":
        displayFaqs()
    elif choice == "2":
        addFaq()
    elif choice == "3":
        deleteFaq()
    elif choice == "4":
        editFaq()
    else:
        print("Invalid choice!")
        viewFaq()

def displayFaqs():
    try:
        with open("./files-chat/faq.txt", "r") as file:
            faqs = file.readlines()
            if not faqs:
                print("No FAQs available!")
                return
            
            i = 1
            for line in faqs:
                if line.strip():
                    if line.startswith("Q:"):
                        print(f"\n{i}) {line.strip()[2:]}")
                    elif line.startswith("A:"):
                        print(f">> {line.strip()[2:]}")
                        i += 1
        input("\nPress Enter to continue...")
    except FileNotFoundError:
        print("FAQ file not found!")

def addFaq():
    question = input("\nEnter FAQ question (or 'back'/'exit'): ")
    if question.lower() == 'exit':
        print(f"\nThank you for chatting with {botName}! Goodbye!")
        exit()
    elif question.lower() == 'back':
        viewFaq()
        return
        
    answer = input("Enter FAQ answer (or 'back'/'exit'): ")
    if answer.lower() == 'exit':
        print(f"\nThank you for chatting with {botName}! Goodbye!")
        exit()
    elif answer.lower() == 'back':
        viewFaq()
        return
    
    with open("./files-chat/faq.txt", "a") as file:
        file.write(f"\nQ: {question}")
        file.write(f"\nA: {answer}\n")
    
    print("FAQ added successfully!")
    input("\nPress Enter to continue...")
    viewFaq()

def deleteFaq():
    displayFaqs()
    try:
        with open("./files-chat/faq.txt", "r") as file:
            faqs = file.readlines()
        
        faq_number = int(input("\nEnter FAQ number to delete: "))
        index = (faq_number - 1) * 3
        
        if 0 <= index < len(faqs):
            del faqs[index:index + 3]
            
            with open("./files-chat/faq.txt", "w") as file:
                file.writelines(faqs)
            print("FAQ deleted successfully!")
        else:
            print("Invalid FAQ number!")
    except ValueError:
        print("Please enter a valid number!")
    
    input("\nPress Enter to continue...")

def editFaq():
    displayFaqs()
    try:
        with open("./files-chat/faq.txt", "r") as file:
            faqs = file.readlines()
        
        faq_number = input("\nEnter FAQ number to edit (or 'back'/'exit'): ")
        if faq_number.lower() == 'exit':
            print(f"\nThank you for chatting with {botName}! Goodbye!")
            exit()
        elif faq_number.lower() == 'back':
            viewFaq()
            return
            
        index = (int(faq_number) - 1) * 3
        
        if 0 <= index < len(faqs):
            question = input("Enter new question (or 'back'/'exit'): ")
            if question.lower() == 'exit':
                print(f"\nThank you for chatting with {botName}! Goodbye!")
                exit()
            elif question.lower() == 'back':
                viewFaq()
                return
                
            answer = input("Enter new answer (or 'back'/'exit'): ")
            if answer.lower() == 'exit':
                print(f"\nThank you for chatting with {botName}! Goodbye!")
                exit()
            elif answer.lower() == 'back':
                viewFaq()
                return
            
            if question:
                faqs[index] = f"Q: {question}\n"
            if answer:
                faqs[index + 1] = f"A: {answer}\n"
                
            with open("./files-chat/faq.txt", "w") as file:
                file.writelines(faqs)
            print("FAQ edited successfully!")
        else:
            print("Invalid FAQ number!")
    except ValueError:
        print("Please enter a valid number!")
    
    input("\nPress Enter to continue...")
    viewFaq()

def viewChats():
    print("View Chats")

def manageKeywords():
    clearScreen()
    print("\nKeyword Management")
    print("1. View Keywords")
    print("2. Add Keyword")
    print("3. Delete Keyword")
    print("4. Edit Keyword")
    print("5. Back")
    print("\nType 'exit' to quit or 'back' to return to admin menu")
    
    choice = input("Enter choice: ").lower()
    if handleNavigation(choice, adminScreen):
        return
        
    if choice == "1":
        viewKeywords()
    elif choice == "2":
        addKeyword()
    elif choice == "3":
        deleteKeyword()
    elif choice == "4":
        editKeyword()
    else:
        print("Invalid choice!")
    
    input("\nPress Enter to continue...")
    manageKeywords()

def viewKeywords():
    print("\nSelect course:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    
    course = input("Enter choice: ")
    filename = ""
    
    if course == "1":
        filename = "./files-chat/computing_keywords.txt"
    elif course == "2":
        filename = "./files-chat/cybersecurity_keywords.txt"
    elif course == "3":
        filename = "./files-chat/datascience_keywords.txt"
    else:
        print("Invalid choice!")
        return
        
    try:
        with open(filename, "r") as file:
            keywords = json.load(file)
            for key, value in keywords.items():
                print(f"\nKeyword: {key}")
                print(f"Response: {value}")
    except FileNotFoundError:
        print("No keywords found!")

def addKeyword():
    print("\nSelect course:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    
    course = input("Enter choice: ")
    filename = ""
    
    if course == "1":
        filename = "./files-chat/computing_keywords.txt"
    elif course == "2":
        filename = "./files-chat/cybersecurity_keywords.txt"
    elif course == "3":
        filename = "./files-chat/datascience_keywords.txt"
    else:
        print("Invalid choice!")
        return
        
    keyword = input("\nEnter keyword: ").lower()
    response = input("Enter response: ")
    
    try:
        keywords = {}
        try:
            with open(filename, "r") as file:
                keywords = json.load(file)
        except FileNotFoundError:
            pass
            
        keywords[keyword] = response
        
        with open(filename, "w") as file:
            json.dump(keywords, file, indent=4)
            
        print("Keyword added successfully!")
    except Exception as e:
        print(f"Error adding keyword: {e}")

def deleteKeyword():
    print("\nSelect course:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    
    course = input("Enter choice: ")
    filename = ""
    
    if course == "1":
        filename = "./files-chat/computing_keywords.txt"
    elif course == "2":
        filename = "./files-chat/cybersecurity_keywords.txt"
    elif course == "3":
        filename = "./files-chat/datascience_keywords.txt"
    else:
        print("Invalid choice!")
        return
        
    try:
        with open(filename, "r") as file:
            keywords = json.load(file)
            
        print("\nCurrent keywords:")
        for key in keywords.keys():
            print(key)
            
        keyword = input("\nEnter keyword to delete: ").lower()
        
        if keyword in keywords:
            del keywords[keyword]
            with open(filename, "w") as file:
                json.dump(keywords, file, indent=4)
            print("Keyword deleted successfully!")
        else:
            print("Keyword not found!")
    except FileNotFoundError:
        print("No keywords found!")

def editKeyword():
    print("\nSelect course:")
    print("1. Computing")
    print("2. Cyber Security")
    print("3. Data Science")
    
    course = input("Enter choice: ")
    filename = ""
    
    if course == "1":
        filename = "./files-chat/computing_keywords.txt"
    elif course == "2":
        filename = "./files-chat/cybersecurity_keywords.txt"
    elif course == "3":
        filename = "./files-chat/datascience_keywords.txt"
    else:
        print("Invalid choice!")
        return
        
    try:
        with open(filename, "r") as file:
            keywords = json.load(file)
            
        print("\nCurrent keywords:")
        for key in keywords.keys():
            print(key)
            
        keyword = input("\nEnter keyword to edit: ").lower()
        
        if keyword in keywords:
            new_response = input("Enter new response: ")
            keywords[keyword] = new_response
            
            with open(filename, "w") as file:
                json.dump(keywords, file, indent=4)
            print("Keyword edited successfully!")
        else:
            print("Keyword not found!")
    except FileNotFoundError:
        print("No keywords found!")

def handleNavigation(userInput, returnFunction=None):
    """
    Handles navigation options (exit/back) consistently across the application
    Args:
        userInput: User's input to check
        returnFunction: Function to call when 'back' is entered
    Returns:
        bool: True if navigation handled, False otherwise
    """
    if userInput.lower() == 'exit':
        print(f"\nThank you for chatting with {botName}! Goodbye!")
        exit()
    elif userInput.lower() == 'back' and returnFunction:
        returnFunction()
        return True
    return False

welcomeScreen()