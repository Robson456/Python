import random
from collections import Counter
 
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
word = random.choice(someWords)
print('Guess the word! HINT: word is a name of a fruit')
letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0 
hang = []
try:
        while (chances != 0) and flag == 0:
            chances -= 1
            try:
                guess = str(input('\nEnter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess)>1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
                    
            if guess != word: #if wrong char print hangman
                hang.insert(0, guess)
                print(str(hang) + ' u have ' + str(chances-flag)+ ' chanses left')
                
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) !=Counter(word)):
                    print(char, end=' ')
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is:",word,end=' ')
                    flag = 1
                    print('\nCongratulations, You won!')
                    break
                else:
                    print('_', end=' ')

        if chances==0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))
except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()