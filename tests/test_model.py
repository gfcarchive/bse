# -*- coding: utf-8 -*-
from bse import model


def test_euro() -> None:
    curr = model.Currency.bycode("EUR")
    assert curr.code == "EUR"
    assert curr.name == "Euro"
    assert curr.exponent == 2
