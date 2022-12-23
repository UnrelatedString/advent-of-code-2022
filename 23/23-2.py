# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict

# so I don't have any more accidentally global internal loop variables...
def main():
    elves = set()
    for y,row in enumerate(slorp()):
        for x, t in enumerate(row):
            if t == '#':
                elves.add(complex(x,y))
    
    dirs = [-1j,1j,-1,1]

    count = 0
    moved = True
    while moved:
        count += 1
        moved = False

        props = defaultdict(lambda:set())
        for e in elves:
            neighbors = {e+o for o in moore} & elves
            if not neighbors:
                continue
            for d in dirs:
                p = 1j if d.imag == 0 else 1
                if not {e+d,e+d+p,e+d-p} & neighbors:
                    props[e+d].add(e)
                    break
        
        for prop in props:
            elf, *q = props[prop]
            if q:
                continue
            elves.remove(elf)
            elves.add(prop)
            moved = True
        
        dirs.append(dirs.pop(0))
    
      #a  print(elves)


    print(count)

if __name__ == '__main__':
    main()
