# -*- coding: utf-8 -*-


import attr
import types
from bse import logger, module, model, register
from bse.config import Config
from urllib.parse import urlparse
from typing import List, Optional, Type


@attr.s
class Engine(object):

    slug: str = attr.ib()
    config: Config = attr.ib()
    _register: register.Register = attr.ib(factory=register.Register)
    _m: module.Mod = attr.ib()
    _log: logger.Logger = attr.ib()

    @_log.default
    def _init_log(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    @_m.default
    def _init_m(self) -> module.Mod:
        m = self._register.load(self.slug)
        return m

    def _hostname(self) -> str:
        urlparts = urlparse(self._m.url)
        if isinstance(urlparts.hostname, bytes):
            return urlparts.hostname.decode("utf-8")
        if isinstance(urlparts.hostname, str):
            return urlparts.hostname
        raise ValueError(f"No host found in URL {self._m.url}")

    def __enter__(self) -> "Engine":
        host = self._hostname()
        self._log.info(f"Searching credentials for {host}")
        rc = self.config.readrc(host)
        creds = model.Credential(username=rc.login, password=rc.password)
        self._m.initsession(creds)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[types.TracebackType],
    ) -> None:
        # do not re-raise the exception, that is responsibility of the caller
        pass

    def accounts(self) -> List[model.Account]:
        return self._m.accounts()

    def transfers(self) -> None:
        pass
