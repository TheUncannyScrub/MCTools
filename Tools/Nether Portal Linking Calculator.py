import os
import sys
import random
import math
from time import *
print('Lightweight Minecraft Tools')
print('For Nether to Overworld press 1 or for Overworld to Nether press 2')

NorO = float(input())
#Nether to Overworld
if NorO == 1:

    print('Nether to Overworld')
    print('Only type numbers!!')
    sleep(1)
    while True:
        try:
            xin = int(input('Nether X Co-Ords: '))
            break
        except:
            print('You must enter a number!')

    while True:
        try:
            yin = int(input('Nether Y Co-Ords: '))
            break
        except:
          print('You must enter a number!')

    while True:
        try:
            zin = int(input('Nether Z Co-Ords: '))
            break
        except:
         print('You must enter a number!')

    xout = (xin) * 8
    yout = (yin) * 8
    zout = (zin) * 8

    print('Build a portal at:' ,xout,yout,zout, 'In the nether')

    sleep(2)
    input('Press ENTER to exit')
#Overworld to Nether
if NorO == 2:

    print('Overworld to Nether')
    print('Only type numbers!!')
    sleep(1)
    while True:
        try:
            xino = int(input('Overworld X Co-Ords: '))
            break
        except:
            print('You must enter a number!')

    while True:
        try:
            yino = int(input('Overworld Y Co-Ords: '))
            break
        except:
          print('You must enter a number!')

    while True:
        try:
            zino = int(input('Overworld Z Co-Ords: '))
            break
        except:
         print('You must enter a number!')

    xouto = (xino) / 8
    youto = (yino) / 8
    zouto = (zino) / 8

    print('Build a portal at:' ,xouto,youto,zouto, 'In the nether')

    sleep(2)
    input('Press ENTER to exit')
