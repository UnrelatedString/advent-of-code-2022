# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re
from functools import lru_cache
from math import ceil

# so I don't have any more accidentally global internal loop variables...
def main():
    blueprints = {}
    time_limit = 6

    for group in slorp(): # line_groups(slorp()):

        index, opo, opc, opb, cpb, opg, bpg = map(int,re.findall(r'\d+', group))
        blueprints[index] = (
            (opo, 0, 0, 0),
            (opc, 0, 0, 0),
            (opb, cpb, 0, 0),
            (opg, 0, bpg, 0)
        )

        
    qsum = 0

    for index, costs in blueprints.items():
        
        final_geodes = 1
        while True:

            unvisited = {((0, 0, 0, final_geodes)[::-1],
                          (0, 0, 0, 0),
                          1)}
            
            visited = set()

            target = (0, 0, 0, 0), (1, 0, 0, 0), time_limit

            def try_add(new_resources, new_robots, new_time):
                new_state = new_resources, new_robots, new_time

                if new_state == target:
                    unvisited.add(new_state)
                    return

                if new_time >= time_limit:
                    return
                if new_state in visited:
                    return
                
                unvisited.add(new_state)


            while unvisited and target not in visited:
                current = unvisited.pop()
                resources, robots, time = current

                #print(current)

                for i in range(4):
                    if resources[i]:
                        new_resources = tuple_augment(resources, i, lambda x: max(0, x - time - 1))
                        new_robots = tuple_augment(robots, i, lambda x: x+1)
                        try_add(new_resources, new_robots, time + 1)
                    if robots[i]:
                        new_resources = tuple(resource + cost for resource, cost in zip(resources, costs[i]))
                        new_robots = tuple_augment(robots, i, lambda x: x-1)
                        try_add(new_resources, new_robots, time + 1)
                
                try_add(resources, robots, time + 1)
                
                visited.add(current)
            
            #print(visited)

            if target in visited:
                print(final_geodes)
            else:
                break

            final_geodes += 1
        
        qsum += (final_geodes - 1) * index

    
    print(qsum)



            

if __name__ == '__main__':
    main()
