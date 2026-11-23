import pytest
import pytest_check as check
'''
def test_compare_2_numbers_test_1():
    assert 1 == 1, "Both numbers are not equal - Test 1"

def test_compare_2_numbers_test_2():
    assert 1 == 1, "Both numbers are not equal - Test 2"

def test_compare_2_numbers_test_3():
    assert 2 == 1, "Both numbers are not equal - Test 3"



# Hard Assertion
def test_compare_2_numbers_test_HardAssert():
    assert 1 == 1, "Both numbers are equal - Test 1"
    assert 1 == 2, "Both numbers are not equal - Test 2"
    assert 2 == 3, "Both numbers are not equal - Test 3"
    assert 3 == 3, "Both numbers are equal - Test 4"

# Soft Assertion
def test_compare_2_numbers_test_SoftAssert():
    check.equal(1, 1, "Both numbers are equal - Test 1")
    check.equal(1, 2, "Both numbers are not equal - Test 2")
    assert 2 == 3, "Both numbers are not equal - Test 1"
    assert 3 == 3, "Both numbers are equal - Test 2"
    assert 5 == 3, "Both numbers are equal - Test 3"
    assert 3 == 3, "Both numbers are equal - Test 4"


# Fixtures

def test_welcome_message_1():
    print("Hello!!")
    print("Welcome Mr. Ankit")
    assert 1 == 1, "Both are Different"
    print("Bye!")

def test_welcome_message_2():
    print("Hello!!")
    print("Welcome Mr. Hetu!")
    print("Bye!")
    '''

# Write a fixture and test
@pytest.fixture()
def greetings():

    print("\n\nbefore test step...")
    print("Hello!")
    yield
    print("before test step...")
    print("Bye!!")


def test_welcome_message_1(greetings):
    print("Welcome Mr. Ankit")
    assert 1 == 1, "Both are Different"


def test_welcome_message_2(greetings):
    print("Welcome Mr. Hetu!")
