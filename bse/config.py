# -*- coding: utf-8 -*-

import attr
from bse import defaults
from json import dumps
from typing import Dict


@attr.s
class Config(object):

    netrc: str = attr.ib()

    def json(self) -> str:
        j = {}
        for attrname in dir(self):
            if attrname.startswith("_"):
                continue
            attr = getattr(self, attrname)
            if callable(attr):
                continue
            j[attrname] = attr
        return dumps(j, indent=4)


def new(params: Dict[str, str]) -> Config:
    return Config(netrc=params[defaults.ENV_NETRC])
