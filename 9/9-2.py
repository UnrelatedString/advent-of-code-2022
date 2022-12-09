# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

head = 0+0j
tails = [0+0j]*9
visited = {0+0j}

def zround(z):
    return complex(round(z.real), round(z.imag))

def update(hhead, tail):
    diff = hhead - tail
    diff = zround(diff)
    if abs(diff**2) > 2 and diff not in (1+1j,1-1j,-1-1j,-1+1j):
        if diff.imag == 0 or diff.real == 0:
            tail += diff/abs(diff)
        else:
            for u in 1+1j,1-1j,-1-1j,-1+1j:
                if abs(diff-u) < abs(diff):
                    tail += u
                    break
    return zround(tail)

for line in slorp():
    dir, n = line.split()
    dir = dict(U=1,D=-1,R=1j,L=-1j)[dir]
    n = int(n)
    for _ in range(n):
        head += dir
        last = head
        for i in range(len(tails)):
            tail = update(last, tails[i])
            tails[i] = tail
            last = tail
        #if tail not in visited:print(tail)
        visited.add(tails[-1])

print(len(visited))