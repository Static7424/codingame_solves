import pytest

from onboarding import main

test_cases = [
    {
        "name": "Imminent danger",
        "input": {
            "threats": [
                "Rock 70m",
                "HotDroid 70m",
                "HardHat 70m Bolt 70m",
                "Sectoid 56m HardHat 60m",
                "HardHat 50m Buzz 59m",
                "Buzz 38m Zap 40m",
                "Zap 20m Charger 34m",
                "Charger 14m Whacker 36m",
                "Whacker 14m MaulMaker 35m",
                "MaulMaker 16m Fuse 39m",
                "Fuse 19m NutCracker 46m",
                "NutCracker 22m Buster 32m",
                "Buster 8m Hitbot 43m",
                "Hitbot 26m DangerDart 40m",
                "DangerDart 35m"
            ]
        },
        "expected_value": [
            "Rock",
            "HotDroid",
            "Bolt",
            "Sectoid",
            "HardHat",
            "Buzz",
            "Zap",
            "Charger",
            "Whacker",
            "MaulMaker",
            "Fuse",
            "NutCracker",
            "Buster",
            "Hitbot",
            "DangerDart"
        ]
    }
]

@pytest.mark.parametrize("case", test_cases, ids = [case["name"] for case in test_cases])
def test_cases_run(case):
    captured_output = []
    input = case["input"]
    
    for threat in input["threats"]:
        if (threat.count(' ') == 1):
            enemy_1, dist_1 = threat.split()
            enemy_2, dist_2 = threat.split()
        else:
            enemy_1, dist_1, enemy_2, dist_2 = threat.split()
        dist_1 = int(dist_1[:-1])
        dist_2 = int(dist_2[:-1])
        output = main(enemy_1, dist_1, enemy_2, dist_2)
        captured_output.append(output)
    
    assert(captured_output == case["expected_value"])