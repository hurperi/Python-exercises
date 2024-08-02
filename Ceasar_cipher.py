import string 

def encrypt(text:str, shift:int)-> str:
    encrypted_text = ""

    #for loop to check each letter in the text
    for i in range(len(text)):
        char = text[i]

        #if character UPPERCASE
        # ord(char) returns the value of letter in unicode. Then we add the shift-value
        if (char.isupper()):
            encrypted_text += chr((ord(char) + shift - 65) % 26 +65)
        #if character is lowercase 
        elif (char.islower()):
            encrypted_text += chr((ord(char) + shift - 97) % 26 +97)
        #if we have special characters
        elif char in string.punctuation:
            encrypted_text += char
        
        # if char is Digital
        elif char.isdigit():
            encrypted_text += char
        
        elif (char.isspace()):
            encrypted_text += char
    
    return encrypted_text






def decrypt(text:str, shift:int) -> str:
    decrypted_text = ""

    # for-loop to check all letters in text
    for i in range(len(text)):
        char = text[i]

        #let's check for uppercase-letters
        if (char.isupper()):
            decrypted_text += chr((ord(char) - shift -65) % 26 + 65)
        
        #if character is lowercase
        elif (char.islower()):
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        
        #check for special characters & empty spaces

        elif char in string.punctuation:
            decrypted_text += char
        
        # if char is Digital
        elif char.isdigit():
            decrypted_text += char
        
        elif (char.isspace()):
            decrypted_text += char


    return decrypted_text






if __name__ == "__main__":
    choice = input("Choose 'e' for encryption, 'd' for decryption: ")
    if choice == "e":
        message = input("Type your secret message: ")
        number = int(input("The shift number: "))
        print(encrypt(message, number))
    
    else:
        message = input("Type your secret message: ")
        number = int(input("The shift number: "))
        print(decrypt(message, number))