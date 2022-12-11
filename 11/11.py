# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def eee(monkeyshit, old):
    return eval(monkeyshit.split('=')[1])

# so I don't have any more accidentally global internal loop variables...
def main():
    monkeys = []
    for g in line_groups(slorp()):
        monkeys.append(dict(
            items = [*map(int,g[1].split(': ')[1].split(', '))],
            op = g[2].split(': ')[1],
            test = int(g[3].split()[-1]),
            a = int(g[4].split()[-1]),
            b = int(g[5].split()[-1])
        ))
    
    #print(monkeys)
    inspections = [0]*len(monkeys)

    for _ in range(20):
        for i,m in enumerate(monkeys):
            for item in m['items']:
                inspections[i] += 1
                item = eee(m['op'], item)
                item //= 3
                if item % m['test'] == 0:
                    monkeys[m['a']]['items'].append(item)
                else:
                    monkeys[m['b']]['items'].append(item)
            m['items'] = []
    
    o,t,*_ = sorted(inspections)[::-1]
    print(o*t)
        

if __name__ == '__main__':
    main()
