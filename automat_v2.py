from random import seed
from random import choice
from numpy.random import randn
from time import sleep
from pyautogui import press
from pyautogui import keyDown
from pyautogui import keyUp

import csv

seed(22052000)

sequence = [4 , 5 , 6 , 7, 8]
sequence2 =[0.19,0.2, 0.25, 0.3, 0.5,0.52, 0.55 ,0.68,0.69, 0.72,1.01,1.24,1.48,1.52,1.74,1.88,1.92,2.03]
values = randn(10)
addon= abs(choice(values))


header = ['Nr.','Wygenerowany czas']

time_for_prep = input("How much time you need to get into vendor machine?")
how_much_rolls = input("How much times should i bet?")

print( f"Okay I'll wait {time_for_prep} seconds and then pick {how_much_rolls} items \n")

sleep(int(time_for_prep))

with open('times.csv', 'w', encoding='UTF8', newline='') as f: # if we use with we don’t need to call the close() method to explicitly close the file:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(int(how_much_rolls)):
        
        values = randn(10)
        addon= abs(choice(values))
        selection=choice(sequence) + addon
        # press('up')\
        keyDown('up')

        randoms = randn(10)
        h_delay = abs(choice(randoms))
        key_press_sim =((h_delay*(100-38)+38)/1000)
        sleep(key_press_sim)
        keyUp('up')

        values = randn(10)
        addon= choice(values)
        selection2 = abs(choice(sequence2) + addon)
        sleep(selection2)
        # press('enter')

        keyDown('enter')
        randoms = randn(10)
        h_delay = abs(choice(randoms))
        key_press_sim =((h_delay*(100-38)+38)/1000)
        sleep(key_press_sim)
        keyUp('enter')

        sleep(selection)

        data = [{f'{i+1}', f'{selection}' ,f'{selection2}' }] #didn't work properly
        writer.writerow(data)