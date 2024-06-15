import sys
import math

def main(n: int, pis: list) -> int:
    pis.sort()
    d = pis[1] - pis[0]
    
    for i, h in enumerate(pis):
        if (i == len(pis) - 1):
            continue
        else:
            if (pis[i + 1] - pis[i] < d):
                d = pis[i + 1] - pis[i]

    return d

# TO PRINT TO CONSOLE

# pis = []

# n = int(input())
# for i in range(n):
#     pis.append(int(input()))

# result = main(n, pis)
# print(result)