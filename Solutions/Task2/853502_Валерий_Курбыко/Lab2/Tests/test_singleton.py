from Singleton.singleton import Singleton
import pytest


class CEO(metaclass=Singleton):
    pass


def test_address():
    obj1 = CEO()
    obj2 = CEO()

    assert id(obj1) == id(obj2)
