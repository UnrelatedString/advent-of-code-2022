# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    shapes = itr.cycle([
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
    ])

    pattern = open(0).readline().strip()
    #print(len(pattern))
    gusts = itr.cycle(pattern)
    grid = set()

    for _ in range(2022):
        shape = next(shapes)
        height = max(p.imag for p in grid) if grid else 0
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
            gust = (-1) ** (next(gusts) == '<')
            if not check_collision(gust):
                pos += gust
            if check_collision(-1j):
                break
            pos -= 1j
        
        grid |= {p + pos for p in shape}
        
       # print(grid)
    print(int(max(p.imag for p in grid)))
    



if __name__ == '__main__':
    main()
