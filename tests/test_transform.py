# -*- coding: utf-8 -*-

from bse import transform
from enum import Enum


def test_default() -> None:
    assert transform.Jsonable.default("A") == "A"

    class _D(transform.Dictable):
        a = "A"

    assert transform.Jsonable.default(_D()) == {"a": "A"}

    class _E(Enum):
        e = 1

    assert transform.Jsonable.default(_E.e) == 1
