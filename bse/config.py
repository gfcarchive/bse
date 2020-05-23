# -*- coding: utf-8 -*-

import attr
import netrc
from bse import defaults
from bse.transform import Jsonable
from typing import Dict, Optional


@attr.s
class NetrcEntry(object):
    machine: str = attr.ib()
    login: Optional[str] = attr.ib()
    password: Optional[str] = attr.ib()
    account: Optional[str] = attr.ib()


@attr.s
class Config(Jsonable):

    netrc: str = attr.ib()

    def readrc(self, machine: str) -> NetrcEntry:
        nrc = netrc.netrc(self.netrc)
        authTokens = nrc.authenticators(machine)
        if not authTokens:
            raise KeyError(f"Credentials for {machine} not found in {self.netrc}")
        return NetrcEntry(
            machine=machine,
            login=authTokens[0],
            account=authTokens[1],
            password=authTokens[2],
        )


def new(params: Dict[str, str]) -> Config:
    return Config(netrc=params[defaults.ENV_NETRC])
