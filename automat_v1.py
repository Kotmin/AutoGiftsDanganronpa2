from random import seed
from random import choice
from numpy.random import randn
from time import sleep

import csv

seed(22052000)

sequence = [4 , 5 , 6 , 7, 8]
values = randn(10)
addon= abs(choice(values))

#last_times = []

header = ['Nr.','Wygenerowany czas']

time_for_prep = input("How much time you need to get into vendor machine?")
how_much_rolls = input("How much times should i bet?")

print( f"Okay I'll wait {time_for_prep} seconds and then pick {how_much_rolls} \n")

sleep(int(time_for_prep))

with open('times.csv', 'w', encoding='UTF8', newline='') as f: # if we use with we don’t need to call the close() method to explicitly close the file:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(int(how_much_rolls)):
        values = randn(10)
        addon= abs(choice(values))
        selection=choice(sequence) + addon
        #last_times.append(selection)
        #print(selection)

        
        data = [selection]
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