# -*- coding: utf-8 -*-

def naive_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))

    if len(A) == 1: return A
    B = set(M(i) for i in A)
    C = A - B

    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A
