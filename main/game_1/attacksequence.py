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
    while True:
        while True: 
            print(f"{player.name}'s Turn") 
            print(f"{player.hp}/{player.maxhp}") 
            print(f'{player.inventory}') 
            print('Change inventory [C] /nAttack [A] /nDrink Health potion [H] /n Change Weapon [W]') 

