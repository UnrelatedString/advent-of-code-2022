# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re
from functools import lru_cache
from math import ceil

# so I don't have any more accidentally global internal loop variables...
def main():
    blueprints = {}
    time_limit = 26

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

            unvisited = {((0, 0, 0, 0),(0, 0, 0, final_geodes)[::-1],
                          
                          0)}
            
            visited = set()


            def try_add(resources, unfulfillable, time):

                resources, unfulfillable = zip(*(
                    (resource + 1, debt - 1) if debt > 0 else (resource, 0) for resource, debt in zip(resources, unfulfillable)
                ))                

                new_state = resources, unfulfillable, time

                # print(new_state)

                if time > time_limit:
                    return
                if new_state in visited:
                    return
                
                # print(new_state)
                unvisited.add(new_state)


            while unvisited:
                current = unvisited.pop()
                resources, unfulfillable, time = current

                # print(f'From {current}:')

                if time == time_limit:
                    if sum(resources) == resources[0] <= time and unfulfillable == (0,0,0,0):
                        break

                for i in range(4):
                    if resources[i]:
                        clear_debt = max(0, resources[i] - time)
                        fulfillable = min(clear_debt, unfulfillable[i])
                        new_resources = tuple_augment(resources, i, lambda x: clear_debt)
                        new_unfulfillable = tuple_augment(unfulfillable, i, lambda x: x - fulfillable)
                        new_unfulfillable = tuple(resource + cost for resource, cost in zip(new_unfulfillable, costs[i]))
                        
                        try_add(new_resources, new_unfulfillable, time + 1)
                
                try_add(resources, unfulfillable, time + 1)
                
                visited.add(current)
            
            else:
                break
            
            # print(visited)

            print(final_geodes)

            final_geodes += 1
        
        qsum += (final_geodes - 1) * index

    
    print(qsum)



            

if __name__ == '__main__':
    main()
