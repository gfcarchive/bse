# -*- coding: utf-8 -*-

import attr
from bse.transform import Jsonable
from typing import Optional


@attr.s
class Security(Jsonable):
    name: str = attr.ib()
    market: str = attr.ib()
    amount: str = attr.ib()
    isin: Optional[str] = attr.ib()
    number: Optional[str] = attr.ib()
    currency: Optional[str] = attr.ib()
    quantity: Optional[int] = attr.ib()
    original_amount: Optional[str] = attr.ib()
    original_currency: Optional[str] = attr.ib()
    exchange_rate: Optional[str] = attr.ib()
    trade_timestamp: Optional[int] = attr.ib()
    price: Optional[str] = attr.ib()
    price_currency: Optional[str] = attr.ib()
    purchase_price: Optional[str] = attr.ib()
    purchase_price_currency: Optional[str] = attr.ib()
