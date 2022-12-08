# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

trees = list(slorp())

# keeping the name lmao
def uniqcummaxes(rows):
    for row in rows: # why didn't i do this before
        last = {}
        fuck = []
        for i,h in enumerate(row):
            h=int(h)
            if h in last:
                fuck.append(i - last[h])
            else:
                fuck.append(i)
            for x in range(h+1):
                last[x] = i
        yield fuck

def rotate(m):
    return list(zip(*m))[::-1]

dmaxes = list(uniqcummaxes(trees))
umaxes = list(uniqcummaxes(trees[::-1]))[::-1]
lmaxes = rotate(uniqcummaxes(rotate(rotate(rotate(trees)))))
rmaxes = rotate(rotate(rotate(uniqcummaxes(rotate(trees)))))

mscore = 0

for y in range(1,len(trees)-1):
    for x in range(1,len(trees[0])-1):
        score = dmaxes[y][x]*umaxes[y][x]*lmaxes[y][x]*rmaxes[y][x]
        #print(x,y,score, trees[y][x])
        mscore = max(score, mscore)


print(mscore)