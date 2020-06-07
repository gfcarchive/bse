# -*- coding: utf-8 -*-
import abc
import attr
from bse import path
from bse import logger
from bse import lua
from bse import model
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

    @abc.abstractmethod
    def transfers(self, account: model.Account) -> List[model.Transfer]:
        pass

    @abc.abstractmethod
    def balance(self, account: model.Account) -> model.Balance:
        pass

    @abc.abstractmethod
    def securities(self, account: model.Account) -> List[model.Security]:
        pass


@attr.s
class LuaMod(Mod):

    script: str = attr.ib()  # script could be either a file path, or a text to execute
    _log: logger.Logger = attr.ib()
    _luart: lua.LuaRuntime = attr.ib(init=False)
    _protocol: str = attr.ib(init=False)
    _timestamp_refresh: int = attr.ib(default=0)
    _cached_balance: Optional[model.Balance] = attr.ib(default=None)
    _cached_transfers: List[model.Transfer] = attr.ib(factory=list)
    _cached_securities: List[model.Security] = attr.ib(factory=list)

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    def _initruntime(self) -> None:
        if path.exists(self.script):
            self.slug = path.fname(self.script).lower()
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
        if path.exists(self.script):
            self._luart.execute(path.readfile(self.script))
        else:
            self._luart.execute(self.script)

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

    def _new_security(self, ls: Any) -> model.Security:
        ls = lua.lua2py(ls)
        return model.Security(
            name=ls["name"],
            market=ls["market"],
            amount=ls["amount"],
            isin=ls.get("isin"),
            number=ls.get("securityNumber"),
            currency=ls.get(""),
            quantity=ls.get(""),
            original_amount=ls.get(""),
            original_currency=ls.get(""),
            exchange_rate=ls.get(""),
            trade_timestamp=ls.get(""),
            price=ls.get(""),
            price_currency=ls.get(""),
            purchase_price=ls.get(""),
            purchase_price_currency=ls.get(""),
        )

    def _refresh(self, account: model.Account, since: int = 1) -> None:
        """
        minimum unix timestamp is 1
        """
        if since != self._timestamp_refresh:
            g = self._luart.globals()
            data = g.RefreshAccount(account, since)
            for k, v in data.items():
                if k == "securities":
                    self._cached_securities.clear()
                    for _, luasecurity in v.items():
                        self._cached_securities.append(self._new_security(luasecurity))

            self._timestamp_refresh = since

    def transfers(self, account: model.Account) -> List[model.Transfer]:
        raise NotImplementedError("Mod:transfers is not implemented")

    def balance(self, account: model.Account) -> model.Balance:
        raise NotImplementedError("Mod:balance is not implemented")

    def securities(self, account: model.Account) -> List[model.Security]:
        self._refresh(account)
        return self._cached_securities
