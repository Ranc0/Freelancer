def emailChecker(email):
    index = -1
    j = 0
    for i in email:
        if i == '@':
            index = j
            break
        j += 1
    if index == 0:
        return 0
    if email[index:] == "@gmail.com" or email[index:] == "@hotmail.com" or email[index:] == "outlook.com":
        return 1
    return 0

def passwordChecker(password):
    if len(password) >= 6 and len(password) <= 20:
        return 1
    return 0

def phoneNumberChecker(phoneNumber):
    if len(phoneNumber) == 13:
        if phoneNumber[0:4] != "+963":
            return 0
        if len(phoneNumber[4:]) != 9:
            return 0
        return 1
    elif len(phoneNumber) == 10:
        if phoneNumber[0:2] != "09":
            return 0
        return 1
    return 0
