import time 
import random 
import attacksequence 
import sys
import g1smods 
import g1main  
from g1main import Monster 
from g1main import Player 
from g1main import Item  
from g1main import classtoname
import threading 
import asyncio 
import os
import registry
from registry import dead
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
        # Securely join that directory with your filename
        u_path = os.path.join(script_dir, 'usernames.txt')
        m_path = os.path.join(script_dir, 'milestones.txt')
        w_path = os.path.join(script_dir, 'pweapon.txt')
        with open(u_path, 'r') as usernames:
            ucontents = usernames.read()
            ulist = ucontents.split(' ')

        with open(m_path, 'r') as milestones: 
            mcontents = milestones.read()
            mlist = mcontents.split(' ')
        inv_path = os.path.join(script_dir, 'inventory.txt')
        with open(inv_path, 'r') as invf: 
            incont = invf.read()
            invs = incont.split(':')
            inlist = []
            for item in invs:  
                plist = item.split(',')
                inlist.append(plist)
        with open(w_path, 'r') as wepf: 
            wcontents = wepf.read()
            wlist = wcontents.split(' ') 

        u_m = dict(zip(ulist, mlist))
        u_i = dict(zip(ulist, inlist))
        u_w = dict(zip(ulist, wlist))
        print(u_m)
        if schoice == 's':
            username = input('Username: ').lower()

            z = 2
            zombie = Monster('zombie', 'na')  
            player = Player()
            player.inventory = u_i[username] 
            mile = u_m[username] 
            while True:
                g1smods.mile_1(mile)
                break
                 

                player.update()  
        if dead == True: 
            break  
                

        if schoice == "e": 
            sys.exit() 

story_run()