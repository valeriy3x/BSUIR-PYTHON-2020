from Cached.cached import cached
import pytest
import time


def fact(number):
    if number == 1 or number == 0:
        return 1

    return number * fact(number - 1)


def test_result():
    assert fact(5) == cached(fact)(5)


def test_time():
    start = time.time()
    cached(fact(200))
    first = time.time() - start

    start = time.time()
    cached(fact(200))
    second = time.time() - start

    assert second < first
