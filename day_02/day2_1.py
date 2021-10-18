import math
from day2_input import intcode


intcode[1] = 12
intcode[2] = 2
n = math.ceil(len(intcode) / 4)


for i in range(n):
    base_i = i*4
    product = 0
    if intcode[base_i] == 99:
        break
    if intcode[base_i] == 1:
        product = intcode[intcode[base_i + 1]] + intcode[intcode[base_i + 2]]
    elif intcode[base_i] == 2:
        product = intcode[intcode[base_i + 1]] * intcode[intcode[base_i + 2]]
    intcode[intcode[base_i + 3]] = product

 
print(intcode)
