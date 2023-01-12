import pytest


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture1(example_fixture):
    assert example_fixture == 1


def test_with_fixture2(example_fixture):
    assert example_fixture == 2
