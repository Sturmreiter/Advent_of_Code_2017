import numpy as np

input = ' 5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'

def updateState(state):
    i = np.argmax(state)
    rest = len(state) - i - 1
    todistribute = state[i]
    state[i] = 0
    if todistribute > rest:
        state[i+1:] += np.repeat(1,rest)
        state[:todistribute-rest] += np.repeat(1,todistribute-rest)
    else:
        state[i+1:i+1+todistribute] += np.repeat(1,todistribute)

state = np.fromstring(input,dtype=int,sep='\t')
state = list(state)

alreadySeen = []
redist = 0
while state not in alreadySeen:
    alreadySeen.append(state[:])
    updateState(state)
    redist += 1

print(redist)
print(redist-alreadySeen.index(state))
