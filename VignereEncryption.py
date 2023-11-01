def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the encryption key: ")
    encrypted_text = vigenere_encrypt(plain_text, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
