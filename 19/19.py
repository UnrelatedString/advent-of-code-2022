# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re
from functools import lru_cache
from math import ceil

# so I don't have any more accidentally global internal loop variables...
def main():
    blueprints = {}
    time_limit = 24

    for group in slorp(): # line_groups(slorp()):

        index, opo, opc, opb, cpb, opg, bpg = map(int,re.findall(r'\d+', group))
        blueprints[index] = (
            (opo, 0, 0, 0),
            (opc, 0, 0, 0),
            (opb, cpb, 0, 0),
            (opg, 0, bpg, 0)
        )

        
    qsum = 0

    for index, cs in blueprints.items():
        initial_robots = (1, 0, 0, 0)
        initial_resources = (0, 0, 0)

        global_best = 0
        global_best_robots = [tuple(map(max,zip(*cs)))]

        @lru_cache(None)
        def search(resources, robots, time):
            def _search(geodes):
                
                #geodes += robots[3]

                if time >= time_limit - 1:
                    best = robots[3]
                    nonlocal global_best_robots, global_best
                    if geodes > global_best:
                        #global_best_robots = [tuple(map(max,zip(*cs)))]
                        global_best = geodes
                        print(geodes, robots)
                    if geodes >= global_best:
                        #print(geodes, robots)
                        global_best_robots.append(robots[:3] + (float('inf'),))
                    return best
                
                if any(all(r>m for r,m in zip(robots, gb)) for gb in global_best_robots):
                    return 0

                cumulative_resources = tuple(
                    
                )

                best = robots[3] * (time_limit - time)
                to_build = [float('inf') for _ in range(4)]

                max_spendable = tuple(max(cost[i] for cost in cs) * (time_limit - time) for i, resource in enumerate(resources))

                for i, c in [*enumerate(cs)][::-1]:
                    wait = max(
                        ceil((cost - resource) / robot) if robot else (cost and float('inf'))
                        for resource, cost, robot in zip(resources, c, robots)
                    ) + 1
                    wait = max(wait, 1)
                    if wait + time < time_limit:
                        to_build[i] = wait
                        new_resources = tuple(min(m, x-y+(z * wait)) for x,y,z,m in zip(resources, c, robots, max_spendable))
                        new_robots = robots[:i] + (robots[i] + 1,) + robots[i+1:]
                        #print(i,new_robots, robots, time)
                        value = search(new_resources, new_robots, time+wait)(geodes+robots[3]*wait)
                        value += robots[3] * wait
                        best = max(best, value)
                    # else:
                    #     print(wait, i, c, robots, time)
                    

                if min(to_build) == float('inf'):
                    # print('fuck', robots, time)
                    value = search(None, robots, time_limit-1)(geodes + best)
                #print(best)
                return best
            return _search
        
        result = search(initial_resources, initial_robots, 0)(0)
        del search # who fucking knows
        print(f'Blueprint {index}: {result}')
        qsum += result * index
    
    print(qsum)



            

if __name__ == '__main__':
    main()
