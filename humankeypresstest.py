from numpy.random import randn
from time import sleep

from random import seed
from random import choice

seed(22052000)


for i in range(10):
    
    randoms = randn(10)
    h_delay = abs(choice(randoms))
    key_press_sim =((h_delay*(100-38)+38)/1000)
    print(key_press_sim)
    