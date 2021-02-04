#####################################################################################################################################
#   author@ Ibrahim AL-Agha
#   date@   February 2, 2021
#####################################################################################################################################

#   Importing Dependencies
import sys
from pynput import keyboard
from termios import tcflush, TCIFLUSH
from time import sleep, time
from numpy import subtract, array, concatenate, sum

keys = []
presstimes = []
releasetimes = []
allpresstimes = []
allreleasetimes = []
ATTEMPTS = 5
THRESHOLD = 0.05
DEBUG = True

#   Initializing Variables
train_file = sys.argv[1]
f = open(train_file)
data = f.read()
f.close()

#   Find Password
def scrape_pass (string_input):
    pword = []
    for letter in string_input:
        if letter != "\n":
            pword.append(letter)
        else:
            pword = "".join(pword)
            return(pword)

text_password = scrape_pass(data)

def getpassstring(array):
    letters = [char for char in array if str(char).isalpha()]
    string = "".join(letters)
    print("String:", string)
    return string

def start ():
    print ("Welcome, User. The password you will be testing against is: {}.".format(text_password))
    sleep(0.5)
    print ("You have {} attempts to enter the correct string of letters.".format(ATTEMPTS))
    sleep(0.5)
    print ("Please press ENTER to submit an attempt or ESC to exit the test.")
    sleep(0.5)
    #password = input("Please start typing now:\n")
    password = text_password
    return (password)

# check to make sure the entry is correct. If so, add it to the data
# that we are collecting.
def check ():
    global presstimes, releasetimes, keys, tries
    print(getpassstring(keys))
    print (tries)
    if (password  == getpassstring(keys)):
        allpresstimes.append(presstimes)
        allreleasetimes.append(releasetimes)
        tries += 1
        keys = []
    presstimes = []
    releasetimes = []

def on_press (key):
    presstimes.append(time())
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(key)

def on_release (key):
    releasetimes.append(time())
    if (key == keyboard.Key.esc or tries >= ATTEMPTS):
        return False
    elif (key == keyboard.Key.enter):
        check()
    

def percent_difference(x1, x2):
    x3 = abs((x2 - x1)/(x1))
    return x3
########################################## MAIN #########################################
password = start().strip()
tries = 0


print("Please start typing now:")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

tcflush(sys.stdin, TCIFLUSH)

allpresstimes = array(allpresstimes)
allreleasetimes = array(allreleasetimes)

k_press = subtract(allreleasetimes, allpresstimes) 
k_inter = subtract(allpresstimes[:,1:], allreleasetimes[:,:-1])
allfeatures = concatenate((k_press[:,:-1], k_inter[:,:-1]), axis = 1)

pd = percent_difference(25, 30)


if pd >= THRESHOLD:
    print("Valid entry")