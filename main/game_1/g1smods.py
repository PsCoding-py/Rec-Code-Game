import time 
import random 
import attacksequence 
import sys
import threading 
import asyncio 
import os
from registry import *
import registry

#intro
def mile_1(mile):
    global dead
    global keys
    while True:
        if mile == '1':
            script_dir = os.path.dirname(os.path.abspath(__file__))            
            n_path = os.path.join(script_dir, 'pnames.txt')
             
            slowtype('Hello Adventurer What is your name?') 
            player.name = input("Name: ").title()
            with open(n_path, 'w') as nfile: 
                pnam = player.name
                nfile.write(pnam) 
            slowtype('You find yourself in a musty dungeon with moss covered walls.') 
            slowtype(f'You remember now, {player.name}, that monster kidnapped your sister. ') 
            slowtype('You must find her!') 
            input('Press [Enter] to continue') 
            print('\n'*30)
            slowtype('Alas a zombie has appeared!', 'red')
                        
            print(attacksequence.aseq(player, zombie, classtoname)) 
            mile = '2'
            player.save(mile)
        elif mile == '2':
            t = 0  
            c = lor()
            while t == 0:
                if c == 'l': 
                    slowtype('You turn left and face a door.')
                    slowtype('Inscribed upon the door is a message')
                    slowtype('Speak the answer to me.') 
                    rr = riddleq('I have a bed but I do not sleep, I run but cannot walk \n I have a bank but there is no money in it \n What am I?', 'A river')
                    if rr == 1: 
                        add_item(player, health_potion)
                        player.update()
                        keys += 1
                        slowtype('You found a sword in a chest in the next room!')
                        add_item(player, sword)
                        player.update()
                        slowtype("You gain a piece of the key to open the gates of Valk's dungeon")
                        mile = '3'
                        player.save(mile)
                        t = 1
                    else: 
                        slowtype('You Failed the riddle the door locks.')
                        
                        c = 'r'
                elif c == 'r': 
                    slowtype('You turn the corner and a skeleton faces you')
                    attacksequence.aseq(player, skeleton, classtoname)
                    keys += 1
                    slowtype("You gain a piece of the key to open the gates of Valk's dungeon")
                    mile = '3'
                    player.save(mile)
                    t = 1
                
        elif mile == '3':
             
            slowtype('Upon the door to the next room is a sentence enscribed in blood')
            slowtype("'A terrible power lies beyond here, Valkor. Bewarned!'", 'red')
            slowtype('You slowly open the door')
            slowtype('As you walk into the dungeon, before you lies a horrid sight!')
            slowtype('It is a monster that looks as if it has been cobbled together out of other monster parts')
            slowtype('Its empty eye socket bores into you as if burning through your soul')
            slowtype('Eventually it lets out an almighty scream "Arghhh!", and it charges at you dragging along his sword across the ground')
            attacksequence.aseq(player, valkor, classtoname)
            mile = '4'
            player.save(mile)
        elif mile == '4': 
             
            # writing for riddle 
            # this riddle is placeholder
            rr = riddleq('I have a bed but I do not sleep, I run but cannot walk \n I have a bank but there is no money in it \n What am I?', 'A river')
            if rr == 1:
                # numericl code that says "go left"
                #they find ahealth potion in a chest
                add_item(player, health_potion)
                mile = '5'
                player.save(mile)
            else: 
                slowtype('YOU DIED!', 'red')
                dead = True 
                sys.exit()
        elif mile == '5': 
             
            # Writing for player getting attacked
            attacksequence.aseq(player, witch, classtoname)
            # writing for player winning
            mile = '6'
            player.save(mile)
        elif mile == '6':
             
            # writing for encountering bane of yarra
            attacksequence.aseq(player, boy, classtoname)
            keys = 2 
            # writing for getting key
            mile = '7'
            player.save(mile) 
        elif mile == '7':
              
            # writing for saying yara
            #writing for getting spell to make ac go up 
            player.ac += 17 
            mile == '8'
        elif mile == '8':
             
            # writing for riddle
            # this riddle is a placeholder
            rr = riddleq('I have a bed but I do not sleep, I run but cannot walk \n I have a bank but there is no money in it \n What am I?', 'A river')
            if rr == 1: 
                # writing for getting bread 
                add_item(player, bread)
                mile = '9'
                player.save(mile)
            else: 
                # writing for falling down chute and going back to riddle
                mile = '4'
                player.save(mile)
        elif mile == '9': 
             
            c = lor()
            if c == 'l': 
                mile = '9-1'
                player.save(mile)
            elif c == 'r': 
                mile = '9-2'
                player.save(mile) 
        elif mile == '9-1': 
            # writing for going into room
            c = lor() 
            if c == 'l': 
                mile = '9-1-1'
                player.save(mile)
            if c == 'r': 
                mile = '9-1-2'
                player.save(mile)
        elif mile == '9-1-1': 
            #writing for finding skeleton 
            attacksequence.aseq(player, skeleton, classtoname)
            mile = '9-1-10'
            player.save(mile)
        elif mile == '9-1-2': 
            #writing for finding chest 
            add_item(player, esword)
            mile = '9-1-10'
            player.save(mile)
        elif mile == '9-1-10':
            # writing for player finding hp 
            add_item(player, health_potion)
            mile = '9-2'
            player.save(mile)
        elif mile == '9-2':
            # valk backstory + encounter 
            attacksequence.aseq(player, valk, classtoname)
            # writing for finding final piece of key 
            keys = 3 
            mile = '10'
            player.save(mile)
        elif mile == '10': 
            # writing for finding guard after opening dungeon
            attacksequence.aseq(player, guard, classtoname) 
            # writing for getting final piece of key 
            mile = '11'
            player.save(mile)
            pass
        elif mile == '11': 
            # writing for finding sister 
            sys.exit()
        

        
            
            

        
        