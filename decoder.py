from hashlib import sha256
import re

# Change this given salt if you need a different one
salt = 'F23694G8'

alphabet_numbers = {'a':4, 'A':4, 'e':3, 'E':3, 'i':1, 'I':1, 'o':0, 'O':0, 'u':9, 'U':9}
a_to_number = {'a':4, 'A':4}
e_to_number = { 'e':3, 'E':3}
i_to_numer = {'i':1, 'I':1}
o_to_number = {'o':0, 'O':0}
u_to_number = { 'u':9, 'U':9}

#The hash to compare to
hash = '1dad458d3e83b92f56ae57990bd1324d0d648590f7662f7519e3d046498b9f1f'

def compare_hash(hash1, hash2):
    if hash1 == hash2:
        return True
    return False


def word_iterator(filepath='domingosiete.txt'):
    with open(filepath) as f:
        for line in f:
            my_list = re.findall(r'[\w]+', line)
            for word in my_list:
                yield word

def encryptfront(word):
    return sha256((salt + word).encode('utf-8')).hexdigest()

def encryptback(word):
    return sha256((word + salt).encode('utf-8')).hexdigest()

def switchCasing(word):
    return word.swapcase()

def changeVocalsForNumbers(word):
    return word.translate(alphabet_numbers)

def upperFirst(word):
    return word.capitalize()

def lowerFirst(word):
    return word[0].lower() + word[1:]

def find_the_word(hash):
    '''
        A decoder that finds if a word matches a given hash on a given document
    '''
    for word in word_iterator():
        if compare_hash(encryptfront(word), hash):
            print(word)
            print(encryptfront(word))
            break
        elif compare_hash(encryptback(word), hash):
            print(word)
            print(encryptback(word))
            break
        elif compare_hash(encryptfront(switchCasing(word)), hash):
            print(word)
            print(encryptfront(switchCasing(word)))
            break
        elif compare_hash(encryptback(switchCasing(word)), hash):
            print(word)
            print(encryptback(switchCasing(word)))
            break
        elif compare_hash(encryptfront(changeVocalsForNumbers(word)), hash):
            print(word)
            print(encryptfront(changeVocalsForNumbers(word)))
            break
        elif compare_hash(encryptback(changeVocalsForNumbers(word)), hash):
            print(word)
            print(encryptback(changeVocalsForNumbers(word)))
            break
        elif compare_hash(encryptfront(changeVocalsForNumbers(switchCasing(word))), hash):
            print(word)
            print(encryptfront(changeVocalsForNumbers(switchCasing(word))))
            break
        elif compare_hash(encryptback(changeVocalsForNumbers(switchCasing(word))), hash):
            print(word)
            print(encryptback(changeVocalsForNumbers(switchCasing(word))))
            break
        elif compare_hash(encryptfront(upperFirst(word)), hash):
            print(word)
            print(encryptfront(upperFirst(word)))
            break
        elif compare_hash(encryptback(upperFirst(word)), hash):
            print(word)
            print(encryptback(upperFirst(word)))
            break
        elif compare_hash(encryptfront(changeVocalsForNumbers(upperFirst(word))), hash):
            print(word)
            print(encryptfront(changeVocalsForNumbers(upperFirst(word))))
            break
        elif compare_hash(encryptback(changeVocalsForNumbers(upperFirst(word))), hash):
            print(word)
            print(encryptback(changeVocalsForNumbers(upperFirst(word))))
            break
        elif compare_hash(encryptfront(lowerFirst(word)), hash):
            print(word)
            print(encryptfront(lowerFirst(word)))
            break
        elif compare_hash(encryptback(lowerFirst(word)), hash):
            print(word)
            print(encryptback(lowerFirst(word)))
            break
        elif compare_hash(encryptfront(changeVocalsForNumbers(lowerFirst(word))), hash):
            print(word)
            print(encryptfront(changeVocalsForNumbers(lowerFirst(word))))
            break   
        elif compare_hash(encryptback(changeVocalsForNumbers(lowerFirst(word))), hash):
            print(word)
            print(encryptback(changeVocalsForNumbers(lowerFirst(word))))
            break
    print('Couldnt finde the word')

def find_the_word_2(hash, filePath):
    '''
        An improved version of decoder that finds if a word matches a given hash on a given document
    '''
    for word in word_iterator(filePath):
        for letter in alphabet_numbers:
            if letter in word:
                word = word.replace(letter, str(alphabet_numbers[letter]))
                if compare_hash(encryptfront(word), hash):
                    print(word)
                    print(encryptfront(word))
                    break
                if compare_hash(encryptback(word), hash):
                    print(word)
                    print(encryptback(word))
                    break
                if compare_hash(encryptfront(switchCasing(word)), hash):
                    print(switchCasing(word))
                    print(encryptfront(switchCasing(word)))
                    break
                if compare_hash(encryptback(switchCasing(word)), hash):
                    print(switchCasing(word))
                    print(encryptback(switchCasing(word)))
                    break
                if compare_hash(encryptfront(upperFirst(word)), hash):
                    print(upperFirst(word))
                    print(encryptfront(upperFirst(word)))
                    break   
                if compare_hash(encryptback(upperFirst(word)), hash):
                    print(upperFirst(word))
                    print(  encryptback(upperFirst(word)))
                    break
                if compare_hash(encryptfront(lowerFirst(word)), hash):
                    print(lowerFirst(word))
                    print(encryptfront(lowerFirst(word)))
                    break
                if compare_hash(encryptback(lowerFirst(word)), hash):
                    print(lowerFirst(word))
                    print(encryptback(lowerFirst(word)))
                    break   

if __name__ == '__main__':
    find_the_word(hash)
    find_the_word_2(hash)