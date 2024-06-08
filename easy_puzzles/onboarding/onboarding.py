import sys
import math

def main(enemy_1: str, dist_1: int, enemy_2: str, dist_2: int) -> str:
    if (dist_1 < dist_2):
        return enemy_1
    else:
        return enemy_2

# TO PRINT TO CONSOLE

# while True:
#     enemy_1 = input()
#     dist_1 = int(input())
#     enemy_2 = input()
#     dist_2 = int(input())

#     result = main(enemy_1, dist_1, enemy_2, dist_2)
#     print(result)