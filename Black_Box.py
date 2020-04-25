from math import sin, cos, pi, radians, trunc

def genGrid():
  grid = []
  for i in range(10):
    row = []
    for j in range(10):
      row.append(".")
    grid.append(row)
  return grid
grid = genGrid()
def displayGrid(grid):
  for row in grid:
    row_str = ""
    for box in row:
      row_str += " " + box + " "
    print(row_str)

def getCoorFromCom(command):
    if command[0] == "T":
        return 0, int(command[1])-1, 90  #90 deg
    elif command[0] == "B":
        return 9, int(command[1])-1, 270    #270 deg
    elif command[0] == "L":
        return (int(command[1])-10) * -1, 0, 360  #360 deg
    elif command[0] == "R":
        return (int(command[1])-10) * -1, 9, 180  #180 deg

def tryGoOut(grid, x, y, v):
    vector = trunc(sin(radians(v))), trunc(cos(radians(v)))
    next_coor = list(map(sum, zip((x, y),vector)))
    if next_coor[1] < 0:
        return "Exits at L" + str(10-x), grid, next_coor[0], next_coor[1], v
    elif next_coor[1] > 9:
        return "Exits at R" + str(10-x), grid, next_coor[0], next_coor[1], v
    elif next_coor[0] < 0:
        return "Exits at T" + str(y+1), grid, next_coor[0], next_coor[1], v
    elif next_coor[0] > 9:
        return "Exits at B" + str(y+1), grid, next_coor[0], next_coor[1], v
    else:
        return "False", grid, next_coor[0], next_coor[1], v

def tryAbsorb(grid, x, y, param):
    if grid[x][y] == "A":
        if param:
            grid[x][y] = "*"
        return "Absorbed"
    else:
        return "False"

    
def tryDeflect(grid, x, y, v):
    out, grid, a, b, v = tryGoOut(grid, x, y, v)
    if out != "False":
        return "False", grid, x, y, v    
    out1, grid, c, d, v1 = tryGoOut(grid, a, b, v + 90)
    out2, grid, e, f, v2 = tryGoOut(grid, a, b, v - 90)

    if out1 != "False" and out2 != "False":
        return "False", grid, x, y, v
    if out1 == "False":
        out1 = tryAbsorb(grid, c, d, False)
    if out2 == "False":
        out2 = tryAbsorb(grid, e, f, False)
    if out1 == "Absorbed" and out2 == "Absorbed":
        return "Reflected", grid, x, y, v
    elif out1 == "Absorbed":
        return "False", grid, x, y, v - 90
    elif out2 == "Absorbed":
        return "False", grid, x, y, v + 90
    else:
        return "False", grid, x, y, v

def plotTrajectory(grid, x, y, v):
    while True:
        grid[x][y] = "+"
        out, grid, x, y, v = tryGoOut(grid, x, y, v)
        if out != "False":    #if a ray exits the box
            print(out)
            break
        else:       #if a ray stays in the box
            out = tryAbsorb(grid, x, y, True)    #check absorb conditions
            if out == "Absorbed":
                break
            out, grid, x, y, v = tryDeflect(grid, x, y, v)   #check deflection condition
            if out == "Reflected":
                grid[x][y] = "+"
                break            
            grid[x][y] = "+"
    displayGrid(grid)
    print(out)
    return grid, out


def xg(x):
    return x -1

def yg(y):
    return 10 - y

while True:
    for i in range(5):
        xord = xg(int(input("X: ")))
        yord = yg(int(input("Y: ")))
        grid[yord][xord] = "A"
    displayGrid(grid)
    command = input("Command: ")
    if command == "X0":
        break
    x, y, v = getCoorFromCom(command)
    grid, output = plotTrajectory(grid, x, y, v)
