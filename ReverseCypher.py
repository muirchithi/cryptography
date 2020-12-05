message = "Three can keep a secret if two of them are dead"
reversedMessage = "daed era meht fo owt fi terces a peek nac eerhT"
translated = " "
i = len(message)-1

while i>=0:
    translated = translated + reversedMessage[i]
    i = i - 1
print("The cipher is : ", translated)