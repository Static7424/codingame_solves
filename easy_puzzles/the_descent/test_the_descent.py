import pytest

from the_descent import main

test_cases = [
    {
        "name": "Descending mountains",
        "input": {
            "mountain_0": [9, 9, 1],
            "mountain_1": [8, 9, 1],
            "mountain_2": [7, 9, 1],
            "mountain_3": [6, 9, 1],
            "mountain_4": [5, 9, 1],
            "mountain_5": [4, 9, 1],
            "mountain_6": [3, 9, 1],
            "mountain_7": [2, 9, 1]
        },
        "expected_value": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    },
    {
        "name": "Scattered mountains",
        "input": {
            "mountain_0": [9, 9, 1],
            "mountain_1": [8, 9, 1],
            "mountain_2": [7, 9, 1],
            "mountain_3": [3, 9, 1],
            "mountain_4": [6, 9, 1],
            "mountain_5": [5, 9, 1],
            "mountain_6": [2, 9, 1],
            "mountain_7": [4, 9, 1]
        },
        "expected_value": [
            0,
            1,
            2,
            4,
            5,
            7,
            3,
            6
        ]
    },
    {
        "name": "Strong mountains 1",
        "input": {
            "mountain_0": [0, 9, 1],
            "mountain_1": [6, 4, 1],
            "mountain_2": [7, 3, 1],
            "mountain_3": [5, 2, 1],
            "mountain_4": [0, 9, 1],
            "mountain_5": [8, 9, 1],
            "mountain_6": [1, 9, 1],
            "mountain_7": [0, 9, 1]
        },
        "expected_value": [
            5,
            2,
            1,
            3,
            2,
            3,
            1,
            6
        ]
    },
    {
        "name": "Strong mountains 2",
        "input": {
            "mountain_0": [0, 9, 1],
            "mountain_1": [6, 2, 0],
            "mountain_2": [0, 3, 1],
            "mountain_3": [5, 3, 1],
            "mountain_4": [0, 9, 1],
            "mountain_5": [8, 3, 1],
            "mountain_6": [0, 9, 1],
            "mountain_7": [6, 9, 1]
        },
        "expected_value": [
            5,
            1,
            7,
            3,
            5,
            1,
            1,
            3
        ]
    },
    {
        "name": "One mountain",
        "input": {
            "mountain_0": [0, 9, 1],
            "mountain_1": [0, 9, 1],
            "mountain_2": [0, 9, 1],
            "mountain_3": [8, 1, 2],
            "mountain_4": [0, 9, 1],
            "mountain_5": [0, 9, 1],
            "mountain_6": [0, 9, 1],
            "mountain_7": [0, 9, 1]
        },
        "expected_value": [
            3,
            3,
            3,
            3,
            3
        ]
    }
]

@pytest.mark.parametrize("case", test_cases, ids = [case["name"] for case in test_cases])
def test_cases_run(case):
    live_input = []
    mountain_heights = []
    mountain_damage = []
    mountain_boosts = []
    captured_output = []
    initial_input = case["input"]
    
    live_input = list(initial_input.values())
    for value in live_input:
        mountain_heights.append(value[0])
        mountain_damage.append(value[1])
        mountain_boosts.append(value[2])
    
    while (mountain_heights != [0, 0, 0, 0, 0, 0, 0, 0]):
        output = main(mountain_heights)
        captured_output.append(output)
        if (mountain_boosts[output] == 1 and mountain_heights[output] - 4 <= 0 or mountain_boosts[output] == 2 and mountain_heights[output] - 4 <= 0 or mountain_heights[output] - mountain_damage[output] <= 0):
            mountain_heights[output] = 0
        else:
            mountain_heights[output] -= mountain_damage[output]
            if (mountain_boosts[output] == 1):
                mountain_damage[output] += 2
        print(mountain_heights)
    
    assert (captured_output == case["expected_value"])