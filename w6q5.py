def feistel_round(left, right, key):
    temp = left
    left = right
    right = temp ^ key
    return left, right

def feistel_cipher(block, key, rounds):
    left, right = block
    for _ in range(rounds):
        left, right = feistel_round(left, right, key)
    return left, right

block = (0b110011, 0b101010)  # 64-bit block divided into two 32-bit halves
key = 0b11110000111100001111000011110000  # 32-bit key
rounds = 4
ciphertext = feistel_cipher(block, key, rounds)
print(bin(ciphertext[0]), bin(ciphertext[1]))
