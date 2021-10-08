from itertools import product

def solution(word):
    can_make = []
    for i in range(1, 6): can_make += product('AEIOU',repeat=i)
    for i in range(len(can_make)): can_make[i] = ''.join(can_make[i])
    can_make.sort()

    return can_make.index(word)+1
