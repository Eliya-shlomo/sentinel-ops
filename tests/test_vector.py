import pytest

from sentinel.vector import Vector


def test_vector_addition() -> None:
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_vector_equality() -> None:
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(1, 3)


def test_vector_len() -> None:
    assert len(Vector(1, 2, 3)) == 3


def test_vector_indexing() -> None:
    assert Vector(3, 4)[0] == 3


def test_vector_abs() -> None:
    assert abs(Vector(3, 4)) == 5.0


def test_vector_hash() -> None:
    assert hash(Vector(1, 2)) == hash(Vector(1, 2))


def test_mismatched_length_addition_raises_error() -> None:
    v1 = Vector(1, 2)
    v2 = Vector(1, 2, 3)
    with pytest.raises(ValueError):
        _ = v1 + v2
