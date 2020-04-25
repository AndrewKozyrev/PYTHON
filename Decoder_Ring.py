import string
parameters = input()
n, w = parameters.split()
n = int(n)
temp_alphabet = string.ascii_uppercase[:28]
alphabet = list(temp_alphabet)
cypher = []
dial2 = []
next_index = (n-1) % (len(alphabet)-1)

while len(alphabet) > 0:
    dial2.append(alphabet[next_index])
    alphabet.pop(next_index)
    if alphabet:
        next_index = (next_index + n) % len(alphabet)-1
first_six_letters = ''.join(dial2[0:6:1])
print(first_six_letters)

alphabet = list(temp_alphabet)
w = list(w)
position_w = [alphabet.index(k) for k in w]

for x in position_w:
    cypher.append(dial2[x])
    front = dial2.pop(0)
    dial2.append(front)
encrypted_word = ''.join(cypher)
print(encrypted_word)