from random import seed
from random import choice
from numpy.random import randn
from time import sleep
from pyautogui import press

import csv

seed(22052000)

sequence = [4 , 5 , 6 , 7, 8]
sequence2 =[0.19,0.2, 0.25, 0.3, 0.5,0.52, 0.55 ,0.68,0.69, 0.72,1.01,1.24,1.48,1.52,1.74,1.88,1.92,2.03]
values = randn(10)
addon= abs(choice(values))

#last_times = []

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
        press('up')
        values = randn(10)
        addon= choice(values)
        selection2 = abs(choice(sequence2) + addon)
        sleep(selection2)
        press('enter')
        sleep(selection)
        #last_times.append(selection)
        #print(selection)


        data = [{f'{i+1}', f'{selection}' ,f'{selection2}' }] #didn't work properly
        writer.writerow(data)

#print(last_times)

# # generate random Gaussian values
# from numpy.random import seed
# from numpy.random import randn
# from random import choice
# # seed random number generator
# seed(1)
# # generate some Gaussian values
# values = randn(10)
# print(values)

# select = abs(choice(values))
# print(select)