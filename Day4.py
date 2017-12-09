import itertools as it

def isValid(pair):
    return False if pair[0] == pair[1] else True

def isRearrangeValid(pair):
    if len(pair[0]) == len(pair[1]):
        if all([isValid((pair[0],''.join(reorderd))) for reorderd in it.permutations(pair[1],len(pair[1]))]):
            return True
        else:
            return False
    return True

sum = 0
with open('Day4_input.txt') as file:
    for phrase in file:
        wordlist = phrase.strip('\n').split(' ')
        sum += (1 if all([isValid(pair) for pair in it.permutations(wordlist,2)]) else 0)
print(sum)

sum2 = 0
with open('Day4_input.txt') as file:
    for phrase in file:
        wordlist = phrase.strip('\n').split(' ')
        sum2 += (1 if all([isRearrangeValid(pair) for pair in it.permutations(wordlist,2)]) else 0)
print(sum2)
