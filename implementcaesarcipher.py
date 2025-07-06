def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                offset = (ord(char) - start + shift) % 26
            elif mode == 'decrypt':
                offset = (ord(char) - start - shift) % 26
            result += chr(start + offset)
        else:
            result += char
    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt
encrypted = caesar_cipher(message, shift, mode='encrypt')
print("Encrypted message:", encrypted)

# Decrypt
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')
print("Decrypted message:", decrypted)
