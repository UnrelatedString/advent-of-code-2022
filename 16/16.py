# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict
import heapq

# so I don't have any more accidentally global internal loop variables...
def main():
    valves = {}
    for line in slorp():
        _, valve, _, _, rate, _, _, _, _, *to = line.split()
        rate = int(rate[5:-1])
        to = ''.join(to).split(',')
        valves[valve] = (rate, to)
    
    worst_case = sum(valves[v][0] for v in valves) * 30
    print(worst_case)
    real = frozenset(v for v in valves if valves[v][0])
    unvisited = {('AA', real, 1)}
    visited = set()
    costs = defaultdict(lambda: worst_case)
    for u in unvisited: costs[u]=0 # maybe
    better = min
    max_time = 1
    # unvisited = 
    # heapq.heapify(unvisited)
    # closed is not open
    while True: # not any(time == 30 for _valve, _closed, time in visited):
        node = better(unvisited, key=lambda n: costs[n])
        valve, closed, time = node
        if time > max_time:
            print(f'Time {time}: least unreleased {costs[node]}')
            max_time = time
        if time == 30:
            print(worst_case - costs[node])
            break
        # cost = sum(valves[v][0] for v in closed) * (30 - time)
        # cost += costs[node]
        # cost = costs[node]
        # cost -= sum(valves[v][0] for v in closed)
        cost = sum(valves[v][0] for v in closed) + costs[node]
        if valve in closed:
            open_this = valve, closed - {valve}, time + 1
            unvisited.add(open_this)
            costs[open_this] = better(costs[open_this], cost)
        for v in valves[valve][1]:
            move = v, closed, time + 1
            for previous in range(time):
                if (v, closed, previous) in visited: # possible pruning strategy?
                    continue
            unvisited.add(move)
            costs[move] = better(costs[move], cost)
        unvisited -= visited # paranoia
        visited.add(node)
    

    # for Time in range(1,31):
    #     for node in visited:
    #         value, closed, time = node
    #         if time == Time:
    #             print(costs[node])

    # for node in sorted(visited, key = lambda n: n[2]):
    #     print(node, costs[node])

    # for node in visited:
    #     value, closed, time = node
    #     if time == 30:
    #         print(worst_case - costs[node])
    
    # # time reversal means wait no that's pointless

    # unvisited = {(valve, frozenset(), 30) for valve in valves}





if __name__ == '__main__':
    main()
