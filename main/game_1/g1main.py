import time 
import random 
import attacksequence 
import sys 

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
wmax = {'stick' : 3 ,'na' : 1, 'sword' : 5} 
wmin = {'stick' : 1, 'na' : 1, 'sword' : 2}
# monster hp dict
mhp = {'zombie' : 5, 'skeleton' : 6} 
#monster attack points dict 
mattack = {'zombie' : 2, 'skeleton' : 2} 
#monster display name 
mdisplay = {'zombie' : 'Zombie', 'skeleton' : 'Skeleton'}
mloot = {'zombie' : "health_potion", 'skeleton' : 'sword'} 
mac = {'zombie' : 2, 'skeleton' : 2} 
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
#Define Items
health_potion = Item(name='Health Potion', amount = 0, cons=True, heal=10, truename='health_potion', wep=False) 
stick = Item(name='Stick', amount=1, cons=False, heal=0, truename='stick', wep=True)
hands = Item(name='hands', amount=0, cons=False, heal=0, truename='na', wep=True)
sword = Item(name='Sword', amount=0, cons=False, heal=0, truename='sword', wep=True) 
###Important###
# 
# 
##Dictionary of Items##
# 
# 
#  
global classtoname 
classtoname = {'health_potion': health_potion, 'stick' : stick, 'sword': sword} 
#Classes Continue 
# 
# 
# 
#
def makeinv(list): 
    printing = ''
    for item in list:
        if item != '': 
            printing += f'[{classtoname[item].name} - {classtoname[item].amount}],' 
        else: 
            printing += f'[ ]' 
    return printing
class Player: 
    def __init__(self): 
        self.maxhp = 20 
        self.hp = 20 
        self.weapon = stick
        self.weapondn = self.weapon.name 
        self.weaponn = self.weapon.truename
        self.inventory = [f'stick', f'', f'', f'', f'', f'', f''] 
        #attick minimum of weapon for random 
        self.amin = wmin[self.weaponn]  
        #attick maximum of weapon for random
        self.amax = wmax[self.weaponn] 
        #minimum damage is 3 with no weapon
        self.attack = 3 + random.randint(self.amin, self.amax) 
        self.d_inventory = f'Inventory: \n{makeinv(self.inventory)}' 
        self.ac = 15  
        self.name = '' 
    def hupdate(self): 
        self.weapondn = self.weapon.name
        self.weaponn = self.weapon.truename
        self.amin = wmin[self.weaponn]  
        #attick maximum of weapon for random
        self.amax = wmax[self.weaponn] 
        #minimum damage is 3 with no weapon
        self.attack = 3 + random.randint(self.amin, self.amax) 
        self.d_inventory = f'Inventory: \n{makeinv(self.inventory)}' 
        self.ac = 15
        for item in self.inventory:
            if item != f'':
                obj = classtoname[item] 
                if obj.amount <= 0: 
                    classtoname[item] = f''
            else: 
                pass 
        if self.hp > self.maxhp: 
            self.hp = self.maxhp
        if self.weapon.amount == 0: 
            self.weapon = hands
    def update(self): 
        self.hupdate() 
        self.hupdate()

class Monster: 
    def __init__(self, type, weapon): 
        #display name 
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


 


