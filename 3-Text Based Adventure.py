
'''
https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3
'''

def start():
    print('Welcome to game\n')
    print('')
    print('You are standing in a dark room....')
    answer = input('There are doors on your left and right side..\nwhich one do you chose ?(L or R):').lower()
    if 'l' in answer:           #lead player to bear room
        bearRoom()
    elif 'r' in answer:         #lead player to monster room
        monsterRoom()
    
    else:
        gameOver('You dont know how to type something properly ??')




def bearRoom():
    print('\n\nAlright ... your are in bear room')
    print('There is bear in this room \nBehind the bear there is another door')
    print('The bear is eating a tasty honey !!!')
    print('What would you do ?(1 or 2) ')
    print('1-Take the Honey\n2-Taunt the door')
    answer = input('>> ')
    
    if answer == '1':
        gameOver('The bear killed you.... RIP')
    
    elif answer == '2':
        print('Your good time...\nThe bear moved away from the door...\nYou can go through it now!')
        diamondRoom()
    else:
        gameOver('You dont know how to type something correctly ??')





def monsterRoom():
    print('\n\nNow you are entered monster room...')
    print('The monster is sleeping...\nBehind the monster there is another door.')
    print('What would you do ? (1 or 2) ')
    print('1-Go through the door silently\n2-Kill the monster and show your courage ?')
    answer = input('>>')
    
    if answer == '1':
        print('Great.....')
        diamondRoom()       #lead player to diamond room
    elif answer == '2':
        gameOver('Game Over...\nThe Monster ate you... He was so hungry !!')
    else:
        gameOver('firstly go and learn how to type a number...')


def diamondRoom():
    print('\n\nYou are in a room filled with diamonds')
    print('And as you may gussed there is another door too !')
    print('What would you do ?(1 or 2) ')
    print('1-Take some diamonds and go through the door')
    print('2-Just go through the door')
    answer = input('>>')
    
    if answer == '1':
        gameOver('They were cursed diamonds! The moment you touched them, the building collapsed and you die !!!')
    elif answer == '2':
        print('Nice.. You are the honest man\nCongrats ! You win the game')
        playAgain()
    else:
        gameOver('Go and learn how to type a number....')
        

def gameOver(reason):
    #print out the reason in new line with \n
    print('\n\n' + reason)
    print('Game Over !!!')
    #below def asks player whether he/she would like to play again or no
    playAgain()
    
def playAgain():
    print('\n\nWould you like to play again ? (y or n) ')
    answer = input('>>').lower()
    
    if 'y' in  answer:
        start()
    elif 'n' in answer:
        print('Thanks for Playing\nGOODBYE..')
        exit()


start()