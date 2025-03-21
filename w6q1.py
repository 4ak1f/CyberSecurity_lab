def xor_encrypt_decrypt(plaintext, key):
    result = ''.join(chr(ord(char) ^ key) for char in plaintext)
    return result

plaintext = 'Cyber Security'

keys = [0, 1, 5]

for key in keys:
    # Encrypt the plaintext
    encrypted_text = xor_encrypt_decrypt(plaintext, key)
    print(f"Encrypted (key={key}): {encrypted_text}")

    # Decrypt the ciphertext 
    decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
    print(f"Decrypted (key={key}): {decrypted_text}\n")
