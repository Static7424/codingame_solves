import sys
import math

def main(n: int, temperatures: str) -> int:
    split_temperatures = temperatures.split()
    if (n == 0):
        closest_to_zero = 0
    else:
        closest_to_zero = int(split_temperatures[0])

    for i in split_temperatures:
        t = int(i)
        if (abs(t) < abs(closest_to_zero)):
            closest_to_zero = t
        elif ((abs(t) == abs(closest_to_zero)) and (t > 0 and closest_to_zero < 0)):
            closest_to_zero = t

    return closest_to_zero

# TO PRINT TO CONSOLE

# n = int(input())
# temperatures = input()

# result = main(n, temperatures)
# print(result)