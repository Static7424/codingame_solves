import sys
import math

def main(message: str) -> str:
    bin_list = []
    output_string = ""

    for char in message:
        bin_conversion = format(ord(char), 'b')
        while (len(bin_conversion) < 7):
            bin_conversion = '0' + bin_conversion
        bin_list.append(bin_conversion)

    bin_string = ''.join(bin_list)

    for index, bin_bit in enumerate(bin_string):
        if (index > 0 and bin_bit == bin_string[index - 1]):
            output_string += '0'
        elif (bin_bit == '0'):
            output_string += " 00 0"
        elif (bin_bit == '1'):
            output_string += " 0 0"

    return output_string[1:]

# TO PRINT TO CONSOLE

# message = input()

# result = main(message)
# print(result)