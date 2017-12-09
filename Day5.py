import numpy as np

input =  'Day5_input.txt'
x = np.genfromtxt(input,dtype=int)

jumps = 0
i = 0
while i < len(x):
    x[i] += 1
    i += x[i]-1
    jumps += 1

print(jumps)

x = np.genfromtxt(input,dtype=int)
jumps2 = 0
i = 0
while i < len(x):
    offset = (-1 if x[i] >= 3 else 1)
    x[i] += offset
    i += x[i]-offset
    jumps2 += 1

print(jumps2)
