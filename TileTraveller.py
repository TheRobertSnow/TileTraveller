position_x = 1
position_y = 3
north = True
south = False
east = False
west = False
running = True

def notValid():
    print("Not a valid direction!")

def direction(direction, position_x, position_y, north, south, east, west, running):
    direction = direction.lower()
    if direction == "n":
        if north == True:
            position_y -= 1
            north, south, east, west, running = options(position_x, position_y, north, south, east, west, running)
        else:
            notValid()
    if direction == "s":
        if south == True:
            position_y += 1
            north, south, east, west, running = options(position_x, position_y, north, south, east, west, running)
        else:
            notValid()
    if direction == "e":
        if east == True:
            position_x += 1
            north, south, east, west, running = options(position_x, position_y, north, south, east, west, running)
        else:
            notValid()
    if direction == "w":
        if west == True:
            position_x -= 1
            north, south, east, west, running = options(position_x, position_y, north, south, east, west, running)
        else:
            notValid()
    return position_x, position_y, north, south, east, west, running

def options(position_x, position_y, north, south, east, west, running):
    if position_x == 1 and position_y == 3:
        north = True
        south = False
        east = False
        west = False
    elif position_x == 1 and position_y == 2:
        north = True
        south = True
        east = True
        west = False
    elif position_x == 1 and position_y == 1:
        north = False
        south = True
        east = True
        west = False
    elif position_x == 2 and position_y == 3:
        north = True
        south = False
        east = False
        west = False
    elif position_x == 2 and position_y == 2:
        north = False
        south = True
        east = False
        west = True
    elif position_x == 2 and position_y == 1:
        north = False
        south = False
        east = True
        west = True
    elif position_x == 3 and position_y == 3:
        print("WINNER")
        running = False
        return north, south, east, west, running
    elif position_x == 3 and position_y == 2:
        north = True
        south = True
        east = False
        west = False
    elif position_x == 3 and position_y == 1:
        north = False
        south = True
        east = False
        west = True
    return north, south, east, west, running
        
while running:
        print("You can travel:", end=" ")
        if north == True:
            print("(N)orth", end=" ")
        if south == True:
            print("(S)outh", end=" ")
        if east == True:
            print("(E)ast", end=" ")
        if west == True:
            print("(W)est", end=" ")
        directionInput = input("Direction: ")
        position_x, position_y, north, south, east, west, running = direction(directionInput, position_x, position_y, north, south, east, west, running)
