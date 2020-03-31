# -*- coding: utf-8 -*-
"""
Here we prepare the basics for including the lupa library. All other modules should use this one and never
directly the lupa module
"""

import lupa  # type: ignore
from . import _globals
from typing import Any

LuaRuntime: Any = lupa.LuaRuntime
LuaError: Any = lupa.LuaError


def runtime() -> LuaRuntime:
    luart = LuaRuntime(unpack_returned_tuples=True)
    g = luart.globals()
    g["print"] = _globals.bse_print
    g["bse_localize_number"] = _globals.bse_localize_number
    g["bse_localize_date"] = _globals.bse_localize_date
    g["bse_localize_amount"] = _globals.bse_localize_amount
    g["bse_urlencode"] = _globals.bse_urlencode
    return luart
