# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    points = set(    )
    for line in slorp():
        points.add(tuple(map(int,line.split(','))))
    
    faces = 0
    for x,y,z in points:
        faces += len({
            (x+1,y,z),
            (x-1,y,z),
            (x,y+1,z),
            (x,y-1,z),
            (x,y,z+1),
            (x,y,z-1)
        } - points)
    
    print(faces)

if __name__ == '__main__':
    main()
