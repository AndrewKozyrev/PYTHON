triangle = [[1], [1, 1]]

def pascalNumbers(n):
    if n == 2:
        return
    n -= 1
    row = triangle[-1]
    next_row = [1]
    for i in range(1, len(row)):
        next_row.append(row[i-1]+row[i])
    next_row.append(1)
    triangle.append(next_row)
    pascalNumbers(n)

def gcd(a, b):
    c = min(abs(a), abs(b))
    d = max(abs(a), abs(b))
    if c == 0:
        return d
    elif d == 0:
        return c
    else:
        return gcd((d-c), c)

x = int(input())
result = []

for _ in range(x):
    h = int(input())
    roulet = []
    pascalNumbers(h)
    rouletScores = []
    for i in range(h):
        roulet.append(list( map( int, input().split() ) ))
        rouletScores.append(sum([x*y for x,y in zip(triangle[i], roulet[-1])])/sum(triangle[i]))
    (x, y) = ((int( sum(rouletScores)*sum(triangle[-1]) ), sum(triangle[-1])))
    d = gcd(x, y)
    result.append((int(x/d), int(y/d)))

for e in result:
    print(str(e[0]) + " " + str(e[1]))
