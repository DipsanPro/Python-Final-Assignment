#program that decrypts messages encoded as above
def decrypt_message(encrypted_message, interval):
    decrypted_message = ''.join(
        encrypted_message[i] for i in range(interval - 1, len(encrypted_message), interval)
    )
    return decrypted_message

encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used for encryption: "))
decrypted_message = decrypt_message(encrypted_message, interval)
print(f"Decrypted message: {decrypted_message}")
