# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

head = 0+0j
tail = 0+0j
visited = {tail}

for line in slorp():
    dir, n = line.split()
    dir = dict(U=1,D=-1,R=1j,L=-1j)[dir]
    n = int(n)
    for _ in range(n):
        head += dir
        if abs((head-tail)**2) > 2:
            if (head-tail).imag == 0 or (head-tail).real == 0:
                tail += dir
            else:
                for u in 1+1j,1-1j,-1-1j,-1+1j:
                    if abs(head-tail-u) < abs(head-tail):
                        tail += u
                        break
        visited.add(tail)

print(len(visited))