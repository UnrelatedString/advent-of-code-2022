ls = [*iter(input,'')]

move = dict(A=1,X=1,B=2,Y=2,C=3,Z=3)

score = 0

for l in ls:
    a,b = (move[c] for c in l.split())
    add = b + 3 * ((b-a+1)%3)
    print(add)
    score += add

print(score)