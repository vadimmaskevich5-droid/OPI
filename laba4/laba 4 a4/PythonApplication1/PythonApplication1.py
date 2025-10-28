import re
def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]


def getCheckSum(string):
    checkSum = 0
    for i in reversed(range(0, len(string) - 1, 2)):
        if int(string[i]) * 2 > 9:
            checkSum = checkSum + 1 + int(string[i]) * 2 - 10
        else:
            checkSum = checkSum + int(string[i]) * 2
    for i in reversed(range(1, len(string) + 1, 2)):
            checkSum += int(string[i])
    return checkSum

def getCardType(string):
    if len(string) == 13 or len(string) == 16 and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and string.startswith("34") or string.startswith("37"):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid"

cardNumber = (input("Введите номер банковской карты: "))
if isValidNumber(cardNumber):
        if getCheckSum(cardNumber) % 10 == 0:
            print(getCardType(cardNumber))
        else:
            print("Invalid")

