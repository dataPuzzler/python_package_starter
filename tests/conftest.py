"""
Location to define test fixtures that are used by multiple test modules. 
https://docs.pytest.org/en/latest/fixture.html.
"""

import pytest


@pytest.fixture(scope="module")
def Animal():
    from sample_pck.animals import Animal
    return Animal

@pytest.fixture(scope="module")
def tom(Animal):
    from sample_pck.animals import create_tom
    return create_tom(Animal)

@pytest.fixture(scope="module")
def jerry(Animal):
    from sample_pck.animals import create_jerry
    return create_jerry(Animal)