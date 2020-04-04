from Vector.vector import Vector
import pytest


def test_incorrect_init():
    with pytest.raises(ValueError):
        Vector([1, 2, 'a'])


def test_equal():
    assert Vector(-1, 5, 2, 10) == Vector(-1, 5, 2, 10)


def test_notequal_vec():
    assert Vector(2, 4, 6) != Vector(4, -3, 10)


def test_notequal_notvec():
    assert Vector(4, 2) != -2


def test_addition():
    first = Vector(3, 2, 1)
    second = Vector(-30, 5, 2)
    assert first + second == Vector(-27, 7, 3)


def test_scal_addition():
    assert Vector(2, 9) + 10 == Vector(12, 19)


def test_sub():
    first = Vector(3, 2, 1, 10)
    second = Vector(5, 2, 10, 7)
    assert first - second == Vector(-2, 0, -9, 3)


def test_mul_const():
    vector = Vector(8, 3, 1)
    assert vector * 5 == Vector(40, 15, 5)


def test_mul_vec():
    first = Vector(7, 5, 9, 6)
    second = Vector(4, -5, 3, 10)
    assert first * second == 90


def test_index():
    vector = Vector(2, 5, -10, 5)
    assert vector[2] == -10


def test_string():
    vector = Vector(-1, 5, 6)
    assert str(vector) == "(-1; 5; 6)"


def test_dimension():
    vector = Vector(-4, -1, 0)
    assert len(vector) == 3


def test_norm():
    vector = Vector(2, 4, 6, 2, 2)
    assert vector.get_norm() == 8


def test_sum_symbol():
    with pytest.raises(TypeError):
        '1' + Vector(2, 3, 4, 5)


def test_roper():
    vector = Vector(2, 3, 4)
    assert 1 + vector == Vector(3, 4, 5)
    assert 1 - vector == Vector(-1, -2, -3)
    assert 1 * vector == Vector(2, 3, 4)


def test_diff_dim():
    with pytest.raises(TypeError):
        Vector(2, 7) - Vector(4, 5, 6, 8)


def test_index_out():
    with pytest.raises(IndexError):
        vector = Vector(4, 6, 7, 8)
        vector[10]


def test_index_value():
    vector = Vector(2, 1, 2)
    vector[0] = 10
    assert vector == Vector(10, 1, 2)


def test_index_out():
    with pytest.raises(ValueError):
        vector = Vector(4, 6, 7, 8)
        vector[1] = 'a'
