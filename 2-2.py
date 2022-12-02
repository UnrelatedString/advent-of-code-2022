ls = [*iter(input,'')]

move = dict(A=1,B=2,C=3)
oof = dict(X=2,Y=0,Z=1)

score = 0

despair = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

for l in ls:
    a,b = l.split()
    a,b = move[a], oof[b]
    add = despair[b][a-1] , 3 * ((b+1)%3)
    print(add)
    score += sum(add)

print(score)