# -*- coding: utf-8 -*-

from bse.mod import ModType, modload


def test_load() -> None:
    m = modload(ModType.Coinbase)
    assert m.version == "1.0"
    assert m.url == "https://api.coinbase.com"
