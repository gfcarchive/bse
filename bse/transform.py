# -*- coding: utf-8 -*-

from enum import Enum
from json import dumps
from typing import Dict, Any


class Dictable(object):
    def todict(self) -> Dict[str, Any]:
        d = {}
        for attrname in dir(self):
            if attrname.startswith("_"):
                continue
            attr = getattr(self, attrname)
            if callable(attr):
                continue
            d[attrname] = attr
        return d


class Jsonable(Dictable):
    @classmethod
    def dump(cls, o: Any) -> str:
        return dumps(o, indent=4, default=cls.default)

    @classmethod
    def default(cls, o: Any) -> Any:
        if isinstance(o, Dictable):
            return o.todict()
        if isinstance(o, Enum):
            return o.value
        return str(o)

    def json(self, indent: int = 4) -> str:
        return dumps(self.todict(), indent=indent)
