import time 
import random 
import attacksequence 
import sys 
import os

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
        self.ac = 13  
        self.name = '' 
    def hupdate(self): 
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
        weapondn = weapono.name
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


 


