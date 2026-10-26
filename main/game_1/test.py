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