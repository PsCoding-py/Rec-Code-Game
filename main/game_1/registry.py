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
zombie = Monster('zombie', 'na')  
player = Player()
skeleton = Monster('skeleton', 'stick')
def lor(): 
    while True:
        slowtype('Left [L] Or Right [R]')
        c = input('> ').lower()
        if c == 'l': 
            return 'l'
        elif c == 'r': 
            return 'r'
        else: 
            print('Invalid Answer Please enter [L] or [R]')
def riddleq(riddle, answer):
    a  = 0
    while a != 3: 
        slowtype(riddle)
        ans = input('What is the answer: ').lower()
        if answer.lower() == ans: 
            return 1
        else: 
            print('Wrong')
            a += 1 
            print(f'{3-a} guesses left')
    print('No guesses left')
    return 0
    