# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

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

# so I don't have any more accidentally global internal loop variables...
def main():
    gs = line_groups(slorp())
    aaa = 0
    for i,(a,b) in enumerate(gs,start=1):
        if comp(eval(a),eval(b)):
            aaa += i

    print(aaa)

if __name__ == '__main__':
    main()
