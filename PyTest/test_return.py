#fixtures
import pytest
@pytest.fixture(scope="function")
def SecondWork():
    print("I am a Secondfixture")
    yield
    print("Teardown of Secondfixture")
def test_yield(SecondWork):
    print("Second check passed.")
