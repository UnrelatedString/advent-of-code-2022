ls = [*iter(input,'e')]

gs = '\n'.join(ls).split('\n\n')

print(sum(sorted(sum(map(int,g.split())) for g in gs)[-3:]))