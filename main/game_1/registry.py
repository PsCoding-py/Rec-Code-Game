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
def add_item(player, item):
    pinv = player.inventory 
    if item.truename in pinv: 
        item.amount += 1 
    elif f'' in pinv: 
        item.amount += 1  
        a = pinv.index(f'') 
        pinv[a] = item.truename
def slowtype(string): 
    for letter in string:
        print(letter, end="", flush=True)
        time.sleep(0.1)
    print('')
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
zombie = Monster('zombie', 'na')  
player = Player()
skeleton = Monster('skeleton', 'stick')
health_potion = Item(name='Health Potion', amount = 0, cons=True, heal=10, truename='health_potion', wep=False) 
stick = Item(name='Stick', amount=1, cons=False, heal=0, truename='stick', wep=True)
hands = Item(name='hands', amount=0, cons=False, heal=0, truename='na', wep=True)
sword = Item(name='Sword', amount=0, cons=False, heal=0, truename='sword', wep=True)
#Variables
dead = False
keys = 0
    