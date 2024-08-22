from os import sep
from sys import stdout


list = [1, 2, 3, 4, 5]

def permutaions(arr):
    if len(arr) == 0: return [[]]
    FirstEl = arr[0]
    Rest = arr[1:]

    PermutationsWoFirst = permutaions(Rest)

    AllPermutations = []

    for perm in PermutationsWoFirst:
        for i in range(len(perm) + 1):
            permWFirst = [*perm[:i], FirstEl, *perm[i:]]
            AllPermutations.append(permWFirst)

    return AllPermutations

print('[')
print(*permutaions([1, 2, 3]), sep = ",\n")
print(']')
# print(permutaions([2, 3, 4]))
# print(permutaions([3, 4]))