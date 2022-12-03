ls = [*iter(input,'')]

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 1 + 26

gs = zip(ls[::3],ls[1::3],ls[2::3])

s=0
for x,y,z in gs:
    item = ({*x} & {*y} & {*z}).pop()
    s += priority(item)

print(s)