position_x = 1
position_y = 1

def relocate(position_x, position_y):     
    for i in range(1, 4):
        for j in range(1, 4):
            if position_x == i and position_y == j:
                print("þú ert hér")
            else:     
                print(j, end=",")
                print(i, end=" ")
        print()  
def direction(direction):
    direction = direction.lower()
    if direction == "n":
        position_y += 1
    if direction == "w":
        postion_x -= 1
    if direction == "e":
        postion_x += 1
    if direction == "s":
        position_y -= 1
        
position = input("n,w,e,s: ")
relocate(position)