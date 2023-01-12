import pytest
import re
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names


def encrypt(plain_text, shift):
    # Initialize a string to store the encrypted text
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Get the ASCII code of the character
            ascii_code = ord(char)
            # Shift the ASCII code
            ascii_code += shift
            # Handle wrapping for upper and lower case letters
            if char.isupper():
                ascii_code -= 26 if ascii_code > ord('Z') else 0
            elif char.islower():
                ascii_code -= 26 if ascii_code > ord('z') else 0
            # Add the shifted character to the encrypted text
            encrypted_text += chr(ascii_code)
        else:
            # Add non-alpha characters to the encrypted text without shifting
            encrypted_text += char
    # print(encrypted_text)
    return encrypted_text

def decrypt(encrypted_text, shift):
    # Initialize a string to store the decrypted text
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Get the ASCII code of the character
            ascii_code = ord(char)
            # Shift the ASCII code
            ascii_code -= shift
            # Handle wrapping for upper and lower case letters
            if char.isupper():
                ascii_code += 26 if ascii_code < ord('A') else 0
            elif char.islower():
                ascii_code += 26 if ascii_code < ord('a') else 0
            # Add the shifted character to the decrypted text
            decrypted_text += chr(ascii_code)
        else:
            # Add non-alpha characters to the decrypted text without shifting
            decrypted_text += char
    # print(decrypted_text)
    return decrypted_text

def crack(encrypted_text):
    for shift in range(1,27):
        decrypted_text = decrypt(encrypted_text, shift)
        if is_english(decrypted_text):
            # print(decrypted_text)
            return decrypted_text
    return "Unable to crack the code.  Perhaps it's not an English word..."

def is_english(text):
    word_list = words.words()
    name_list = names.words()

    if text.lower() in word_list or text in name_list:
      # print(True)
      return True
    else:
      # print(False)
      return False

# is_english("Aimee")
# encrypt("Nick", 15)
# decrypt("Cxrz", 15)
# crack("Cxrz")