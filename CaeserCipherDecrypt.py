def decrypt(ciphertext, s):
    decrypt_chars = []

    for char in ciphertext:

        if char.isupper():
            decrypt_chars += chr(((ord(char) - 65 - s) % 26) + 65)
        else:
            decrypt_chars += chr(((ord(char) - 97 - s) % 26) + 97)
    return "".join(decrypt_chars)


ciphertext1 = input("Enter the cipher text ")
s = int(input("enter the key for the shift "))
print("Cipher Text : " + ciphertext1)
print("Shift " + str(s))
print("decrypt text " + decrypt(ciphertext1, s))
