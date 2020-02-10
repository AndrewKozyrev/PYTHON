from itertools import permutations

sum = 4
#sum = int(input("Enter a sum: "))
q = [1] * sum

def rewrite(arg):
  temp = arg.pop()
  arg[-1] = arg[-1] + temp
  arg.sort(reverse=True)
  return arg

def arrangements(arg):
  temp = list(set(permutations(arg)))
  res = list(map(list, temp))
  res.sort()
  return res

a = []
a += arrangements(rewrite(q))

for element in a:
  temp1 = rewrite(element)
  temp2 = arrangements(temp1)
  a += temp2
  b = list(map(tuple, a))
  b = set(b)
  a = list(b)
  a = list(map(list, a))
  print(a)