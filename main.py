import json
from difflib import get_close_matches

def getmeaning(word):

    word = word.lower()
    if word in dictionaryData:
        return dictionaryData[word]
    elif word.title() in dictionaryData:
        return dictionaryData[word.title()]
    elif word.capitalize() in dictionaryData:
        return dictionaryData[word.capitalize()]
    elif word.upper() in dictionaryData:
        return dictionaryData[word.upper()]
    else:
        match = get_close_matches(word,dictionaryData.keys())[0]
        print(f'word {word} was not found, you might wanted to say {match}')
        decide = input('press y or n')
        if decide == 'y':
            return dictionaryData[match]
        elif decide == 'n':
            return 'This word does not exist'
        else:
            return 'you have entered the wrong input (y/n)'


def getword():
    word = input('write the word to lookup: ')
    return word


x = 'y'
while x == 'y':
    dictionaryData = json.load(open('data.json'))

    word = getword()
    meaning = getmeaning(word)

    if type(meaning) == list:

        print(f'The meaning of {word}:')
        for item in meaning:
            print(f'- {item}')
    else:
        print(meaning)

