# This program is better than gareths version 2.0
import random

def rollAgain():
    print('Would you like to roll again?')
    roll = input()

    if roll == 'yes':
        charPick()

    elif roll == 'no':
        print('Please press enter to exit')
        input()

    else:
        print('Invalid input, please input either "yes" or "no"')
        rollAgain()
        
def charPick():
    num = random.randint(1,22)
    if num == 1: print ('Your Chracter is Genji')
    if num == 2: print ('Your Chracter is Mccre')
    if num == 3: print ('Your Chracter is Pharah')
    if num == 4: print ('Your Chracter is Reaper')
    if num == 5: print ('Your Chracter is Soldier: 76')
    if num == 6: print ('Your Chracter is Tracer')
    if num == 7: print ('Your Chracter is Bastion')
    if num == 8: print ('Your Chracter is Hanzo')
    if num == 9: print ('Your Chracter is Junkrat')
    if num == 10: print ('Your Chracter is Mei')
    if num == 11: print ('Your Chracter is Torbjorn')
    if num == 12: print ('Your Chracter is Widowmaker')
    if num == 13: print ('Your Chracter is D.VA')
    if num == 14: print ('Your Chracter is Reinhardt')
    if num == 15: print ('Your Chracter is Roadhog')
    if num == 16: print ('Your Chracter is Winston')
    if num == 17: print ('Your Chracter is Zarya')
    if num == 18: print ('Your Chracter is Ana')
    if num == 19: print ('Your Chracter is Lucio')
    if num == 20: print ('Your Chracter is Mercy')
    if num == 21: print ('Your Chracter is Symmetra')
    if num == 22: print ('Your Chracter is Zenyatta')
    print()

    rollAgain()

charPick()
