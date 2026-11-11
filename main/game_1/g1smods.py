
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
from registry import player 
from registry import skeleton 
from registry import zombie
from registry import slowtype
#intro
def mile_1(mile):
    mile = 1 
    if mile == 1:
        slowtype('Hello Adventurer What is your name?') 
        player.name = input("Name: ").title() 
        slowtype('You find yourself in a musty dungeon with moss covered walls.') 
        slowtype(f'You remeber now, {player.name}, that monster kidnapped your sister. ') 
        slowtype('You must find her!') 
        input('Press [Enter] to continue') 
        print('\n'*30)
        slowtype('Alas a zombie has appeared!')
                    
        print(attacksequence.aseq(player, zombie, classtoname)) 
        print(attacksequence.aseq(player, skeleton, classtoname))
        mile = 2
    if mile == 2: 
        print('')
