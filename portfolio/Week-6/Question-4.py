def encrypt_message(message):
    no_spaces = message.replace(" ", "")
    encrypted = no_spaces[::-1]
    return encrypted

message = input("Enter a message to encrypt: ")
encrypted_message = encrypt_message(message)
print(f"Encrypted message: {encrypted_message}")