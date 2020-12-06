import pyperclip


def main():
    myMessage = 'Common sense is not so common'
    myKey = 8

    ciphertext = encryptmessage(myKey, myMessage)
    print(ciphertext + '|')


def encryptmessage(key, message):
    # string representing column in the grid
    ciphertext = [''] * key

    # loop through each column in ciphertext
    for col in range(key):
        pointer = col
        # keep looping to make the pointer walk through the whole length of the message
        while pointer < len(message):
            # place the current character at the pointer position inside the message in the
            # current column in our ciphertext-list
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # conver the ciphertext-list into a single string value
    return ''.join(ciphertext)


if __name__ == "__main__":
    main()
