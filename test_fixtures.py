#fixtures
import pytest

@pytest.fixture(scope="function")#if it is module it will run once for entire test file if it is function it will run before each test case in file
def preWork():
    print("I am a fixture")

def test_initialcheck(preWork):
    print("Initial check passed.")

