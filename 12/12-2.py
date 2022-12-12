# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def zind(z,g):
    return g[int(z.imag)][int(z.real)]

def zin(z,g):
    return z.real >= 0 and z.imag >= 0 and z.real < len(g[0]) and z.imag < len(g)

def dco(a,b,g):
    if not (zin(a,g) and zin(b,g)): return False
    a=zind(a,g)
    b=zind(b,g)
    da = ord('a' if a == 'S' else a)
    db = ord('z' if b == 'E' else b)
    return db-1<=da

# so I don't have any more accidentally global internal loop variables...
def main():
    grid = slorp()
    unvisited = set()
    for y,row in enumerate(grid):
        for x,v in enumerate(row):
            if v in 'Sa':
                unvisited.add(complex(x, y))
    #unvisited = {4j}
    dists = {z:0 for z in unvisited}
    visited = set()
    e=None
    while e not in visited:
        _,n = min((dists[u],repr(u)) for u in unvisited)
        n=eval(n)
        unvisited.remove(n)
        for z in 1,-1,1j,-1j:
            if dco(n,n+z,grid):
                if n+z not in visited: unvisited.add(n+z)
                if zind(n+z,grid) == 'E': e = n+z
                dists[n+z] = min(dists[n]+1,dists.get(n+z,float('inf')))
        visited.add(n)
        #print(dists,e is not None)
    print(dists[e])
        


if __name__ == '__main__':
    main()
