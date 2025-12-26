import pytest
@pytest.fixture(scope="function")#Session will run once for whole test suite 
def preSetUpWork():
    print("I am a thirdfixture")