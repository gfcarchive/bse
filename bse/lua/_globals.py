# -*- coding: utf-8 -*-
"""
These are functions to load into the global scope of the lua interpreter
"""

import binascii
import hmac
import hashlib
import inspect
import time
from babel.numbers import format_decimal, format_currency  # type: ignore
from babel.dates import format_datetime  # type: ignore
from bse import logger
from bse import __version__
from bse.lua._connection import Connection
from bse.lua._json import JSON
from datetime import datetime
from lupa import LuaRuntime  # type: ignore
from typing import Any, Callable, Union
from urllib.parse import quote, unquote


def _log() -> logger.Logger:
    return logger.new(inspect.stack()[1][3])


def bse_version() -> str:
    return __version__


def bse_print(*args: Any) -> None:
    strs = [str(a) for a in args]
    _log().debug(" ".join(strs))


def bse_localize_number(n: float, format: str = None) -> str:
    _log().debug(f"n: {n}, format: {format}")
    return format_decimal(n, format=format, locale="en_US")


def bse_localize_date(d: datetime, format: str = None) -> str:
    _log().debug(f"d: {d}, format: {format}")
    if format:
        return format_datetime(d, format=format, locale="en_US")
    return format_datetime(d, locale="en_US")


def bse_localize_amount(n: float, currency: str = None, format: str = None) -> str:
    _log().debug(f"n: {n}, currency: {currency}, format: {format}")
    if currency:
        if format:
            return format_currency(n, currency, format=format, locale="en_US")
        return format_currency(n, currency, locale="en_US")
    return format_decimal(n, locale="en_US")


def bse_urlencode(o: Any, charset: str = None) -> str:
    _log().debug(f"o: {o}, charset: {charset}")
    if not isinstance(o, str):
        o = str(o)
    if not charset:
        charset = "iso-8859-1"
    else:
        charset = charset.lower()
    return quote(o, encoding=charset)


def bse_urldecode(s: str) -> str:
    _log().debug(f"s: {s}")
    return unquote(s)


def bse_encode_str(s: str, charset: str) -> str:
    _log().debug(f"s: {s}, charset: {charset}")
    charset = charset.lower()
    b = s.encode(encoding=charset)
    return b.hex()


def bse_decode_stream(b: str, charset: str) -> str:
    _log().debug(f"b: {b}, charset: {charset}")
    bs = bytes.fromhex(b)
    charset = charset.lower()
    return bs.decode(charset)


def bse_base64_encode(d: str) -> str:
    """
    Calculates the Base64 encoded string from a string containing the hexademical representation of a string
    """
    _log().debug(f"d: {d}")
    b = bytes.fromhex(d)
    return binascii.b2a_base64(b, newline=False).decode("ascii")


def bse_base64_decode(d: str) -> str:
    """
    Given a Base64 encoded string it returns a string containing the hexademical representation of the bytes
    """
    _log().debug(f"d: {d}")
    b = binascii.a2b_base64(d)
    return b.hex()


def bse_sha512(d: str) -> str:
    _log().debug(f"len(d): {len(d)}")
    alg = hashlib.sha512()
    alg.update(d.encode())
    return alg.hexdigest()


def bse_sha256(d: str) -> str:
    _log().debug(f"len(d): {len(d)}")
    alg = hashlib.sha256()
    alg.update(d.encode())
    return alg.hexdigest()


def bse_sha1(d: str) -> str:
    _log().debug(f"len(d): {len(d)}")
    alg = hashlib.sha1()
    alg.update(d.encode())
    return alg.hexdigest()


def bse_md5(d: str) -> str:
    _log().debug(f"len(d): {len(d)}")
    alg = hashlib.md5()
    alg.update(d.encode())
    return alg.hexdigest()


def bse_hmac(
    key: Union[str, bytes], d: Union[str, bytes], method: Callable[[], Any]
) -> bytes:
    if not isinstance(d, bytes):
        d = d.encode("ascii")
    if not isinstance(key, bytes):
        key = key.encode("ascii")
    h = hmac.new(key, d, digestmod=method)
    _log().debug(f"{method.__name__}({'*' * len(key)}, {d!r}) = {h.hexdigest()}")
    return h.digest()


def bse_hmac512(key: Union[str, bytes], d: Union[str, bytes]) -> bytes:
    return bse_hmac(key, d, hashlib.sha512)


def bse_hmac384(key: Union[str, bytes], d: Union[str, bytes]) -> bytes:
    return bse_hmac(key, d, hashlib.sha384)


def bse_hmac256(key: Union[str, bytes], d: Union[str, bytes]) -> bytes:
    return bse_hmac(key, d, hashlib.sha256)


def bse_time() -> int:
    t = time.time()
    _log().debug(f"timestamp: {t}")
    return int(t)


def bse_sleep(seconds: int) -> None:
    _log().debug(f"seconds: {seconds}")
    time.sleep(seconds)


def bse_connection() -> Connection:
    return Connection()


def bse_json(luart: LuaRuntime) -> Callable[..., Any]:
    def _jsonf(json: str = None) -> JSON:
        return JSON(luart, json)

    return _jsonf
