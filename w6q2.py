def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) + shift - offset) % 26 + offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - offset) % 26 + offset)
        else:
            result += char
    return result

text = input("Enter text to cipher it using caesar cipher technique: ")
shift = int(input("Enter the shift key: "))
encrypted = caesar_cipher(text, shift, 'encrypt')
decrypted = caesar_cipher(encrypted, shift, 'decrypt')

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
