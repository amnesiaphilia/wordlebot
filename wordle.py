import yaml

positionalValue = {
    '0': {'a': 140, 'b': 173, 'c': 198, 'd': 111, 'e': 72, 'f': 134, 'g': 115, 'h': 69, 'i': 34, 'j': 20, 'k': 20, 'l': 87, 'm': 107, 'n': 37, 'o': 41, 'p': 141, 'q': 23, 'r': 105, 's': 365, 't': 149, 'u': 33, 'v': 43, 'w': 82, 'y': 6, 'z': 3}, 
    '1': {'b': 16, 'c': 40, 'd': 20, 'f': 8, 'g': 11, 'h': 144, 'i': 201, 'l': 200, 'm': 38, 'n': 87, 'o': 279, 'p': 61, 'r': 267, 's': 16, 't': 77, 'u': 185, 'v': 15, 'w': 44, 'x': 14, 'z': 2, 'a': 303, 'e': 241, 'y': 22, 'j': 2, 'k': 10, 'q': 5}, 
    '2': {'a': 306, 'b': 56, 'h': 9, 'i': 266, 'l': 111, 'o': 243, 'u': 165, 'y': 29, 'r': 163, 't': 111, 'e': 177, 'm': 61, 'f': 25, 'd': 75, 's': 80, 'g': 67, 'p': 57, 'k': 12, 'n': 137, 'v': 49, 'c': 56, 'w': 26, 'z': 11, 'x': 12, 'j': 3, 'q': 1}, 
    '3': {'c': 150, 's': 170, 't': 139, 'e': 318, 'o': 132, 'd': 69, 'r': 150, 'u': 82, 'v': 45, 'i': 158, 'g': 76, 'p': 50, 'b': 24, 'l': 162, 'n': 182, 'a': 162, 'k': 55, 'f': 35, 'h': 28, 'z': 20, 'm': 68, 'j': 2, 'w': 25, 'x': 3, 'y': 3}, 
    '4': {'k': 113, 'e': 421, 'y': 364, 't': 253, 'r': 212, 'd': 118, 's': 36, 'n': 130, 'x': 8, 'l': 155, 'g': 41, 'w': 17, 'm': 42, 'i': 11, 'f': 26, 'a': 63, 'c': 31, 'o': 58, 'h': 137, 'u': 1, 'p': 56, 'z': 4, 'b': 11}
    }

letterValues = {'a': 974, 'b': 280, 'c': 475, 'k': 210, 's': 667, 'e': 1229, 't': 729, 'y': 424, 'o': 753, 'h': 387, 'r': 897, 'i': 670, 'd': 393, 'l': 715, 'u': 466, 'v': 152, 'n': 573, 'g': 310, 'p': 365, 'm': 316, 'f': 228, 'x': 37, 'w': 194, 'z': 40, 'j': 27, 'q': 29}

wordValues = {}
bestWord = {'word': 'stare', 'score': 5815}
bestWordPositional = {'word': 'slate', 'score': 1431}
bestWordNonPositional = {'word': 'alert', 'score': 4544}

wordLetters = {}

""" with open("words.yaml", "r") as file:
        words = yaml.safe_load(file) """

""" for item in words['words']: #this for loop looked over every word and assigned a score to each letter in each position
    #print(item)
    for i, letter in enumerate(item):
        #print(f'{i}: {letter}')
        if letter in positionalValue[str(i)]:
            positionalValue[str(i)][letter] = positionalValue[str(i)][letter] + 1
        else:
            positionalValue[str(i)][letter] = 1 """

""" for item in words['words']: #this code was used to evaluate each word and assign it a score based on how frequently each letter in each position appears in the overall word list
    wordValues[item] = {}
    for i, letter in enumerate(item):
        #print(f'{letter} in position {i} = {positionalValue[str(i)][letter]}')
        wordValues[item][str(i)] = positionalValue[str(i)][letter]
    wordValues[item]['score'] = wordValues[item]['0'] + wordValues[item]['1'] + wordValues[item]['2'] + wordValues[item]['3'] + wordValues[item]['4']
    #print(wordValues[item])
        

with open("wordValues.yaml", "w") as outfile:
        yaml.dump(wordValues,outfile) """

""" with open("wordValues.yaml", "r") as file: #this code was used to determine which word has the single highest value based on positional letter scores. that word is 'slate'
        wordValues = yaml.safe_load(file)
for item in wordValues:
    if wordValues[item]['score'] > bestWord['score']:
        bestWord['word'] = item
        bestWord['score'] = wordValues[item]['score']
    else:
        continue
    print(bestWord) """

""" with open("words.yaml", "r") as file: #this for loop looked over every word and assigned a score to each letter regardless of position
        words = yaml.safe_load(file)

for item in words['words']: 
    #print(item)
    for i, letter in enumerate(item):
        #print(f'{i}: {letter}')
        if letter in letterValues:
            letterValues[letter] = letterValues[letter] + 1
        else:
            letterValues[letter] = 1

print(letterValues) """

# at this point I used replace function to change 'score' to 'positionalScore' in the words.yaml file
# shortly thereafter I realized this had the unfortunate effect of changing the key for the word 'score' to 'positionalScore' which was dumb.

""" with open("words.yaml", "r") as file: #this code was used to add a score based on non-positional letter values. repeated letters in a word were only counted once.
        words = yaml.safe_load(file)

with open("wordValues.yaml", "r") as file2: 
        wordValues = yaml.safe_load(file2)

for item in words['words']: 
    print(item)
    #wordValues[item] = {}
    wordLetters = []
    wordValues[item]['score'] = 0
    wordValues[item]['totalScore'] = 0
    #print(wordLetters)
    for i, letter in enumerate(item):
        #print(f'{letter} in position {i} = {positionalValue[str(i)][letter]}')
        if letter not in wordLetters:
            wordLetters.append(letter)
            wordValues[item]['score'] += letterValues[letter]
        else:
            continue
        #print(wordValues[item]['score'])
    #print(wordValues[item])
    wordValues[item]['totalScore'] = wordValues[item]['score'] + wordValues[item]['positionalScore']

with open("wordValues.yaml", "w") as outfile:
        yaml.dump(wordValues,outfile) """

""" with open("wordValues.yaml", "r") as file: #this code was used to determine which word has the single highest value based on non-positional letter scores. that word is 'alert'
        wordValues = yaml.safe_load(file)
for item in wordValues:
    if wordValues[item]['score'] > bestWord['score']:
        bestWord['word'] = item
        bestWord['score'] = wordValues[item]['score']
    else:
        continue
    print(bestWord) """

""" with open("wordValues.yaml", "r") as file: #this code was used to determine which word has the single highest value based on the total score. that word is 'stare'
        wordValues = yaml.safe_load(file)
for item in wordValues:
    if wordValues[item]['totalScore'] > bestWord['score']:
        bestWord['word'] = item
        bestWord['score'] = wordValues[item]['totalScore']
    else:
        continue
    print(bestWord) """

""" valueCheck = []
count = 0

with open("wordValues.yaml", "r") as file: 
        wordValues = yaml.safe_load(file)
for item in wordValues:
    if wordValues[item]['totalScore'] not in valueCheck:
        valueCheck.append(wordValues[item]['totalScore'])
    else:
        #print(f'{item} has the same score as another word')
        count += 1
print(f'{count} words have matching scores') """

""" bestGuess = {'word': 'aaaaa', 'totalScore': 0, 'positionalScore': 0, 'score': 0}
bestGuessWord = '' """

""" with open("wordValues.yaml", "r") as file: 
        wordValues = yaml.safe_load(file)
for item in wordValues:
    if wordValues[item]['totalScore'] > bestGuess['totalScore']:
        bestGuess = wordValues[item]
        bestGuessWord = item
        print(bestGuess)
    elif wordValues[item]['totalScore'] == bestGuess['totalScore']:
        if wordValues[item]['positionalScore'] > bestGuess['positionalScore']:
            bestGuess = wordValues[item]
            bestGuessWord = item
        else:
            continue
    else:
        continue
print(f'The best guess is {bestGuessWord}') """

blackLetters = []
guessState = {
    'blackLetters': [],
    'yellowLetters': [],
    'greenLetters': [],
    '0': {'green': '', 'yellow': []},
    '1': {'green': '', 'yellow': []},
    '2': {'green': '', 'yellow': []},
    '3': {'green': '', 'yellow': []},
    '4': {'green': '', 'yellow': []},
}

testState = {
    'blackLetters': [],
    'yellowLetters': ['t'],
    'greenLetters': [],
    '0': {'green': '', 'yellow': []},
    '1': {'green': '', 'yellow': []},
    '2': {'green': '', 'yellow': ['t']},
    '3': {'green': '', 'yellow': []},
    '4': {'green': '', 'yellow': []},
}

with open("wordValues.yaml", "r") as file: 
    wordValues = yaml.safe_load(file)

def findBestWord(wordValues):
    bestGuess = {'word': 'aaaaa', 'totalScore': 0, 'positionalScore': 0, 'score': 0}
    bestGuessWord = ''
    for item in wordValues:
        if wordValues[item]['totalScore'] > bestGuess['totalScore']:
            bestGuess = wordValues[item]
            bestGuessWord = item
            #print(bestGuess)
        elif wordValues[item]['totalScore'] == bestGuess['totalScore']:
            if wordValues[item]['positionalScore'] > bestGuess['positionalScore']:
                bestGuess = wordValues[item]
                bestGuessWord = item
            else:
                continue
        else:
            continue
    print(f'The best guess is {bestGuessWord}')
    return bestGuessWord

def updateWordList(wordValues,guessState):
    newWordValues = {}
    #print(guessState['blackLetters'])
    for item in wordValues:
        currentWordBlackLetter = False
        currentWordGreenMismatch = False
        currentWordYellows = []
        currentWordMissingYellow = False
        currentWordYellowMatch = False
        for i, letter in enumerate(item):
            #print(letter)
            if letter in guessState['blackLetters']:
                currentWordBlackLetter = True
                #print(f'black letter in {item} index {i}')
                continue
            elif guessState[str(i)]['green'] != '':
                if guessState[str(i)]['green'] == letter:
                    continue
                    #print(f'green match in {item} index {i}')
                else:
                    currentWordGreenMismatch = True
                    #print(f'green mismatch in {item} index {i}')
            elif letter in guessState['yellowLetters']:
                currentWordYellows.append(letter)
                if letter in guessState[str(i)]['yellow']:
                    currentWordYellowMatch = True
                else:
                    continue
            else:
                continue
        for yellow in guessState['yellowLetters']:
            #print(yellow)
            if yellow in currentWordYellows:
                #print('in')
                continue
            else:
                #print('missing')
                currentWordMissingYellow = True
        #print(currentWordMissingYellow)
        if currentWordBlackLetter == True or currentWordGreenMismatch == True or currentWordYellowMatch == True or currentWordMissingYellow == True:
            continue
        else:
            newWordValues[item] = wordValues[item]
    return newWordValues

#findBestWord(wordValues)
#wordValues = updateWordList(wordValues,blackLetters)

def updateGuessState(currentState):
    lastGuess = input('What word did you guess? ').lower()
    guessResults = input('Input the results using b, y, and g - for example \'gbbbb\' if the first letter was green and all others black.\nResults: ').lower()
    updateBlackLetters = []
    for i, letter in enumerate(lastGuess):
        if guessResults[i] == 'b':
            if guessResults[i] not in currentState['yellowLetters'] or guessResults[i] not in currentState['greenLetters']:
                currentState['blackLetters'].append(letter)
        elif guessResults[i] == 'y': 
            currentState['yellowLetters'].append(letter)
            currentState[str(i)]['yellow'].append(letter)
        elif guessResults[i] == 'g': 
            currentState['greenLetters'].append(letter)
            currentState[str(i)]['green'] = letter
            #print(letter)
            #print(currentState['yellowLetters'])
            if letter in currentState['yellowLetters']:
                removeAllYellow = currentState['yellowLetters'].count(letter)
                for i in range(removeAllYellow):
                    currentState['yellowLetters'].remove(letter)
    if len(currentState['blackLetters']) > 0:
        #print(currentState['blackLetters'])
        for ii, blackLetter in enumerate(currentState['blackLetters']):
            #print(f'index {ii} and letter {blackLetter}')
            if blackLetter not in currentState['greenLetters'] and blackLetter not in currentState['yellowLetters']:
                updateBlackLetters.append(blackLetter)
            currentState['blackLetters'] = updateBlackLetters
    return currentState

while True:
    print(len(wordValues))
    findBestWord(wordValues)
    guessState = updateGuessState(guessState)
    #print(guessState)
    wordValues = updateWordList(wordValues,guessState)
