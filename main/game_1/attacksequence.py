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

def aseq(player, monster): 
    turn = 0 
    while True:
        while True:  
            print(f'{player.name} vs. {monster.name}')
            print(f"{player.name}'s Turn") 
            print(f"{player.hp}/{player.maxhp}") 
            print(f'{player.inventory}') 
            print('Change inventory [C] /nAttack [A] /nUse Item [H] /n Change Weapon [W]')  
            choice = input('Choice: ').lower()
            if choice == 'a': 
                aroll = random.randint(1,20) 
                if aroll > monster.ac: 
                    print(f'You hit the {monster.name} and dealt {player.attack} damage') 
                    monster.hp -= player.attack
                if aroll < monster.ac: 
                    print(f'You missed the {monster.name}') 
            if choice == 'h': 
                while True:  
                    try:
                        print(player.d_inventory)
                        slot = int(input('Slot: ')) 
                    except: 
                        print('Please enter a valid intiger')
                    if slot <= 7 and slot >= 0: 
                        player.inventory
                        
                    


