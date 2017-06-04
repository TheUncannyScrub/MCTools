import os
import sys
import random
import math
from time import *
import decimal

print('Welcome to PythonMinecraftTools')
sleep(1)
print('A Console based Minecraft tool with many purposes')
sleep(1)
print('Press "1" to use the Resource Calculator')
print('Press "2" to use the Basic Minecraft Time Converstion Table')
print('Press "3" to use the Nether Portal Linking Calculator')


while True:
    try:
        tooltype = int(input('Here: '))
        if tooltype >= 4:
            print('Please enter a valid option')
            tooltype = int(input('Here: '))
            if tooltype >= 4:
                print('Please enter a valid option')
                tooltype = int(input('IVE GIVE YOU ENOUGH TIMES TO GET IT RIGHT.. ENTER A NUMBER 1 OR 2!!!!: '))
                if tooltype >= 4:
                    print('Screw you!! Re-open the program because im not going to error check your stupidity')
                    
        break
    except:
        print('You must enter a valid number')

if tooltype == 1:
    sleep(1)
    print('-')
    print('Minecraft Resource Calculator')
    sleep(1)
    print('If you need help visit the README')
    print('-')
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

if tooltype == 2:
    print('-')
    print('Times Converstions in Minecraft')
    print('-')
    sleep(1)
    print('MC Time to Real Time')
    print('1 Minute = 0.8 Seconds')
    print('1 Hour = 50 Seconds')
    print('1 Day = 20 Minutes')
    print('1 Week = 2.3 Hours')
    print('1 Month = 10 Hours')
    print('1 Year = 5 Days')
    print('-')
    print('Day Time = 10 Minutes')
    print('Sunset/Dusk = 1.5 Minutes')
    print('Night Time = 7 Minutes')
    print('Sunrise/dawn = 1.5 Minutes')
    print('-')

    sleep(1)
    input('Press ENTER to exit')

if tooltype == 3:
    sleep(1)
    print('-')
    print('Nether Portal linking calculator')
    sleep(1)
    print('If you need help visit the README')
    print('-')
    print('Enter the X, Y and Z Co-ords')
    print('then press enter')
    print('-')
    sleep(1)
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

