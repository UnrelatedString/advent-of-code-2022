# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict
from functools import lru_cache


# so I don't have any more accidentally global internal loop variables...
def main():
    valves = {}
    for line in slorp():
        _, valve, _, _, rate, _, _, _, _, *to = line.split()
        rate = int(rate[5:-1])
        to = ''.join(to).split(',')
        valves[valve] = (rate, to)
    
    ordered_valves = tuple(valves)
    valve_bits = {
            v: 1<<i for i,v in enumerate(ordered_valves) if valves[v][0]
        }

    def unmask(open_mask):
        for valve in ordered_valves:
            if open_mask & 1:
                yield valve
            open_mask >>= 1


    @lru_cache
    def release(open_mask):
        return sum(valves[v][0] for v in unmask(open_mask))

    dists = {}
    for valve in valves:
        hence = defaultdict(lambda: float('inf'), {valve: 0})
        unvisited = {valve}
        visited = set()
        for other in dists:
            hence[other] = dists[other][valve]
            unvisited.add(other)
        
        while unvisited:
            current = min(unvisited, key = lambda node: hence[node])
            unvisited.remove(current)
            for v in valves[current][1]:
                if v not in visited:
                    unvisited.add(v)
                    hence[v] = min(hence[v], hence[current] + 1)
            visited.add(current)
        
        dists[valve] = hence
    
    #print('distances computed')

    def distance_to(a, b):
        return dists[a][b]

    @lru_cache(1000)
    def distance_to_any_closed(current, open_mask):
        if open_mask == 2**len(ordered_valves) - 1:
            return float('inf')
        
        #print(open_mask, 2**len(ordered_valves) - 1)
        
        return min(
            distance_to(current, destination) for destination in unmask(~open_mask)
        )
        



    @lru_cache(1000)
    def search(valve, opened, time):
        released = release(opened)
        if time == 30:
            return released
        
        further = released * (30 - time) # default value just waiting in place

        if valve in valve_bits and not valve_bits[valve] & opened:
            open_this = search(valve, valve_bits[valve] | opened, time + 1)
            further = max(further, open_this)
        for v in valves[valve][1]:
            if distance_to_any_closed(v, opened) < (29 - time):
                move = search(v, opened, time + 1)
                further = max(further, move)

        #print(valve, opened, time, further + released)
        return further + released


    print(search('AA', 0, 1))






if __name__ == '__main__':
    main()
