# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    nums = slorp()
    s = 0
    for num in nums:
        x = 0
        for d in num:
            x *= 5
            x += '=-012'.index(d) - 2
        s += x
    
    print(s)

    normalf = []
    while s:
        q, r = divmod(s, 5)
        normalf.append(r)
        s = q
    
    balanced = ''
    carry = 0
    for d in normalf:
        carry, d = divmod(d + 2 + carry, 5)
        balanced += '=-012'[d]

    print(balanced[::-1])

if __name__ == '__main__':
    main()
