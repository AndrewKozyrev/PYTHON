def get_gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    res = a + b
    return res

def get_average(roul):
    prev_level = cur_level = [roul[0]]
    for i in range(1, len(roul)):
        cur_level = []
        for k in range(i + 1):
            sum_elem = roul[i][k]
            cell = []
            if k == 0:
                cell.append(sum_elem + prev_level[0][0])
            elif k == i:
                cell.append(sum_elem + prev_level[-1][0])
            else:
                for elem in prev_level[k - 1]:
                    cell.append(sum_elem + elem)
                for elem in prev_level[k]:
                    cell.append(sum_elem + elem)
            cur_level.append(cell)
        prev_level = cur_level
    ans = []
    for s in cur_level:
        for elem in s:
            ans.append(elem)
    num = sum(ans)
    den = len(ans)
    gcd = get_gcd(num, den)
    num //= gcd
    den //= gcd
    return (num, den)

#### Ввод входных данных ####################
n = int(input()) # Кол-во наборов входных данных
results = []
for _ in range(n):
    height = int(input()) # Высота рулетки
    roul = [] # Рулетка
    for i in range(height):
        roul.append(list(map(int, input().split()))) # Заполнение очередного уровня
    results.append(get_average(roul))
for i in range(n):
    print(results[i][0], results[i][1])


            
