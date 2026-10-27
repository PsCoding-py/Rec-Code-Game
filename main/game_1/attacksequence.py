import time 
import random 
import threading 
import asyncio 
def slowtype(string): 
    for letter in string:
        print(letter, end="", flush=True)
        time.sleep(0.1) 
    print('') 

     
def remove_num(string): 
    string.replace("0","") 
    string.replace("1","") 
    string.replace("2","") 
    string.replace("3","") 
    string.replace("4","") 
    string.replace("5","") 
    string.replace("6","") 
    string.replace("7","") 
    string.replace("8","") 
    string.replace("9","") 
    string.replace("-","") 
    string.replace(' ','') 
# Attack sequence function 
def add_item(player, item):
    pinv = player.inventory 
    if item.truename in pinv: 
        item.amount += 1 
    elif f'' in pinv: 
        item.amount += 1  
        a = pinv.index(f'') 
        pinv[a] = item.truename 
    else: 
        print('No space in inventory choose an item to swap out or exit.') 
        cforso = input('Swap out [S] or Drop Item [D]').lower()
        if cforso == 's': 
            print(player.d_inventory) 
            try: 
                cas = int(input('Choose a slot: ')) 
                player.inventory[cas] = item.truename 
                item.amount += 1 
            except: 
                print('Enter a valid value (1-7), if you have entered a valid value an error has occured') 
        
locker = threading.Lock()       
def aseq(player, monster, classtoname): 
    turn = 0 
    a=1 
    #main loop 
    done = False 
    md = False  
    while True: 
        global choice, slot 
        #player turn
        while True:  
            slowtype(f'{player.name} vs. {monster.d_name}')
            slowtype(f"{player.name}'s Turn") 
            print(f"{monster.hp}/{monster.maxhp}")
            print(f"{player.hp}/{player.maxhp}") 
            print(f'{player.d_inventory}') 
            print(f'Player has {classtoname[player.weapon].name} equipped as main weapon') 
            print('Change inventory [C] \nAttack [A] \nUse Item [H] \nChange Weapon [W]')  
            choice = input('Choice: ').lower()
            if choice == 'a': 
                aroll = random.randint(1,20) 
                if aroll > monster.mac: 
                    z = player.attack 
                    slowtype(f'You hit the {monster.d_name} and dealt {z} damage') 
                    monster.hp -= z
                elif aroll <= monster.mac: 
                    slowtype(f'You missed the {monster.d_name}') 
            if choice == 'h': 
                while True:  
                    try:
                        print(player.d_inventory) 
                        slot =  int(input('Slot: ')) - 1  
                        item = player.inventory[slot] 
                        print(item)  
                        item = classtoname[item] 
                        if slot <= 6 and slot >= 0: 
                            if item.cons == True:   
                                player.hp += item.heal 
                                item.amount -= 1 
                                print(f'You healed {item.heal} damage.') 
                                player.update() 
                                break 
                            else: 
                                print('This item is not consumeable') 
                         
                    except: 
                        print('Please enter a valid value (1-7), if you have an error has occured') 
            if choice == 'w': 
                print('Choose a Weapon') 
                print(player.d_inventory) 
                try:
                    choslot = int(input('Choose a slot: ')) 
                    pinv = player.inventory 
                    witem = pinv[choslot] 
                    if witem.wep == True: 
                        player.weapon = witem 
                        break 
                    else: 
                        print('That item is not equippable as a weapon')
                     
                except: 
                    print('Please enter a valid slot number (1-7), if you have an error has occured') 
            if choice == 'c':
                print('Change inventory: ') 
                print('Drop Item [D]') 
                print('Move Item Slot [M]') 
                print('Drop All of Item [A]') 
                cchoice = input('Decision: ').lower() 
                if cchoice == 'd': 
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
                if cchoice == 'a': 
                    try: 
                        print(player.d_inventory) 
                        print('Choose a Slot') 
                        cdslot = int(input('Slot: ')) - 1
                        cditem = classtoname[player.inventory[cdslot]]  
                        cditem.amount = 0
                        if cditem.amount == 0: 
                            player.inventory[cdslot] = f'' 
                            player.update()  

                    except:
                        print('Please enter a valid slot number (1-7), if you have entered a valid number an error has occured.') 

                

        #monster turn()
            break 
        if monster.hp <= 0: 
            md = True 
            slowtype(f"You have defeated the {monster.d_name}") 
            slowtype(f"You got a {monster.mloot.name}") 
            loot = monster.mloot 
            add_item(player, loot) 
            player.update() 
            print(player.d_inventory) 
            done != True 
            
            break 
            
        elif player.hp <= 0: 
            slowtype('YOU DIED!') 
            global dead 
            dead = True
            break
        while True: 
            slowtype(f'{monster.d_name} vs. {player.name}')
            slowtype(f"{monster.d_name}'s Turn") 
            print(f"{monster.hp}/{monster.maxhp}")
            print(f"{player.hp}/{player.maxhp}") 
            aroll = random.randint(1,20) 
            if aroll > player.ac: 
                slowtype(f'The {monster.d_name} hit you and dealt {monster.attack} damage') 
                player.hp -= monster.attack
            elif aroll <= player.ac: 
                slowtype(f'The {monster.d_name} missed you') 
            break 
        #check if player or zombie is dead
        if monster.hp <= 0: 
            md = True 
            slowtype(f"You have defeated the {monster.d_name}") 
            slowtype(f"You got a {monster.mloot.name}") 
            loot = monster.mloot 
            add_item(player, loot) 
            player.update() 
            print(player.d_inventory)
             
            break 
            
        elif player.hp <= 0: 
            slowtype('YOU DIED!')  
            dead = True
            break   
        if md == True: 
            break 
    return 'Broken' 
        
        
                    

                             
            
                        
                        
                    


