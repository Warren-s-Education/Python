import pytest

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

@pytest.mark.skip
def test_some_primes():
    assert 14 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
