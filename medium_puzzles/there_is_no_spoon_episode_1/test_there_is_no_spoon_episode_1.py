import pytest

from there_is_no_spoon_episode_1 import main

test_cases = [
    {
        "name": "Example",
        "input": {
            "width": 2,
            "height": 2,
            "lines": [
                "00",
                "0."
            ]
        },
        "expected_value": [
            "0 0 1 0 0 1",
            "1 0 -1 -1 -1 -1",
            "0 1 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Horizontal",
        "input": {
            "width": 5,
            "height": 1,
            "lines": [
                "0.0.0"
            ]
        },
        "expected_value": [
            "0 0 2 0 -1 -1",
            "2 0 4 0 -1 -1",
            "4 0 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Vertical",
        "input": {
            "width": 1,
            "height": 4,
            "lines": [
                "0",
                "0",
                "0",
                "0"
            ]
        },
        "expected_value": [
            "0 0 -1 -1 0 1",
            "0 1 -1 -1 0 2",
            "0 2 -1 -1 0 3",
            "0 3 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Square",
        "input": {
            "width": 3,
            "height": 3,
            "lines": [
                "0.0",
                "...",
                "0.0"
            ]
        },
        "expected_value": [
            "0 0 2 0 0 2",
            "2 0 -1 -1 2 2",
            "0 2 2 2 -1 -1",
            "2 2 -1 -1 -1 -1"
        ]
    },
    {
        "name": "T",
        "input": {
            "width": 3,
            "height": 3,
            "lines": [
                "000",
                ".0.",
                ".0."
            ]
        },
        "expected_value": [
            "0 0 1 0 -1 -1",
            "1 0 2 0 1 1",
            "2 0 -1 -1 -1 -1",
            "1 1 -1 -1 1 2",
            "1 2 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Diagonal",
        "input": {
            "width": 4,
            "height": 4,
            "lines": [
                "0...",
                ".0..",
                "..0.",
                "...0"
            ]
        },
        "expected_value": [
            "0 0 -1 -1 -1 -1",
            "1 1 -1 -1 -1 -1",
            "2 2 -1 -1 -1 -1",
            "3 3 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Complex",
        "input": {
            "width": 4,
            "height": 4,
            "lines": [
                "00.0",
                "0.00",
                ".0.0",
                "000."
            ]
        },
        "expected_value": [
            "0 0 1 0 0 1",
            "1 0 3 0 1 2",
            "3 0 -1 -1 3 1",
            "0 1 2 1 0 3",
            "2 1 3 1 2 3",
            "3 1 -1 -1 3 2",
            "1 2 3 2 1 3",
            "3 2 -1 -1 -1 -1",
            "0 3 1 3 -1 -1",
            "1 3 2 3 -1 -1",
            "2 3 -1 -1 -1 -1"
        ]
    },
    {
        "name": "Shuriken",
        "input": {
            "width": 7,
            "height": 7,
            "lines": [
                "..0....",
                ".......",
                "..0.0.0",
                ".......",
                "0.0.0..",
                ".......",
                "....0.."
            ]
        },
        "expected_value": [
            "2 0 -1 -1 2 2",
            "2 2 4 2 2 4",
            "4 2 6 2 4 4",
            "6 2 -1 -1 -1 -1",
            "0 4 2 4 -1 -1",
            "2 4 4 4 -1 -1",
            "4 4 -1 -1 4 6",
            "4 6 -1 -1 -1 -1"
        ]
    }
]

@pytest.mark.parametrize("case", test_cases, ids = [case["name"] for case in test_cases])
def test_cases_run(case):
    input = case["input"]
    output = main(input["width"], input["height"], input["lines"])
    assert (output == case["expected_value"])