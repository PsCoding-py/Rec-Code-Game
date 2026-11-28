import time 
import random 
import attacksequence 
import sys
import g1smods 
from registry import *  

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
        slowtype('Start Game [S] \nExit Game [E] \nReset Save File [R]') 
        schoice = input('Choice: ').lower() 
        dead = False
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
        # Securely join that directory with your filename
        u_path = os.path.join(script_dir, 'usernames.txt')
        m_path = os.path.join(script_dir, 'milestones.txt')
        w_path = os.path.join(script_dir, 'pweapon.txt')
        n_path = os.path.join(script_dir, 'pnames.txt')
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
        with open(n_path, 'r') as nfile: 
            ncont = nfile.read() 

        u_m = dict(zip(ulist, mlist))
        u_i = dict(zip(ulist, inlist))
        u_w = dict(zip(ulist, wlist))
        if schoice == 's':
            username = 'jim'
            z = 2
            zombie = Monster('zombie', 'na')  
            player.inventory = u_i[username]
            global mile 
            mile = u_m[username] 
            while True:
                player.name = ncont
                g1smods.mile_1(mile)
                break
                 

                player.update()  
        if dead == True: 
            break  
                

        if schoice == "e": 
        
            sys.exit() 
        if schoice == 'r':
            with open(m_path, 'w') as mfile: 
                mfile.write('1')
            with open(w_path, 'w') as wfile: 
                wfile.write('stick')
            with open(inv_path, 'w') as ifile: 
                ifile.write('stick,,,,,,')
            

story_run()