
from random import choice
from english_words import english_words_set
words = list(english_words_set)
word = choice(words)

gameOver = False

guessed = []

chances = 5
while not gameOver:
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    guess = input("Enter a guess : ").lower()
    guessed.append(guess)
    if guess not in word:
        chances -= 1
    print("Chances left : " + str(chances))
    win = True
    for letter in word:
        if letter not in guessed:
            win = False

    if win == True:
        print("You won!!!")
        gameOver = True
    
    if chances <= 0:
        print("You lost")
        print("The word was "+ word)
        gameOver = True


