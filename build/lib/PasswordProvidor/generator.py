# core.py

import string
import random

class Generator:
    def __init__(self, haveSpecialChar, haveLetter, length):
        self.haveSpecialChar = haveSpecialChar
        self.haveLetter = haveLetter
        self.length = length
        self.savedPasswords = []
    
    def generatePassword(self):
        listOfChar = []
        password = ""
        if self.haveLetter:
            if self.haveSpecialChar:
                for char in string.ascii_letters:
                    for character in string.punctuation:
                        listOfChar.append(char)
                        listOfChar.append(character)
                        listOfChar.append(str(random.randint(0, 9)))
            else:
                for char in string.ascii_letters:
                    listOfChar.append(char)
                    listOfChar.append(str(random.randint(0, 9)))
        else:
            for i in range(random.randint(0, 100)):
                listOfChar.append(str(random.randint(0, 9)))

        for i in range(self.length):
            password += random.choice(listOfChar)

        print(f"This is your password: {password}")
        self.savedPasswords.append(password)
        return password
    
    def getRecentPassword(self):
        try:
            return self.savedPasswords[len(self.savedPasswords) - 1]
        except IndexError:
            raise IndexError("There are no passwords to fetch in savedPasswords.")
    
    def getPasswordLength(password):
        try:
            return len(password)
        except TypeError:
            raise TypeError("Password has to have a length.")
    
    def removePassword(self, password):
        try:
            self.savedPasswords.remove(password)
        except ValueError:
            raise ValueError(f"There is no {password} in savedPasswords.")
