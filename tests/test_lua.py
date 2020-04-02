# -*- coding: utf-8 -*-
import lupa  # type: ignore
import pytest  # type: ignore
from bse import lua


def test_environment_not_initialized() -> None:
    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    with pytest.raises(lua.LuaError):
        lua.environment(luart)


_env_d = {"description": "this is just a description", "extensionName": "string"}


def test_min_env() -> None:
    luart = lupa.LuaRuntime(unpack_returned_tuples=True)
    g = luart.globals()
    for k, v in _env_d.items():
        g[k] = v
    env = lua.environment(luart)
    assert env["name"] == env["extensionName"]
