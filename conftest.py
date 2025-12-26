import pytest

@pytest.fixture(scope="function")
def preSetUpWork():
    print("I am a third fixture")