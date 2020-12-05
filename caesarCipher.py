#Caesar Cipher

import pyperclip
#the string to be encrypted

message = input('Input String to be encrypted\n')

#encryption/decryption key is 13
key = 13

#tell the program wether to encrypt or decrypt
mode = 'decrypt'

# every possible symbol that can be encrypted
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
#message = message.upper()

#run encryption/decryption on every letter
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) #get number of the letter
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num -key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        #add encrypted or decrypted number symbols at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting or decrypting it
        translated = translated + symbol


print(translated)

pyperclip.copy(translated)


