import string
import more_itertools as mi

alpha = string.ascii_lowercase

def slorp():
    return (line.strip('\n') for line in open(0))

def line_groups(lines):
    return [group.split('\n') for group in '\n'.join(lines).strip('\n').split('\n\n')]