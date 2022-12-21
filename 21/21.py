# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from functools import lru_cache


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
        v = monkeys[m]
        if type(v) == list:
            a, o, b = v
            return eval(f'{e(a)} {o} {e(b)}')
        else:
            return v
    
    print(e('root'))


if __name__ == '__main__':
    main()
