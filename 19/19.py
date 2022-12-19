# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re
from functools import lru_cache

# so I don't have any more accidentally global internal loop variables...
def main():
    blueprints = {}
    time_limit = 24

    for group in slorp(): # line_groups(slorp()):

        index, opo, opc, opb, cpb, opg, bpg = map(int,re.findall(r'\d+', group))
        costs = (
            (opo, 0, 0, 0),
            (opc, 0, 0, 0),
            (opb, cpb, 0, 0),
            (opg, 0, bpg, 0)
        )

        blueprints[index] = costs

    qsum = 0

    for index, cs in blueprints.items():
        initial_robots = (1, 0, 0, 0)
        initial_resources = (0, 0, 0)

        @lru_cache(None)
        def search(resources, robots, time):
            if time == time_limit - 1:
                return robots[3]
            
            best = 0
            can_build = [0,0,0,0]
            for i, c in enumerate(cs):
                if all(x>=y for x,y in zip(resources, c)):
                    can_build[i] = 1
                    new_resources = tuple(x-y+z for x,y,z in zip(resources, c, robots))
                    new_robots = robots[:i] + (robots[i] + 1,) + robots[i+1:]
                    #print(i,new_robots, robots, time)
                    best = max(best, search(new_resources, new_robots, time+1))

            if not all(can_build) or any(c>r for c,r in zip(can_build, robots)):
                new_resources = tuple(x+z for x,z in zip(resources, robots))
                best = max(best, search(new_resources, robots, time+1))

            best += robots[3]
            #print(best)
            return best
        
        result = search(initial_resources, initial_robots, 0)
        print(f'Blueprint {index}: {result}')
        qsum += result * index
    
    print(qsum)



            

if __name__ == '__main__':
    main()
