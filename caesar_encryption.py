def caesar_encryption(text, shift):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Turn texts to uppercase and loop through each character
    for char in text.upper():
        if char in alphabet:
            #Find the index of the character
            char_index = alphabet.find(char)
            #Calculate new index with the shift and wrap around using modulo
            new_index = (char_index + shift) % 26
            #Append the encrypted character to the result
            result += alphabet[new_index]
        else:
            #If it's not an alphabetic character, keep it unchanged
            result += char
    #result is the encrypted text
    return result

def caesar_decryption(text, shift):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Turn texts to uppercase and loop through each character
    for char in text.upper():
        if char in alphabet:
            #Find the index of the character
            char_index = alphabet.find(char)
            #Calculate new index with the negative shift and wrap around using modulo
            new_index = (char_index - shift) % 26
            #Append the decrypted character to the result
            result += alphabet[new_index]
        else:
            #If it's not an alphabetic character, keep it unchanged
            result += char
    #result is the decrypted text
    return result

def brute_force_decryption(encrypted_text):
    print("\nBrute Force Decryption Attempts:\n")
    # This function will try all possible shifts (1-25) to decrypt the text
    for shift in range(1, 26):
        decrypted_text = caesar_decryption(encrypted_text, shift)
        print(f"Shift: {shift}, Decrypted Text: {decrypted_text}")
        


# Example usage
if __name__ == "__main__":
    original_text = "Hello, World!"
    shift_value = 3
    encrypted_text = caesar_encryption(original_text, shift_value)
    decrypted_text = caesar_decryption(encrypted_text, shift_value)
    brute_force_answer = brute_force_decryption(encrypted_text)
    print("\nBrute Force Decryption Ended.\n")
    

    print(f"Original Text: {original_text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")