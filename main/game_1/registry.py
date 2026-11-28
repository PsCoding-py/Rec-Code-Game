import time 
import random  
import sys
import threading 
import asyncio 
import os

import time 
import random 
import attacksequence 
import sys 
import os  
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
# Functions 
# 
# 
# 
#  
def pick_loot(pool): 
    listofi = pool.split(',') 
    a = len(listofi) - 1 
    index = random.randint(0, a)
    return listofi[index]
   
#Lists
# 
# 
# 
#     
wmax = {'stick' : 3 ,'na' : 1, 'sword' : 5, 'fire_sword' : 10, 'staff' : 5, 'esword' : 10} 
wmin = {'stick' : 1, 'na' : 1, 'sword' : 2, 'fire_sword': 3, 'staff' : 1, 'esword' : 5}
# monster hp dict
mhp = {'zombie' : 5, 'skeleton' : 6, 'valkor' : 16, 'witch' : 20, 'bane_of_yara' : 19, 'valk' : 28, 'guard' : 8} 
#monster attack points dict 
mattack = {'zombie' : 2, 'skeleton' : 2, 'valkor' : 2, 'witch' : 2, 'bane_of_yara' : 4, 'valk' : 6, 'guard' : 2} 
#monster display name 
mdisplay = {'zombie' : 'Zombie', 'skeleton' : 'Skeleton', 'valkor': 'Valkor', 'witch' : 'Evil Witch', 'bane_of_yara' : 'Bane Of Yara - Destroyer of Books', 'valk' : 'Valk the Destroyer', 'guard' : 'Prison Guard'}
mloot = {'zombie' : "health_potion", 'skeleton' : 'sword', 'valkor' : 'shield', 'witch' : 'staff', 'bane_of_yara' : 'fire_sword', 'valk' : 'bread', 'guard' : 'health_potion'} 
mac = {'zombie' : 2, 'skeleton' : 2, 'valkor' : 12, 'witch' : 13, 'bane_of_yara' : 15, 'valk' : 13, 'guard' : 7} 
#Classes
#
#
#
#
class Item: 
    def __init__(self, name, amount, cons, heal, truename, wep): 
        self.amount = amount 
        self.name = name  
        self.cons = cons 
        self.heal = heal 
        self.truename = truename 
        self.wep = wep
class specialAttack: 
    def __init__(self, name, tname, heal, plusattack, cooldown):
        self.cooldown = cooldown 
        self.name = name 
        self.heal = heal 
        self.plusattack = plusattack
        self.truename = tname
        self.cleft = 0
        self.activated = 0
        self.available = True
    def activate(self, turn):
        self.activated = turn
        self.cleft = self.cooldown
        self.available = False
    def turnpassed(self):
        if self.available == False:
            self.cleft -= 1
        elif self.cleft == 0: 
            self.available = True
      

spin = specialAttack(name='Spin', tname='spin', heal=0, plusattack=2, cooldown=2)
jump = specialAttack(name="Jump Smash", tname='jump', heal=0, plusattack = 6, cooldown=5)
overhead = specialAttack(name="Overhead Slice", tname='ohead', heal=0, plusattack=5, cooldown=4)
slice = specialAttack(name='Slice',tname='slice', heal=0, plusattack=1, cooldown=0)
# attack types? jump slice spin and overhead


#Define Items
health_potion = Item(name='Health Potion', amount = 1, cons=True, heal=10, truename='health_potion', wep=False) 
stick = Item(name='Stick', amount=1, cons=False, heal=0, truename='stick', wep=True)
hands = Item(name='hands', amount=1, cons=False, heal=0, truename='na', wep=True)
sword = Item(name='Sword', amount=1, cons=False, heal=0, truename='sword', wep=True)
fire_sword = Item(name='Fire Sword', amount=0, cons=False, heal=0, truename='fire_sword', wep=True) 
shield = Item(name='Shield', amount = 1, cons=False, heal=0, truename='shield', wep=False)
staff = Item(name='Magic Staff', amount=1, cons=False, heal=0, truename='staff', wep=True)
bread = Item(name='Bread', amount = 1, cons=True, heal=1, truename='bread', wep=False)
esword = sword = Item(name='Enchanted Sword', amount=1, cons=False, heal=0, truename='esword', wep=True)
###Important###
# 
# 
##Dictionary of Items##
# 
# 
#  
global classtoname 
classtoname = {'health_potion': health_potion, 'stick' : stick, 'sword': sword, 'na' : hands, 'fire_sword' : fire_sword,'shield' : shield, 'staff' : staff, 'bread' : bread,'esword' : esword}
nametomove = {'spin' : spin, 'jump' : jump, 'ohead' : overhead, 'slice' : slice} 
#Classes Continue 
# 
# 
# 
#
def makeinv(list): 
    printing = ''
    for item in list:
        if item != '': 
            itemo = classtoname[item]
            itemn = itemo.name 
            itema = itemo.amount
            printing += f'[{itemn} - {itema}],' 
        else: 
            printing += f'[ ]' 
    return printing
def movedisp(list): 
    printing = ''
    for move in list: 
        printing = printing + move.name + " - " + str(move.cleft) + ' ,'
    return printing
        
class Player:  
    def __init__(self): 
        self.maxhp = 20 
        self.hp = 20 
        self.weapon = stick
        self.weapondn = self.weapon.name 
        self.weaponn = self.weapon.truename
        self.inventory = u_i[username] 
        #attick minimum of weapon for random 
        self.amin = wmin[self.weaponn]  
        #attick maximum of weapon for random
        self.amax = wmax[self.weaponn] 
        #minimum damage is 3 with no weapon
        self.attack = 3 + random.randint(self.amin, self.amax) 
        self.d_inventory = f'Inventory: \n{makeinv(self.inventory)}' 
        self.ac = 13  
        self.name = ncont
        self.lmoves = [spin, jump, slice, overhead]
        self.dmoves = movedisp(self.lmoves) 
    def hupdate(self):
        self.dmoves = movedisp(self.lmoves) 
        self.weapondn = self.weapon.name
        self.weaponn = self.weapon.truename
        self.amin = wmin[self.weaponn]  
        #attick maximum of weapon for random
        self.amax = wmax[self.weaponn] 
        #minimum damage is 3 with no weapon
        self.attack = 3 + random.randint(self.amin, self.amax)
        inv = self.inventory 
        self.d_inventory = f'Inventory: \n{makeinv(inv)}' 
        for item in self.inventory:
            if item != '':
                obj = classtoname[item]
                itemsl = self.inventory.index(item)
                if obj.amount <= 0:
                    self.inventory[itemsl] = ''
            else: 
                pass 
        if self.hp > self.maxhp: 
            self.hp = self.maxhp
        if self.weapon.amount == 0: 
            self.weapon = hands
        if shield.name in self.inventory: 
            self.ac = 15
            print('SE')
    def update(self): 
        self.hupdate() 
        self.hupdate()
    def save(self, mile):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        u_path = os.path.join(script_dir, 'usernames.txt')
        m_path = os.path.join(script_dir, 'milestones.txt')
        w_path = os.path.join(script_dir, 'pweapon.txt')
        inv_path = os.path.join(script_dir, 'inventory.txt')
        with open(m_path, 'w') as mfile: 
            mfile.write(mile) 
        with open(w_path, 'w') as wfile: 
            wfile.write(self.weapon.truename)
        with open(inv_path, 'w') as invfile:
            writeinv = ','.join(self.inventory)
            invfile.write(writeinv)
        
        return 1


class Monster: 
    def __init__(self, type, weapon): 
        #display name
        weapono = classtoname[weapon]
        self.weapondn = weapono.name
        self.d_name = mdisplay[type] 
        self.maxhp = mhp[type] 
        self.hp = mhp[type] 
        self.mattack = mattack[type]
        #attick minimum of weapon for random
        self.amin = wmin[weapon]  
        #attick maximum of weapon for random
        self.amax = wmax[weapon] 
        self.attack = self.mattack + random.randint(self.amin, self.amax) 
        self.mloot = classtoname[pick_loot(mloot[type])] 
        self.mac = mac[type]  
#
#Objects  
## Player ##
username = 'jim'
player = Player()
player.inventory = u_i[username]
global mile 
mile = u_m[username]
player.name = ncont

## Monsters ##
zombie = Monster('zombie', 'na')
skeleton = Monster('skeleton', 'stick')
valkor = Monster('valkor', 'sword')
witch = Monster('witch', 'staff')
boy = Monster('bane_of_yara', 'fire_sword')
valk = Monster('valk', 'staff')
guard = Monster('guard', 'sword')
#Variables
dead = False
keys = 0


 


         
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
def add_item(player, item):
    pinv = player.inventory 
    if item.truename in pinv: 
        item.amount += 1 
    elif f'' in pinv: 
        item.amount = 1  
        a = pinv.index(f'') 
        pinv[a] = item.truename
    else: 
        don = input('Inventory is Full drop item? [Y] [N]: ').lower()
        if don =='y':
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
def slowtype(string, colour=''):
    if colour != '':
        colour = colours[colour]
    else:
        pass
    for letter in string:
        print(colour + letter, end="", flush=True)
        time.sleep(0.1)
    print(colours['reset'])
def lor(): 
    while True:
        slowtype('Left [L] Or Right [R]')
        _c = input('> ').lower()
        if _c == 'l': 
            return 'l'
        elif _c == 'r': 
            return 'r'
        else: 
            print('Invalid Answer Please enter [L] or [R]')
def riddleq(riddle, answer):
    _a  = 0
    while _a != 3: 
        slowtype(riddle)
        _ans = input('What is the answer: ').lower()
        if answer.lower() == _ans: 
            return 1
        else: 
            print('Wrong')
            _a += 1 
            print(f'{3-_a} guesses left')
    print('No guesses left')
    return 0
#Objects And Variables






