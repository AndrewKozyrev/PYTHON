from itertools import permutations
from copy import deepcopy

sum = int(input("Enter a sum: "))
n = int(input("Arrangement page: "))
q = [1] * sum

def rewrite(arg):
    c = deepcopy(arg)
    temp = c.pop()
    c[-1] = c[-1] + temp
    return c

def arrangements(arg):
    temp = list(set(permutations(arg)))
    res = list(map(list, temp))
    res.sort()
    return res

def leaveUnique(**kwargs):
    a = kwargs["total"]
    if len(kwargs) > 1:
        b = kwargs["new"]
        a.append(b)
    temp1 = list(map(tuple, a))
    temp2 = set(temp1)
    temp1 = list(temp2)
    temp2 = list(map(list, temp1))
    return temp2

a = [q]


def treeFunc(arg):
    for element in arg:
        if type(element) == list and len(element) > 1:
            if element not in a:
                a.append(element)
            temp1 = rewrite(element)
            temp2 = arrangements(temp1)
            treeFunc(temp2)
        else:
            if element not in a:
                a.append(element) 
            break

treeFunc(a)
a.sort()

for e in a:
    print(' '.join(list(map(str, e))))

print(a[n-1])