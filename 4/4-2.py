# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ronge(s):
    a,b=s.split('-')
    return range(int(a),1+int(b))

count = 0
for line in iter(input,''):
    x,y = map(ronge,line.split(','))
    if set(x) & set(y):
        count += 1

print(count)