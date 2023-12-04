def guessGame()

    import random
    MAX_GUESS = 5
    RAND_MAX = 10
    guess = 0
    randNum = random.randrange(1, RAND_MAX+1)
    # randNum = 6
    while True:
        
        guessNum = int(input("Enter a number >> "))
        guess += 1
        if guess == 1:
            guessSpelling = "guess"
        else:
            guessSpelling = "guesses"
        if guessNum == randNum:
            print("You guessed the right number at", guess, guessSpelling, ".")
            break
        if guess == MAX_GUESS:
            print("You have guessed", guess, "times and maximum guess limit reached, try again!")
            print('The number was:', randNum)
            break
        elif guessNum < randNum:
            print("You guessed below, try a higher number")
        else:
            print("The number guessed is above, try a lower number")
        
    print("Thanks for playing!")


def callGuessGame():
    # playAgain = True:
    playAgain = "yes"
    while playAgain:
        x = guessGame()
        return x
    y = input("Do you want to play again (yes to play/no to quit)? >> ")
    y = y.lower()
    if y not playAgain:
        playAgain = False
        break
    else:
        playAgain = True
