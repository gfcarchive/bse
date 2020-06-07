# -*- coding: utf-8 -*-

import attr
from bse.transform import Jsonable


@attr.s
class Error(Jsonable):

    _exc: Exception = attr.ib()
    type: str = attr.ib(init=False)
    message: str = attr.ib(init=False)

    def __attrs_post_init__(self) -> None:
        self.type = self._exc.__class__.__name__
        self.message = str(self._exc)
