import time 
import random 
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
class Item: 
    def __init__(self, name, amount): 
        self.amount = amount 
        self.name = name 
health_potion = Item(name='Health Potion', amount = 5) 
stick = Item(name='stick', amount=1)
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
        self.name = ''
class Monster: 
    def __init__(self, type, weapon): 
        #display name 
        self.d_name = mdisplay[type] 
        self.hp = mhp[type] 
        self.mattack = mattack[type]
        #attick minimum of weapon for random
        self.amin = wmin[weapon]  
        #attick maximum of weapon for random
        self.amax = wmax[weapon] 
        self.attack = self.mattack + random.randint(self.amin, self.amax)  
 


