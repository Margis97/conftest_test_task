import pytest
import random


@pytest.fixture(scope="function")
def setup_common():
    print(1)

