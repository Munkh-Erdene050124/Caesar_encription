Caesar Cipher Implementation in Python
A clean and efficient Python implementation of the Caesar Cipher, featuring both encryption and decryption functions. This project demonstrates basic cryptography principles using string manipulation and modular arithmetic.

How it Works
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet.
The Mathematical Formula
implementation utilizes the following logic for each character 
Encryption: E_n(x) = (x + n) \mod 26
Decryption: D_n(x) = (x - n) \mod 26
By using the modulo operator (%), the code ensures that if a shift goes past 'Z', it wraps back around to the beginning of the alphabet.

Implementation Details
The code is structured into two primary functions:

caesar_encryption(text, shift):
Converts all input text to uppercase.
Iterates through each character.
Shifts alphabetic characters while leaving spaces and punctuation (like !, ,, .) untouched.

caesar_decryption(text, shift):
Reverses the encryption process by applying a negative shift.

brute_force_decryption(encrypted_text):
Finds all the possible matches using brute force

Usage
To use this script, ensure you have Python 3.x installed.

Clone the repository: git clone https://github.com/Munkh-Erdene050124/Caesar_encription.git

Run the script: python caesar_cipher.py

Security Disclaimer
The Caesar Cipher is an ancient encryption method and is not secure for modern data protection. It is vulnerable to:
Brute Force: Only 25 possible keys exist.
Frequency Analysis: Common letters in the English language (like 'E' or 'T') easily reveal the shift pattern.
This project is for educational purposes only.