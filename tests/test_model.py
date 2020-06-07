# -*- coding: utf-8 -*-
from bse import model


def test_euro() -> None:
    curr = model.Currency.bycode("EUR")
    assert curr.code == "EUR"
    assert curr.name == "Euro"
    assert curr.exponent == 2


def test_error() -> None:
    exc = ValueError("v is wrong")
    err = model.Error(exc)
    assert err.type == exc.__class__.__name__
    assert err.message == str(exc)
    assert err.__todict__().get("type") == exc.__class__.__name__
    assert err.__todict__().get("message") == str(exc)
