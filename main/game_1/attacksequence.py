import time 
import random 
import threading 
import asyncio 
import sys
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright / high-intensity colors
BRIGHT_BLACK = "\033[90m"  # Often appears as gray
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset
RESET = "\033[0m"
colours = {
    # Standard colors
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    
    # Bright / high-intensity colors
    "gray": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    
    # Reset
    "reset": "\033[0m"
}
def slowtype(string, colour=''):
    if colour != '':
        colour = colours[colour]
    else:
        pass
    for letter in string:
        print(colour + letter, end="", flush=True)
        time.sleep(0.1)
    print(colours['reset'])

     
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
            slowtype(f'{player.name} vs. {monster.d_name}', '')
            slowtype(f"{player.name}'s Turn") 
            print(RED + f"{monster.hp}/{monster.maxhp}")
            print(GREEN + f"{player.hp}/{player.maxhp}") 
            print(BLUE + f'{player.d_inventory}') 
            print(RESET + f'Player has {player.weapondn} equipped as main weapon') 
            print('Change inventory [C] \nAttack [A] \nUse Item [H] \nChange Weapon [W]')
            print('Type [E] to exit any menu')  
            choice = input('Choice: ').lower()
            if choice == 'a': 
                aroll = random.randint(1,20) 
                if aroll > monster.mac: 
                    z = player.attack 
                    slowtype(f'You hit the {monster.d_name} and dealt {z} damage', 'red') 
                    monster.hp -= z
                elif aroll <= monster.mac: 
                    slowtype(f'You missed the {monster.d_name}')
                break 
            if choice == 'h': 
                while True:  
                    try:
                        print(player.d_inventory) 
                        slot =  int(input('Slot: ')) - 1  
                        item = player.inventory[slot] 
                        print(item)  
                        item = classtoname[item]
                        if slot == 'esc': 
                            break 
                        if slot <= 6 and slot >= 0: 
                            if item.cons == True:   
                                player.hp += item.heal 
                                item.amount -= 1 
                                print(GREEN + f'You healed {item.heal} damage.') 
                                player.update() 
                                break 
                            else: 
                                print('This item is not consumeable') 
                         
                    except: 
                        print(RED + 'Please enter a valid value (1-7), if you have an error has occured') 
                break
            if choice == 'w':
                 
                print('Choose a Weapon') 
                print(player.d_inventory) 
                try:
                    choslot = int(input('Choose a slot: ')) 
                    pinv = player.inventory 
                    witem = pinv[choslot - 1]
                    witem = classtoname[witem] 
                    if witem.wep == True: 
                        player.weapon = witem
                        player.update() 
                        break 

                    else: 
                        print('That item is not equippable as a weapon')
                     
                except: 
                    print(RED + 'Please enter a valid slot number (1-7), if you have an error has occured') 
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
                        break  

                    except:
                        print(RED + 'Please enter a valid slot number (1-7), if you have entered a valid number an error has occured.') 
                if cchoice == 'a': 
                    try: 
                        print(player.d_inventory) 
                        print('Choose a Slot') 
                        caslot = int(input('Slot: ')) - 1
                        caitem = classtoname[player.inventory[caslot]]  
                        caitem.amount = 0
                        if caitem.amount == 0: 
                            player.inventory[caslot] = f'' 
                            player.update()
                        break  

                    except:
                        print(RED + 'Please enter a valid slot number (1-7), if you have entered a valid number an error has occured.') 
                if cchoice == 'm': 
                    try: 
                        print(player.d_inventory) 
                        print('Choose the Slot of the item you want to move') 
                        cmmove = int(input('Slot: ')) - 1  
                        print('Choose the slot you want to move the item to') 
                        while True: 
                                print(player.d_inventory)  
                                cmtarget = int(input('Slot')) - 1  
                                if player.inventory[cmtarget] == f'': 
                                    break 
                                else: 
                                    print('Enter an Empty Slot')
                        cmitem = classtoname[player.inventory[cmmove]]  
                        player.inventory[cmmove] = f''
                        break 



                    except:
                        print(RED + 'Please enter a valid slot number (1-7), if you have entered a valid number an error has occured.')
            else: 
                print(RED + 'You have entered an invalid ')  

                

        #monster turn() 
        if monster.hp <= 0: 
            md = True 
            slowtype(f"You have defeated the {monster.d_name}", 'green') 
            slowtype(f"You got a {monster.mloot.name}", 'reset') 
            loot = monster.mloot 
            add_item(player, loot) 
            player.update() 
            print(player.d_inventory) 
            done != True 
            
            break 
            
        elif player.hp <= 0: 
            slowtype('YOU DIED!', 'red') 
            global dead 
            dead = True
            sys.exit()
            break
        while True: 
            slowtype(f'{monster.d_name} vs. {player.name}')
            slowtype(f"{monster.d_name}'s Turn", 'red') 
            print(RED + f"{monster.hp}/{monster.maxhp}")
            print(GREEN + f"{player.hp}/{player.maxhp}") 
            aroll = random.randint(1,20) 
            if aroll > player.ac: 
                slowtype(f'The {monster.d_name} hit you and dealt {monster.attack} damage', 'red') 
                player.hp -= monster.attack
            elif aroll <= player.ac: 
                slowtype(f'The {monster.d_name} missed you', 'green') 
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
            slowtype('YOU DIED!', 'red')  
            dead = True
            sys.exit()
            break   
        if md == True: 
            break 
    return '' 
        
        
                    

                             
            
                        
                        
                    


