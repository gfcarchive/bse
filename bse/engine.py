# -*- coding: utf-8 -*-


import attr
import types
from bse import logger, mod, model
from bse.config import Config
from urllib.parse import urlparse
from typing import Optional, Type


@attr.s
class Engine(object):

    modtype: mod.ModType = attr.ib()
    config: Config = attr.ib()
    _m: mod.Mod = attr.ib()
    _log: logger.Logger = attr.ib()

    @_log.default
    def _init_log(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    @_m.default
    def _init_m(self) -> mod.Mod:
        m = mod.modload(self.modtype)
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
        self._log.debug(f"Searching credentials for {host}")
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

    def accounts(self) -> None:
        pass

    def transfers(self) -> None:
        pass
