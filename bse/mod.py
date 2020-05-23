# -*- coding: utf-8 -*-
import abc
import attr
from bse import path
from bse import logger
from bse import lua
from bse import model
from enum import Enum
from typing import Any, Dict, List, Optional


class ModError(Exception):
    pass


@attr.s
class Mod(abc.ABC):
    version: str = attr.ib(init=False)
    url: Optional[str] = attr.ib(init=False)
    description: str = attr.ib(init=False)
    name: str = attr.ib(init=False)
    slug: str = attr.ib(init=False)

    @abc.abstractmethod
    def initsession(self, creds: model.Credential) -> None:
        pass

    @abc.abstractmethod
    def accounts(self) -> List[model.Account]:
        pass


@attr.s
class LuaMod(Mod):

    _script: str = attr.ib()  # _script could be either a file path, or a text to execute
    _log: logger.Logger = attr.ib()
    _luart: lua.LuaRuntime = attr.ib(init=False)
    _protocol: str = attr.ib(init=False)

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    def _initruntime(self) -> None:
        if path.exists(self._script):
            self.slug = path.fname(self._script)
        else:
            self.slug = "string"
        self._luart = lua.runtime(self.slug, self._log)

    def _runprologue(self) -> None:
        self._luart.execute(lua.prologue())

    def _initattrs(self) -> None:
        d = lua.descriptor(self._luart)

        self.version = d.version
        self.url = d.url
        self.description = d.description
        self.name = d.name
        self._protocol = d.protocol

    def _runscript(self) -> None:
        if path.exists(self._script):
            self._luart.execute(path.readfile(self._script))
        else:
            self._luart.execute(self._script)

    def __attrs_post_init__(self) -> None:
        try:
            self._initruntime()
            self._runprologue()
            self._runscript()
            self._initattrs()
        except lua.LuaError as e:
            raise ModError(e)

    def initsession(self, creds: model.Credential) -> None:
        g = self._luart.globals()
        g.InitializeSession(
            self._protocol, self.name, creds.username, None, creds.password, None
        )

    def _new_account(self, a: Dict[str, Any]) -> model.Account:
        return model.Account(
            name=a["name"],
            portfolio=a["portfolio"],
            number=a["accountNumber"],
            currency=a["currency"],
            type=model.AccountType.moneymoneymap(a["type"]),
        )

    def accounts(self) -> List[model.Account]:
        g = self._luart.globals()
        luaaccounts = g.ListAccounts(None)
        acclist = [self._new_account(a) for _, a in luaaccounts.items()]
        self._log.debug(acclist, extra={"context": "[Accounts]"})
        return acclist


class ModType(Enum):
    Coinbase = "Coinbase"

    def script(self) -> str:
        if self == ModType.Coinbase:
            return path.join(path.here(__file__), "scripts", "Coinbase.lua")
        raise NotImplementedError(f"Module Type {self} is not configured")


def modload(modtype: ModType) -> Mod:
    script = modtype.script()
    return LuaMod(script)
