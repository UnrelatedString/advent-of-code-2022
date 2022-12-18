# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from functools import lru_cache

# so I don't have any more accidentally global internal loop variables...
def main():
    points = set(    )
    for line in slorp():
        points.add(tuple(map(int,line.split(','))))
    
    faces = 0
    o = []
    for x,y,z in points:
        neighbors = [
            (x+1,y,z),
            (x-1,y,z),
            (x,y+1,z),
            (x,y-1,z),
            (x,y,z+1),
            (x,y,z-1)
        ]
        o += neighbors
    
    # o.sort()

    # @lru_cache
    # def 

    maxes = [m+2 for m in map(max,zip(*points))]

    surface = {(-1,-1,-1)}
    water = set()
    while surface:
        # layer = {(x, y, z)
        #                 for x in range(-1, max(p[0] for p in points)+2)
        #                 for y in range(-1, max(p[1] for p in points)+2)
        #                 for z in range(-1, max(p[2] for p in points)+2)
        #                 if (x, y, z) not in (points | water) and {
        #                     (x+1,y,z),
        #                     (x-1,y,z),
        #                     (x,y-1,z),
        #                     (x,y+1,z),
        #                     (x,y,z+1),
        #                     (x,y,z-1)} & water}
        newsurface = set()
        for x,y,z in surface:
            if not (
                -1 <= x <= maxes[0] and
                -1 <= y <= maxes[1] and
                -1 <= z <= maxes[2]
            ):
                continue
            newsurface |= {
                (x+1,y,z),
                (x-1,y,z),
                (x,y+1,z),
                (x,y-1,z),
                (x,y,z+1),
                (x,y,z-1)
            } - surface - water - points
        
        water |= surface
        surface = newsurface

    print(sum(1 for n in o if n in water))
    #print(o, water)

if __name__ == '__main__':
    main()
