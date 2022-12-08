# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

trees = list(slorp())

def uniqcummaxes(rows):
    rows = [*rows]
    maxes = rows[0]
    yield maxes
    for row in rows[1:]:
        x = [max(a,b) if a != b else '/' for a,b in zip(maxes, row)]
        yield x
        maxes = [max(a,b) for a,b in zip(maxes, x)]

def rotate(m):
    return list(zip(*m))[::-1]

dmaxes = list(uniqcummaxes(trees))
umaxes = list(uniqcummaxes(trees[::-1]))[::-1]
lmaxes = rotate(uniqcummaxes(rotate(rotate(rotate(trees)))))
rmaxes = rotate(rotate(rotate(uniqcummaxes(rotate(trees)))))

visible = 0

for y in range(len(trees)):
    for x in range(len(trees[0])):
        if trees[y][x] in (dmaxes[y][x],umaxes[y][x],lmaxes[y][x],rmaxes[y][x],):
            visible += 1
            #if not {x,y} & {0,4}:
            #    print(x, y, trees[y][x])


print(visible)