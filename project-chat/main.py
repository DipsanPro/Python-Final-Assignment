import random
import os

# Open the file and read the names
with open("names.txt", "r") as file:
    botName = (random.choice([line.strip() for line in file if line.strip()]))

# Welcome screen
def welcomeScreen():
    print("Welcome to TBC chatbot!, I am", botName, "how can i help you today?")
    name = input("What is your name?: ")
    phone = input("What is your phone number?: ")
    if len(phone) != 10 and int(phone) == int:
        welcomeScreen()
    
    

welcomeScreen()
