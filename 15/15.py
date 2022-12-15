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
        if r[0] < new[1] < r[1]:
            new[1] = r[0]
        if r[0] < new[0] < r[1]:
            new[0] = r[1]
        if new[0] >= new[1]:
            return None
    return tuple(new)


# so I don't have any more accidentally global internal loop variables...
def main():
    #empty = set()
    ranges = []
    beacons = set()
    Y = 2000000
    for line in slorp():
        
        sensor, beacon = map(ppp, line.split(': '))
        beacons.add(beacon)
        d = sensor - beacon
        ad = abs(d.imag)+abs(d.real)
        xr = int(ad + 1 - abs(Y - sensor.imag))
        #print(xr)
        # for D in range(int(ad)+1):
        #     dx = D - (Y - sensor.imag)
        #     if dx <= 0:
        #         continue
        #     empty |= {sensor.real + dx + Y * 1j, sensor.real - dx + Y * 1j}

        # for dx in range(xr):
        #     for x in inclusive(sensor.real - dx, sensor.real + dx):
        #         empty.add(complex(x, Y))

        x = int(sensor.real)
        if xr < 0:
            continue
        r = x-xr+1, x+xr
        #print(r,xr)
        r = clip_range(ranges, r)
        #print(r)
        if r:
            ranges.append(r)
        
    empty_total = 0
    for r in ranges:
        empty_total += r[1] - r[0]
        for beacon in beacons:
            if beacon.imag == Y and beacon.real in range(*r):
                empty_total -= 1
    print(empty_total)


if __name__ == '__main__':
    main()
