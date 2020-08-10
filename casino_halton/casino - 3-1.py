from fractions import Fraction
x = int(input())
final = []

def get_average(roulette, path):
    average = Fraction(0, 1)
    for i in range(len(roulette)):
        level_sum = Fraction(0, 1)
        for k in range(i + 1):
            level_sum += Fraction(roulette[i][k] * path[i][k], 1)
        level_sum /= 2 ** i
        average += level_sum
    return average

# Треугольник Паскаля
def rebuild_path(prev_path, prev_height, cur_height):
    for i in range(prev_height, cur_height):
        path.append([])
        for k in range(i + 1):
            if k == 0:
                path[i].append(path[i - 1][0])
            elif k == i:
                path[i].append(path[i - 1][-1])
            else:
                path[i].append(path[i - 1][k] + path[i - 1][k - 1])
    return path
                

path = [[1]]
max_height = 1
for _ in range(x):
    height = int(input())
    if height > max_height:
        path = rebuild_path(path, max_height, height)
        max_height = height
    roulette = []
    for i in range(height):
        roulette.append(list(map(int, input().split())))
    final.append(get_average(roulette, path))
for i in range(x):
    print(final[i].numerator, final[i].denominator)
