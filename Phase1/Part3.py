z1 = [1, 1, 1, 2, 3, 3, 2, 3, 2]
z2 = [1, 1, 3, 2, 3, 1, 2, 3, 2]
x = len(z1)
print(x)


# 4
def hamming(z1, z2):
    ans = 0
    n = len(z1)
    for i in range(0, n):
        if z1[i] != z2[i]:
            ans += 1
    return ans


print(hamming(z1, z2))

# 5

