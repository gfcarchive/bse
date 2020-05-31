# -*- coding: utf-8 -*-

import attr
from bse import path
from bse.transform import Jsonable
from typing import Dict

try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree  # type: ignore


_dbpath = path.join(path.here(__file__), "iso4217.xml")
_db: Dict[str, "Currency"] = {}


@attr.s(frozen=True)
class Currency(Jsonable):
    code: str = attr.ib()
    name: str = attr.ib()
    exponent: int = attr.ib()

    @classmethod
    def bycode(cls, code: str) -> "Currency":
        if not _db:
            _updatedb()
        return _db[code]


def _updatedb() -> None:
    for _, elem in etree.iterparse(_dbpath, events=["end"]):
        if elem.tag == "CcyNtry":
            name = elem.findtext("CcyNm")
            code = elem.findtext("Ccy")
            expstr = elem.findtext("CcyMnrUnts")
            try:
                # this can happen when exp = N.A.
                exp = int(expstr)
            except Exception:
                exp = -1

            _db[code] = Currency(code=code, name=name, exponent=exp)
            elem.clear()
