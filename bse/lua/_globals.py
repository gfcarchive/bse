# -*- coding: utf-8 -*-
"""
These are all functions to load into the global scope of the lua interpreter
"""

from babel.numbers import format_decimal  # type: ignore
from babel.dates import format_datetime  # type: ignore
from bse import logger
from datetime import datetime
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
