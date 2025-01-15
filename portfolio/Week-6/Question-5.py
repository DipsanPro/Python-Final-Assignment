import random
import string

def encrypt_message(message):
    interval = random.randint(2, 20)
    encrypted_message = []
    message_index = 0

    while message_index < len(message):
        for _ in range(interval - 1):
            encrypted_message.append(random.choice(string.ascii_lowercase))
        encrypted_message.append(message[message_index])
        message_index += 1

    return ''.join(encrypted_message), interval

# Test the function
message = input("Enter a message to encrypt: ")
encrypted_message, interval = encrypt_message(message)
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")