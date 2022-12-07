# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

dirs = {}
current = ['/']

for line in slorp():
    if not line: pass
    if tuple(current) not in dirs:
        dirs[tuple(current)] = set()
    x = dirs[tuple(current)]
    if line.startswith('$ cd'):
        t = line[5:]
        if t == '/':
            current = [t]
        elif t == '..':
            current.pop()
        else:
            current.append(t)
    elif line.startswith('$ ls'):
        pass # lmao
    elif line.startswith('dir '):
        t = line[4:]
        x.add(t)
    else:
        s, n = line.split()
        x.add((int(s), n))

sizes = {}

def measure(dir):
    if dir in sizes:
        return sizes[dir]
    size = 0
    for e in dirs[dir]:
        if type(e) is str:
            size += measure((*dir, e))
        else:
            size += e[0]
    sizes[dir] = size
    return size

used = measure(('/',))
unused = 70000000 - used

print(min(sizes[dir] for dir in sizes if sizes[dir] + unused >= 30000000))