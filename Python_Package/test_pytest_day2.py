import pytest

# Parametrized tests

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(4,5,10),(10,10,20)])
def test_compare(a,b,expected):
    assert a+b == expected

# Markers: Categorized

@pytest.mark.regression

def test_compare_2_number_test_2():
    assert 1 == 1, "Both numbers are not equals - test 1"