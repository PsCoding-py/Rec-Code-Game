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
    string.replace(' ','') 

def aseq(player, monster): 
    turn = 0  
    while True:
        while True:  
            print(f'{player.name} vs. {monster.d_name}')
            print(f"{player.name}'s Turn") 
            print(f"{monster.hp}/{monster.maxhp}")
            print(f"{player.hp}/{player.maxhp}") 
            print(f'{player.inventory}') 
            print('Change inventory [C] \nAttack [A] \nUse Item [H] \nChange Weapon [W]')  
            choice = input('Choice: ').lower()
            if choice == 'a': 
                aroll = random.randint(1,20) 
                if aroll > monster.mac: 
                    print(f'You hit the {monster.d_name} and dealt {player.attack} damage') 
                    monster.hp -= player.attack
                elif aroll < monster.mac: 
                    print(f'You missed the {monster.d_name}') 
            if choice == 'h': 
                while True:  
                    try:
                        print(player.d_inventory)
                        slot = int(input('Slot: ')) - 1  
                        item = player.inventory[slot] 
                        item = remove_num(item) 
                        item = classtoname[item] 
                    except: 
                        print('Please enter a valid intiger')
                    
                    if slot <= 6 and slot >= 0: 
                        if item.cons == True:   
                            player.hp += item.heal 
                            item.amount -= 1 
                    else: 
                        print('Please enter a value from 1-7') 
            break 
        while True: 
            print(f'{player.name} vs. {monster.d_name}')
            print(f"{player.name}'s Turn") 
            print(f"{monster.hp}/{monster.maxhp}")
            print(f"{player.hp}/{player.maxhp}") 
            aroll = random.randint(1,20) 
            if aroll > player.ac: 
                print(f'The {monster.d_name} hit you and dealt {monster.attack} damage') 
                player.hp -= monster.attack
            elif aroll < player.ac: 
                print(f'The {monster.d_name} missed you') 
            break
        if monster.hp <= 0: 
            print(f"You have defeated the {monster.d_name}") 
            print(f"You got a {monster.mloot.name}") 
            loot = monster.mloot 
            if monster.mloot.name in player.inventory:
                loot = monster.mloot 
                loot.amount += 1  
            else: 
                if f'' in player.inventory: 
                    ind = player.inventory.index(f'') 
                    player.inventory[ind] = loot.name + '-' + str(loot.amount) 
            break
        elif player.hp <= 0: 
            print('YOU DIED!') 
            global dead 
            dead = True
            break
                    

                             
            
                        
                        
                    


