def get_key(dictionary, value):
    key = (list(dictionary.keys())[list(dictionary.values()).index(value)])
    return key

def rotor1(num=0):
    l_port = [1, 2, 3, 4]
    
    while num > 0:
        ##### rotating a rotor
        temp = l_port.pop(0)
        l_port.append(temp)
        #####
        num -= 1
    
    l = {'A': l_port[0], 'B': l_port[1], 'C': l_port[2], 'D': l_port[3]}     ## mapping letter --> port
    r = ['A', 'B', 'C', 'D']      ## right port
    
    ##### mapping left port ---> right port 
    d = {1: l_port.index(1), 2: (l_port.index(2) + 2) % 4, 3: l_port.index(3) - 1, 4: l_port.index(4) - 1}
    #####
    
    rotor = {'A': r[d[l['A']]], 'B': r[d[l['B']]], 'C': r[d[l['C']]], 'D': r[d[l['D']]]}
    return rotor

def rotor2(num=0):
    l_port = [1, 2, 3, 4]
    
    while num > 0:
        ##### rotating a rotor
        temp = l_port.pop(0)
        l_port.append(temp)
        #####
        num -= 1
    
    l = {'A': l_port[0], 'B': l_port[1], 'C': l_port[2], 'D': l_port[3]}     ## mapping letter --> port
    r = ['A', 'B', 'C', 'D']      ## right port
    
    ##### mapping left port ---> right port 
    d = {1: l_port.index(1), 2: (l_port.index(2) + 1) % 4, 3: l_port.index(3) - 1, 4: l_port.index(4)}
    #####
    
    rotor = {'A': r[d[l['A']]], 'B': r[d[l['B']]], 'C': r[d[l['C']]], 'D': r[d[l['D']]]}    
    return rotor

def reflector():
    reflector = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A'}
    return reflector

def joinRotors(x=0, y=0):
    first = rotor1(x)
    second = rotor2(y)
    r = reflector()
    
    joined = {'A': get_key(first, get_key(second, r[ second[first['A']] ]) ),  \
              'B': get_key(first, get_key(second, r[ second[first['B']] ]) ), \
              'C': get_key(first, get_key(second, r[ second[first['C']] ]) ), \
              'D': get_key(first, get_key(second, r[ second[first['D']] ]) )}
    
    return joined

offset  = int(input())
word    = input()

def driver(word, k):
    y = k // 4
    cypher = []
    for i in range(0, len(word)):
        enigma = joinRotors(i+k, y)
        cypher.append(enigma[word[i]])
        if (i + k + 1) % 4 == 0:
            y += 1
    return ''.join(cypher)

print(driver(word, k=offset))