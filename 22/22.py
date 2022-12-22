# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re

# so I don't have any more accidentally global internal loop variables...
def main():
    m, path = line_groups(line.strip('\n') for line in open('input.txt'))

    for i in range(len(m)):
        m[i] += ' ' * (len(m[0]) - len(m[i]) + 1)

    path = re.findall(r'\d+|[LR]', *path)

    for x,t in enumerate(m[0]):
        if t == '.':
            pos = x + 0j
            break
    
    dir = 0
    
    for inst in path:
        if inst == 'L':
            dir -= 1
        elif inst == 'R':
            dir += 1
        else:
            for _ in range(int(inst)):
                new = pos + (1j) ** dir
                new = complex(new.real % len(m[int(new.imag % len(m))]), new.imag % len(m))
                while zind(new, m) == ' ':
                    new += (1j) ** dir
                    new = complex(new.real % len(m[int(new.imag % len(m))]), new.imag % len(m))
                if zind(new, m) == '#':
                    break
                pos = new
        
        dir %= 4
        print(pos, dir, inst)
    
    pos += 1+1j

    print(int(pos.imag * 1000 + pos.real * 4 + dir))

                    


if __name__ == '__main__':
    main()
