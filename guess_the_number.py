from random import randint

difficulty = input('Please choose your difficulty\n->Easy\n->Medium\n->Hard\n').lower()

if difficulty == "easy":
    number = randint(0,25)
    max_tries = 10
    print("Please guess a number between 0 and 25")
elif difficulty == "medium":
    number = randint(0,50)
    max_tries = 7
    print("Please guess a number between 0 and 50")
else:
    number = randint(0,100)
    max_tries = 5
    print("Please guess a number between 0 and 100")

tries = 0

while tries < max_tries:
    
    guess = int(input('Guess your number ? -> '))

    if guess == number:
        print('You Won 😁')
        break

    elif guess < number:
        print("Your guess is too low!! \n")

    else:
        print("You guess is too high!! \n")

    tries += 1

    print("Tries left : ", str(max_tries - tries))

if tries >= max_tries:
    print('You lost 😞')
    print('The number was : ', str(number))


