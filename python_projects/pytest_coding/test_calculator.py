import json
import pytest

def read_json(file_path):
    with open(file_path, "r") as jsonfile:
        data = json.load(jsonfile)
        return [(item["operation"], item["a"], item["b"], item["expected"]) for item in data]

@pytest.mark.parametrize("operation,a,b,expected", read_json("test_data.json"))
def test_calculator_operations(operation, a, b, expected):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    else:
        pytest.fail(f"Unknown operation {operation}")
    assert result == expected
