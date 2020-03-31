# -*- coding: utf-8 -*-
"""
These are all functions to load into the global scope of the lua interpreter
"""

from babel.numbers import format_decimal, format_currency  # type: ignore
from babel.dates import format_datetime  # type: ignore
from bse import logger
from datetime import datetime
from urllib.parse import quote
from typing import Any


def bse_print(*args: Any) -> None:
    strs = [str(a) for a in args]
    logger.new("bse_print").debug(" ".join(strs))


def bse_localize_number(n: float, format: str = None) -> str:
    logger.new("bse_localze_number").debug(f"n: {n}, format: {format}")
    return format_decimal(n, format=format, locale="en_US")


def bse_localize_date(d: datetime, format: str = None) -> str:
    logger.new("bse_localze_datetime").debug(f"d: {d}, format: {format}")
    if format:
        return format_datetime(d, format=format, locale="en_US")
    return format_datetime(d, locale="en_US")


def bse_localize_amount(n: float, currency: str = None, format: str = None) -> str:
    logger.new("bse_localze_amount").debug(
        f"n: {n}, currency: {currency}, format: {format}"
    )
    if currency:
        if format:
            return format_currency(n, currency, format=format, locale="en_US")
        return format_currency(n, currency, locale="en_US")
    return format_decimal(n, locale="en_US")


def bse_urlencode(s: str, charset: str = None) -> str:
    logger.new("bse_urlencode").debug(f"s: {s}, charset: {charset}")
    if not charset:
        charset = "iso-8859-1"
    else:
        charset = charset.lower()
    return quote(s, encoding=charset)
