def _grid(position):
    for i in range(1, 10):
        if position == i:
            print("o", end='')
        else:
            print("x", end='')
        if i % 3 == 0:
            print()

_grid(3)
