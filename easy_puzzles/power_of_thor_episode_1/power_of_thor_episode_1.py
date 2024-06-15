import sys
import math

def main(light_x: int, light_y: int, current_tx: int, current_ty: int) -> tuple:

    move_direction = ""

    if (current_ty > light_y and current_ty > 0):
        move_direction = move_direction + "N"
        current_ty = int(current_ty) - 1
    elif (current_ty < light_y and current_ty < 17):
        move_direction = move_direction + "S"
        current_ty = int(current_ty) + 1
    if (current_tx > light_x and current_tx > 0):
        move_direction = move_direction + "W"
        current_tx = int(current_tx) - 1
    elif (current_tx < light_x and current_tx < 39):
        move_direction = move_direction + "E"
        current_tx = int(current_tx) + 1

    return move_direction, current_tx, current_ty

# TO PRINT TO CONSOLE

# light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
# current_tx = initial_tx
# current_ty = initial_ty

# while True:
#     result, current_tx, current_ty = main(light_x, light_y, current_tx, current_ty)
#     remaining_turns = int(input())
#     print(result)