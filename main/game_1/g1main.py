import time 
import random 
import attacksequence 
import sys  
def pick_loot(pool): 
    listofi = pool.split(',') 
    a = len(listofi) - 1 
    index = random.randint(0, a)
    return listofi[index]  
def makeinv(list): 
    printing = ''
    for item in list: 
        printing += f'[{item}]' 
    return printing    
wmax = {'stick' : 3 ,'na' : 0} 
wmin = {'stick' : 1, 'na' : 0 }
# monster hp dict
mhp = {'zombie' : 5} 
#monster attack points dict 
mattack = {'zombie' : 2} 
#monster display name 
mdisplay = {'zombie' : 'Zombie'}
mloot = {'zombie' : "health_potion"} 
mac = {'zombie' : 2}
class Item: 
    def __init__(self, name, amount, cons, heal): 
        self.amount = amount 
        self.name = name  
        self.consumable = cons 
        self.heal = heal
health_potion = Item(name='Health Potion', amount = 5, cons=True, heal=10) 
stick = Item(name='stick', amount=1, cons=False, heal=0) 
classtoname = {'health_potion': health_potion, 'stick' : stick}
class Player: 
    def __init__(self): 
        self.maxhp = 20 
        self.hp = 20 
        self.weapon = 'stick' 
        self.inventory = [f'{stick.name}-{stick.amount}', f'', f'', f'', f'', f'', f''] 
        #attick minimum of weapon for random 
        self.amin = wmin[self.weapon]  
        #attick maximum of weapon for random
        self.amax = wmax[self.weapon] 
        #minimum damage is 3 with no weapon
        self.attack = 3 + random.randint(self.amin, self.amax) 
        self.d_inventory = f'Inventory: \n{makeinv(self.inventory)}' 
        self.ac = 15  
        self.name = ''
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


 


