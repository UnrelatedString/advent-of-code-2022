# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from functools import lru_cache

from sympy.solvers import solve

from sympy import Symbol

# so I don't have any more accidentally global internal loop variables...
def main():
    monkeys = {}
    for line in slorp():
        m, v = line.split(': ')
        m = m[:4]
        l = v.split()
        if len(l) == 1:
            monkeys[m] = int(*l)
        else:
            monkeys[m] = l
    
    @lru_cache(None)
    def e(m):
        if m == 'humn':
            return 'x'
        v = monkeys[m]
        if type(v) == list:
            a, o, b = v
            if m == 'root':
                o = '-'
            return f'({e(a)} {o} {e(b)})'
        else:
            return v
    
    ex = e('root')
    x = Symbol('x')

    print(solve(eval(ex), x))


if __name__ == '__main__':
    main()
