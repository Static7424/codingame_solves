import pytest

from temperatures import main

test_cases = [
    {
        "name": "Simple test case",
        "input": {
            'n': 4,
            "temperatures": "1 -2 -8 4 5"
        },
        "expected_value": 1
    },
    {
        "name": "Only negative numbers",
        "input": {
            'n': 3,
            "temperatures": "-12 -5 -137"
        },
        "expected_value": -5
    },
    {
        "name": "Choose the right temperature",
        "input": {
            'n': 6,
            "temperatures": "42 -5 12 21 5 24"
        },
        "expected_value": 5
    },
    {
        "name": "Choose the right temperature 2",
        "input": {
            'n': 6,
            "temperatures": "42 5 12 21 -5 24"
        },
        "expected_value": 5
    },
    {
        "name": "Complex test case",
        "input": {
            'n': 10,
            "temperatures": "-5 -4 -2 12 -40 4 2 18 11 5"
        },
        "expected_value": 2
    },
    {
        "name": "No temperature",
        "input": {
            'n': 0,
            "temperatures": ""
        },
        "expected_value": 0
    }
]

@pytest.mark.parametrize("case", test_cases, ids = [case["name"] for case in test_cases])
def test_cases_run(case):
    input = case["input"]
    output = main(input['n'], input["temperatures"])
    assert (output == case["expected_value"])