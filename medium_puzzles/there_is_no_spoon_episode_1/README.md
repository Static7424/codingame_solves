# There is No Spoon - Episode 1

## The Goal

The game is played on a rectangular grid with a given size. Some cells contain power nodes. The rest of the cells are empty.

The goal is to find, when they exist, the horizontal and vertical neighbours of each node.

## Rules

To do this, you must find each (x1,y1) coordinates containing a node, and display the (x2,y2) coordinates of the next node to the right, and the (x3,y3) coordinates of the next node to the bottom within the grid.

If a neighbour does not exist, you must output the coordinates (-1,-1) instead of (x2,y2) and/or (x3,y3).

You lose if:
- you give an incorrect neighbour for a node.
- you give the neighbours for an empty cell.
- you compute the same node twice.
- you forget to compute the neighbours of a node.

### Victory Conditions

You win when all nodes have been correctly displayed.

### Example

#### Initial Phase

In this example, there are three nodes in a 2 by 2 grid. The cell at (1,1) is empty.

![image_1](https://cdn-games.codingame.com/no-spoon-game/example/0.png)

#### Round 1

The node at (0,0) has two neighbours.

`0 0 1 0 0 1`

![image_2](https://cdn-games.codingame.com/no-spoon-game/example/1.png)

#### Round 2

The node at (1,0) has no neighbours.

`1 0 -1 -1 -1 -1`

![image_3](https://cdn-games.codingame.com/no-spoon-game/example/2.png)

#### Round 3

The node at (0,1) has no neighbours.

`0 1 -1 -1 -1 -1`

![image_4](https://cdn-games.codingame.com/no-spoon-game/example/3.png)

## Note

Do not forget to execute the tests from the "Test cases" window.

Warning: the tests provided are similar to the validation tests used to compute the final score but remain different. This is a hardcoding prevention mechanism. Hardcoded solutions will not get any points.

Regarding the viewer, note that:
- A debug mode is available from the settings panel (the dented wheel).
- You can zoom/unzoom with the mouse wheel and move using drag'n drop (useful for large grids).

## Game Input

The program must first read the initialization data from standard input. Then, provide to the standard output one line per instruction.

### Initialization Input

Line 1: one integer `width` for the number of cells along the x axis.

Line 2: one integer `height` for the number of cells along the y axis.

Next `height` lines: A string `line` containing `width` characters. A dot . represents an empty cell. A zero 0 represents a cell containing a node.

### Output for One Game Turn

One line per node. Six integers on each line: `x1 y1 x2 y2 x3 y3`.

Where:
- (`x1`,`y1`) the coordinates of a node.
- (`x2`,`y2`) the coordinates of the closest neighbour on the right of the node.
- (`x3`,`y3`) the coordinates of the closest bottom neighbour.

If there is no neighbour, the coordinates should be (-1,-1).

### Constraints

0 < `width` ≤ 30

0 < `height` ≤ 18

0 ≤ `x1` < `width`

0 ≤ `y1` < `height`

-1 ≤ `x2`, `x3` < `width`

-1 ≤ `y2`, `y3` < `height`

Allocated response time to first output line ≤ 1s.

Response time between two output lines ≤ 100ms.