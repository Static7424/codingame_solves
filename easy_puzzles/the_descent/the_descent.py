import sys
import math

def main(mountains: list) -> int:
    highest_mountain_index = 0
    
    for index, mountain in enumerate(mountains):
        if (mountain > mountains[highest_mountain_index]):
            highest_mountain_index = index
    
    return highest_mountain_index

# TO PRINT TO CONSOLE

# while True:
#     mountains = []

#     for i in range(8):
#         mountains.append(int(input()))

#     result = main(mountains)
#     print(result)