
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
from registry import *
import registry
#intro
def mile_1(mile):
    global dead
    global keys 
    if mile == '1':
        slowtype('Hello Adventurer What is your name?') 
        player.name = input("Name: ").title() 
        slowtype('You find yourself in a musty dungeon with moss covered walls.') 
        slowtype(f'You remeber now, {player.name}, that monster kidnapped your sister. ') 
        slowtype('You must find her!') 
        input('Press [Enter] to continue') 
        print('\n'*30)
        slowtype('Alas a zombie has appeared!')
                    
        print(attacksequence.aseq(player, zombie, classtoname)) 
        mile = '2'
    if mile == '2': 
        c = lor()
        if c == 'l': 
            slowtype('You turn left and face a door.')
            slowtype('Enscribed upon the door is a message')
            slowtype('Speak the answer to me.') 
            rr = riddleq('I have a bed but I do not sleep, I run but cannot walk \n I have a bank but there is no money in it \n What am I?', 'A river')
            if rr == 1: 
                add_item(player, health_potion)
                keys += 1
                print("You gain a peice of the key to open the gates of Valkor's dungeon")
            else: 
                c = 'r'
        elif c == 'r': 
            slowtype('You turn the corner and a skeleton faces you')
            attacksequence.aseq(player, skeleton, classtoname)
            keys += 1
            print("You gain a peice of the key to open the gates of Valkor's dungeon")
        

        

            

