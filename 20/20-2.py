# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    # indices, shit = zip(*enumerate(map(int,slorp())))
    # for i in range(len(shit)):
    #     j = indices.index(i)
    #     v = shit[j]
    #     k = v + j + 1
    #     k %= len(shit) + 1
    #     if k >= j:
    #         shit = shit[:j] + shit[j+1:k] + (v,) + shit[k:]
    #         indices = indices[:j] + indices[j+1:k] + (i,) + indices[k:]
    #     else:
    #         shit = shit[:k] + (v,) + shit[k:j] + shit[j+1:]
    #         indices = indices[:k] + (i,) + indices[k:j] + indices[j+1:]
    #     print(shit, indices, j, k, v)
    
    # s = 0
    # for x in range(1,4):
    #     x *= 1000
    #     #x -= 1
    #     x %= len(shit)
    #     s += shit[x]
    # print(s)

    key = 811589153

    ll = {}
    zero = None
    for i, v in enumerate(slorp()):
        v = int(v) * key
        ll[i] = [v, i-1, i+1]
        if not v:
            zero = i
    size = i + 1
    ll[size - 1][2] = 0
    ll[0][1] = size - 1

    # key %= size

    def prill():
        return
        current = zero
        for _ in range(size):
            print(ll[current][0], end=', ')
            current = ll[current][2]
        print()

    prill()

    for _ in range(10):
        for i in range(size):
            v, _, _ = ll[i]
            # j = v % size
            j = abs(v)
            N, P = (2, 1)[::v//j if v else 1]
            j %= size - 1
            p, n = ll[i][P], ll[i][N]
            ll[p][N] = n
            ll[n][P] = p

            current = p
            for _ in range(j):
                current = ll[current][N]

            nn = ll[current][N]
            ll[current][N] = i
            ll[i][P] = current
            ll[i][N] = nn
            ll[nn][P] = i

            prill()
    
    s = 0
    current = zero
    for _ in range(3):
        for _ in range(1000):
            current = ll[current][2]
        # print(current, ll[current])
        s += ll[current][0]
    
    print(s)

    

if __name__ == '__main__':
    main()
