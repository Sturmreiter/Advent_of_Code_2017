import math

input = 312051

ring = math.ceil((math.sqrt(input)-1)/2)
rest = input - ((ring-1)*2+1)**2
while rest - 2*ring > 0:
    rest -= 2*ring
if rest <= ring:
    way = 2*ring - rest
else:
    way = rest
print(way)
