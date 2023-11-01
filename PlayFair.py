def prepare_key(key):
    # Remove duplicate letters and spaces from the key
    key = key.replace(" ", "").upper()
    unique_chars = []
    for char in key:
        if char not in unique_chars:
            unique_chars.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars

def find_positions(key_matrix, char):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    key_matrix = []
    key_chars = prepare_key(key)
    for i in range(0, 25, 5):
        key_matrix.append(key_chars[i:i+5])
    
    # Pre-process the plaintext
    plaintext = plaintext.replace(" ", "").upper()
    # Replace 'J' with 'I'
    plaintext = plaintext.replace("J", "I")
    # Split plaintext into digraphs
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            # Check if the last digraph is incomplete (odd length)
            # and if it already contains 'X', skip adding 'X'
            if len(digraphs) > 0 and digraphs[-1][-1] == 'X':
                digraphs.append(plaintext[i] + "")
            else:
                digraphs.append(plaintext[i] + "X")
            i += 1
        else:
            digraphs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    
    # If the last digraph has 'X', remove it
    if len(digraphs) > 0 and len(digraphs[-1]) == 1:
        digraphs[-1] = digraphs[-1] + "X"
    
    # Encrypt the digraphs using the Playfair cipher rules
    ciphertext = ""
    for digraph in digraphs:
        row1, col1 = find_positions(key_matrix, digraph[0])
        row2, col2 = find_positions(key_matrix, digraph[1])
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1
        ciphertext += key_matrix[row1][col1] + key_matrix[row2][col2]
    
    # Remove any trailing 'X' character
    if len(ciphertext) % 2 != 0 and ciphertext[-1] == 'X':
        ciphertext = ciphertext[:-1]
    return ciphertext, key_matrix

def playfair_decrypt(ciphertext, key):
    key_matrix = []
    key_chars = prepare_key(key)
    for i in range(0, 25, 5):
        key_matrix.append(key_chars[i:i+5])
    
    # Decrypt the ciphertext using the Playfair cipher rules
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_positions(key_matrix, char1)
        row2, col2 = find_positions(key_matrix, char2)
        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1
        plaintext += key_matrix[row1][col1] + key_matrix[row2][col2]
    
    # Remove any trailing 'X' character
    if len(plaintext) % 2 != 0 and plaintext[-1] == 'X':
        plaintext = plaintext[:-1]
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    encrypted_message, key_matrix = playfair_encrypt(plaintext, key)
    
    print("\nMatrix representation of the key:")
    for row in key_matrix:
        print(row)
    
    print("\nEncrypted message:", encrypted_message)
    option = input("\nDo you want to decrypt the message? (y/n): ")
    if option.lower() == 'y':
        decrypted_message = playfair_decrypt(encrypted_message, key)
        print("\nDecrypted message:", decrypted_message)
