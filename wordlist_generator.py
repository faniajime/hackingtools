import re

class WordlistGenerator:
    def __init__(self):
        self.alphabet_numbers = {'a':4, 'A':4, 'e':3, 'E':3, 'i':1, 'I':1, 'o':0, 'O':0, 'u':9, 'U':9}
        self.a_to_number = {'a':4, 'A':4}
        self.e_to_number = { 'e':3, 'E':3}
        self.i_to_numer = {'i':1, 'I':1}
        self.o_to_number = {'o':0, 'O':0}
        self.u_to_number = { 'u':9, 'U':9}


    def word_iterator(self, filepath):
        '''
            Preforms text processing to extract all of the words from a file
        '''
        with open(filepath) as f:
            for line in f:
                my_list = re.findall(r'[\w]+', line)
                for word in my_list:
                    yield word


    def switchCasing(self,word):
        '''
            Changes the casing of a word
        '''
        return word.swapcase()

    def changeVocalsForNumbers(self, word):
        '''
            Changes vocals for numbers
        '''
        return word.translate(self.alphabet_numbers)

    def upperFirst(self, word):
        '''
            Changes the first letter of the word to uppercase
        '''
        return word.capitalize()

    def lowerFirst(word):
        '''
            Changes the first letter of the word to lowercase
        '''
        return word[0].lower() + word[1:]

    def generateWordlist(self, exitPath, basePath):
        '''
            Generates a list of wordlists by changing every letter of a text
            exitPath: The path where the wordlist will be generated
            basePath: The path of a text to use as reference
        '''
        with open(exitPath, 'a') as f:
            for word in self.word_iterator(basePath):
                f.write(word + '\n')
                f.write(self.switchCasing(word) + '\n')
                f.write(self.changeVocalsForNumbers(word) + '\n')
                f.write(self.upperFirst(word) + '\n')
                f.write(self.lowerFirst(word) + '\n')
                f.write(self.switchCasing(self.changeVocalsForNumbers(word)) + '\n')
                f.write(self.upperFirst(self.changeVocalsForNumbers(word)) + '\n')
                f.write(self.lowerFirst(self.changeVocalsForNumbers(word)) + '\n')
                for letter in word:
                    if letter in self.alphabet_numbers:
                        f.write(word.replace(letter, str(self.alphabet_numbers[letter])) + '\n')
                        f.write(self.switchCasing(word.replace(letter, str(self.alphabet_numbers[letter])))+ '\n')
                        f.write(self.upperFirst(word.replace(letter, str(self.alphabet_numbers[letter])))+ '\n')
                        f.write(self.lowerFirst(word.replace(letter, str(self.alphabet_numbers[letter])))+ '\n')

if __name__ == '__main__':
    wl_gen = WordlistGenerator()
    wl_gen.generateWordlist('wordlist.txt', 'tonto.txt')