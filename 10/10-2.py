# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ticks(insts):
    reg = 1
    for inst in insts:
        if inst[0] == 'n':
            yield reg
        else:
            n = int(inst.split()[1])
            yield reg
            yield reg
            reg += n
            

# so I don't have any more accidentally global internal loop variables...
def main():
    # h
    yeet = 0
    grid = [[" "]*40 for _ in range(6)]
    for i,s in enumerate(ticks(slorp())):
        y, x = divmod(i%(40*6),40)
        if abs(x-s) <= 1:
            grid[y][x]='#'
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    main()
