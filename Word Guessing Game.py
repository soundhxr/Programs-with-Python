from time import sleep
from random import choice
print("Welcome to this word guessing game!\nInstructions:\nYou win this game by guessing the secret word correctly\nThe word to guess is represented by a row of dashes, representing each letter of the word\nYou will be given 8 points. In each of your turns, you should guess a letter which you think might occur in the word\nIf you guess a letter which occurs in the word, I will write it in all its correct positions\nIf the suggested letter does not occur in the word, you lose 1 point out of 8 points\nYou should find the secret word before you run out of points\nYou may also guess the whole word at any time\nIf the word is correct, the game is over and you win\nIf the word is wrong, YOU LOSE\nNow, Let's Play")
word_list = ["MATHEMATICS", "OXYGEN", "IVORY", "IVY", "JELLY", "BUFFOON", "PUPPY", "ZOMBIE", "MORNING", "IDEA", "SEQUEL", "FENCE", "WASTE", "REJECT", "SOCIETY", "GRIEVE", "ZEBRA", "DEATH", "IMPOSTOR", "POP", "TRUST", "MUSIC", "VIDEO", "ALGEBRA", "CONTACT", "XEROX", "ASSASSINATION", "HISTORY"]
word = choice(word_list)
secret_word = list(word)
alphabets = list("QWERTYUOIPASDFGHJKLZXCVBNM")
dash = []
guessed_right = []
guesses = []
lst = []
word_guess = ""
turns = 8
for i in secret_word:
    dash.append("_")
print("secret word: ", *dash)
s = list(range(len(secret_word)))
while turns != 0 and word_guess != word:
    while True:
        letter = input("\nguess a letter in the word: ").upper()
        if letter in guesses:
            print("\nYou have already entered this letter, try a different letter")
            continue
        if letter not in alphabets:
            print("\ninvalid input")
            continue
        else:
            break
    guesses.append(letter)
    for k in s:
        if secret_word[k] == letter:
            dash[k] = letter
            guessed_right.append(letter)
            lst.append(letter)
    print("secret word:", *dash)
    if len(lst) == 0:
        print("Oops, you guessed it wrong. You lose a point")
        turns -= 1
    lst.clear()
    if secret_word == dash:
        print("\ncongratulations, you win!")
        break
    #sleep(2)
    print("\nYour points:", turns)
    #sleep(2)
    print("No. of dashes to be filled:", len(secret_word) - len(guessed_right))
    #sleep(2)
    print("Letters entered:",*guesses)
    #sleep(2)
    if turns != 0:
        wt = input("\nwant to guess the word? (y/n): ").upper()
        if wt == 'Y':
            word_guess = input("the secret word is: ").upper()
            if word_guess == word:
                print("\nyou got it right! YOU WIN")
            else:
                print("\nyou guessed it wrong, YOU LOSE")
                print("The secret word is", word)
                break
if turns == 0:
    print("\nyou are out of points, YOU LOSE.")
    print("The secret word is", word)
