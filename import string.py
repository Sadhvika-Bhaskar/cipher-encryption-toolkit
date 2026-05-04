import string

# ---------- Caesar Cipher ----------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------- Monoalphabetic Cipher ----------
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
reverse_key = {key[i]: chr(65+i) for i in range(26)}

def mono_encrypt(text):
    result = ""
    for char in text.upper():
        if char in string.ascii_uppercase:
            result += key[ord(char)-65]
        else:
            result += char
    return result

def mono_decrypt(text):
    result = ""
    for char in text:
        if char in reverse_key:
            result += reverse_key[char]
        else:
            result += char
    return result

# ---------- Vigenere Cipher ----------
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 65
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            j += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)]) - 65
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            j += 1
        else:
            result += char
    return result

# ---------- Main Menu ----------
def main():
    while True:
        print("\n--- Cipher Toolkit ---")
        print("1. Caesar Cipher")
        print("2. Monoalphabetic Cipher")
        print("3. Vigenere Cipher")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            text = input("Enter text: ")
            shift = int(input("Enter shift: "))
            print("Encrypted:", caesar_encrypt(text, shift))
            print("Decrypted:", caesar_decrypt(caesar_encrypt(text, shift), shift))

        elif choice == '2':
            text = input("Enter text: ")
            enc = mono_encrypt(text)
            print("Encrypted:", enc)
            print("Decrypted:", mono_decrypt(enc))

        elif choice == '3':
            text = input("Enter text: ")
            key = input("Enter key: ")
            enc = vigenere_encrypt(text, key)
            print("Encrypted:", enc)
            print("Decrypted:", vigenere_decrypt(enc, key))

        elif choice == '4':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()