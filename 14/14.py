# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    rock = set()
    for path in slorp():
        points = [eval(point) for point in path.split(' -> ')]
        rock |= set(points)
        for a, b in zip(points, points[1:]):
            for x in range(*sorted([a[0],b[0]+1])):
                for y in range(*sorted([a[1],b[1]+1])):
                    rock.add((x,y))
    
    abyss = max(p[1] for p in rock)
    origin = (500,0)
    sand = set()
    while True:
        x, y = origin
        o = rock | sand
        while y <= abyss+1:
            print(x,y)
            if (x, y+1) not in o:
                y += 1
            elif (x-1, y+1) not in o:
                y += 1
                x -= 1
            elif (x+1, y+1) not in o:
                y += 1
                x += 1
            else:
                sand.add((x,y))
                break
        else:
            break
    print(len(sand))



if __name__ == '__main__':
    main()
