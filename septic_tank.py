from typing import List
from collections.abc import Iterable

import string
import more_itertools as mi

alpha = string.ascii_lowercase

def slorp():
    return [line.strip('\n') for line in open(0)]

def line_groups(lines) -> List[List[str]]:
    return [group.split('\n') for group in '\n'.join(lines).strip('\n').split('\n\n')]

'''
Recursively split on a series of delimiters
'''
def serial_split(string: str, delimiters):
    if delimiters:
        head, *tail = delimiters
        return (serial_split(slice, tail) for slice in string.split(head))
    else:
        return string

