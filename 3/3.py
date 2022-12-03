ls = [*iter(input,'')]

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 1 + 26

s=0
for l in ls:
    item = ({*l[:len(l)//2]} & {*l[len(l)//2:]}).pop()
    s += priority(item)

print(s)