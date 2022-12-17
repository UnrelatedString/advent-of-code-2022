# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    shapes = [
        (0, 1, 2, 3),

        (1+2j,
        1j, 1+1j, 2+1j,
        1),

        (2+2j,
        2+1j,
        0, 1, 2),

        (0, 1j, 2j, 3j),

        (1j, 1+1j,
        0, 1)
    ]

    pattern = open('input.txt').readline().strip()

    again, originally, shape, gust = simulate(itr.cycle(enumerate(shapes)),
                                              itr.cycle(enumerate(pattern)))
    #print(again, originally, shape, gust)
    
    cycle_length = again[0] - originally[0]
    cycle_value = again[1] - originally[1]

    abridge = 1000000000000 - originally[0]
    cycles, excess = divmod(abridge, cycle_length)

    ret = cycle_value * cycles # + originally[1]

    ret += simulate(itr.islice(itr.cycle(enumerate(shapes)), shape, None),
                    itr.islice(itr.cycle(enumerate(pattern)), gust, None),
                    originally[0] + excess)
    
    print(ret - 1)



def simulate(shapes, gusts, limit = None):
    rocks = 0
    seen = {}
    grid = set()
    while True:
        top = int(max(p.imag for p in grid) if grid else 0)

        if rocks == limit:
            return top

        i, shape = next(shapes)
        height = top
        height += 4
        #height += max(p.imag for p in shape)

        pos = complex(2, height)

        def check_collision(offset):
            for p in shape:
                z = p + offset + pos
                if z in grid or z.real < 0 or z.real > 6 or z.imag <= 0:
                    return True
            return False

        while True:
            j, gust = next(gusts)

            if pos == complex(2, height):
                if (i,j) in seen:
                    return (rocks, top), seen[(i,j)], i, j
                seen[(i,j)] = rocks, top

            gust = (-1) ** (gust == '<')
            if not check_collision(gust):
                pos += gust
            if check_collision(-1j):
                break
            pos -= 1j
        
        grid |= {p + pos for p in shape}
        rocks += 1



if __name__ == '__main__':
    main()
