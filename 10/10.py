# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def ticks(insts):
    reg = 1
    for inst in insts:
        if inst[0] == 'n':
            yield reg
        else:
            n = int(inst.split()[1])
            yield reg
            yield reg
            reg += n
            

# so I don't have any more accidentally global internal loop variables...
def main():
    # h
    yeet = 0 
    vs = list(ticks(slorp()))
    for i in range(6):
        j=19+(40*i)
        yeet += vs[j]*(j+1)
        #print(vs[j]*j)
    print(yeet)

if __name__ == '__main__':
    main()
