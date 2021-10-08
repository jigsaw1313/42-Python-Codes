import random

attempts_list = []

def showScore():
    if len(attempts_list) <= 0:
        print('Currently there is no high score at this game , you may be the first one to get the hit... lets go !!!')
    else:
        print('current high score is %s' %attempts_list)

def myGame():
    randomNumber= int(random.randint(0, 15));
    print('***    WELCOME TO NUMBER GEUSSING GAME   ****')
    playerName= input("Hello My friend , what is your name ?: ")
    willYouPlay = input('Hello %s welcome to game of guessing numbers, would you like to play this game ?(Enter YES/NO)' %playerName)
    attempt = 0
    showScore()
    while willYouPlay == 'yes' or "YES":
        try:
            guess = int(input('Ok %s, Lets go..\t choose a number between 0 and 15:' %playerName))
            if guess < 0 or guess > 15:
                raise ValueError('Please choose a number between 0 and 15 %s')
            if guess == randomNumber:
                print('You got it %s , very well' %playerName)
                attempt += 1
                attempts_list.append(attempt)
                print('Its took you %i to guess the correct number' %attempt)
                
                askPlayAgain = input('Would you like to play again my friend ?: (Enter YES/NO): ')
                attempt = 0
                showScore()
                randomNumber = random.randint(0, 15)
                if askPlayAgain == 'no':
                    print("That's fine, Have a Good day %s" %playerName)
                    break
                    #! HINTS ON GAME
                    
            elif guess > randomNumber:
                    print('Oh no, It is lower')
                    attempt += 1
            elif guess < randomNumber:
                    print('hmmm, It is higher')
                    attempt += 1
        except ValueError as err:
            print('oh noo...., that is not a valid value, Please Try Again')
            print("({})".format(err))
    else :
        print('That is fine , have cool one!')
if __name__ == '__main__':
    myGame()
                                
