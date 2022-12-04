# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ronge(s):
    a,b=s.split('-')
    return int(a),int(b)

count = 0
for line in iter(input,''):
    x,y = map(ronge,line.split(','))
    if (x[0]>=y[0] and x[1]<=y[1]) or (x[0]<=y[0] and x[1]>=y[1]):
        count += 1

print(count)