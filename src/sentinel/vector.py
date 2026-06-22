import math
from typing import Any


class Vector:
    def __init__(self, *components: float) -> None:
        self._storage = tuple(components)

    def __len__(self) -> int:
        return len(self._storage)

    def __getitem__(self, index: int) -> float:
        return self._storage[index]

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            return False

        return all(a == b for a, b in zip(self._storage, other._storage, strict=True))

    def __hash__(self) -> int:
        return hash(self._storage)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Cannot add vectors of different lengths")

        new_components = [a + b for a, b in zip(self._storage, other._storage, strict=True)]
        return Vector(*new_components)

    def __abs__(self) -> float:
        return math.sqrt(sum(x**2 for x in self._storage))

    def __repr__(self) -> str:
        return f"Vector{self._storage}"
