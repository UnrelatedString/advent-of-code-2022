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

    @lru_cache(None)
    def search(positions, opened, time, transit):
        released = release(opened)
        if time == 26:
            return released
        
        further = released * (26 - time) # default value just waiting in place

        choiceses = []
        for valve in positions:
            choices = []
            choiceses.append(choices)
            if valve in valve_bits and not valve_bits[valve] & opened:
                open_this = (valve, valve_bits[valve] | opened, time + 1)
                choices.append(open_this)
            for v in unmask(~opened):
                if 0 < dists[valve][v] < (25 - time):
                    move = (v, opened, time + dists[valve][v])
                    choices.append(move)
            if not choices:
                choices.append((valve, opened, 26))
        
        if len(choiceses) == 1:
            assert transit
            for choice in choiceses[0]:
                if choice[2] == transit[0][1]:
                    new_positions = choice[0], transit[0][0]
                    chosen = search(new_positions, *choice[1:], ())
                elif choice[2] > transit[0][1]:
                    chosen = search(transit[0][:1], choice[1], transit[0][1], (choice[::2],))
                else:
                    chosen = search(choice[:1], *choice[1:], transit)
                further = max(further, chosen)
        else:
            assert not transit
            for choice in itr.product(*choiceses):
                if choice[0][2] != choice[1][2]:
                    first, second = sorted(choice, key=lambda c:c[2])
                    second = tuple(second[::2]),
                    first = first[:1], *first[1:]
                    chosen = search(*first, second)
                else:
                    new_positions = tuple(sorted((choice[0][0], choice[1][0])))
                    new_opened = choice[0][1] | choice[1][1]
                    new_time = choice[0][2]
                    chosen = search(new_positions, new_opened, new_time, ())
                further = max(further, chosen)



        #print(valve, opened, time, further + released)
        return further + released


    print(search(('AA', 'AA'), 0, 1, ()))






if __name__ == '__main__':
    main()
