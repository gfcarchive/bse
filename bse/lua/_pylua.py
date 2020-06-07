# -*- coding: utf-8 -*-

from lupa import LuaRuntime  # type: ignore
from typing import Any


def py2lua(luart: LuaRuntime, o: Any) -> Any:
    for t in (int, float, str):
        if isinstance(o, t):
            return o
    for t in (dict, list):
        if isinstance(o, t):
            table = luart.table_from(o)
            for k, v in table.items():
                table[k] = py2lua(luart, v)
            return table
    raise ValueError(
        "Object '{o}' of type '{type(o)}' could not be converted to a Lua type"
    )


def _isiterable(o: Any) -> bool:
    return hasattr(o, "items") and callable(o.items)


def lua2py(o: Any) -> Any:
    if _isiterable(o):
        d = {}
        for k, v in o.items():
            if _isiterable(v):
                d[k] = lua2py(v)
            else:
                d[k] = v
        return d
    return o
