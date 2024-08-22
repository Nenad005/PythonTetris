matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate = list(zip(*matrix[::-1]))
import math

def remov_nb(n):
    results = []
    summ = sum([i for i in range(n+1)])
    od = int(math.sqrt(summ))
    print(summ)
    for i in range(od, summ):
        for j in range(od, (summ-i)//i + 1):
            if (summ-i-j) == i*j and j <= n:
                results.append([i, j])
    return [(result[0], result[1]) for result in results]

print(remov_nb(1000003))