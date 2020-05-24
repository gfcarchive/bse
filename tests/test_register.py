# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import register


def test_missing_slug() -> None:
    r = register.Register()
    with pytest.raises(register.RegisterError):
        r.load("this slug does not exist")


def test_available_slug() -> None:
    r = register.Register()
    assert r.load("coinbase").slug == "coinbase"


def test_available_slugs() -> None:
    r = register.Register()
    assert "coinbase" in r.slugs()
