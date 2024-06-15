import pytest

from power_of_thor_episode_1 import main

test_cases = [
    {
        "name": "Straight line",
        "input": {
            "light_x": 31,
            "light_y": 4,
            "initial_tx": 5,
            "initial_ty": 4
        },
        "expected_value":
            ["E"] * 26
    },
    {
        "name": "Up",
        "input": {
            "light_x": 31,
            "light_y": 4,
            "initial_tx": 31,
            "initial_ty": 17
        },
        "expected_value":
            ["N"] * 13
    },
    {
        "name": "Easy angle",
        "input": {
            "light_x": 0,
            "light_y": 17,
            "initial_tx": 31,
            "initial_ty": 4
        },
        "expected_value":
            ["SW"] * 13 +
            ["W"] * 18
    },
    {
        "name": "Optimal angle",
        "input": {
            "light_x": 36,
            "light_y": 17,
            "initial_tx": 0,
            "initial_ty": 0
        },
        "expected_value":
            ["SE"] * 17 +
            ["E"] * 19
    }
]

@pytest.mark.parametrize("case", test_cases, ids = [case["name"] for case in test_cases])
def test_cases_run(case):
    captured_output = []
    input = case["input"]
    
    output, current_tx, current_ty = main(input["light_x"], input["light_y"], input["initial_tx"], input["initial_ty"])
    captured_output.append(output)
    
    while (current_tx != input["light_x"] or current_ty != input["light_y"]):
        output, current_tx, current_ty = main(input["light_x"], input["light_y"], current_tx, current_ty)
        captured_output.append(output)
        
    assert (captured_output == case["expected_value"])