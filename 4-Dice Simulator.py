import random

'''
https://www.geeksforgeeks.org/dice-rolling-simulator-using-python-random/
This is source code of below codes
i have made some correction on codes and used def and functions
Mohammad.R Mohammadi
'''

def startGame():
    print('*** Welcome To Rolling Dices *** ')
    userName = input('May I Know Your Name ?\n>>>> ')
    print('')
    print('Welcom Mr/Mrs %s To Dice Rolling Simulator.\n' %userName)
    willPlay = input('Would You Like To Roll Dices ? (Y or N)\n>>>> ').lower()
    if 'y' in willPlay:
        print('Perfect, Let\'s Play...')
        rollDice()
    else :
        print('It Was Good to See You...\nGoodBye...')
        exit()


def rollDice():
    number = random.randint(1, 6)
    print('\nThe Dices Is ' + str(number))
    print('')
    print('')
    if number == 1:
        print('[-----]')
        print('[-----]')
        print('[--X--]')
        print('[-----]')
        print('[-----]')
        
    if number == 2:
        print('[-----]')
        print('[X----]')
        print('[-----]')
        print('[----X]')
        print('[-----]')
    
    if number == 3:
        print('[-----]')
        print('[-----]')
        print('[X-X-X]')
        print('[-----]')
        print('[-----]')
        
    if number == 4:
        print('[-----]')
        print('[X---X]')
        print('[-----]')
        print('[X---X]')
        print('[-----]')
        
    if number == 5:
        print('[-----]')
        print('[X---X]')
        print('[--X--]')
        print('[X---X]')
        print('[-----]')
        
    if number == 6:
        print('[-----]')
        print('[X-X-X]')
        print('[-----]')
        print('[X-X-X]')
        print('[-----]')
    askToPlay()



def askToPlay():
        playAgain = input('Would Like to Play Again ?(Y o N)\n>>>> ').lower()
        if playAgain == 'y':
            rollDice()

        elif playAgain == 'n':
            print('Gool Luck My Friend....\nGoodBye')
            exit()
        
        else:
            print('Wring Input...\n')
        askToPlay()
startGame()
