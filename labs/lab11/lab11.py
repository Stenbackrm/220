"""
Name: Robert Stenback
Hangman.py
"""
from random import randint
def read_words(file):
    word_file = open(file, 'r')
    words = word_file.readlines()
    return words

def secret_word(word_list):
    word_range = randint(0, len(word_list)- 1)
    word = word_list[word_range]
    word = word[0:-1]
    return word
#done ^

def guessed_word(generated_word, lines, guessed_letter, tries):
    #generates lines and replaces them EX ____ -> _a__
    if lines == '' or guessed_letter == '':
        word_len = len(generated_word)
        lines = '_' * word_len
    else:
        x = 0
        prox = 0
        generated_word = list(generated_word)
        lines = list(lines)
        for i in generated_word:
            if i == guessed_letter:
                lines[x] = generated_word[x]
                x = x + 1
            else:
                try:
                    generated_word.index(str(guessed_letter))
                except:
                    prox = prox + 1
                x = x + 1
        if prox > 0:
            tries = tries - 1
            print('thats not the correct letter', 7 + tries, 'tries left')
        lines = ''.join(lines)

    return lines, tries

def game_over(word, lines, tries):
    return word == lines or tries == -7

def word_spelled(word, lines):
    return word == lines

def play_game():
    #handles game logic
    lines = ''
    guessed_letter = ''
    tries = 0
    word = secret_word(read_words('words.txt'))
    lines, tries = guessed_word(word, lines, guessed_letter, tries)
    print(lines)
    while game_over(word, lines, tries) == False:
        guessed_letter = input('enter your letter:').lower()
        lines, tries = guessed_word(word, lines, guessed_letter,tries)
        print(lines)
    if word_spelled(word,lines) == True:
        print('you win!!! you had ', tries + 7, 'tries left')
    else:
        print('you lose :( the word was: ', word)



def main():
    play_game()

if __name__ == '__main__':
    main()