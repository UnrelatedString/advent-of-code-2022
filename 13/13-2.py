# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from functools import cmp_to_key

def comp(a,b):
    if type(a) is not type(b):
        if type(a) is int:
            a = [a]
        if type(b) is int:
            b = [b]
    if type(a) is int:
        if a == b:
            return None
        else:
            return a < b
    else:
        for A,B in zip(a,b):
            c = comp(A,B)
            if c is not None:
                return c
        if len(a) == len(b):
            return None
        else:
            return len(a) < len(b)

def cum(a,b):
    return (-1)**(comp(eval(a),eval(b)))

# so I don't have any more accidentally global internal loop variables...
def main():
    gs = line_groups(slorp())
    lines = ['[[2]]','[[6]]']
    for g in gs:
        lines += g
    
    s = sorted(lines, key=cmp_to_key(cum))
    #for l in s:print(l)
    print((s.index('[[2]]')+1)*(s.index('[[6]]')+1))

if __name__ == '__main__':
    main()
