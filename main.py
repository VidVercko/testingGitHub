from math import sqrt
t = {(5, 9), (4, 7), (4, 8), (3, 0), (5, 6), (2, 8), (10, 6), (6, 2), (1, 6), (9, 4), (2, 5), (10, 3), (1, 2), (5, 5), (8, 1), (10, 7), (8, 10), (3, 6), (1, 10), (4, 1), (10, 9), (6, 4), (5, 4), (4, 5), (1, 4), (2, 3), (4, 2), (0, 8), (0, 1), (8, 3), (10, 10), (9, 2), (3, 8), (2, 0), (4, 3), (1, 7), (0, 9), (7, 8)}

#

def razdalja(x0, y0, x1, y1):
    return sqrt(((abs(x0-x1))**2)+(abs(y0-y1)**2))

def bliznja_drevesa(_x, _y, r, drevesa):
    return {(x,y) for x,y in drevesa if razdalja(_x,_y,x,y) <= r and not (x == _x and y == _y)}


def opica(x, y, r, drevesa, s=set()):
    s.add((x,y))
    availableTrees = bliznja_drevesa(x,y,r,drevesa).difference(s)
    if(len(availableTrees) == 0):
        return s
    else:
        for _x, _y in availableTrees:
            s = s.union(opica(_x,_y,r,drevesa,s))
    return s

opica(2, 0, 2, t)