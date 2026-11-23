import time 
import random 
import attacksequence 
import sys
import g1main  
from g1main import Monster 
from g1main import Player 
from g1main import Item  
from g1main import classtoname
import threading 
import asyncio 
import os

         
colours = {
    # Standard colors
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    
    # Bright / high-intensity colors
    "gray": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    
    # Reset
    "reset": "\033[0m"
} 
def add_item(player, item):
    pinv = player.inventory 
    if item.truename in pinv: 
        item.amount += 1 
    elif f'' in pinv: 
        item.amount = 1  
        a = pinv.index(f'') 
        pinv[a] = item.truename
    else: 
        don = input('Inventory is Full drop item? [Y] [N]: ').lower()
        if don =='y':
            try: 
                print(player.d_inventory)  
                print('Choose a Slot') 
                cdslot = int(input('Slot: ')) - 1
                cditem = classtoname[player.inventory[cdslot]]  
                cditem.amount -= 1
                if cditem.amount == 0: 
                    player.inventory[cdslot] = f'' 
                    player.update()  
            except:
                        print('Please enter a valid slot number (1-7), if you have entered a valid number an error has occured.')
def slowtype(string, colour=''):
    if colour != '':
        colour = colours[colour]
    else:
        pass
    for letter in string:
        print(colour + letter, end="", flush=True)
        time.sleep(0.1)
    print(colours['reset'])
def lor(): 
    while True:
        slowtype('Left [L] Or Right [R]')
        _c = input('> ').lower()
        if _c == 'l': 
            return 'l'
        elif _c == 'r': 
            return 'r'
        else: 
            print('Invalid Answer Please enter [L] or [R]')
def riddleq(riddle, answer):
    _a  = 0
    while _a != 3: 
        slowtype(riddle)
        _ans = input('What is the answer: ').lower()
        if answer.lower() == _ans: 
            return 1
        else: 
            print('Wrong')
            _a += 1 
            print(f'{3-_a} guesses left')
    print('No guesses left')
    return 0
#Objects And Variables





#
#Objects  
player = Player()
zombie = Monster('zombie', 'na')
skeleton = Monster('skeleton', 'stick')
valkor = Monster('valkor', 'sword')
health_potion = Item(name='Health Potion', amount = 1, cons=True, heal=10, truename='health_potion', wep=False) 
stick = Item(name='Stick', amount=1, cons=False, heal=0, truename='stick', wep=True)
hands = Item(name='hands', amount=1, cons=False, heal=0, truename='na', wep=True)
sword = Item(name='Sword', amount=1, cons=False, heal=0, truename='sword', wep=True)
fire_sword = Item(name='Fire Sword', amount=0, cons=False, heal=0, truename='fire_sword', wep=True) 
#Variables
dead = False
keys = 0
    