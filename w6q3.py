class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.create_matrix(key)

    def create_matrix(self, key):
        matrix = []
        seen = set()
        key = key.replace(" ", "").upper()
        for char in key:
            if char not in seen and char != 'J':
                seen.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def preprocess_text(self, text):
        text = text.replace(" ", "").upper()
        result = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                result.append(text[i] + 'X')
                i += 1
            else:
                result.append(text[i:i + 2])
                i += 2
        if len(result[-1]) == 1:
            result[-1] += 'X'
        return result

    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None

    def encrypt(self, plaintext):
        pairs = self.preprocess_text(plaintext)
        ciphertext = []
        for pair in pairs:
            x1, y1 = self.find_position(pair[0])
            x2, y2 = self.find_position(pair[1])
            if x1 == x2:
                y1 = (y1 + 1) % 5
                y2 = (y2 + 1) % 5
            elif y1 == y2:
                x1 = (x1 + 1) % 5
                x2 = (x2 + 1) % 5
            else:
                y1, y2 = y2, y1
            ciphertext.append(self.matrix[x1][y1] + self.matrix[x2][y2])
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
        plaintext = []
        for pair in pairs:
            x1, y1 = self.find_position(pair[0])
            x2, y2 = self.find_position(pair[1])
            if x1 == x2:
                y1 = (y1 - 1) % 5
                y2 = (y2 - 1) % 5
            elif y1 == y2:
                x1 = (x1 - 1) % 5
                x2 = (x2 - 1) % 5
            else:
                y1, y2 = y2, y1
            plaintext.append(self.matrix[x1][y1] + self.matrix[x2][y2])
        return ''.join(plaintext).replace('X', '')

if __name__ == "__main__":
    key = "MONARCHY"
    playfair = PlayfairCipher(key)
    
    plaintext = input("Enter text you want to cipher- ")
    print(f"Original Text: {plaintext}")
    
    encrypted_text = playfair.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = playfair.decrypt(encrypted_text)
    print(f"Decrypted Text: {decrypted_text}")
