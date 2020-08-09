x = int(input())
def maxSum(arg):
    maxsofar = maxendinghere = 0
    i = 0
    partitions = {}
    for (idx, x) in enumerate(arg):
        maxendinghere = max(maxendinghere + x, 0)
        partitions[maxendinghere] = str(i) + ' ' + str(idx)
        if maxendinghere == 0:
            i = idx + 1
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar, partitions

def anchoredSum(subchain):
    parts = []
    maxsofar = p1 = 0
    for x in subchain:
        p1 = p1 + x
        maxsofar = max(maxsofar, p1)
    parts.append(maxsofar)
    subchain.reverse()
    maxsofar = p2 = 0
    for x in subchain:
        p2 = p2 + x
        maxsofar = max(maxsofar, p2)
    parts.append(maxsofar)
    return max(parts)

def maxScore(arg1, arg2):
    N, black = list(map(int, arg1.split()))
    sectors = list(map(int, arg2.split()))
    chain = []
    if black == -1:
        chain = sectors
    else:
        chain = sectors[black+1::] + sectors[0:black:]
    m1, partitions = maxSum(chain)
    i, j = list(map(int, list(partitions[m1].split())))
    subchain = chain[j+1:] + chain[:i]
    m2 = anchoredSum(subchain)
    return m1 + m2

output = []
for i in range(x):
    temp1 = input()
    temp2 = input()
    reply = maxScore(temp1, temp2)
    output.append(reply)
for line in output:
    print(line)