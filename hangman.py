from random import choice
from time import sleep
man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
alphabet =("q,w,e,r,t,y,u,ı,o,p,ğ,ü,a,s,d,f,g,h,j,k,l,ş,i,z,x,c,v,b,n,m,ö,ç".split(","))
words = ["microsoft", "apple", "teacher", "house", "student", "github"]
word = choice(words)
board = " _ "*len(word)
print("-"*35)
print("Welcome to the Hangman.")
print("-"*35)
sleep(1)
print("\nThe word is {} letters".format(len(word)))
sleep(1)
print(board)
guesses = ""
used = ""
win = False


def letterGuess():
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def board():
    sleep(0.2)
    print("\n", man[len(used)])
    print("Used letters:", end=" ")
    for i in used:
        print(i, end=",")


while True:

    board()
    guess = input("\nType a letter: ").casefold()
    guesses += guess
    letterGuess()

    if guess not in alphabet and len(guess) != len(word):
        print()
        print("*" * 35)
        print("Please type a letter!")
        print("*" * 35)
        continue

    if guess not in word:
        if guess not in used:
            used += guess
    if len(used) == 6:
        print("\nYou Lose")
        print("the word was {}.".format(word))
        break
    for i in range(len(word)):
        if word[i] not in guesses:
            win = False
            break
        else:
            win = True
    if win:
        print("\nYou Win!")
        break


















