from random import seed
from random import choice
from numpy.random import randn

seed(22052000)

sequence = [4 , 5 , 6 , 7, 8]
values = randn(10)
addon= abs(choice(values))

for i in range(100):
    values = randn(10)
    addon= abs(choice(values))
    selection=choice(sequence) +addon

    #print(selection)



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