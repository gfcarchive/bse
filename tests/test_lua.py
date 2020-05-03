# -*- coding: utf-8 -*-
import lupa  # type: ignore
import pytest  # type: ignore
from bse import lua


def test_descriptor_not_initialized() -> None:
    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    with pytest.raises(lua.LuaError):
        lua.descriptor(luart)


_descr_d = {
    "ProtocolWebBanking": "Protocol",
    "description": "this is just a description",
    "extensionName": "string",
}


def test_min_descriptor() -> None:
    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    g = luart.globals()
    for k, v in _descr_d.items():
        g[k] = v
    descriptor = lua.descriptor(luart)
    assert descriptor.name == _descr_d["extensionName"]
