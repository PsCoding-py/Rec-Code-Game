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
locker = threading.Lock()
def slowtype(string): 
    for letter in string:
        print(letter, end="", flush=True)
        time.sleep(0.1)
    print('')
         
def player_ticker(player_obj): 
    while True: 
        player_obj.update()  
        time.sleep(0.05)
def story_run(): 
    while True: 
        slowtype('Start Game [S] \nExit Game [E]') 
        schoice = input('Choice: ').lower() 
        dead = False 
        if schoice == 's':
            z = 2
            zombie = Monster('zombie', 'na')  
            player = Player() 
            jim = Monster('jim', 'na') 
            while True: 
                if z == '1':
                    slowtype('Hello Adventurer What is your name?') 
                    player.name = input("Name: ").title() 
                    slowtype('You find yourself in a musty dungeon with moss covered walls.') 
                    slowtype(f'You remeber now, {player.name}, that monster kidnapped your sister. ') 
                    slowtype('You must find her!') 
                    input('Press [Enter] to continue') 
                    print('\n'*30)
                    slowtype('Alas a zombie has appeared!')
                print(attacksequence.aseq(player, zombie, classtoname)) 
                print(attacksequence.aseq(player, jim, classtoname)) 

                player.update()  
        if dead == True: 
            break  
                

        if schoice == "e": 
            sys.exit() 

story_run()