import numpy as np

input = 'Day2_input.txt'
x = np.genfromtxt(input,dtype=int,filling_values=0)
largest = np.amax(x,axis=1)
smallest = np.amin(x,axis=1)
diff = largest - smallest
sum = np.sum(diff)

print(sum)

sum2 = 0
(rownr,colnr) = x.shape
for row in x:
    dividearray = np.zeros((rownr-1,colnr))
    for i in range(colnr-1):
        dividearray[i,:] = np.roll(row,i+1)
    div = np.divide(dividearray,row)
    intidx = np.equal(np.mod(div,1),0)
    sum2 += div[intidx]

print(sum2)
