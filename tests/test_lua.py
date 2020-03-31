# -*- coding: utf-8 -*-
import lupa  # type: ignore
import pytest  # type: ignore
from bse import lua


def test_webbanking_validation_error() -> None:
    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    with pytest.raises(lua.LuaError):
        lua.WebBanking(luart).validate()


_webbanking_d = {
    "version": 1.0,
    "url": "https://host/app",
    "description": "this is just a description",
    "services": ["services"],
    "extensionName": "string",
}


@pytest.mark.parametrize(
    "key", ["version", "url", "description", "services", "extensionName"]
)
def test_webbanking_missing(key: str) -> None:
    d = dict(_webbanking_d)
    d.pop("version")

    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    g = luart.globals()
    for k, v in d.items():
        g[k] = v
    with pytest.raises(lua.LuaError):
        wb = lua.WebBanking(luart)
        wb.validate()
