import random
from WordList import *

class Wordle:

    def __init__(self):
        self.correctWord = ""
        self.splitWord = ["0","0","0","0","0"]

    def generate_random_word_and_split(self):
        word = random.choice(wordlist)
        self.correctWord = word
        self.splitWord = list(word)

    def __check_input_for_validity(self, input):
        if input in wordlist:
            return True
        return False

    def __guess_checker(self, input):
        inputList = list(input)
        #2 is right in right location, 1 is right in wrong location
        #and 0 is wrong letter entirely
        #0 is not used, 1 is used
        valueList = [0,0,0,0,0]
        lettersUsed = [0,0,0,0,0]
        for i in range(5):
            if (inputList[i] == self.splitWord[i]):
                    valueList[i] = 2
                    lettersUsed[i] = 1
        for i in range(5):
            result = self.__guess_checker_helper(inputList[i], lettersUsed)
            if valueList[i] == 0:
                valueList[i] = result
        return valueList
    
    def __guess_checker_helper(self, letter, lettersUsed):
        for j in range(5):
            if (letter == self.splitWord[j] and lettersUsed[j] == 0):
                lettersUsed[j] = 1
                return 1
        return 0

    def setupWordleGame(self):
        self.generate_random_word_and_split()
        print(self.correctWord)

    def __inputparsing(self, input):
        #removes the $g from the string
        input = input[2:]
        input = input.strip()
        return input

    def __checkAndEndGame(self, user, result):
        if result == [2, 2, 2, 2, 2] or user.guessCount == 6:
            user.gameActive = False
            #Todo: all points when game ends should go here
        return

    def convertNumbersToSymbols(self, user):
        result = ""
        for guess in user.guessArray:
            for i in guess:
                if i == 2:
                    result += "🟩"
                elif i == 1:
                    result += "🟨"
                else:
                    result += "⬛"
            result += "\n"
        return result
        
    def wordleGame(self, input, user):
        input = self.__inputparsing(input)
        if not (self.__check_input_for_validity(input)):
            return [9, 9, 9, 9, 9]
        user.guessCount += 1
        if (user.guessCount == 6):
            return [8, 8, 8, 8, 8]
        result = self.__guess_checker(input)
        self.__checkAndEndGame(user, result)
        return result
        

    


