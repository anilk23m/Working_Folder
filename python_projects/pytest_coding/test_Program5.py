def is_even_or_odd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

def test_even():
    result = is_even_or_odd(4)
    print(f"Test for 4: {result}")

def test_odd():
    result = is_even_or_odd(7)
    assert result == "Odd", "given no should be Odd"
