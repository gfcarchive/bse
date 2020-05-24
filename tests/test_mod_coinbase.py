# -*- coding: utf-8 -*-

from bse import register


def test_load() -> None:
    m = register.Register().load("coinbase")
    assert m.version == "1.0"
    assert m.url == "https://api.coinbase.com"
