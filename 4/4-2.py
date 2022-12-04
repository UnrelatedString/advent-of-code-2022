# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ronge(s):
    a,b=s
    return range(int(a),1+int(b))

count = 0
for line in slorp():
    x,y = map(ronge,serial_split(line, ',-'))
    if set(x) & set(y):
        count += 1

print(count)