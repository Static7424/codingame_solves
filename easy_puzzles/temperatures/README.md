# Temperatures

## The Goal

In this exercise, you have to analyze records of temperature to find the closest to zero.

![image_1](https://code.codingame.com/fileservlet?id=2553414341796)

Here, -1 is the closest to 0.

## Rules

Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).

## Game Input

Your program must read the data from the standard input and write the result on the standard output.

### Input

Line 1: `N`, the number of temperatures to analyze.

Line 2: a string with the `N` temperatures expressed as integers ranging from -273 to 5526.

### Output

Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.

### Constraints

0 ≤ `N` < 10000

### Example

#### Input

```
5
1 -2 -8 4 5
```

#### Output

```
1
```