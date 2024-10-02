import random

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar_cipher(text: str, shift: int):
    result = ""
    for char in text:
        if char in charset:
            new_index = (charset.index(char) + shift) % len(charset)
            result += charset[new_index]
        else:
            result += char  # Keep non-alphanumeric characters unchanged
    return result

def caesar_decipher(text: str, shift: int):
    result = ""
    for char in text:
        if char in charset:
            new_index = (charset.index(char) - shift) % len(charset)
            result += charset[new_index]
        else:
            result += char  # Keep non-alphanumeric characters unchanged
    return result

# Get the secret message from the user
secret_message = str(input(f"\nInput phrase you want ciphered\n\n>> "))
shift_value = random.randint(1, 26)  # Randomly select a shift value from 1 to 26

encrypted_message = caesar_cipher(secret_message, shift_value)

# Attempt to decrypt using all possible shifts
decrypted_messages = {}
for shift in range(1, 63):  # Try all shift values from 1 to 26
    attempt = caesar_decipher(encrypted_message, shift)
    decrypted_messages[shift] = attempt


print("Encrypted:", encrypted_message)
print("\nPossible Decryptions:")
for shift, message in decrypted_messages.items():
    print(f"Shift {shift}: {message}")


correct_decryption = None
for shift, message in decrypted_messages.items():
    if message == secret_message:
        correct_decryption = message
        print(f"\nCorrect decryption found with Shift {shift}: {correct_decryption}")
        break

if not correct_decryption:
    print("\nNo correct decryption found.")