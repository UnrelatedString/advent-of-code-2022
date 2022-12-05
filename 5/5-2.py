# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

crates, moves = line_groups(slorp())

stacks = [[] for _ in range(9)]
for line in crates[:-1][::-1]:
    row = line[1::4]
    for stack, crate in zip(stacks, row):
        if crate != ' ':
            stack.append(crate)

for line in moves:
    q,f,t = map(int,line.split()[1::2])
    stacks[t-1] += [stacks[f-1].pop() for _ in range(q) if stacks[f-1]][::-1]

print(''.join(s[-1] for s in stacks if s))