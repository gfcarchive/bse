# -*- coding: utf-8 -*-

import attr
from ._currency import Currency
from bse.transform import Jsonable
from typing import Dict


@attr.s
class Balance(Jsonable):
    state: Dict[Currency, int] = attr.ib()
