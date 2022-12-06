# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

fuck = input()
for i in range(len(fuck)):
    if len(set(fuck[i:][:4])) == 4:
        print(i+4)
        break