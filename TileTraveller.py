#| Daníel Þór Gestsson og Róbert Snær Harðarsson | HR | H2019 | Assignment 8: Tile Traveller | 17/09/19 |
# https://github.com/TheRobertSnow/TileTraveller
position_x = 1
position_y = 3
north = True
east = False
south = False
west = False
running = True

def notValid():
    print("Not a valid direction!")

def direction(direction, position_x, position_y, north, east, south, west, running):    # Function that updates the current position according to given direction
    direction = direction.lower()
    if direction == "n":
        if north == True:
            position_y -= 1
            north, east, south, west, running = options(position_x, position_y, north, east, south, west, running)
        else:
            notValid()
    if direction == "s":
        if south == True:
            position_y += 1
            north, east, south, west, running = options(position_x, position_y, north, east, south, west, running)
        else:
            notValid()
    if direction == "e":
        if east == True:
            position_x += 1
            north, east, south, west, running = options(position_x, position_y, north, east, south, west, running)
        else:
            notValid()
    if direction == "w":
        if west == True:
            position_x -= 1
            north, east, south, west, running = options(position_x, position_y, north, east, south, west, running)
        else:
            notValid()
    return position_x, position_y, north, east, south, west, running    # return updated values to global variables

def options(position_x, position_y, north, east, south, west, running): # Function that prints valid directions in relation to current position
    if position_x == 1 and position_y == 3:
        print("You can travel: (N)orth.")
        north = True
        east = False
        south = False
        west = False
    elif position_x == 1 and position_y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        north = True
        east = True
        south = True
        west = False
    elif position_x == 1 and position_y == 1:
        print("You can travel: (E)ast or (S)outh.")
        north = False
        east = True
        south = True
        west = False
    elif position_x == 2 and position_y == 3:
        print("You can travel: (N)orth.")
        north = True
        east = False
        south = False
        west = False
    elif position_x == 2 and position_y == 2:
        print("You can travel: (S)outh or (W)est.")
        north = False
        east = False
        south = True
        west = True
    elif position_x == 2 and position_y == 1:
        print("You can travel: (E)ast or (W)est.")
        north = False
        east = True
        south = False
        west = True
    elif position_x == 3 and position_y == 3:
        print("Victory!")
        running = False
        return north, south, east, west, running
    elif position_x == 3 and position_y == 2:
        print("You can travel: (N)orth or (S)outh.")
        north = True
        east = False
        south = True
        west = False
    elif position_x == 3 and position_y == 1:
        print("You can travel: (S)outh or (W)est.")
        north = False
        east = False
        south = True
        west = True
    return north, east, south, west, running

print("You can travel: (N)orth.")
while running:
        directionInput = input("Direction: ")
        #--- send global variables to function and receve global variables for updated position and direction availability.
        position_x, position_y, north, east, south, west, running = direction(directionInput, position_x, position_y, north, east, south, west, running)
