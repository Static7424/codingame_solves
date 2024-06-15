import sys
import math

def main(width: int, height: int, lines: list) -> list:
    node_cords = []
    results = []
    
    for lines_index, line in enumerate(lines):
        for line_index, node in enumerate(line):
            if (node == '0'):
                node_cords.append([line_index, lines_index])

    for node in node_cords:
        result = ""
        for element in node:
            result += f"{element} "
        right_node = [node[0] + 1, node[1]]
        while (not(right_node in node_cords) and right_node[0] < width):
            right_node = [right_node[0] + 1, right_node[1]]

        bottom_node = [node[0], node[1] + 1]
        while (not(bottom_node in node_cords) and bottom_node[1] < height):
            bottom_node = [bottom_node[0], bottom_node[1] + 1]

        if not(right_node in node_cords) and not(bottom_node in node_cords):
            result += f"-1 -1 -1 -1"
        elif not(right_node in node_cords):
            result += f"-1 -1 "
            for element in bottom_node:
                result += f"{element} "
            result = result[:-1]
        elif not(bottom_node in node_cords):
            for element in right_node:
                result += f"{element} "
            result += f"-1 -1"
        else:
            for element in right_node:
                result += f"{element} "
            for element in bottom_node:
                result += f"{element} "
            result = result[:-1]

        results.append(result)
    
    return results

# TO PRINT TO CONSOLE

# lines = []

# width = int(input())
# height = int(input())
# for i in range(height):
#     lines.append(input())

# result = main(width, height, lines)
# for line in result:
#     print(line)