# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

gs = line_groups(slorp())

print(sum(sorted(sum(map(int,g)) for g in gs)[-3:]))