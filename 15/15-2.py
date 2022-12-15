# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ppp(c):
    c = c.split('at ')[1].split(', ')
    c = (int(s[2:]) for s in c)
    return complex(*c)

# half open a la python
def clip_range(ranges, new):
    new = list(new)
    for r in ranges:
        if r[0] <= new[1] < r[1]:
            new[1] = r[0]
        if r[0] <= new[0] < r[1]:
            new[0] = r[1]
        if new[0] >= new[1]:
            return None
    return tuple(new)


# so I don't have any more accidentally global internal loop variables...
def main():
    #empty = set()
    bound = 4000000
    sbs = []
    for line in slorp():
        
        sensor, beacon = map(ppp, line.split(': '))
        sbs.append((sensor, beacon))
    
    for Y in range(bound+1):
        ranges = []
        for sensor, beacon in sbs:
            d = sensor - beacon
            ad = abs(d.imag)+abs(d.real)

            
            xr = int(ad + 1 - abs(Y - sensor.imag))
            x = int(sensor.real)
            if xr < 0:
                continue
            r = x-xr+1, x+xr
            #print(r,xr)
            r = clip_range(ranges, r)
            #print(r)
            if r:
                ranges.append(r)
        
    
        x = 0
        #print(sorted(ranges))
        for r in sorted(ranges):
            if x >= r[1]: continue # how is my merge code this bad
            if x < r[0]:
                print(x * 4000000 + Y, x, Y)
                #0/0
            x = r[1]    


if __name__ == '__main__':
    main()
