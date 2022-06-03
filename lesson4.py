def findCoin(x, y):
    if -1 <= x <= 1:
        if -1 <= y <= 1:
            print('Монетка где-то рядом')
        else:
            print('Монетки в области поиска нет')
    else:
        print('Монетки в области поиска нет')
    print()

while True:
    point_x = float(input('Введите координату X: '))
    point_y = float(input('Введите координату Y: '))
    findCoin(point_x, point_y)