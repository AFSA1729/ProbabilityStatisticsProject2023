import numpy as np
import pandas as pd
import itertools

a = [1, 1, 1, 2, 3, 3, 2, 3, 2]
b = [1, 1, 3, 2, 3, 1, 2, 3, 2]
x = len(a)
print(x)


# 4
def hamming(z1, z2):
    ans = 0
    n = len(z1)
    for i in range(0, n):
        if z1[i] != z2[i]:
            ans += 1
    return ans


print(hamming(a, b))


# 5
def min_hamming(z1, z2):
    z1_values = list(pd.Series(z1).value_counts().index)
    permutations = list(itertools.permutations(z1_values))
    min_ham = 1000000000
    for i in range(0, len(permutations)):
        tmp = [0] * len(z2)
        for j in range(0, len(z2)):
            tmp[j] = permutations[i][z2[j] - 1]
        print(tmp)
        if min_ham > hamming(tmp, z1):
            min_ham = hamming(tmp, z1)
    return min_ham


min_hamming(a, b)
