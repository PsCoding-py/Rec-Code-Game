import os
list = ['stick', f'', ''] 
a=list.index('') 
print(a) 
import time 
def slowtype(string, sec): 
    for letter in string:
        print(letter, end="", flush=True)
        time.sleep(0.3) 
time.sleep(1) 
print('hi') 
slowtype('hi jim', 0.5)
script_dir = os.path.dirname(os.path.abspath(__file__)) 
inv_path = os.path.join(script_dir, 'inventory.txt')
with open(inv_path, 'r') as invf: 
    incont = invf.read() 
    inlist = incont.split(',')