# Algoritmo Quick sort basico

import random


def partition(A, L, R):
    i = L + 1
    piv = A[L]

    for j in range(L+1, R+1):
        if A[j] < piv:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[L], A[i-1] = A[i-1], A[L]
    return i-1


def rand_partition(A, L, R):
    rand = L + random.randint(L, R) % (R-L+1)
    A[rand], A[L] = A[L], A[rand]
    return partition(A, L, R)


def quick_sort(A, L, R):
    if L < R:
        piv_pos = rand_partition(A, L, R)
        quick_sort(A, L, piv_pos-1)
        quick_sort(A, piv_pos+1, R)


n = int(input())
a = list(map(int, input().split()))
quick_sort(a, 0, n-1)
print(*a)
