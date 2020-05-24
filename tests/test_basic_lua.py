# -*- coding: utf-8 -*-
import lupa  # type: ignore
import pytest  # type: ignore
from bse import lua, module


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


def test_hmac256() -> None:
    key = "fake_key"
    data = "1590067388GET/v2/user"
    digest = lua._globals.bse_hmac256(key, data)

    assert (
        digest.hex()
        == "c6ea132e0da7f210b21f8081525c22d637108d385cb42b46c8fe0fc318cdcfe0"
    )


def test_string_script() -> None:
    script = """
WebBanking {
  version = 1.0,
  url = "https://google.com",
  services = {"Service Name"},
  description = "this is a description",
}
    """
    m = module.LuaMod(script)
    assert m.description == "this is a description"
    assert m.slug == "string"
