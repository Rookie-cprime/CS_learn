bottom = 1
roof = 100
print('Please think of a number between 0 and 100!')
o = True
while o:
    temp = (roof+bottom)//2
    print('Is your secret number %d?'%(temp))
    t = True
    while t:
        x = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
        if x == 'h':
            roof = temp
            t = False
        elif x == 'l':
            bottom = temp
            t = False
        elif x == 'c':
            print('Game over. Your secret number was:%d'%(temp))
            o = False
            break
        else:
            print('Sorry, I did not understand your input.')