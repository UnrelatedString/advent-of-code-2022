# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict as dd
from collections import deque


# so I don't have any more accidentally global internal loop variables...
def main():
    blizzards = dd(lambda: set())
    for y, line in enumerate(slorp()[1:-1]):
        for x, t in enumerate(line[1:-1]):
            if t != '.':
                dir = '>v<^'.index(t)
                blizzards[dir].add(complex(x,y))
    
    goal = complex(x, y+1)
    dims = x+1,y+1
    period = (x + 1) * (y + 1)
    origin = 0-1j

    unvisited = {(origin, period)}

    visited = set()
    dists = dd(lambda: float('inf'), {(origin, period): 0})

    def blizzard_at(z, time):
        if z in (origin, goal):
            return False
        for dir in range(4):
            bs = blizzards[dir]
            shifted = z
            shifted -= (1j)**dir * time
            shifted = complex(shifted.real % dims[0], shifted.imag % dims[1])
            if shifted in bs:
                return True
        return False

    while unvisited:
        node = min(unvisited, key=lambda n:dists[n])
        unvisited.remove(node)

        pos, time = node

        

        if pos == goal:
            print(dists[(pos, time)])
            #print(dists)
            break
            
        time %= period
        #print(node)

        for o in von_neumann + (0,):
            new_pos = pos + o
            if 0 <= new_pos.real <= x and (0 <= new_pos.imag <= y or new_pos in (origin, goal)) \
                and (new_pos, time+1) not in visited and not blizzard_at(new_pos, time + 1):

                unvisited.add((new_pos, time + 1))
                dists[(new_pos, time + 1)] = min(dists[(new_pos, time + 1)], dists[node] + 1)
        
        visited.add(node)
   


if __name__ == '__main__':
    main()
