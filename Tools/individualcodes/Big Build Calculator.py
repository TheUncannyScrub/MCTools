import os
import sys
import random
import math
from time import *
import decimal

print('Minecraft Resource Calculator')
print('Enter the individual items and the calculator will')
print('tell you how many chest or stacks it is!')
print('*Only works for items that stack up to 64*')

sleep(1)
while True:
    try:
        print('Enter an amount of individual items')
        numinput = float(input('Here: '))
        stacks = (numinput) / 64
        chests = (numinput) / 1728
        dubchest = (numinput) / 3456

        print(round(stacks,2), "Stack(s)")
        print(round(chests,2), "Chest(s)")
        print(round(dubchest,2), "Double Chest(s)")
        break
    except:
        print('You must enter a number!')


sleep(2)
input('Press ENTER to exit')