import string
import re

def encryptor():
    #set alphabets
    lower_case = string.ascii_lowercase
    punctuation = string.punctuation
    #set punctuation to include space and punctuation characters
    punctuation = " " + punctuation  # Include space in punctuation
    #initialize encrypted text
    encrypted_text = ""


    #get text
    user_text = input("Enter text to encrypt: ").lower().strip()

    #set shift
    shift = int(input("Enter shift value (1-25): "))
    #shift text
    for char in user_text:
        if char in lower_case:
            #shift lower case letters
            shifted_index = (lower_case.index(char) + shift) % 26
            encrypted_text += lower_case[shifted_index]

        #if char.isspace():
            #keep spaces as is
           # encrypted_text += " "
        
        if char in punctuation:
            #shift upper case letters
            shifted_index = (punctuation.index(char) + shift) % 33 #the length of punctuation is 33 (including space)
            encrypted_text += punctuation[shifted_index]
    print(f"{user_text} -> {encrypted_text}")


def decryptor(encrypted, shift):

    lower_case = string.ascii_lowercase
    punctuation = string.punctuation
    #set punctuation to include space and punctuation characters
    punctuation = " " + punctuation  # Include space in punctuation

    #initialize decrypted text
    decrypted_text = ""
    #shift text
    for char in encrypted:
        if char in lower_case:
            #shift lower case letters back
            shifted_index = (lower_case.index(char) - shift) % 26
            decrypted_text += lower_case[shifted_index]
        if char in punctuation:
            #shift punctuation back
            shifted_index = (punctuation.index(char) - shift) % 33 #the length of punctuation is 33 (including space)
            decrypted_text += punctuation[shifted_index]
    return f"{encrypted} -> {decrypted_text}"

    
#set translation table for shifted text and alphabet
#translate text using the translation table (encryption)
#return encryption
if __name__ == "__main__":
    encryptor()
    # Ask if the user wants to decrypt
    decrypt_choice = input("Do you want to decrypt the text? (yes/no): ").strip().lower()
    if decrypt_choice == 'yes':
        encrypted_text = input("Enter the encrypted text: ")
        shift = int(input("Enter the shift value used for encryption: "))
        decrypted_text = decryptor(encrypted_text, shift)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Encryption complete. No decryption performed.")