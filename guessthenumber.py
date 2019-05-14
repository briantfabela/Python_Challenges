from random import randint # import the random integer function

def getName():
    '''Prompts the user to input their name'''

    return input("What is your name? ").strip() # get name from player, strip whitespace


def chooseDifficulty():
    '''Loop for error handling the difficulty selection process'''

    while True:
        try:
            diff = int(input("Please select a difficulty from 1 to 3: "))
            if diff >= 1 and diff <= 3: return diff # only way to break out of loop
        except ValueError: # if user did not select a number
            print("Please input a valid integer")
        else: # if user did not select a number from 1 to 3
            print("Please input an integer from 1 and 3")


def randomNums(difficulty):
    '''Will return the guess range as well as the number to guess based on
       the selected difficulty'''

    start = randint(1, 5) # random number between 1 and 5

    # select the end of the guess range based on difficulty
    if difficulty == 1:
        end = randint(start+6, start+10) # 1 to (7 to 15)
    elif difficulty == 2:
        end = randint(start+20, 40+start**2) # 1 to (21 to 65)
    else:
        end = randint(start+70, 120+start**2) # 1 to (71 to 145)

    n = randint(start+2, end) - 1 # account for inclusivity of randint()'s range

    return str(start), str(end), n # return start & end as string, and the number as int

def guessNumber(name):
    '''The guessing game is be played inside this function'''

    # choose difficulty and get the number range and number to guess
    rangeStart, rangeEnd, number = randomNums(chooseDifficulty())

    print("Hi "+name+", I'm thinking of a number between", rangeStart, " and ", rangeEnd)

    guess = 0 # variable storing the user's guess
    nog = 0 # number of guesses

    while guess != number: # until the guess is correct
        try:
            guess = int(input("Guess: "))
            nog+=1

            if guess == number: 
                print("Ding ding ding! You guessed right!")
            elif guess > number: 
                print("Lower!")
            else:
                print("Higher!")

        except ValueError:
            print("Please input a valid integer")

    print("\nYou guessed", number, "after", nog, "guesses!\n\n")

def main():
    name = getName() # get name from player
    
    # after getting the user's name, we can just keep them playing inside guessNumber()
    while True:
        guessNumber(name)
    
if __name__ == "__main__":
    main()