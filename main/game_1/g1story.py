import time 
import random 
import attacksequence 
import sys 
import g1main 
def run():
    while True: 
        print('Start Game [S] /nExit Game [E]') 
        schoice = input('Choice: ').lower() 
        dead = False 
        if schoice == 's': 
            zombie = Monster('zombie', 'na')  
            player = Player() 

            while True: 
                print('Hello Adventurer What is your name?') 
                player.name = input("Name: ") 
                print('You find yourself in a musty dungeon with moss covered walls.') 
                print(f'You remeber now, {player.name}, that monster kidnapped your sister. ') 
                print('You must find her!') 
                input('Press [Enter] to continue') 
                print('\n'*30)
                print('Alas a zombie has appeared!')
                attacksequence.aseq(player, zombie) 

        if dead == True: 
            break  
                

        if schoice == "e": 
            sys.exit() 

run()