# Cipher should eliminate capitalization, spaces & punctuation for maximum effectivness 
import string

def caesar():
    message = input("\nPlease input your message.\n").replace(" ","").lower().strip(string.punctuation)
    shift = int(input("What is the shift desired for the encoding?\n "))
    
    if (shift % 26 == 0):
        return("There can be no shift if divisible by 26")
    
    # decode option is simple math - inverse operations
    if "e" not in input("\nType 'e' or 'E' to encode, anything else will decode\n"):
        shift = len(string.ascii_letters) - shift
    
    alphabet = string.ascii_letters.lower()
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)

if __name__ == '__main__':
	print(caesar())

