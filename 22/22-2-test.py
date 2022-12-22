# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re

# so I don't have any more accidentally global internal loop variables...
def main():
    m, path = line_groups(line.strip('\n') for line in open('test.txt'))

    for i in range(len(m)):
        m[i] += ' ' * (len(m[0]) - len(m[i]) + 1)

    path = re.findall(r'\d+|[LR]', *path)

    for x,t in enumerate(m[0]):
        if t == '.':
            pos = x + 0j
            break
    
    dir = 0
    
    edgemap = {
        (2,0,3): (0,1,3),
        (2,0,2): (1,1,3),
        (2,0,0): (3,2,0),
        (2,1,0): (3,2,3),
        (2,2,1): (0,1,1),
        (2,2,2): (1,1,1),
        (3,2,1): (0,1,2)
    }
    edgemap = {k:v.pop() for k,v in bidict(edgemap).items()}

    pm = [[*r] for r in m]

    for inst in path:
        if inst == 'L':
            dir -= 1
        elif inst == 'R':
            dir += 1
        else:
            for _ in range(int(inst)):
                new = pos + (1j) ** dir
                newdir = dir
                if new.imag >= len(m) or new.real >= len(m[int(new.imag)]) or zind(new, m) == ' ':
                    xq, xr, yq, yr = *divmod(pos.real, 4), *divmod(pos.imag, 4)
                    #print(xq, xr, yq, yr)
                    xq, yq, newdir = edgemap[(xq, yq, dir)]
                    cr = complex(xr, yr)
                    cr *= (-1j) ** (newdir - dir)
                    xr, yr = cr.real % 4, cr.imag % 4
                    new = complex(xq*4 + (3 - xr), yq*4 + (3-yr))
                    newdir ^= 2
                    #print(xq, yq, new, newdir)
                if zind(new, m) == '#':
                    break
                pos, dir = new, newdir
                pm[int(pos.imag)][int(pos.real)] = '>v<^'[dir]
        
        dir %= 4
        #print(pos, dir, inst)
        #pm[int(pos.imag)][int(pos.real)] = '>v<^'[dir]
        for r in pm:
            print(''.join(r))
        print()
    
    pos += 1+1j

    print(int(pos.imag * 1000 + pos.real * 4 + dir))

                    


if __name__ == '__main__':
    main()
