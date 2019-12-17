##guess the number game
## ctrl+alt+n to run

##1 - store a number (random) static range to begin with but option to enter range
##2 - enter a selection
##3 - is this number correct? print 'congratulations'
##if not - is it larger? return 'smaller'
##else return 'larger'
##play again?

from random import seed
from random import randint
# Global Variable config
state = None
number = 0
vcheck = True

# Random Number Setup
seed(1)
rannum = randint(0, 10)
print(rannum)
# New Random


def randomiser():
    global rannum
    rannum = randint(0, 10)
    return rannum


# User Input to enter a number - updates global variable
def numberinput():
    global number
    number = input("Please enter a number between 1 & 10: ")
    return number


def check(num1,num2):
    global state
    global vcheck
    print("check running")
    raninp = int(num1)
    usrinp = int(num2)
    if raninp == usrinp:
        state = "Correct!"
        vcheck = False
    elif raninp > usrinp:
        state = "Larger"
        vcheck = True
    elif raninp < usrinp:
        state = "Smaller"
        vcheck = True
    else:
        state = "Something Else"
        vcheck = True
    return state
    return vcheck
    print("check" + str(state) + str(vcheck))


def game(rannum,number,vcheck):
    while check:
        numberinput()
        print("game > numberinput" + str(state) + str(vcheck))
        check(rannum,number)
        print("game > check" + str(state) + str(vcheck))
    
game(rannum,number,vcheck)


"""
# Want to play again?
def playagain(icheck=True):
    if icheck == True:
        numberinput()
    else:
        print("you ended here")
        exit()


"""




       
