import numpy as np

def mod26(matrix):
    return np.mod(matrix, 26)

def text_to_matrix(text, n):
    text = text.replace(" ", "").upper()
    while len(text) % n != 0:  # Ensure text length is multiple of n
        text += 'X'
    return [ord(c) - 65 for c in text]

def matrix_to_text(matrix):
    return ''.join(chr(x + 65) for x in matrix)

def hill_encrypt(text, key_matrix, n):
    text_matrix = text_to_matrix(text, n)
    encrypted_matrix = np.dot(np.array(text_matrix).reshape(-1, n), key_matrix)
    encrypted_matrix = mod26(encrypted_matrix).flatten()
    return matrix_to_text(encrypted_matrix)

def hill_decrypt(text, key_matrix, n):
    inv_key = np.linalg.inv(key_matrix) 
    inv_key = mod26(inv_key).astype(int) 
    text_matrix = text_to_matrix(text, n)
    decrypted_matrix = np.dot(np.array(text_matrix).reshape(-1, n), inv_key)
    decrypted_matrix = mod26(decrypted_matrix).flatten()
    return matrix_to_text(decrypted_matrix)

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]]) 
text = "HELLO"

encrypted_text = hill_encrypt(text, key_matrix, 3)
decrypted_text = hill_decrypt(encrypted_text, key_matrix, 3)

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
