#module = a file containing python code. May contain functions, classes, etc.
#used with modular programming, which is to separate a program into parts
'''
import messages 
import messages as m

m.hello()
m.bye()
from messages import hello, bye
from messages import * (this one is dangerous)
'''
#help("modules")

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper or scissors?: ").lower()

if player == computer: 
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")