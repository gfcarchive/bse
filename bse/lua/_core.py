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
    g["bse_version"] = _globals.bse_version
    g["bse_localize_number"] = _globals.bse_localize_number
    g["bse_localize_date"] = _globals.bse_localize_date
    g["bse_localize_amount"] = _globals.bse_localize_amount
    g["bse_urlencode"] = _globals.bse_urlencode
    g["bse_urldecode"] = _globals.bse_urldecode
    g["bse_encode_str"] = _globals.bse_encode_str
    g["bse_decode_stream"] = _globals.bse_decode_stream
    g["bse_base64_encode"] = _globals.bse_base64_encode
    g["bse_base64_decode"] = _globals.bse_base64_decode
    g["bse_sha512"] = _globals.bse_sha512
    g["bse_sha256"] = _globals.bse_sha256
    g["bse_sha1"] = _globals.bse_sha1
    g["bse_md5"] = _globals.bse_md5
    g["bse_hmac512"] = _globals.bse_hmac512
    g["bse_hmac384"] = _globals.bse_hmac384
    g["bse_hmac256"] = _globals.bse_hmac256
    g["bse_time"] = _globals.bse_time
    g["bse_sleep"] = _globals.bse_sleep
    g["bse_connection"] = _globals.bse_connection
    g["bse_json"] = _globals.bse_json
    return luart
